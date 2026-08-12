#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import ipaddress
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG = ROOT / "config" / "special-lists.json"
ALLOWLIST = ROOT / "config" / "allowlist.txt"
CATEGORIES_DIR = ROOT / "lists" / "categories"
LEGACY_SPECIAL_DIR = ROOT / "lists" / "special"
IPS_DIR = ROOT / "lists" / "ips"
METADATA = ROOT / "metadata" / "special-lists.json"

DOMAIN_RE = re.compile(r"^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$", re.I)
WAYBACK_CAPTURE_RE = re.compile(r"/web/(\d{8,14})")


class SourceUnavailableError(RuntimeError):
    """Remote source is temporarily unavailable; callers may safely defer this source."""


# If one upstream host is clearly unreachable, do not spend minutes retrying every
# configured list from the same host during the same GitHub Actions run.
UNAVAILABLE_HOSTS: dict[str, str] = {}


def args_parser() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Build optional extended BlackRabbitZ lists from configured live sources")
    p.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    p.add_argument("--include-heavy", action="store_true", help="Include very large NRD/DGA variants")
    p.add_argument("--only", action="append", default=[], help="Build only one or more variant ids")
    p.add_argument("--force", action="store_true", help="Re-download even when generated files already exist")
    return p.parse_args()


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_allowlist() -> set[str]:
    if not ALLOWLIST.is_file():
        return set()
    out: set[str] = set()
    for line in ALLOWLIST.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip().lower().rstrip(".")
        if line and not line.startswith("#") and DOMAIN_RE.fullmatch(line):
            out.add(line)
    return out


def extract_domain(line: str) -> str | None:
    text = line.strip().lower()
    if not text or text.startswith(("#", "!", "[")):
        return None
    text = text.split("#", 1)[0].strip()
    if not text:
        return None

    # Hosts-style lines.
    fields = text.split()
    if len(fields) >= 2:
        try:
            ipaddress.ip_address(fields[0])
            text = fields[1]
        except ValueError:
            pass

    # Common Adblock/wildcard wrappers.
    if text.startswith("||"):
        text = text[2:]
    if text.startswith("*."):
        text = text[2:]
    text = text.lstrip(".")
    text = text.split("^", 1)[0]
    text = text.split("/", 1)[0]
    text = text.rstrip(".")

    # URL input.
    if "://" in text:
        host = urlparse(text).hostname
        text = host.lower().rstrip(".") if host else ""

    if text.startswith("www.") and DOMAIN_RE.fullmatch(text[4:]):
        # Preserve www if it is explicitly present; this branch merely validates below.
        pass

    if DOMAIN_RE.fullmatch(text):
        return text
    return None


def extract_ipv4(line: str) -> str | None:
    text = line.strip().split("#", 1)[0].strip()
    if not text or text.startswith(("!", "[")):
        return None
    text = text.split()[0]
    try:
        network = ipaddress.ip_network(text, strict=False)
    except ValueError:
        return None
    if network.version != 4:
        return None
    return str(network.network_address) if network.prefixlen == 32 else str(network)


def download(url: str, dest: Path) -> None:
    host = (urlparse(url).hostname or "unknown").lower()
    if host in UNAVAILABLE_HOSTS:
        raise SourceUnavailableError(
            f"{host} is unavailable in this run; skipping remaining sources from this host "
            f"({UNAVAILABLE_HOSTS[host]})"
        )

    # Keep retries useful but bounded. A completely offline archive host should not
    # block the entire list build for many minutes per configured variant.
    delays = (0, 5, 15)
    last_error: Exception | None = None
    host_wide_failure = False

    for attempt, delay in enumerate(delays, start=1):
        if delay:
            time.sleep(delay)
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "BlackRabbitZ-DNS-Blocklists/3.3.5 (+https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists)",
                "Accept": "text/plain,*/*;q=0.8",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=300) as response, dest.open("wb") as out:
                content_type = response.headers.get("Content-Type", "")
                shutil.copyfileobj(response, out, length=1024 * 1024)
            # An HTML error/landing page instead of raw list data is a failed source fetch.
            head = dest.read_bytes()[:512].lower()
            if b"<html" in head or b"<!doctype html" in head:
                raise RuntimeError(f"Upstream returned HTML instead of raw list data ({content_type})")
            return

        except urllib.error.HTTPError as exc:
            last_error = exc
            dest.unlink(missing_ok=True)
            print(
                f"WARN download attempt {attempt}/{len(delays)} failed for {host}: HTTP {exc.code}",
                file=sys.stderr,
            )
            # 404/410 and similar source-specific errors do not imply that every
            # other list on the same upstream host is unavailable.
            if exc.code in {429, 500, 502, 503, 504}:
                host_wide_failure = True
            if exc.code not in {408, 429, 500, 502, 503, 504}:
                break

        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as exc:
            last_error = exc
            host_wide_failure = True
            dest.unlink(missing_ok=True)
            print(
                f"WARN download attempt {attempt}/{len(delays)} failed for {host}: {exc}",
                file=sys.stderr,
            )

        except RuntimeError as exc:
            # Invalid upstream payload (for example an HTML landing page). Retry this
            # source, but do not trip the host-wide circuit breaker.
            last_error = exc
            dest.unlink(missing_ok=True)
            print(
                f"WARN download attempt {attempt}/{len(delays)} failed for {host}: {exc}",
                file=sys.stderr,
            )

    if host_wide_failure:
        UNAVAILABLE_HOSTS[host] = str(last_error)

    raise SourceUnavailableError(
        f"source unavailable after {len(delays)} attempt(s): {last_error}"
    )


def sort_unique(src: Path, dest: Path) -> None:
    env = dict(os.environ)
    env["LC_ALL"] = "C"
    if shutil.which("sort"):
        with dest.open("wb") as out:
            subprocess.run(["sort", "-u", str(src)], check=True, stdout=out, env=env)
        return
    # Fallback for non-POSIX local execution. Large NRD files are intended for GitHub Actions.
    values = sorted(set(src.read_text(encoding="utf-8", errors="ignore").splitlines()))
    dest.write_text("\n".join(values) + ("\n" if values else ""), encoding="utf-8")


def write_normalized_payload(raw: Path, normalized: Path, kind: str, allowlist: set[str]) -> int:
    if kind == "raw":
        shutil.copyfile(raw, normalized)
        return sum(1 for line in normalized.open("r", encoding="utf-8", errors="ignore") if line.strip() and not line.lstrip().startswith(("#", "!")))

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=normalized.parent, prefix="special-unsorted-") as tmp:
        tmp_path = Path(tmp.name)
        with raw.open("r", encoding="utf-8", errors="ignore") as fh:
            for line in fh:
                if kind == "domains":
                    value = extract_domain(line)
                    if value and value not in allowlist:
                        tmp.write(value + "\n")
                elif kind == "ipv4":
                    value = extract_ipv4(line)
                    if value:
                        tmp.write(value + "\n")
                else:
                    raise ValueError(f"Unsupported kind: {kind}")
    try:
        sort_unique(tmp_path, normalized)
    finally:
        tmp_path.unlink(missing_ok=True)
    return sum(1 for line in normalized.open("r", encoding="utf-8", errors="strict") if line.strip())


def output_directory(kind: str) -> Path:
    return IPS_DIR if kind == "ipv4" else CATEGORIES_DIR


def remove_old_variant_files(variant_id: str, kind: str) -> None:
    directory = output_directory(kind)
    for path in directory.glob(f"{variant_id}*.txt"):
        path.unlink(missing_ok=True)


def header_lines(config: dict, variant: dict, entries: int, part: int | None, parts: int | None) -> list[str]:
    lines = [
        "# BlackRabbitZ DNS Blocklists",
        f"# Source: {config['source_family']}",
        f"# Original project: {config['source_repository']}",
        f"# Upstream data URL: {variant['source_url']}",
        f"# License/source attribution: {config['license']} (see THIRD_PARTY.md)",
        f"# Entries in this file: {entries}",
    ]
    if part is not None and parts is not None:
        lines.append(f"# Part: {part:02d}/{parts:02d}")
    lines.append("")
    return lines


def split_lines_payload(normalized: Path, variant: dict, config: dict) -> list[dict]:
    kind = variant["kind"]
    directory = output_directory(kind)
    directory.mkdir(parents=True, exist_ok=True)
    max_bytes = int(config["split_max_bytes"])
    variant_id = variant["id"]

    if kind == "raw":
        # Preserve Adblock syntax byte-for-byte. It is a format-specific list,
        # not a BlackRabbitZ plain-domain file.
        out = directory / f"{variant_id}.txt"
        remove_old_variant_files(variant_id, kind)
        shutil.copyfile(normalized, out)
        entries = sum(1 for line in out.open("r", encoding="utf-8", errors="ignore") if line.strip() and not line.lstrip().startswith(("#", "!")))
        return [{"file": out.relative_to(ROOT).as_posix(), "entries": entries, "bytes": out.stat().st_size, "sha256": sha256(out)}]

    # First form payload chunks below the byte budget. Reserve 1 KiB for our generated header.
    budget = max(1024, max_bytes - 1024)
    chunks: list[list[str]] = []
    current: list[str] = []
    current_bytes = 0
    with normalized.open("r", encoding="utf-8", errors="strict") as fh:
        for line in fh:
            if not line.strip():
                continue
            b = len(line.encode("utf-8"))
            if current and current_bytes + b > budget:
                chunks.append(current)
                current = []
                current_bytes = 0
            current.append(line)
            current_bytes += b
    if current:
        chunks.append(current)
    if not chunks:
        raise RuntimeError(f"No usable entries after normalization for {variant_id}")

    remove_old_variant_files(variant_id, kind)
    files: list[dict] = []
    total_parts = len(chunks)
    for idx, chunk in enumerate(chunks, start=1):
        if total_parts == 1:
            out = directory / f"{variant_id}.txt"
        else:
            out = directory / f"{variant_id}-part-{idx:02d}.txt"
        with out.open("w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(header_lines(config, variant, len(chunk), idx if total_parts > 1 else None, total_parts if total_parts > 1 else None)))
            fh.writelines(chunk)
        if out.stat().st_size > max_bytes:
            raise RuntimeError(f"Generated file exceeds split limit: {out} ({out.stat().st_size} > {max_bytes})")
        files.append({"file": out.relative_to(ROOT).as_posix(), "entries": len(chunk), "bytes": out.stat().st_size, "sha256": sha256(out)})
    return files


def existing_files(variant_id: str, kind: str) -> list[Path]:
    directory = output_directory(kind)
    direct = directory / f"{variant_id}.txt"
    if direct.is_file():
        return [direct]
    parts = sorted(directory.glob(f"{variant_id}-part-*.txt"))
    return parts


def metadata_for_existing(variant: dict) -> dict | None:
    # Merged variants do not own a standalone published file. Their previous
    # successful merge state is tracked in metadata/special-lists.json instead.
    if variant.get("merge_into"):
        return None
    files = existing_files(variant["id"], variant["kind"])
    if not files:
        return None
    # Placeholder files are committed only so the planned list layout is visible
    # before the first successful upstream import. They must never suppress the real build.
    for path in files:
        try:
            head = path.read_text(encoding="utf-8", errors="ignore")[:2048]
        except OSError:
            return None
        if "# Status: Placeholder;" in head:
            return None
    infos = []
    for path in files:
        entries = sum(1 for line in path.open("r", encoding="utf-8", errors="ignore") if line.strip() and not line.startswith(("#", "!", "[")))
        infos.append({"file": path.relative_to(ROOT).as_posix(), "entries": entries, "bytes": path.stat().st_size, "sha256": sha256(path)})
    return {
        "status": "existing",
        "kind": variant["kind"],
        "entries": sum(x["entries"] for x in infos),
        "parts": len(infos),
        "files": infos,
        "source_url": variant["source_url"],
    }


def is_placeholder(path: Path) -> bool:
    try:
        return "# Status: Placeholder;" in path.read_text(encoding="utf-8", errors="ignore")[:2048]
    except OSError:
        return True


def combine_existing_variant_files(variant: dict, dest: Path) -> bool:
    """Combine previously published standalone output into a temporary raw file.

    This makes the v3.3.3 migration cheap: if v3.3.2 already downloaded a source,
    its normalized standalone output can be merged into the functional target
    without downloading it again.
    """
    files = existing_files(variant["id"], variant["kind"])
    if not files or any(is_placeholder(path) for path in files):
        return False
    with dest.open("w", encoding="utf-8", newline="\n") as out:
        for path in files:
            with path.open("r", encoding="utf-8", errors="ignore") as fh:
                for line in fh:
                    if line.lstrip().startswith(("#", "!", "[")) or not line.strip():
                        continue
                    out.write(line if line.endswith("\n") else line + "\n")
    return dest.stat().st_size > 0


def leading_comment_block(path: Path) -> list[str]:
    lines: list[str] = []
    if not path.is_file():
        return lines
    with path.open("r", encoding="utf-8", errors="ignore") as fh:
        for line in fh:
            stripped = line.rstrip("\r\n")
            if not stripped or stripped.lstrip().startswith("#"):
                lines.append(stripped)
                continue
            break
    return lines


def merge_into_category(normalized: Path, target_category: str, allowlist: set[str]) -> dict:
    target = CATEGORIES_DIR / f"{target_category}.txt"
    if not target.is_file():
        raise RuntimeError(f"Merge target does not exist: {target.relative_to(ROOT)}")

    before = 0
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=CATEGORIES_DIR, prefix=f"{target_category}-merge-") as tmp:
        tmp_path = Path(tmp.name)
        with target.open("r", encoding="utf-8", errors="ignore") as fh:
            for line in fh:
                value = extract_domain(line)
                if value and value not in allowlist:
                    tmp.write(value + "\n")
                    before += 1
        with normalized.open("r", encoding="utf-8", errors="strict") as fh:
            shutil.copyfileobj(fh, tmp)

    sorted_path = tmp_path.with_suffix(".sorted")
    try:
        sort_unique(tmp_path, sorted_path)
        after = sum(1 for line in sorted_path.open("r", encoding="utf-8") if line.strip())
        prefix = leading_comment_block(target)
        saw_entries = False
        out_prefix: list[str] = []
        for line in prefix:
            if line.startswith("# Entries:"):
                out_prefix.append(f"# Entries: {after}")
                saw_entries = True
            else:
                out_prefix.append(line)
        if not saw_entries:
            insert_at = 1 if out_prefix else 0
            out_prefix.insert(insert_at, f"# Entries: {after}")
        provenance = "# Additional third-party integrations: see THIRD_PARTY.md"
        if provenance not in out_prefix:
            # Keep it in the header without forcing a visible README source split.
            insert_at = next((i for i, line in enumerate(out_prefix) if line == ""), len(out_prefix))
            out_prefix.insert(insert_at, provenance)
        while out_prefix and out_prefix[-1] == "":
            out_prefix.pop()

        temp_target = target.with_suffix(".txt.tmp")
        with temp_target.open("w", encoding="utf-8", newline="\n") as out:
            for line in out_prefix:
                out.write(line + "\n")
            out.write("#\n")
            with sorted_path.open("r", encoding="utf-8") as src:
                shutil.copyfileobj(src, out)
        temp_target.replace(target)
    finally:
        tmp_path.unlink(missing_ok=True)
        sorted_path.unlink(missing_ok=True)

    return {
        "target": target.relative_to(ROOT).as_posix(),
        "entries_before": before,
        "entries_after": after,
        "entries_added": max(0, after - before),
    }


def build_variant(config: dict, variant: dict, allowlist: set[str], force: bool) -> dict:
    merge_target = variant.get("merge_into")
    if not merge_target and not force:
        existing = metadata_for_existing(variant)
        if existing:
            print(f"SAME {variant['id']}: using {existing['parts']} existing file(s)")
            return existing

    output_directory(variant["kind"]).mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="brz-special-") as td:
        td_path = Path(td)
        raw = td_path / "raw.txt"
        normalized = td_path / "normalized.txt"

        migrated_existing = False
        if merge_target and not force:
            migrated_existing = combine_existing_variant_files(variant, raw)

        if migrated_existing:
            print(f"MERGE {variant['id']}: reusing existing standalone output -> {merge_target}")
        else:
            print(f"GET  {variant['id']}")
            download(variant["source_url"], raw)

        entries = write_normalized_payload(raw, normalized, variant["kind"], allowlist)
        minimum = int(variant.get("min_entries", 1))
        if entries < minimum:
            raise RuntimeError(f"{variant['id']}: only {entries:,} entries after normalization; expected at least {minimum:,}")

        if merge_target:
            if variant["kind"] != "domains":
                raise RuntimeError(f"{variant['id']}: merge_into is supported only for domain lists")
            merged = merge_into_category(normalized, str(merge_target), allowlist)
            # Delete the v3.3.2 parallel output only after the functional merge succeeded.
            remove_old_variant_files(variant["id"], variant["kind"])
            print(
                f"OK   {variant['id']}: {entries:,} source entries merged into {merge_target}; "
                f"+{merged['entries_added']:,} unique domains"
            )
            return {
                "status": "merged",
                "kind": variant["kind"],
                "source_entries": entries,
                "entries": merged["entries_after"],
                "entries_added": merged["entries_added"],
                "parts": 0,
                "files": [],
                "merge_into": str(merge_target),
                "target": merged["target"],
                "source_url": variant["source_url"],
            }

        files = split_lines_payload(normalized, variant, config)
        total = sum(x["entries"] for x in files)
        print(f"OK   {variant['id']}: {total:,} entries -> {len(files)} file(s)")
        return {
            "status": "built",
            "kind": variant["kind"],
            "entries": total,
            "parts": len(files),
            "files": files,
            "source_url": variant["source_url"],
        }


def main() -> int:
    args = args_parser()
    config_path = args.config if args.config.is_absolute() else (ROOT / args.config)
    config = json.loads(config_path.read_text(encoding="utf-8"))
    allowlist = load_allowlist()
    only = set(args.only)

    CATEGORIES_DIR.mkdir(parents=True, exist_ok=True)
    IPS_DIR.mkdir(parents=True, exist_ok=True)

    # v3.3.2 migration: remove legacy source-named placeholder/build outputs.
    if LEGACY_SPECIAL_DIR.exists():
        for legacy in LEGACY_SPECIAL_DIR.glob("hagezi-*.txt"):
            legacy.unlink(missing_ok=True)
    for legacy in IPS_DIR.glob("hagezi-*.txt"):
        legacy.unlink(missing_ok=True)
    METADATA.parent.mkdir(parents=True, exist_ok=True)

    previous: dict = {}
    if METADATA.is_file():
        try:
            previous = json.loads(METADATA.read_text(encoding="utf-8"))
        except Exception:
            previous = {}

    result = {
        "schema_version": 2,
        "integration_revision": int(config.get("integration_revision", 1)),
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "source_family": config.get("source_family"),
        "source_policy": config.get("source_policy", "live_optional_skip_on_failure"),
        "split_max_bytes": config["split_max_bytes"],
        "items": {},
    }

    failures: list[str] = []
    unavailable: list[str] = []
    built_any = False
    for item in config["items"]:
        item_result = {"point": item["point"], "variants": {}}
        for variant in item.get("variants", []):
            vid = variant["id"]
            old = previous.get("items", {}).get(item["id"], {}).get("variants", {}).get(vid)
            previous_revision = int(previous.get("integration_revision", 0) or 0)
            current_revision = int(config.get("integration_revision", 1))
            if (
                variant.get("merge_into")
                and not args.force
                and previous_revision == current_revision
                and old
                and old.get("status") == "merged"
                and old.get("merge_into") == variant.get("merge_into")
            ):
                # The merge already succeeded in an earlier v3.3.3 run. Keep the
                # functional target and make sure no obsolete parallel output survived.
                remove_old_variant_files(variant["id"], variant["kind"])
                item_result["variants"][vid] = old
                print(f"SAME {vid}: already merged into {variant['merge_into']}")
                continue
            if only and vid not in only:
                if old:
                    item_result["variants"][vid] = old
                continue
            if variant.get("heavy") and not args.include_heavy:
                old = previous.get("items", {}).get(item["id"], {}).get("variants", {}).get(vid)
                existing = metadata_for_existing(variant)
                item_result["variants"][vid] = old or existing or {
                    "status": "not_built",
                    "kind": variant["kind"],
                    "entries": 0,
                    "parts": 0,
                    "files": [],
                    "source_url": variant["source_url"],
                    "note": "Run update-special-lists.py with --include-heavy to build this variant.",
                }
                print(f"SKIP {vid}: heavy list (use --include-heavy)")
                continue
            try:
                item_result["variants"][vid] = build_variant(config, variant, allowlist, args.force)
                built_any = True
            except SourceUnavailableError as exc:
                unavailable.append(f"{vid}: {exc}")
                old = previous.get("items", {}).get(item["id"], {}).get("variants", {}).get(vid)
                if old:
                    preserved = dict(old)
                    preserved["update_status"] = "source_unavailable"
                    preserved["update_error"] = str(exc)
                    item_result["variants"][vid] = preserved
                    print(
                        f"SKIP {vid}: source unavailable; preserving previously generated data",
                        file=sys.stderr,
                    )
                else:
                    item_result["variants"][vid] = {
                        "status": "source_unavailable",
                        "kind": variant["kind"],
                        "entries": 0,
                        "parts": 0,
                        "files": [],
                        "source_url": variant["source_url"],
                        "error": str(exc),
                        "note": "Remote source unavailable; build deferred and will be retried on a later run.",
                    }
                    print(
                        f"SKIP {vid}: source unavailable; continuing without this source",
                        file=sys.stderr,
                    )
            except Exception as exc:
                failures.append(f"{vid}: {exc}")
                old = previous.get("items", {}).get(item["id"], {}).get("variants", {}).get(vid)
                if old:
                    item_result["variants"][vid] = old
                    print(f"WARN {vid}: {exc}; preserving previous metadata", file=sys.stderr)
                else:
                    item_result["variants"][vid] = {
                        "status": "failed",
                        "kind": variant["kind"],
                        "entries": 0,
                        "parts": 0,
                        "files": [],
                        "source_url": variant["source_url"],
                        "error": str(exc),
                    }
                    print(f"FAIL {vid}: {exc}", file=sys.stderr)
        result["items"][item["id"]] = item_result

    METADATA.write_text(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote {METADATA.relative_to(ROOT)}")

    if unavailable:
        print(
            f"Deferred {len(unavailable)} source variant(s) because a remote source was unavailable. "
            "The normal BlackRabbitZ build may continue."
        )
    if failures and not previous:
        print("One or more first-build variants failed for a non-network reason:", file=sys.stderr)
        for msg in failures:
            print(f"  - {msg}", file=sys.stderr)
        return 1
    if failures:
        print(f"Completed with {len(failures)} non-network warning(s); previous generated data was preserved where available.")
    elif built_any:
        print("Special-list build completed successfully.")
    elif unavailable:
        print("No remote special-list data was changed in this run.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

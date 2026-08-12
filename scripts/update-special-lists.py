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
SPECIAL_DIR = ROOT / "lists" / "special"
IPS_DIR = ROOT / "lists" / "ips"
METADATA = ROOT / "metadata" / "special-lists.json"

DOMAIN_RE = re.compile(r"^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$", re.I)
WAYBACK_CAPTURE_RE = re.compile(r"/web/(\d{8,14})")


def args_parser() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Build archived/special BlackRabbitZ lists from configured sources")
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
    delays = (0, 5, 15, 30, 60)
    last_error: Exception | None = None
    for attempt, delay in enumerate(delays, start=1):
        if delay:
            time.sleep(delay)
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "BlackRabbitZ-DNS-Blocklists/3.2 (+https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists)",
                "Accept": "text/plain,*/*;q=0.8",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=300) as response, dest.open("wb") as out:
                content_type = response.headers.get("Content-Type", "")
                shutil.copyfileobj(response, out, length=1024 * 1024)
            # A Wayback HTML wrapper instead of raw data is a failed source fetch for our purposes.
            head = dest.read_bytes()[:512].lower()
            if b"<html" in head or b"<!doctype html" in head:
                raise RuntimeError(f"Archive returned HTML instead of raw list data ({content_type})")
            return
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, RuntimeError) as exc:
            last_error = exc
            dest.unlink(missing_ok=True)
            print(f"WARN download attempt {attempt}/{len(delays)} failed: {exc}", file=sys.stderr)
    raise RuntimeError(f"Archive download failed after {len(delays)} attempts: {last_error}")


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
    return IPS_DIR if kind == "ipv4" else SPECIAL_DIR


def remove_old_variant_files(variant_id: str, kind: str) -> None:
    directory = output_directory(kind)
    for path in directory.glob(f"{variant_id}*.txt"):
        path.unlink(missing_ok=True)


def header_lines(config: dict, variant: dict, entries: int, part: int | None, parts: int | None) -> list[str]:
    capture = WAYBACK_CAPTURE_RE.search(variant["source_url"])
    capture_text = capture.group(1) if capture else "unknown"
    lines = [
        "# BlackRabbitZ DNS Blocklists",
        f"# Source: {config['source_family']}",
        f"# Original project: {config['source_repository']}",
        f"# Archived source capture: {capture_text}",
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
        # Preserve archived Adblock syntax byte-for-byte. It is a format-specific list,
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
    files = existing_files(variant["id"], variant["kind"])
    if not files:
        return None
    # Placeholder files are committed only so the planned list layout is visible
    # before the first archive import. They must never suppress the real build.
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


def build_variant(config: dict, variant: dict, allowlist: set[str], force: bool) -> dict:
    if not force:
        existing = metadata_for_existing(variant)
        if existing:
            print(f"SAME {variant['id']}: using {existing['parts']} existing file(s)")
            return existing

    output_directory(variant["kind"]).mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="brz-special-") as td:
        td_path = Path(td)
        raw = td_path / "raw.txt"
        normalized = td_path / "normalized.txt"
        print(f"GET  {variant['id']}")
        download(variant["source_url"], raw)
        entries = write_normalized_payload(raw, normalized, variant["kind"], allowlist)
        minimum = int(variant.get("min_entries", 1))
        if entries < minimum:
            raise RuntimeError(f"{variant['id']}: only {entries:,} entries after normalization; expected at least {minimum:,}")
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

    SPECIAL_DIR.mkdir(parents=True, exist_ok=True)
    IPS_DIR.mkdir(parents=True, exist_ok=True)
    METADATA.parent.mkdir(parents=True, exist_ok=True)

    previous: dict = {}
    if METADATA.is_file():
        try:
            previous = json.loads(METADATA.read_text(encoding="utf-8"))
        except Exception:
            previous = {}

    result = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "source_family": config.get("source_family"),
        "archive_snapshot": config.get("archive_snapshot"),
        "split_max_bytes": config["split_max_bytes"],
        "items": {},
    }

    failures: list[str] = []
    built_any = False
    for item in config["items"]:
        item_result = {"point": item["point"], "variants": {}}
        for variant in item.get("variants", []):
            vid = variant["id"]
            if only and vid not in only:
                old = previous.get("items", {}).get(item["id"], {}).get("variants", {}).get(vid)
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

    if failures and not previous:
        print("One or more first-build variants failed:", file=sys.stderr)
        for msg in failures:
            print(f"  - {msg}", file=sys.stderr)
        return 1
    if failures:
        print(f"Completed with {len(failures)} warning(s); previous generated data was preserved where available.")
    elif built_any:
        print("Special-list build completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

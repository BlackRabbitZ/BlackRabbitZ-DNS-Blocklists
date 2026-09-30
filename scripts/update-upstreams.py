#!/usr/bin/env python3
"""Safe upstream refresh for BlackRabbitZ DNS Blocklists.

Key differences from the legacy importer:
- upstream data is stored per source and REPLACED after a successful refresh;
- manually curated domains live separately in sources/manual/;
- failed upstreams keep their last known-good source cache;
- privacy/device categories use critical-service and functional-endpoint guards;
- filtered sources support positive and negative rules;
- rejected/ambiguous candidates are written to review/quarantine/;
- lists/categories/*.txt are deterministic generated unions of manual + caches.

This prevents the old "once imported, forever present" behavior while keeping
manual BlackRabbitZ entries intact.
"""
from __future__ import annotations

import argparse
import hashlib
import ipaddress
import json
import re
import sys
import time
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "scripts" / "upstream-sources.json"
ALLOWLIST_PATH = ROOT / "config" / "allowlist.txt"
CRITICAL_PATH = ROOT / "config" / "critical-services.txt"
FUNCTIONAL_TOKENS_PATH = ROOT / "config" / "functional-guard-tokens.txt"
CATEGORY_DIR = ROOT / "lists" / "categories"
MANUAL_DIR = ROOT / "sources" / "manual"
UPSTREAM_DIR = ROOT / "sources" / "upstream"
QUARANTINE_DIR = ROOT / "review" / "quarantine"
REPORT_PATH = ROOT / "metadata" / "upstream-update.json"

DOMAIN_RE = re.compile(
    r"^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?\.)+"
    r"[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?$",
    re.IGNORECASE,
)
SKIP_NAMES = {"localhost", "localhost.localdomain", "broadcasthost", "ip6-localhost", "ip6-loopback"}


def normalize_domain(value: str) -> str | None:
    value = value.strip().lower().rstrip(".")
    if value.startswith("*."):
        value = value[2:]
    value = value.lstrip(".")
    value = value.split("^", 1)[0].split("$", 1)[0].strip()
    if not value or value in SKIP_NAMES:
        return None
    try:
        ipaddress.ip_address(value)
        return None
    except ValueError:
        pass
    try:
        value = value.encode("idna").decode("ascii")
    except (UnicodeError, ValueError):
        return None
    return value if DOMAIN_RE.fullmatch(value) else None


def extract_domain(line: str) -> str | None:
    raw = line.strip()
    if not raw or raw.startswith(("#", "!", "@@")):
        return None
    match = re.match(r"^\|\|([^/^$|]+)\^", raw)
    if match:
        return normalize_domain(match.group(1))
    parts = raw.split()
    if len(parts) >= 2:
        try:
            ipaddress.ip_address(parts[0])
            return normalize_domain(parts[1])
        except ValueError:
            pass
    if raw.startswith(("http://", "https://")):
        try:
            return normalize_domain(urllib.parse.urlsplit(raw).hostname or "")
        except ValueError:
            return None
    match = re.match(r"^(?:address|server)=/([^/]+)/", raw)
    if match:
        return normalize_domain(match.group(1))
    if " #" in raw:
        raw = raw.split(" #", 1)[0].strip()
    if "\t#" in raw:
        raw = raw.split("\t#", 1)[0].strip()
    if raw.startswith("*."):
        raw = raw[2:]
    first = raw.split()[0] if raw.split() else ""
    return normalize_domain(first)


def parse_domains(text: str) -> set[str]:
    return {d for line in text.splitlines() if (d := extract_domain(line))}


def load_domains(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return parse_domains(path.read_text(encoding="utf-8", errors="ignore"))


def load_rules(path: Path) -> set[str]:
    return load_domains(path)


def load_tokens(path: Path) -> list[str]:
    if not path.exists():
        return []
    return [line.strip().lower() for line in path.read_text(encoding="utf-8", errors="ignore").splitlines() if line.strip() and not line.lstrip().startswith("#")]


def suffix_match(domain: str, roots: set[str] | list[str]) -> bool:
    return any(domain == root or domain.endswith("." + root) for root in roots)


def source_slug(source: dict) -> str:
    name = re.sub(r"[^a-z0-9]+", "-", str(source.get("name", "source")).lower()).strip("-")[:56] or "source"
    digest = hashlib.sha256(str(source.get("url", "")).encode()).hexdigest()[:8]
    return f"{name}-{digest}"


def fetch_text(url: str, timeout: int, retries: int, max_bytes: int) -> str:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        request = urllib.request.Request(url, headers={
            "User-Agent": "BlackRabbitZ-DNS-Blocklists-Updater/2.0",
            "Accept": "text/plain,*/*;q=0.8",
            "Accept-Encoding": "identity",
        })
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                content_length = response.headers.get("Content-Length")
                if content_length and int(content_length) > max_bytes:
                    raise RuntimeError(f"source reports {content_length} bytes, above limit {max_bytes}")
                data = response.read(max_bytes + 1)
                if len(data) > max_bytes:
                    raise RuntimeError(f"download exceeded {max_bytes} bytes")
                return data.decode("utf-8", errors="ignore")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, RuntimeError) as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(min(2**attempt, 8))
    raise RuntimeError(f"download failed after {retries} attempts: {last_error}")


def choose_candidates(domains: set[str], source: dict) -> set[str]:
    trust = str(source.get("trust", "filtered" if source.get("include_keywords") else "direct"))
    include_keywords = [str(x).lower() for x in source.get("include_keywords", [])]
    include_suffixes = [str(x).lower().lstrip(".") for x in source.get("include_suffixes", [])]
    exclude_keywords = [str(x).lower() for x in source.get("exclude_keywords", [])]
    exclude_suffixes = [str(x).lower().lstrip(".") for x in source.get("exclude_suffixes", [])]
    min_matches = max(1, int(source.get("min_keyword_matches", 1)))

    chosen: set[str] = set()
    for domain in domains:
        if suffix_match(domain, exclude_suffixes) or any(token in domain for token in exclude_keywords):
            continue
        if trust == "direct" and not include_keywords and not include_suffixes:
            chosen.add(domain)
            continue
        suffix_ok = suffix_match(domain, include_suffixes) if include_suffixes else False
        matches = sum(1 for token in include_keywords if token in domain)
        if suffix_ok or matches >= min_matches:
            chosen.add(domain)
    return chosen


def functional_guard(domain: str, tokens: list[str]) -> str | None:
    low = domain.lower()
    for token in tokens:
        if token in low:
            return token
    return None


def write_domain_file(path: Path, domains: set[str], header_lines: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    if header_lines:
        lines.extend(header_lines)
        while lines and lines[-1] == "":
            lines.pop()
        lines.append("")
    lines.extend(sorted(domains))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def validate_config(config: dict) -> list[str]:
    errors: list[str] = []
    if config.get("version") != 2:
        errors.append("unsupported config version; expected 2")
    if config.get("mode") != "replace-source-cache":
        errors.append("mode must be replace-source-cache")
    categories = config.get("categories")
    if not isinstance(categories, dict) or not categories:
        errors.append("no categories configured")
        return errors
    for category, settings in categories.items():
        manual = MANUAL_DIR / f"{category}.txt"
        category_path = CATEGORY_DIR / f"{category}.txt"
        if not manual.exists():
            errors.append(f"missing manual source: {manual.relative_to(ROOT)}")
        if not category_path.exists():
            errors.append(f"category file does not exist: {category_path.relative_to(ROOT)}")
        sources = settings.get("sources", [])
        if not sources:
            errors.append(f"{category}: no sources configured")
        seen: set[str] = set()
        for source in sources:
            url = source.get("url", "")
            if not isinstance(url, str) or not url.startswith("https://"):
                errors.append(f"{category}: source URL must use https: {url!r}")
            if int(source.get("min_entries", 0)) < 1:
                errors.append(f"{category}: min_entries must be >= 1 for {source.get('name')}")
            slug = source_slug(source)
            if slug in seen:
                errors.append(f"{category}: duplicate source id: {slug}")
            seen.add(slug)
    return errors


def filter_safety(category: str, candidates: set[str], source: dict, protected: set[str], tokens: list[str]) -> tuple[set[str], list[tuple[str, str]]]:
    accepted: set[str] = set()
    rejected: list[tuple[str, str]] = []
    guard = bool(source.get("functional_guard", False))
    for domain in candidates:
        if suffix_match(domain, protected):
            rejected.append((domain, "critical-or-allowlisted"))
            continue
        if guard:
            token = functional_guard(domain, tokens)
            if token:
                rejected.append((domain, f"functional-token:{token}"))
                continue
        accepted.add(domain)
    return accepted, rejected


def cache_header(category: str, source: dict, accepted: set[str]) -> list[str]:
    return [
        "# BlackRabbitZ DNS Blocklists - upstream source cache",
        f"# Category: {category}",
        f"# Source: {source.get('name')}",
        f"# URL: {source.get('url')}",
        f"# Entries: {len(accepted)}",
        "# This file is replaced after a successful source refresh; it is not additive.",
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="download/report but do not write caches/categories")
    parser.add_argument("--check-config", action="store_true", help="validate configuration and exit")
    args = parser.parse_args()

    config = load_config()
    errors = validate_config(config)
    if errors:
        for error in errors:
            print(f"CONFIG ERROR: {error}", file=sys.stderr)
        return 2
    if args.check_config:
        print(f"Configuration OK: {len(config['categories'])} categories, replace-source-cache mode.")
        return 0

    defaults = config.get("defaults", {})
    timeout = int(defaults.get("timeout_seconds", 90))
    retries = int(defaults.get("retries", 3))
    max_bytes = int(defaults.get("max_download_bytes", 157286400))
    max_growth_ratio = float(defaults.get("max_source_growth_ratio", 1.0))
    max_shrink_ratio = float(defaults.get("max_source_shrink_ratio", 0.70))
    min_growth_allowance = int(defaults.get("minimum_growth_allowance", 1000))
    max_growth_absolute = int(defaults.get("max_growth_absolute", 500000))

    allowlist = load_rules(ALLOWLIST_PATH)
    critical = load_rules(CRITICAL_PATH)
    functional_tokens = load_tokens(FUNCTIONAL_TOKENS_PATH)
    all_sources = [s for settings in config["categories"].values() for s in settings.get("sources", [])]
    usage = Counter(s["url"] for s in all_sources)
    domain_cache: dict[str, set[str]] = {}
    error_cache: dict[str, str] = {}
    report: dict = {"generated_at": datetime.now(timezone.utc).isoformat(), "categories": {}}
    failures = guards = updates = quarantined_count = 0

    for category, settings in config["categories"].items():
        print(f"\n[{category}]")
        category_report = {"sources": [], "quarantine": 0}
        quarantine_rows: list[tuple[str, str, str]] = []
        for source in settings["sources"]:
            name, url = source["name"], source["url"]
            slug = source_slug(source)
            cache_path = UPSTREAM_DIR / category / f"{slug}.txt"
            old_cache = load_domains(cache_path)
            try:
                if url in error_cache:
                    raise RuntimeError(error_cache[url])
                if url in domain_cache:
                    parsed = domain_cache[url]
                else:
                    parsed = parse_domains(fetch_text(url, timeout, retries, max_bytes))
                    if len(parsed) < int(source["min_entries"]):
                        raise RuntimeError(f"parsed only {len(parsed):,} domains; expected at least {int(source['min_entries']):,}")
                    if usage[url] > 1:
                        domain_cache[url] = parsed
                selected = choose_candidates(parsed, source)
                category_protected = allowlist | (critical if settings.get("protect_critical", False) else set())
                accepted, rejected = filter_safety(category, selected, source, category_protected, functional_tokens)
                for domain, reason in rejected:
                    quarantine_rows.append((domain, name, reason))

                if old_cache:
                    growth = max(0, len(accepted - old_cache))
                    shrink = len(old_cache - accepted)
                    allowed_growth = max(min_growth_allowance, min(int(len(old_cache) * float(source.get("max_source_growth_ratio", max_growth_ratio))), int(source.get("max_growth_absolute", max_growth_absolute))))
                    allowed_shrink = max(50, int(len(old_cache) * float(source.get("max_source_shrink_ratio", max_shrink_ratio))))
                    if growth > allowed_growth:
                        guards += 1
                        raise RuntimeError(f"growth guard: +{growth:,} exceeds allowance {allowed_growth:,}; last good cache kept")
                    if shrink > allowed_shrink:
                        guards += 1
                        raise RuntimeError(f"shrink guard: -{shrink:,} exceeds allowance {allowed_shrink:,}; last good cache kept")

                if not args.dry_run:
                    write_domain_file(cache_path, accepted, cache_header(category, source, accepted))
                if accepted != old_cache:
                    updates += 1
                print(f"  OK   {name}: parsed={len(parsed):,}, selected={len(selected):,}, accepted={len(accepted):,}, quarantined={len(rejected):,}")
                category_report["sources"].append({"name": name, "status": "ok", "parsed": len(parsed), "selected": len(selected), "accepted": len(accepted), "quarantined": len(rejected)})
            except Exception as exc:
                failures += 1
                if url not in domain_cache:
                    error_cache[url] = str(exc)
                print(f"  WARN {name}: {exc}", file=sys.stderr)
                category_report["sources"].append({"name": name, "status": "kept-last-good", "error": str(exc), "cached": len(old_cache)})

        category_report["quarantine"] = len(quarantine_rows)
        quarantined_count += len(quarantine_rows)
        report["categories"][category] = category_report
        if not args.dry_run:
            qpath = QUARANTINE_DIR / f"{category}.tsv"
            if quarantine_rows:
                qpath.parent.mkdir(parents=True, exist_ok=True)
                lines = ["domain\tsource\treason"] + ["\t".join(row) for row in sorted(set(quarantine_rows))]
                qpath.write_text("\n".join(lines) + "\n", encoding="utf-8")
            elif qpath.exists():
                qpath.unlink()

    if not args.dry_run:
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build-categories.py")], check=True)

    report["summary"] = {"source_cache_updates": updates, "source_failures": failures, "guards": guards, "quarantined": quarantined_count, "dry_run": args.dry_run}
    if not args.dry_run:
        REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
        REPORT_PATH.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print("\n=== upstream refresh summary ===")
    print(f"source cache updates : {updates}")
    print(f"source failures      : {failures}")
    print(f"guards triggered     : {guards}")
    print(f"quarantined          : {quarantined_count}")
    if args.dry_run:
        print("dry-run              : no files written")
    # Source download failures are tolerated because last-good caches are kept.
    # Guard failures are non-zero so an implausible source mutation cannot be proposed automatically.
    return 3 if guards else 0


if __name__ == "__main__":
    raise SystemExit(main())

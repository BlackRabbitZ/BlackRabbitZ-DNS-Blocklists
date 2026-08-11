#!/usr/bin/env python3
"""Add newly published upstream domains to BlackRabbitZ category lists.

The importer is intentionally additive: it never removes an existing BlackRabbitZ
entry. Upstream data is normalized to DNS names, deduplicated, checked against a
small safety allowlist and guarded against implausibly large one-run growth.
"""

from __future__ import annotations

import argparse
import ipaddress
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "scripts" / "upstream-sources.json"
ALLOWLIST_PATH = ROOT / "config" / "allowlist.txt"
CATEGORY_DIR = ROOT / "lists" / "categories"

DOMAIN_RE = re.compile(
    r"^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?\.)+"
    r"[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?$",
    re.IGNORECASE,
)

SKIP_NAMES = {
    "localhost",
    "localhost.localdomain",
    "broadcasthost",
    "ip6-localhost",
    "ip6-loopback",
}


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

    # Adblock/AdGuard domain rule: ||example.org^
    match = re.match(r"^\|\|([^/^$|]+)\^", raw)
    if match:
        return normalize_domain(match.group(1))

    # Hosts file: 0.0.0.0 example.org
    parts = raw.split()
    if len(parts) >= 2:
        try:
            ipaddress.ip_address(parts[0])
            return normalize_domain(parts[1])
        except ValueError:
            pass

    # Full URL feeds.
    if raw.startswith(("http://", "https://")):
        try:
            return normalize_domain(urllib.parse.urlsplit(raw).hostname or "")
        except ValueError:
            return None

    # dnsmasq/AdGuard Home variants.
    match = re.match(r"^(?:address|server)=/([^/]+)/", raw)
    if match:
        return normalize_domain(match.group(1))

    # RPZ-ish "domain CNAME ." / plain-domain files / inline comments.
    if " #" in raw:
        raw = raw.split(" #", 1)[0].strip()
    if "\t#" in raw:
        raw = raw.split("\t#", 1)[0].strip()
    if raw.startswith("*."):
        raw = raw[2:]

    first = raw.split()[0] if raw.split() else ""
    return normalize_domain(first)


def parse_domains(text: str) -> set[str]:
    result: set[str] = set()
    for line in text.splitlines():
        domain = extract_domain(line)
        if domain:
            result.add(domain)
    return result


def load_existing(path: Path) -> set[str]:
    result: set[str] = set()
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        for line in handle:
            domain = extract_domain(line)
            if domain:
                result.add(domain)
    return result


def load_allowlist(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return load_existing(path)


def is_allowlisted(domain: str, allowlist: set[str]) -> bool:
    return any(domain == item or domain.endswith("." + item) for item in allowlist)


def fetch_text(url: str, timeout: int, retries: int, max_bytes: int) -> str:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "BlackRabbitZ-DNS-Blocklists-Updater/1.0",
                "Accept": "text/plain,*/*;q=0.8",
                "Accept-Encoding": "identity",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                content_length = response.headers.get("Content-Length")
                if content_length and int(content_length) > max_bytes:
                    raise RuntimeError(
                        f"source reports {content_length} bytes, above limit {max_bytes}"
                    )
                data = response.read(max_bytes + 1)
                if len(data) > max_bytes:
                    raise RuntimeError(f"download exceeded {max_bytes} bytes")
                return data.decode("utf-8", errors="ignore")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, RuntimeError) as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(min(2**attempt, 8))
    raise RuntimeError(f"download failed after {retries} attempts: {last_error}")


def leading_header_lines(path: Path) -> list[str]:
    header: list[str] = []
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        for line in handle:
            stripped = line.strip()
            if stripped == "" or stripped.startswith("#"):
                header.append(line.rstrip("\n\r"))
                continue
            break
    return header


def rewrite_category(path: Path, domains: set[str]) -> None:
    header = leading_header_lines(path)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Keep project metadata, but replace a previous auto-update marker.
    header = [line for line in header if not line.startswith("# Auto-updated:")]
    insert_at = len(header)
    for index, line in enumerate(header):
        if line.startswith("# Entries:"):
            insert_at = index + 1
            break
    header.insert(insert_at, f"# Auto-updated: {timestamp}")

    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for line in header:
            handle.write(line + "\n")
        if not header or header[-1].strip() != "":
            handle.write("\n")
        for domain in sorted(domains):
            handle.write(domain + "\n")


def filtered(domains: set[str], source: dict) -> set[str]:
    keywords = [str(item).lower() for item in source.get("include_keywords", [])]
    if not keywords:
        return domains
    return {domain for domain in domains if any(keyword in domain for keyword in keywords)}


def load_config() -> dict:
    with CONFIG_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_config(config: dict) -> list[str]:
    errors: list[str] = []
    if config.get("version") != 1:
        errors.append("unsupported config version")
    if config.get("mode") != "additive":
        errors.append("only additive mode is supported")
    categories = config.get("categories")
    if not isinstance(categories, dict) or not categories:
        errors.append("no categories configured")
        return errors

    for category, settings in categories.items():
        path = CATEGORY_DIR / f"{category}.txt"
        if not path.exists():
            errors.append(f"category file does not exist: {path.relative_to(ROOT)}")
        sources = settings.get("sources", [])
        if not sources:
            errors.append(f"{category}: no sources configured")
        for source in sources:
            url = source.get("url", "")
            if not isinstance(url, str) or not url.startswith("https://"):
                errors.append(f"{category}: source URL must use https: {url!r}")
            if int(source.get("min_entries", 0)) < 1:
                errors.append(f"{category}: min_entries must be >= 1 for {source.get('name')}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="download and report, do not write")
    parser.add_argument("--check-config", action="store_true", help="validate configuration and exit")
    args = parser.parse_args()

    config = load_config()
    errors = validate_config(config)
    if errors:
        for error in errors:
            print(f"CONFIG ERROR: {error}", file=sys.stderr)
        return 2
    if args.check_config:
        print(f"Configuration OK: {len(config['categories'])} auto-updated categories.")
        return 0

    defaults = config.get("defaults", {})
    timeout = int(defaults.get("timeout_seconds", 90))
    retries = int(defaults.get("retries", 3))
    max_bytes = int(defaults.get("max_download_bytes", 157286400))
    default_ratio = float(defaults.get("max_growth_ratio", 0.35))
    default_absolute = int(defaults.get("max_growth_absolute", 500000))
    minimum_allowance = int(defaults.get("minimum_growth_allowance", 1000))
    allowlist = load_allowlist(ALLOWLIST_PATH)

    all_sources = [
        source
        for settings in config["categories"].values()
        for source in settings.get("sources", [])
    ]
    usage = Counter(source["url"] for source in all_sources)
    domain_cache: dict[str, set[str]] = {}
    error_cache: dict[str, str] = {}

    changed_categories = 0
    total_added = 0
    source_failures = 0
    guarded_categories = 0

    for category, settings in config["categories"].items():
        path = CATEGORY_DIR / f"{category}.txt"
        existing = load_existing(path)
        candidates: set[str] = set()
        successful_sources = 0

        print(f"\n[{category}] existing={len(existing):,}")
        for source in settings["sources"]:
            name = source["name"]
            url = source["url"]
            min_entries = int(source["min_entries"])

            try:
                if url in error_cache:
                    raise RuntimeError(error_cache[url])
                if url in domain_cache:
                    domains = domain_cache[url]
                else:
                    text = fetch_text(url, timeout, retries, max_bytes)
                    domains = parse_domains(text)
                    if len(domains) < min_entries:
                        raise RuntimeError(
                            f"parsed only {len(domains):,} domains; expected at least {min_entries:,}"
                        )
                    if usage[url] > 1:
                        domain_cache[url] = domains
                selected = filtered(domains, source)
                candidates.update(selected)
                successful_sources += 1
                print(
                    f"  OK   {name}: parsed={len(domains):,}, selected={len(selected):,}"
                )
            except Exception as exc:  # fail-safe: preserve last good category
                source_failures += 1
                error_cache[url] = str(exc)
                print(f"  WARN {name}: {exc}", file=sys.stderr)

        if successful_sources == 0:
            print("  KEEP no upstream source succeeded; category left unchanged")
            continue

        imported = {domain for domain in candidates if not is_allowlisted(domain, allowlist)}
        new_domains = imported - existing
        if not new_domains:
            print("  SAME no new domains")
            continue

        ratio = float(settings.get("max_growth_ratio", default_ratio))
        absolute = int(settings.get("max_growth_absolute", default_absolute))
        proportional = int(len(existing) * ratio)
        allowed_growth = max(minimum_allowance, min(absolute, proportional or minimum_allowance))

        if len(new_domains) > allowed_growth:
            guarded_categories += 1
            print(
                f"  GUARD refusing +{len(new_domains):,} domains; one-run allowance is "
                f"{allowed_growth:,}. Review upstreams/config manually.",
                file=sys.stderr,
            )
            continue

        merged = existing | new_domains
        print(f"  ADD  +{len(new_domains):,} => {len(merged):,}")
        if not args.dry_run:
            rewrite_category(path, merged)
        changed_categories += 1
        total_added += len(new_domains)

    print("\n=== upstream update summary ===")
    print(f"changed categories : {changed_categories}")
    print(f"new domains        : {total_added:,}")
    print(f"source warnings    : {source_failures}")
    print(f"growth guards      : {guarded_categories}")
    if args.dry_run:
        print("dry-run             : no files written")

    # A growth guard is treated as a failed update so Actions will not commit a
    # partial run. Individual unavailable sources are warnings; categories with
    # other successful sources can still update safely.
    return 3 if guarded_categories else 0


if __name__ == "__main__":
    raise SystemExit(main())

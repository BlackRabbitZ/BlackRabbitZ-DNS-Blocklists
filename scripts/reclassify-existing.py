#!/usr/bin/env python3
"""One-time cleanup and modularisation of existing BlackRabbitZ category lists.

The script is deliberately conservative. It only applies critical-service
protection to privacy/device categories, and separates domains already covered
by specialised categories from the broad trackers/telemetry lists. Security and
content feeds are not filtered by functional-name heuristics.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORY_DIR = ROOT / "lists" / "categories"
MANUAL_DIR = ROOT / "sources" / "manual"
ALLOWLIST = ROOT / "config" / "allowlist.txt"
CRITICAL = ROOT / "config" / "critical-services.txt"
REPORT = ROOT / "metadata" / "cleanup-report.json"

DOMAIN_RE = re.compile(r"^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?$", re.I)

PRIVACY_DEVICE = {
    "ads", "trackers", "telemetry", "social-trackers", "mobile-tracking",
    "affiliate-tracking", "consent-cmp", "windows-telemetry", "apple-telemetry",
    "android-telemetry", "linux-telemetry", "nas-telemetry", "server-telemetry",
    "native-tracking", "smart-tv", "iot", "gaming-telemetry",
}
SPECIALISED_FOR_TRACKERS = {
    "telemetry", "social-trackers", "mobile-tracking", "affiliate-tracking",
    "consent-cmp", "windows-telemetry", "apple-telemetry", "android-telemetry",
    "linux-telemetry", "nas-telemetry", "server-telemetry", "native-tracking",
    "smart-tv", "iot", "gaming-telemetry",
}
SPECIALISED_FOR_TELEMETRY = {
    "mobile-tracking", "windows-telemetry", "apple-telemetry", "android-telemetry",
    "linux-telemetry", "nas-telemetry", "server-telemetry", "smart-tv", "iot",
    "gaming-telemetry",
}


def extract_domain(line: str) -> str | None:
    value = line.strip().lower().rstrip(".")
    if not value or value.startswith(("#", "!", "@@")):
        return None
    if value.startswith("||") and "^" in value:
        value = value[2:].split("^", 1)[0]
    if " #" in value:
        value = value.split(" #", 1)[0].strip()
    if value.startswith("*."):
        value = value[2:]
    value = value.split()[0] if value.split() else ""
    return value if DOMAIN_RE.fullmatch(value) else None


def read_domains(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {d for line in path.read_text(encoding="utf-8", errors="ignore").splitlines() if (d := extract_domain(line))}


def is_suffix_match(domain: str, roots: set[str]) -> bool:
    return any(domain == root or domain.endswith("." + root) for root in roots)


def header(path: Path, count: int) -> list[str]:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines() if path.exists() else []
    out: list[str] = []
    for line in lines:
        if line.strip() == "" or line.startswith("#"):
            if line.startswith("# Entries:"):
                line = f"# Entries: {count}"
            if not line.startswith("# Auto-updated:"):
                out.append(line)
            continue
        break
    if not any(x.startswith("# Entries:") for x in out):
        out.insert(0, f"# Entries: {count}")
    while out and out[-1] == "":
        out.pop()
    return out


def write_category(path: Path, domains: set[str]) -> None:
    h = header(path, len(domains))
    path.write_text("\n".join(h + ["", *sorted(domains)]) + "\n", encoding="utf-8")


def write_plain(path: Path, domains: set[str], category: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = [
        "# BlackRabbitZ DNS Blocklists - manual baseline",
        f"# Category: {category}",
        "# This file is the manually retained source-of-truth after the one-time cleanup.",
        "# Automatic upstream data is stored separately under sources/upstream/.",
        "",
        *sorted(domains),
    ]
    path.write_text("\n".join(text) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write cleaned categories and sources/manual")
    args = parser.parse_args()

    categories = {p.stem: read_domains(p) for p in sorted(CATEGORY_DIR.glob("*.txt"))}
    allow_roots = read_domains(ALLOWLIST)
    critical_roots = read_domains(CRITICAL)
    report: dict[str, dict[str, int]] = {}

    cleaned = {name: set(domains) for name, domains in categories.items()}
    for name, domains in cleaned.items():
        before = len(domains)
        # User allowlist is global; critical-service protection is conservative
        # and only applies to privacy/device categories.
        domains.difference_update({d for d in domains if is_suffix_match(d, allow_roots)})
        if name in PRIVACY_DEVICE:
            domains.difference_update({d for d in domains if is_suffix_match(d, critical_roots)})
        report[name] = {"before": before, "after_safety": len(domains), "removed_safety": before - len(domains)}

    tracker_specialised = set().union(*(cleaned.get(x, set()) for x in SPECIALISED_FOR_TRACKERS))
    if "trackers" in cleaned:
        before = len(cleaned["trackers"])
        cleaned["trackers"].difference_update(tracker_specialised)
        report["trackers"]["removed_specialised_overlap"] = before - len(cleaned["trackers"])

    telemetry_specialised = set().union(*(cleaned.get(x, set()) for x in SPECIALISED_FOR_TELEMETRY))
    if "telemetry" in cleaned:
        before = len(cleaned["telemetry"])
        cleaned["telemetry"].difference_update(telemetry_specialised)
        report["telemetry"]["removed_specialised_overlap"] = before - len(cleaned["telemetry"])

    for name in report:
        report[name]["final"] = len(cleaned[name])

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps({"mode": "applied" if args.apply else "dry-run", "categories": report}, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if args.apply:
        for name, domains in cleaned.items():
            write_category(CATEGORY_DIR / f"{name}.txt", domains)
            write_plain(MANUAL_DIR / f"{name}.txt", domains, name)

    total_removed = sum(v.get("before", 0) - v.get("final", 0) for v in report.values())
    print(f"Categories: {len(report)}; removed from broad/privacy lists: {total_removed:,}")
    for name, values in report.items():
        removed = values["before"] - values["final"]
        if removed:
            print(f"  {name}: {values['before']:,} -> {values['final']:,} (-{removed:,})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

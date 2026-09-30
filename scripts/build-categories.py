#!/usr/bin/env python3
"""Deterministically build category lists from manual + cached upstream sources."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORY_DIR = ROOT / "lists" / "categories"
MANUAL_DIR = ROOT / "sources" / "manual"
UPSTREAM_DIR = ROOT / "sources" / "upstream"
CONFIG_PATH = ROOT / "scripts" / "upstream-sources.json"
ALLOWLIST = ROOT / "config" / "allowlist.txt"
CRITICAL = ROOT / "config" / "critical-services.txt"
DOMAIN_RE = re.compile(r"^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?$", re.I)

TRACKER_SPECIALISED = {
    "telemetry", "social-trackers", "mobile-tracking", "affiliate-tracking", "consent-cmp",
    "windows-telemetry", "apple-telemetry", "android-telemetry", "linux-telemetry",
    "nas-telemetry", "server-telemetry", "native-tracking", "smart-tv", "iot", "gaming-telemetry",
}
TELEMETRY_SPECIALISED = {
    "mobile-tracking", "windows-telemetry", "apple-telemetry", "android-telemetry",
    "linux-telemetry", "nas-telemetry", "server-telemetry", "smart-tv", "iot", "gaming-telemetry",
}


def extract(line: str) -> str | None:
    d = line.strip().lower().rstrip(".")
    if not d or d.startswith(("#", "!", "@@")):
        return None
    if d.startswith("||") and "^" in d:
        d = d[2:].split("^", 1)[0]
    if " #" in d:
        d = d.split(" #", 1)[0].strip()
    if d.startswith("*."):
        d = d[2:]
    d = d.split()[0] if d.split() else ""
    return d if DOMAIN_RE.fullmatch(d) else None


def read(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {x for line in path.read_text(encoding="utf-8", errors="ignore").splitlines() if (x := extract(line))}


def protected(domain: str, roots: set[str]) -> bool:
    return any(domain == root or domain.endswith("." + root) for root in roots)


def header(path: Path, category: str, count: int) -> list[str]:
    old = path.read_text(encoding="utf-8", errors="ignore").splitlines() if path.exists() else []
    out: list[str] = []
    for line in old:
        if line.strip() == "" or line.startswith("#"):
            if line.startswith("# Entries:"):
                line = f"# Entries: {count}"
            if not line.startswith("# Auto-updated:"):
                out.append(line)
            continue
        break
    if not out:
        out = [
            "# BlackRabbitZ DNS Blocklists", f"# Category: {category}", "# Author: BlackRabbitZ",
            "# Repository: https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists",
            "# License: GPL-3.0-only for project-original material; third-party notices: THIRD_PARTY.md",
            f"# Entries: {count}",
        ]
    if not any(x.startswith("# Entries:") for x in out):
        out.append(f"# Entries: {count}")
    while out and out[-1] == "":
        out.pop()
    return out


def write(path: Path, category: str, domains: set[str]) -> None:
    h = header(path, category, len(domains))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(h + ["", *sorted(domains)]) + "\n", encoding="utf-8", newline="\n")


def collect(category: str) -> set[str]:
    domains = read(MANUAL_DIR / f"{category}.txt")
    cache_dir = UPSTREAM_DIR / category
    if cache_dir.exists():
        for path in sorted(cache_dir.glob("*.txt")):
            domains.update(read(path))
    return domains


def build_sets() -> dict[str, set[str]]:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    all_categories = {p.stem for p in MANUAL_DIR.glob("*.txt")} | set(config.get("categories", {}))
    allow_roots = read(ALLOWLIST)
    critical_roots = read(CRITICAL)
    sets = {category: collect(category) for category in sorted(all_categories)}

    # Explicit allowlist applies globally. Extra critical-service protection is
    # limited to categories that opt into protect_critical.
    for category in list(sets):
        sets[category] = {d for d in sets[category] if not protected(d, allow_roots)}
    for category, settings in config.get("categories", {}).items():
        if settings.get("protect_critical", False) and category in sets:
            sets[category] = {d for d in sets[category] if not protected(d, critical_roots)}

    # Keep broad lists broad: specialised telemetry/device/mobile domains live in
    # their own opt-in lists instead of silently making trackers more restrictive.
    specialised = set().union(*(sets.get(c, set()) for c in TRACKER_SPECIALISED))
    if "trackers" in sets:
        sets["trackers"].difference_update(specialised)

    specialised_telemetry = set().union(*(sets.get(c, set()) for c in TELEMETRY_SPECIALISED))
    if "telemetry" in sets:
        sets["telemetry"].difference_update(specialised_telemetry)
    return sets


def main() -> int:
    sets = build_sets()
    for category, domains in sets.items():
        write(CATEGORY_DIR / f"{category}.txt", category, domains)
    print(f"Built {len(sets)} category lists from manual + per-source upstream caches.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

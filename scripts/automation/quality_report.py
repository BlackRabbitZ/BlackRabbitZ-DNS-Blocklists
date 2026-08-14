#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import ROOT, category_files, is_allowlisted, load_allowlist, normalize_domain

JSON_OUT = ROOT / "metadata" / "quality.json"
MD_OUT = ROOT / "QUALITY.md"


def scan_file(path: Path, allowlist: set[str]) -> dict:
    entries = invalid = duplicates = out_of_order = allowlist_hits = 0
    previous: str | None = None
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        for raw in handle:
            text = raw.strip()
            if not text or text.startswith(("#", "!")):
                continue
            entries += 1
            domain = normalize_domain(text)
            if not domain:
                invalid += 1
                continue
            if previous is not None:
                if domain == previous:
                    duplicates += 1
                elif domain < previous:
                    out_of_order += 1
            previous = domain
            if is_allowlisted(domain, allowlist):
                allowlist_hits += 1
    return {
        "entries": entries,
        "invalid": invalid,
        "duplicates": duplicates,
        "out_of_order": out_of_order,
        "allowlist_collisions": allowlist_hits,
    }


def build_report() -> dict:
    allowlist = load_allowlist()
    files = {}
    totals = {"entries": 0, "invalid": 0, "duplicates": 0, "out_of_order": 0, "allowlist_collisions": 0}
    for path in category_files():
        result = scan_file(path, allowlist)
        files[path.name] = result
        for key in totals:
            totals[key] += result[key]
    return {"schema_version": 1, "totals": totals, "files": files}


def write_markdown(report: dict) -> str:
    totals = report["totals"]
    lines = [
        "# Qualitätsbericht",
        "",
        "Automatisch erzeugter Qualitätsstatus der Kategorie-Blocklisten.",
        "",
        "| Kennzahl | Wert |",
        "|---|---:|",
        f"| Einträge (Summe der Kategorien) | {totals['entries']:,} |",
        f"| Ungültige Domains | {totals['invalid']:,} |",
        f"| Duplikate innerhalb einer Datei | {totals['duplicates']:,} |",
        f"| Nicht sortierte Einträge | {totals['out_of_order']:,} |",
        f"| Allowlist-Kollisionen | {totals['allowlist_collisions']:,} |",
        "",
        "## Kategorien mit Auffälligkeiten",
        "",
        "| Datei | Ungültig | Duplikate | Sortierung | Allowlist |",
        "|---|---:|---:|---:|---:|",
    ]
    bad = 0
    for name, item in report["files"].items():
        if item["invalid"] or item["duplicates"] or item["out_of_order"] or item["allowlist_collisions"]:
            bad += 1
            lines.append(
                f"| `{name}` | {item['invalid']} | {item['duplicates']} | {item['out_of_order']} | {item['allowlist_collisions']} |"
            )
    if not bad:
        lines.append("| — | 0 | 0 | 0 | 0 |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Bei Qualitätsfehlern Exit 1 zurückgeben")
    parser.add_argument("--json-out", type=Path, default=JSON_OUT)
    parser.add_argument("--md-out", type=Path, default=MD_OUT)
    args = parser.parse_args()

    report = build_report()
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    args.md_out.write_text(write_markdown(report), encoding="utf-8")
    totals = report["totals"]
    print(json.dumps(totals, indent=2, sort_keys=True))
    failures = totals["invalid"] + totals["duplicates"] + totals["out_of_order"] + totals["allowlist_collisions"]
    return 1 if args.check and failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

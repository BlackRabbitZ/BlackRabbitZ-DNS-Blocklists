#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from common import ROOT

JSON_OUT = ROOT / "metadata" / "statistics.json"
MD_OUT = ROOT / "STATISTICS.md"


def count_payload(path: Path) -> int:
    count = 0
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        for raw in handle:
            text = raw.strip()
            if text and not text.startswith(("#", "!")):
                count += 1
    return count


def collect(directory: Path) -> dict[str, int]:
    return {path.name: count_payload(path) for path in sorted(directory.glob("*.txt"))}


def main() -> int:
    categories = collect(ROOT / "lists" / "categories")
    combined = collect(ROOT / "lists" / "combined")
    report = {
        "schema_version": 1,
        "category_files": len(categories),
        "category_entry_sum": sum(categories.values()),
        "combined_files": len(combined),
        "combined_entry_sum": sum(combined.values()),
        "categories": categories,
        "combined": combined,
    }
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "# Listen-Statistiken",
        "",
        "Automatisch erzeugte Größenübersicht. Die Summen sind Dateisummen und keine globale Deduplizierung über Kategorien hinweg.",
        "",
        f"- Kategorie-Dateien: **{len(categories):,}**",
        f"- Summe Kategorie-Einträge: **{sum(categories.values()):,}**",
        f"- Kombinierte Dateien: **{len(combined):,}**",
        f"- Summe kombinierte Einträge: **{sum(combined.values()):,}**",
        "",
        "## Kategorien",
        "",
        "| Datei | Einträge |",
        "|---|---:|",
    ]
    lines += [f"| `{name}` | {count:,} |" for name, count in sorted(categories.items())]
    lines += ["", "## Kombinierte Listen", "", "| Datei | Einträge |", "|---|---:|"]
    lines += [f"| `{name}` | {count:,} |" for name, count in sorted(combined.items())]
    lines.append("")
    MD_OUT.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("category_files", "category_entry_sum", "combined_files", "combined_entry_sum")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

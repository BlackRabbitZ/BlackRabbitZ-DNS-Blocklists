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
    seen: set[str] = set()

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

            if domain in seen:
                duplicates += 1
            else:
                seen.add(domain)

            if previous is not None and domain < previous:
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


def _update_entries_header(lines: list[str], count: int) -> list[str]:
    updated: list[str] = []
    replaced = False
    for line in lines:
        if line.startswith("# Entries:"):
            updated.append(f"# Entries: {count}")
            replaced = True
        else:
            updated.append(line)

    # Existing project files normally already contain this header.  If a file
    # has no metadata header at all, do not invent one here.
    return updated


def fix_file(path: Path, allowlist: set[str]) -> dict:
    """Canonicalize one category list without touching its leading metadata.

    The category format in this repository is a leading comment/header block
    followed by one domain per line.  To avoid accidentally destroying a
    manually structured file, automatic repair is skipped when a comment is
    found after the first payload entry.
    """

    raw_lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    header: list[str] = []
    domains: set[str] = set()
    payload_started = False
    has_inline_comments = False

    removed_invalid = 0
    removed_duplicates = 0
    removed_allowlist = 0
    normalized_entries = 0

    for raw in raw_lines:
        text = raw.strip()

        if not payload_started and (not text or text.startswith(("#", "!"))):
            header.append(raw.rstrip("\r\n"))
            continue

        if not text:
            # Empty payload lines have no semantic meaning and are omitted in
            # canonical output.
            continue

        if text.startswith(("#", "!")):
            has_inline_comments = True
            continue

        payload_started = True
        domain = normalize_domain(text)
        if not domain:
            removed_invalid += 1
            continue

        if is_allowlisted(domain, allowlist):
            removed_allowlist += 1
            continue

        if domain in domains:
            removed_duplicates += 1
            continue

        if domain != text:
            normalized_entries += 1
        domains.add(domain)

    if has_inline_comments:
        return {
            "changed": False,
            "skipped": True,
            "reason": "Kommentar innerhalb des Payload-Bereichs gefunden",
            "invalid_removed": 0,
            "duplicates_removed": 0,
            "allowlist_removed": 0,
            "normalized": 0,
            "entries_after": len(domains),
        }

    sorted_domains = sorted(domains)
    header = _update_entries_header(header, len(sorted_domains))

    # Keep exactly one trailing newline.  Leading metadata and its blank/#
    # separator are preserved as they already exist in the repository.
    output_lines = header + sorted_domains
    new_text = "\n".join(output_lines).rstrip("\n") + "\n"
    old_text = path.read_text(encoding="utf-8", errors="ignore").replace("\r\n", "\n")

    changed = new_text != old_text
    if changed:
        path.write_text(new_text, encoding="utf-8", newline="\n")

    return {
        "changed": changed,
        "skipped": False,
        "reason": "",
        "invalid_removed": removed_invalid,
        "duplicates_removed": removed_duplicates,
        "allowlist_removed": removed_allowlist,
        "normalized": normalized_entries,
        "entries_after": len(sorted_domains),
    }


def fix_all() -> dict:
    allowlist = load_allowlist()
    files: dict[str, dict] = {}
    totals = {
        "files_changed": 0,
        "files_skipped": 0,
        "invalid_removed": 0,
        "duplicates_removed": 0,
        "allowlist_removed": 0,
        "normalized": 0,
    }

    for path in category_files():
        result = fix_file(path, allowlist)
        name = path.relative_to(ROOT).as_posix()
        files[name] = result

        if result["changed"]:
            totals["files_changed"] += 1
        if result["skipped"]:
            totals["files_skipped"] += 1
        totals["invalid_removed"] += result["invalid_removed"]
        totals["duplicates_removed"] += result["duplicates_removed"]
        totals["allowlist_removed"] += result["allowlist_removed"]
        totals["normalized"] += result["normalized"]

    return {"totals": totals, "files": files}


def build_report() -> dict:
    allowlist = load_allowlist()
    files: dict[str, dict] = {}
    totals = {
        "entries": 0,
        "invalid": 0,
        "duplicates": 0,
        "out_of_order": 0,
        "allowlist_collisions": 0,
    }

    for path in category_files():
        result = scan_file(path, allowlist)
        files[path.relative_to(ROOT).as_posix()] = result
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
                f"| `{name}` | {item['invalid']} | {item['duplicates']} | "
                f"{item['out_of_order']} | {item['allowlist_collisions']} |"
            )

    if not bad:
        lines.append("| — | 0 | 0 | 0 | 0 |")

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Bei Qualitätsfehlern Exit 1 zurückgeben",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Kategorie-Dateien normalisieren, sortieren und sicher bereinigen",
    )
    parser.add_argument("--json-out", type=Path, default=JSON_OUT)
    parser.add_argument("--md-out", type=Path, default=MD_OUT)
    args = parser.parse_args()

    if args.fix:
        fixes = fix_all()
        print("Automatische Bereinigung:")
        print(json.dumps(fixes["totals"], indent=2, sort_keys=True))

        skipped = [name for name, item in fixes["files"].items() if item["skipped"]]
        if skipped:
            print("Nicht automatisch bearbeitete Dateien:")
            for name in skipped:
                print(f"- {name}: {fixes['files'][name]['reason']}")

    report = build_report()
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    args.md_out.write_text(write_markdown(report), encoding="utf-8")

    totals = report["totals"]
    print("Qualitätsstatus:")
    print(json.dumps(totals, indent=2, sort_keys=True))

    failures = (
        totals["invalid"]
        + totals["duplicates"]
        + totals["out_of_order"]
        + totals["allowlist_collisions"]
    )
    return 1 if args.check and failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

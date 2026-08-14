#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from common import ROOT, category_files, is_allowlisted, load_allowlist, normalize_domain, payload_lines


def changed_category_files(diff_range: str) -> list[Path]:
    proc = subprocess.run(
        ["git", "diff", "--name-only", diff_range, "--", "lists/categories"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    result = []
    for line in proc.stdout.splitlines():
        path = ROOT / line.strip()
        if path.suffix == ".txt" and path.exists():
            result.append(path)
    return sorted(set(result))


def check_json() -> list[str]:
    errors: list[str] = []
    for path in sorted((ROOT / "config").glob("*.json")) + sorted((ROOT / "scripts").glob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: ungültiges JSON: {exc}")
    return errors


def validate_file(path: Path, allowlist: set[str]) -> list[str]:
    errors: list[str] = []
    previous: str | None = None
    entries = 0
    declared: int | None = None
    with path.open("r", encoding="utf-8", errors="strict") as handle:
        for line_no, raw in enumerate(handle, start=1):
            text = raw.strip()
            if text.startswith("# Entries:"):
                try:
                    declared = int(text.split(":", 1)[1].strip().replace(".", "").replace(",", ""))
                except ValueError:
                    errors.append(f"{path.relative_to(ROOT)}:{line_no}: ungültiger Entries-Header")
                continue
            if not text or text.startswith(("#", "!")):
                continue
            entries += 1
            domain = normalize_domain(text)
            if not domain:
                errors.append(f"{path.relative_to(ROOT)}:{line_no}: ungültige Domain: {text[:160]}")
                if len(errors) >= 100:
                    break
                continue
            if previous is not None and domain <= previous:
                relation = "Duplikat" if domain == previous else "nicht sortiert"
                errors.append(f"{path.relative_to(ROOT)}:{line_no}: {relation}: {domain}")
            previous = domain
            if is_allowlisted(domain, allowlist):
                errors.append(f"{path.relative_to(ROOT)}:{line_no}: Allowlist-Kollision: {domain}")
            if len(errors) >= 100:
                break
    if declared is not None and declared != entries:
        errors.append(f"{path.relative_to(ROOT)}: Entries-Header {declared:,} != tatsächliche Einträge {entries:,}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--diff-range", help="Nur geänderte Kategorie-Dateien prüfen, z. B. BASE...HEAD")
    parser.add_argument("--full", action="store_true")
    args = parser.parse_args()

    errors = check_json()
    allowlist = load_allowlist()
    files = category_files() if args.full or not args.diff_range else changed_category_files(args.diff_range)
    print(f"Prüfe {len(files)} Kategorie-Datei(en).")
    for path in files:
        errors.extend(validate_file(path, allowlist))
        if len(errors) >= 200:
            break

    if errors:
        for error in errors[:200]:
            print(f"FEHLER: {error}")
        if len(errors) > 200:
            print(f"… {len(errors) - 200} weitere Fehler")
        return 1
    print("Repository-Validierung erfolgreich: JSON, Domains, Sortierung, Duplikate, Header und Allowlist geprüft.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

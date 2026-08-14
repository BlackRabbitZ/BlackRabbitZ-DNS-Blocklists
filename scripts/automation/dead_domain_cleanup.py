#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import ROOT, category_files, remove_domains_from_file
from dns_tools import check_domains

STATE_PATH = ROOT / "metadata" / "dns-health-state.json"


def main() -> int:
    parser = argparse.ArgumentParser(description="Entfernt erst nach mindestens drei getrennten NXDOMAIN-Bestätigungen.")
    parser.add_argument("--state", type=Path, default=STATE_PATH)
    parser.add_argument("--required-checks", type=int, default=3)
    parser.add_argument("--workers", type=int, default=24)
    parser.add_argument("--timeout", type=int, default=2)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.state.exists():
        print("Keine DNS-Health-State-Datei vorhanden; nichts zu bereinigen.")
        return 0
    state = json.loads(args.state.read_text(encoding="utf-8"))
    candidates: dict[str, dict] = state.get("candidates", {})
    ready = sorted(
        domain
        for domain, record in candidates.items()
        if len(set(record.get("checks", []))) >= args.required_checks
    )
    if not ready:
        print("Keine Domain hat die erforderliche Anzahl bestätigter NXDOMAIN-Prüfungen erreicht.")
        return 0

    print(f"Finale DNS-Gegenprüfung für {len(ready):,} Kandidaten …")
    final = check_domains(ready, timeout=args.timeout, workers=args.workers)
    dead = {item.domain for item in final if item.classification == "nxdomain"}
    recovered = {item.domain for item in final if item.classification == "exists"}
    temporary = {item.domain for item in final if item.classification == "temporary"}
    print(f"Bestätigt NXDOMAIN: {len(dead):,}; wieder vorhanden: {len(recovered):,}; temporär: {len(temporary):,}")

    removed = 0
    if not args.dry_run:
        for path in category_files():
            removed += remove_domains_from_file(path, dead)
        for domain in dead | recovered:
            candidates.pop(domain, None)
        state["candidates"] = dict(sorted(candidates.items()))
        args.state.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"Entfernte Listeneinträge: {removed:,}" if not args.dry_run else "Dry-run: keine Dateien geändert.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

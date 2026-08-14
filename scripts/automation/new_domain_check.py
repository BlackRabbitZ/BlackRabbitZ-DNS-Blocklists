#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

from common import ROOT, normalize_domain, remove_domains_from_file
from dns_tools import check_domains


def changed_additions(diff_range: str | None) -> dict[Path, set[str]]:
    command = ["git", "diff", "--unified=0", "--no-ext-diff"]
    if diff_range:
        command.append(diff_range)
    command += ["--", "lists/categories"]
    proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=True)
    current: Path | None = None
    additions: dict[Path, set[str]] = defaultdict(set)
    for line in proc.stdout.splitlines():
        if line.startswith("+++ b/"):
            current = ROOT / line[6:]
            continue
        if not current or not line.startswith("+") or line.startswith("+++"):
            continue
        text = line[1:].strip()
        if not text or text.startswith(("#", "!")):
            continue
        domain = normalize_domain(text)
        if domain:
            additions[current].add(domain)
    return additions


def main() -> int:
    parser = argparse.ArgumentParser(description="Prüft neu hinzugefügte Domains auf bestätigtes NXDOMAIN.")
    parser.add_argument("--diff-range", default=None, help="Git-Diff-Bereich, z. B. BASE...HEAD; leer = Working Tree gegen HEAD")
    parser.add_argument("--remove-nxdomain", action="store_true", help="Bestätigte NXDOMAIN-Einträge aus den betroffenen Dateien entfernen")
    parser.add_argument("--fail-on-nxdomain", action="store_true", help="Bei bestätigtem NXDOMAIN mit Fehler beenden")
    parser.add_argument("--max-domains", type=int, default=25000)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--timeout", type=int, default=2)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    additions = changed_additions(args.diff_range)
    domains = set().union(*additions.values()) if additions else set()
    if not domains:
        print("Keine neu hinzugefügten Domains gefunden.")
        return 0
    if len(domains) > args.max_domains:
        print(
            f"FEHLER: {len(domains):,} neue Domains überschreiten das DNS-Prüflimit von {args.max_domains:,}. "
            "Der Lauf wird absichtlich gestoppt, statt öffentliche Resolver mit einem Massencheck zu belasten.",
            file=sys.stderr,
        )
        return 3

    print(f"Prüfe {len(domains):,} neue Domains über Cloudflare und Google DNS …")
    results = check_domains(domains, timeout=args.timeout, workers=args.workers)
    dead = {item.domain for item in results if item.classification == "nxdomain"}
    temporary = [item for item in results if item.classification == "temporary"]
    exists = sum(1 for item in results if item.classification == "exists")

    removed = 0
    if dead and args.remove_nxdomain:
        for path, file_domains in additions.items():
            removed += remove_domains_from_file(path, dead & file_domains)

    print(f"DNS vorhanden : {exists:,}")
    print(f"NXDOMAIN      : {len(dead):,}")
    print(f"Temporär/unkl.: {len(temporary):,}")
    if removed:
        print(f"Entfernt      : {removed:,}")
    for domain in sorted(dead)[:100]:
        print(f"  NXDOMAIN {domain}")
    if len(dead) > 100:
        print(f"  … {len(dead) - 100:,} weitere NXDOMAIN")
    for item in temporary[:25]:
        print(f"  WARN {item.domain}: {', '.join(item.statuses)}")

    if args.report:
        payload = {
            "checked": len(results),
            "exists": exists,
            "nxdomain": len(dead),
            "temporary": len(temporary),
            "nxdomain_domains": sorted(dead)[:1000],
            "temporary_domains": [item.domain for item in temporary[:1000]],
        }
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if dead and args.fail_on_nxdomain:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

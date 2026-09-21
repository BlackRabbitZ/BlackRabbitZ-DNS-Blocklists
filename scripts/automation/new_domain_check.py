#!/usr/bin/env python3
"""
BlackRabbitZ DNS Blocklists - new-domain NXDOMAIN check

Purpose
-------
Inspect only domains newly added to lists/categories/ in the current Git diff.
For normal-sized updates, domains that are confirmed as NXDOMAIN are removed
again before generated profiles are rebuilt.

Large-update policy
-------------------
The old behavior aborted the whole GitHub Actions job when more than 25,000
new domains appeared. That made legitimate large upstream refreshes fail.

This version keeps the safety limit but supports an explicit oversize policy:
  --oversize-policy skip  -> do not perform a mass DNS check; continue safely
  --oversize-policy fail  -> preserve the old fail-closed behavior (exit 3)

The workflow supplied with this fix uses "skip". This avoids hammering public
DNS infrastructure while allowing the upstream refresh to complete.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import os
from pathlib import Path
import re
import subprocess
import sys
import threading
from typing import Dict, Iterable, List, Set, Tuple

try:
    import dns.exception
    import dns.resolver
except ImportError:
    print(
        "FEHLER: Python-Modul 'dnspython' fehlt. "
        "Installiere es mit: python3 -m pip install 'dnspython>=2.6,<3'",
        file=sys.stderr,
    )
    raise SystemExit(2)


DOMAIN_RE = re.compile(
    r"^(?=.{1,253}\.?$)(?:[A-Za-z0-9](?:[A-Za-z0-9_-]{0,61}[A-Za-z0-9])?\.)+[A-Za-z0-9-]{2,63}\.?$"
)

_thread_local = threading.local()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prüft neu hinzugefügte Blocklist-Domains auf bestätigtes NXDOMAIN."
    )
    parser.add_argument(
        "--path",
        default="./lists/categories",
        help="Kategorie-Verzeichnis (Standard: ./lists/categories)",
    )
    parser.add_argument(
        "--max-domains",
        type=int,
        default=25_000,
        help="Maximale Anzahl Domains für einen Live-DNS-Check (Standard: 25000)",
    )
    parser.add_argument(
        "--oversize-policy",
        choices=("skip", "fail"),
        default="skip",
        help="Verhalten oberhalb des Limits: skip oder fail (Standard: skip)",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=24,
        help="Parallele DNS-Prüfungen für normale Batches (Standard: 24)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=2.0,
        help="DNS-Timeout/Lifetime pro Anfrage in Sekunden (Standard: 2.0)",
    )
    return parser.parse_args()


def is_domain(value: str) -> bool:
    value = value.strip().rstrip(".").lower()
    if not value or value.startswith("#"):
        return False
    if "/" in value or " " in value or "\t" in value:
        return False
    if value in {"localhost", "localhost.localdomain"}:
        return False
    return bool(DOMAIN_RE.fullmatch(value))


def normalize_domain(line: str) -> str | None:
    value = line.strip()
    if not value or value.startswith("#"):
        return None

    # Category files are expected to contain one plain domain per line.
    # Tolerate an inline comment without treating it as part of the domain.
    if " #" in value:
        value = value.split(" #", 1)[0].strip()

    value = value.rstrip(".").lower()
    return value if is_domain(value) else None


def git_added_domains(category_dir: Path) -> Dict[str, Set[Path]]:
    """
    Return {domain: {file1, file2, ...}} for newly added lines under category_dir.
    Uses the current working-tree diff against HEAD, which is exactly the state
    after scripts/update-upstreams.py changed category files.
    """
    repo_root = Path.cwd().resolve()
    category_abs = category_dir.resolve()

    try:
        rel = category_abs.relative_to(repo_root)
    except ValueError:
        print(
            f"FEHLER: --path muss innerhalb des Repositorys liegen: {category_abs}",
            file=sys.stderr,
        )
        raise SystemExit(2)

    proc = subprocess.run(
        ["git", "diff", "--no-color", "--unified=0", "--", str(rel)],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        print("FEHLER: git diff konnte nicht gelesen werden.", file=sys.stderr)
        if proc.stderr:
            print(proc.stderr.rstrip(), file=sys.stderr)
        raise SystemExit(2)

    additions: Dict[str, Set[Path]] = {}
    current_file: Path | None = None

    for raw in proc.stdout.splitlines():
        if raw.startswith("+++ "):
            marker = raw[4:].strip()
            if marker == "/dev/null":
                current_file = None
                continue
            if marker.startswith("b/"):
                marker = marker[2:]
            candidate = (repo_root / marker).resolve()
            try:
                candidate.relative_to(category_abs)
            except ValueError:
                current_file = None
                continue
            current_file = candidate
            continue

        if current_file is None:
            continue
        if not raw.startswith("+") or raw.startswith("+++"):
            continue

        domain = normalize_domain(raw[1:])
        if domain:
            additions.setdefault(domain, set()).add(current_file)

    return additions


def get_resolver(timeout: float):
    resolver = getattr(_thread_local, "resolver", None)
    current_timeout = getattr(_thread_local, "resolver_timeout", None)
    if resolver is None or current_timeout != timeout:
        resolver = dns.resolver.Resolver(configure=True)
        resolver.timeout = timeout
        resolver.lifetime = timeout
        _thread_local.resolver = resolver
        _thread_local.resolver_timeout = timeout
    return resolver


def check_domain(domain: str, timeout: float) -> Tuple[str, str]:
    """
    Returns:
      ("nxdomain", domain) -> DNS says the name does not exist
      ("exists", domain)   -> domain exists, even if it has no A record
      ("unknown", domain)  -> timeout/SERVFAIL/no resolver/etc.; never delete
    """
    resolver = get_resolver(timeout)

    try:
        # raise_on_no_answer=False means an existing name without an A record
        # is not incorrectly treated as NXDOMAIN.
        resolver.resolve(
            domain,
            "A",
            search=False,
            raise_on_no_answer=False,
        )
        return ("exists", domain)
    except dns.resolver.NXDOMAIN:
        return ("nxdomain", domain)
    except (
        dns.resolver.NoNameservers,
        dns.resolver.YXDOMAIN,
        dns.exception.Timeout,
        dns.resolver.LifetimeTimeout,
        OSError,
    ):
        return ("unknown", domain)
    except Exception:
        # Quality check must never delete a domain on an ambiguous resolver error.
        return ("unknown", domain)


def remove_domains(domains: Set[str], domain_files: Dict[str, Set[Path]]) -> int:
    by_file: Dict[Path, Set[str]] = {}
    for domain in domains:
        for path in domain_files.get(domain, set()):
            by_file.setdefault(path, set()).add(domain)

    removed = 0
    for path, remove_set in sorted(by_file.items(), key=lambda item: str(item[0])):
        try:
            original = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            continue

        lines = original.splitlines()
        kept: List[str] = []

        for line in lines:
            domain = normalize_domain(line)
            if domain is not None and domain in remove_set:
                removed += 1
                continue
            kept.append(line)

        # Preserve normal text-file convention used by the repository.
        new_text = "\n".join(kept)
        if original.endswith("\n") or kept:
            new_text += "\n"

        if new_text != original:
            path.write_text(new_text, encoding="utf-8", newline="\n")
            print(
                f"NXDOMAIN bereinigt: {path.as_posix()} "
                f"({len(remove_set)} Kandidat(en))"
            )

    return removed


def main() -> int:
    args = parse_args()

    if args.max_domains < 1:
        print("FEHLER: --max-domains muss >= 1 sein.", file=sys.stderr)
        return 2
    if args.workers < 1:
        print("FEHLER: --workers muss >= 1 sein.", file=sys.stderr)
        return 2
    if args.timeout <= 0:
        print("FEHLER: --timeout muss > 0 sein.", file=sys.stderr)
        return 2

    category_dir = Path(args.path)
    additions = git_added_domains(category_dir)
    domains = sorted(additions)
    count = len(domains)

    if count == 0:
        print("Keine neuen Domains für die NXDOMAIN-Prüfung gefunden.")
        return 0

    print(f"Neue Domains im aktuellen Upstream-Diff: {count:,}")

    if count > args.max_domains:
        if args.oversize_policy == "fail":
            print(
                f"FEHLER: {count:,} neue Domains überschreiten das DNS-Prüflimit "
                f"von {args.max_domains:,}. Der Lauf wird absichtlich gestoppt, "
                "statt öffentliche Resolver mit einem Massencheck zu belasten.",
                file=sys.stderr,
            )
            return 3

        print(
            f"HINWEIS: {count:,} neue Domains überschreiten das DNS-Prüflimit "
            f"von {args.max_domains:,}. Die Live-NXDOMAIN-Prüfung wird für diesen "
            "Lauf übersprungen. Der Upstream-Import darf weiterlaufen; es werden "
            "keine Massenabfragen an DNS-Resolver gesendet."
        )
        return 0

    workers = min(args.workers, max(1, count))
    print(
        f"NXDOMAIN-Prüfung läuft für {count:,} Domain(s) "
        f"mit maximal {workers} parallelen Abfragen …"
    )

    nxdomain: Set[str] = set()
    unknown = 0
    exists = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [
            executor.submit(check_domain, domain, args.timeout)
            for domain in domains
        ]

        for future in concurrent.futures.as_completed(futures):
            status, domain = future.result()
            if status == "nxdomain":
                nxdomain.add(domain)
            elif status == "exists":
                exists += 1
            else:
                unknown += 1

    print(
        "DNS-Prüfung abgeschlossen: "
        f"existiert={exists:,}, NXDOMAIN={len(nxdomain):,}, "
        f"unklar/Timeout={unknown:,}"
    )

    if not nxdomain:
        print("Keine bestätigten NXDOMAINs aus den neuen Upstream-Zugängen entfernt.")
        return 0

    removed = remove_domains(nxdomain, additions)
    print(
        f"Fertig: {removed:,} neu hinzugefügte NXDOMAIN-Zeile(n) "
        "aus Kategorie-Dateien entfernt."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

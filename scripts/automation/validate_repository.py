#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ipaddress
import json
import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

from common import ROOT, load_allowlist, normalize_domain

LIST_DIRS = {
    "categories": ROOT / "lists" / "categories",
    "combined": ROOT / "lists" / "combined",
    "ips": ROOT / "lists" / "ips",
    "regex": ROOT / "lists" / "regex",
}

ENTRY_HEADER_RE = re.compile(
    r"^#\s*Entries(?:\s+in\s+this\s+file)?\s*:\s*([\d.,]+)\s*$",
    re.IGNORECASE,
)

MAX_ERRORS_PER_FILE = 50
MAX_ERRORS_TOTAL = 300


@dataclass
class Issue:
    path: Path
    line: int | None
    message: str

    def plain(self) -> str:
        rel = self.path.relative_to(ROOT)
        if self.line is None:
            return f"{rel}: {self.message}"
        return f"{rel}:{self.line}: {self.message}"


@dataclass
class Stats:
    files: int = 0
    entries: int = 0
    duplicates: int = 0
    invalid: int = 0
    unsorted: int = 0
    allowlist_collisions: int = 0
    header_errors: int = 0

    def add(self, other: "Stats") -> None:
        self.files += other.files
        self.entries += other.entries
        self.duplicates += other.duplicates
        self.invalid += other.invalid
        self.unsorted += other.unsorted
        self.allowlist_collisions += other.allowlist_collisions
        self.header_errors += other.header_errors


def parse_declared_entries(text: str) -> int | None:
    match = ENTRY_HEADER_RE.match(text)
    if not match:
        return None
    number = match.group(1).replace(".", "").replace(",", "")
    try:
        return int(number)
    except ValueError:
        return None


def fast_is_allowlisted(domain: str, allowlist: set[str]) -> bool:
    """Gleiche Semantik wie domain == item / Subdomain, aber ohne O(N*M)-Scan."""
    if not allowlist:
        return False
    parts = domain.split(".")
    return any(".".join(parts[index:]) in allowlist for index in range(len(parts)))


def changed_files(diff_range: str, scope: str) -> list[Path]:
    directory = LIST_DIRS[scope]
    rel_dir = directory.relative_to(ROOT)

    proc = subprocess.run(
        ["git", "diff", "--name-only", diff_range, "--", str(rel_dir)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )

    result: list[Path] = []
    for line in proc.stdout.splitlines():
        path = ROOT / line.strip()
        if path.suffix.lower() == ".txt" and path.exists() and path.is_file():
            result.append(path)

    return sorted(set(result))


def scope_files(scope: str, diff_range: str | None) -> list[Path]:
    if diff_range:
        return changed_files(diff_range, scope)
    directory = LIST_DIRS[scope]
    if not directory.exists():
        return []
    return sorted(path for path in directory.glob("*.txt") if path.is_file())


def check_json() -> list[Issue]:
    issues: list[Issue] = []
    paths = (
        sorted((ROOT / "config").glob("*.json"))
        + sorted((ROOT / "scripts").glob("*.json"))
    )

    for path in paths:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            issues.append(Issue(path, None, f"ungültiges JSON: {exc}"))

    return issues


def _read_payload(path: Path):
    with path.open("r", encoding="utf-8", errors="strict") as handle:
        for line_no, raw in enumerate(handle, start=1):
            text = raw.strip()
            yield line_no, text


def validate_domain_file(
    path: Path,
    *,
    allowlist: set[str],
    check_allowlist: bool,
) -> tuple[list[Issue], Stats]:
    issues: list[Issue] = []
    stats = Stats(files=1)
    seen: set[str] = set()
    previous: str | None = None
    declared: int | None = None

    try:
        iterator = _read_payload(path)
        for line_no, text in iterator:
            parsed_header = parse_declared_entries(text)
            if parsed_header is not None:
                declared = parsed_header
                continue

            if not text or text.startswith(("#", "!")):
                continue

            stats.entries += 1
            domain = normalize_domain(text)

            if not domain:
                stats.invalid += 1
                issues.append(Issue(path, line_no, f"ungültige Domain: {text[:160]}"))
                if len(issues) >= MAX_ERRORS_PER_FILE:
                    break
                continue

            # Set-basierte Prüfung erkennt Duplikate auch dann, wenn die Datei
            # versehentlich nicht mehr sortiert ist.
            if domain in seen:
                stats.duplicates += 1
                issues.append(Issue(path, line_no, f"Duplikat: {domain}"))
            else:
                seen.add(domain)

            if previous is not None and domain < previous:
                stats.unsorted += 1
                issues.append(
                    Issue(
                        path,
                        line_no,
                        f"nicht sortiert: {domain} steht nach {previous}",
                    )
                )
            previous = domain

            if check_allowlist and fast_is_allowlisted(domain, allowlist):
                stats.allowlist_collisions += 1
                issues.append(Issue(path, line_no, f"Allowlist-Kollision: {domain}"))

            if len(issues) >= MAX_ERRORS_PER_FILE:
                break

    except UnicodeDecodeError as exc:
        stats.invalid += 1
        issues.append(Issue(path, None, f"Datei ist nicht gültiges UTF-8: {exc}"))
    except OSError as exc:
        stats.invalid += 1
        issues.append(Issue(path, None, f"Datei konnte nicht gelesen werden: {exc}"))

    if declared is not None and declared != stats.entries:
        stats.header_errors += 1
        issues.append(
            Issue(
                path,
                None,
                f"Entries-Header {declared:,} != tatsächliche Einträge {stats.entries:,}",
            )
        )

    return issues, stats


def validate_ip_file(path: Path) -> tuple[list[Issue], Stats]:
    issues: list[Issue] = []
    stats = Stats(files=1)
    seen: set[str] = set()
    previous: str | None = None
    declared: int | None = None

    expected_version: int | None = None
    lower_name = path.name.lower()
    if "ipv4" in lower_name:
        expected_version = 4
    elif "ipv6" in lower_name:
        expected_version = 6

    try:
        for line_no, text in _read_payload(path):
            parsed_header = parse_declared_entries(text)
            if parsed_header is not None:
                declared = parsed_header
                continue

            if not text or text.startswith(("#", "!")):
                continue

            stats.entries += 1

            try:
                address = ipaddress.ip_address(text)
            except ValueError:
                stats.invalid += 1
                issues.append(Issue(path, line_no, f"ungültige IP-Adresse: {text[:160]}"))
                if len(issues) >= MAX_ERRORS_PER_FILE:
                    break
                continue

            if expected_version is not None and address.version != expected_version:
                stats.invalid += 1
                issues.append(
                    Issue(
                        path,
                        line_no,
                        f"falsche IP-Version: erwartet IPv{expected_version}, gefunden IPv{address.version}: {text}",
                    )
                )

            canonical = str(address)

            if canonical in seen:
                stats.duplicates += 1
                issues.append(Issue(path, line_no, f"Duplikat: {canonical}"))
            else:
                seen.add(canonical)

            # Die bestehenden BlackRabbitZ-IP-Listen sind textuell sortiert.
            if previous is not None and canonical < previous:
                stats.unsorted += 1
                issues.append(
                    Issue(
                        path,
                        line_no,
                        f"nicht sortiert: {canonical} steht nach {previous}",
                    )
                )
            previous = canonical

            if len(issues) >= MAX_ERRORS_PER_FILE:
                break

    except UnicodeDecodeError as exc:
        stats.invalid += 1
        issues.append(Issue(path, None, f"Datei ist nicht gültiges UTF-8: {exc}"))
    except OSError as exc:
        stats.invalid += 1
        issues.append(Issue(path, None, f"Datei konnte nicht gelesen werden: {exc}"))

    if declared is not None and declared != stats.entries:
        stats.header_errors += 1
        issues.append(
            Issue(
                path,
                None,
                f"Entries-Header {declared:,} != tatsächliche Einträge {stats.entries:,}",
            )
        )

    return issues, stats


def validate_regex_pattern(pattern: str) -> str | None:
    """Prüft bevorzugt mit GNU grep -P (PCRE). Python-re ist nur Fallback."""
    grep = shutil.which("grep")

    if grep:
        try:
            proc = subprocess.run(
                [grep, "-P", "-e", pattern],
                input="",
                text=True,
                capture_output=True,
                timeout=5,
                check=False,
            )
        except subprocess.TimeoutExpired:
            return "RegEx-Kompilierung hat das Zeitlimit überschritten"

        # grep: 0 = Match, 1 = kein Match aber gültiger Ausdruck, >1 = Fehler.
        if proc.returncode in (0, 1):
            return None
        message = (proc.stderr or proc.stdout).strip()
        return message or f"PCRE-Prüfung fehlgeschlagen (Exit {proc.returncode})"

    try:
        re.compile(pattern)
    except re.error as exc:
        return str(exc)

    return None


def validate_regex_file(path: Path) -> tuple[list[Issue], Stats]:
    issues: list[Issue] = []
    stats = Stats(files=1)
    seen: set[str] = set()
    declared: int | None = None

    try:
        for line_no, text in _read_payload(path):
            parsed_header = parse_declared_entries(text)
            if parsed_header is not None:
                declared = parsed_header
                continue

            if not text or text.startswith(("#", "!")):
                continue

            stats.entries += 1

            if text in seen:
                stats.duplicates += 1
                issues.append(Issue(path, line_no, f"Duplikat-RegEx: {text[:160]}"))
            else:
                seen.add(text)

            regex_error = validate_regex_pattern(text)
            if regex_error:
                stats.invalid += 1
                issues.append(
                    Issue(path, line_no, f"ungültige RegEx: {regex_error}: {text[:160]}")
                )

            if len(issues) >= MAX_ERRORS_PER_FILE:
                break

    except UnicodeDecodeError as exc:
        stats.invalid += 1
        issues.append(Issue(path, None, f"Datei ist nicht gültiges UTF-8: {exc}"))
    except OSError as exc:
        stats.invalid += 1
        issues.append(Issue(path, None, f"Datei konnte nicht gelesen werden: {exc}"))

    if declared is not None and declared != stats.entries:
        stats.header_errors += 1
        issues.append(
            Issue(
                path,
                None,
                f"Entries-Header {declared:,} != tatsächliche Einträge {stats.entries:,}",
            )
        )

    return issues, stats


def print_stats(scope: str, stats: Stats) -> None:
    labels = {
        "categories": "Kategorie-Blocklisten",
        "combined": "Kombinierte Profile",
        "ips": "IP-Blocklisten",
        "regex": "RegEx-Blocklisten",
    }
    print(f"\n=== {labels[scope]} ===")
    print(f"Dateien:              {stats.files:,}")
    print(f"Einträge:              {stats.entries:,}")
    print(f"Duplikate:             {stats.duplicates:,}")
    print(f"Ungültige Einträge:    {stats.invalid:,}")
    if scope != "regex":
        print(f"Sortierungsfehler:     {stats.unsorted:,}")
    if scope in {"categories", "combined"}:
        print(f"Allowlist-Kollisionen: {stats.allowlist_collisions:,}")
    print(f"Header-Fehler:         {stats.header_errors:,}")


def emit_issue(issue: Issue) -> None:
    print(f"FEHLER: {issue.plain()}")

    if os.environ.get("GITHUB_ACTIONS") == "true":
        rel = issue.path.relative_to(ROOT)
        message = issue.message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
        if issue.line is None:
            print(f"::error file={rel}::{message}")
        else:
            print(f"::error file={rel},line={issue.line}::{message}")


def validate_scope(
    scope: str,
    *,
    diff_range: str | None,
    allowlist: set[str],
) -> tuple[list[Issue], Stats]:
    files = scope_files(scope, diff_range)
    print(f"\nPrüfe {len(files)} Datei(en) in lists/{scope}/.")

    all_issues: list[Issue] = []
    total = Stats()

    for path in files:
        if scope in {"categories", "combined"}:
            issues, stats = validate_domain_file(
                path,
                allowlist=allowlist,
                check_allowlist=True,
            )
        elif scope == "ips":
            issues, stats = validate_ip_file(path)
        elif scope == "regex":
            issues, stats = validate_regex_file(path)
        else:
            raise ValueError(f"Unbekannter Scope: {scope}")

        all_issues.extend(issues)
        total.add(stats)

        if len(all_issues) >= MAX_ERRORS_TOTAL:
            break

    return all_issues, total


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Vollständige BlackRabbitZ-Blocklisten-Validierung"
    )
    parser.add_argument(
        "--scope",
        choices=("all", "categories", "combined", "ips", "regex", "config"),
        default="all",
        help="Welche Repository-Bereiche geprüft werden sollen",
    )
    parser.add_argument(
        "--diff-range",
        help="Nur geänderte Listen in diesem Git-Diff prüfen, z. B. BASE...HEAD",
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="Alle Dateien des gewählten Scopes prüfen (Standard ohne --diff-range)",
    )
    args = parser.parse_args()

    print("====================================================")
    print(" BlackRabbitZ DNS Blocklists - Repository Validator")
    print("====================================================")

    all_issues: list[Issue] = []

    if args.scope in {"all", "config"}:
        print("\n=== JSON-Konfiguration ===")
        json_issues = check_json()
        if json_issues:
            all_issues.extend(json_issues)
            print(f"JSON-Fehler: {len(json_issues)}")
        else:
            print("JSON-Konfiguration: OK")

    if args.scope == "config":
        if all_issues:
            for issue in all_issues[:MAX_ERRORS_TOTAL]:
                emit_issue(issue)
            return 1
        print("\n✅ Konfigurationsprüfung erfolgreich.")
        return 0

    allowlist = load_allowlist()
    scopes = (
        ("categories", "combined", "ips", "regex")
        if args.scope == "all"
        else (args.scope,)
    )

    for scope in scopes:
        issues, stats = validate_scope(
            scope,
            diff_range=args.diff_range,
            allowlist=allowlist,
        )
        print_stats(scope, stats)
        all_issues.extend(issues)

        if len(all_issues) >= MAX_ERRORS_TOTAL:
            break

    if all_issues:
        print("\n====================================================")
        print(f"❌ VALIDIERUNG FEHLGESCHLAGEN: {len(all_issues)} Fehler")
        print("====================================================")
        for issue in all_issues[:MAX_ERRORS_TOTAL]:
            emit_issue(issue)
        if len(all_issues) > MAX_ERRORS_TOTAL:
            print(f"... {len(all_issues) - MAX_ERRORS_TOTAL} weitere Fehler")
        return 1

    print("\n====================================================")
    print("✅ ALLE GEPRÜFTEN BLACKRABBITZ-LISTEN SIND GÜLTIG")
    print("====================================================")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

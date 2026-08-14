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

# Ein Adblock-Host darf auch nur aus einem TLD-Label bestehen, z. B. ||actor^.
ADBLOCK_HOST_RE = re.compile(
    r"^(?=.{1,253}$)"
    r"(?:[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?\.)*"
    r"[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?$",
    re.IGNORECASE,
)

MAX_ISSUES_PER_FILE = 50
MAX_ISSUES_TO_PRINT = 300


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
    adblock_files: int = 0
    duplicates: int = 0
    invalid: int = 0
    unsorted: int = 0
    allowlist_collisions: int = 0
    header_errors: int = 0

    def add(self, other: "Stats") -> None:
        self.files += other.files
        self.entries += other.entries
        self.adblock_files += other.adblock_files
        self.duplicates += other.duplicates
        self.invalid += other.invalid
        self.unsorted += other.unsorted
        self.allowlist_collisions += other.allowlist_collisions
        self.header_errors += other.header_errors

    @property
    def errors(self) -> int:
        return (
            self.duplicates
            + self.invalid
            + self.unsorted
            + self.allowlist_collisions
            + self.header_errors
        )


def add_issue(issues: list[Issue], issue: Issue) -> None:
    """Details begrenzen, Prüfung und Zähler aber NIE vorzeitig abbrechen."""
    if len(issues) < MAX_ISSUES_PER_FILE:
        issues.append(issue)


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
            yield line_no, raw.strip()


def detect_category_format(path: Path) -> str:
    """
    Erkennt gemischte Kategorieformate.

    Rückgabe:
      - "adblock" für Adblock Plus / AdGuard Filterlisten
      - "domains" für normale DNS-Domainlisten
    """
    try:
        with path.open("r", encoding="utf-8", errors="strict") as handle:
            for index, raw in enumerate(handle):
                if index >= 250:
                    break
                text = raw.strip()
                lowered = text.lower()

                if lowered in {"[adblock plus]", "[adblock]"}:
                    return "adblock"

                if lowered.startswith("! syntax:") and "adblock" in lowered:
                    return "adblock"

                # Starker Indikator für DNS-artige Adblock-Regeln.
                if text.startswith(("||", "@@||")) and "^" in text:
                    return "adblock"

    except (UnicodeDecodeError, OSError):
        # Der eigentliche Validator erzeugt später die konkrete Fehlermeldung.
        pass

    return "domains"


def header_count_non_hash_unique(path: Path) -> int:
    """
    Spiegelt die bestehende count_entries()-Logik aus scripts/update-lists.sh:
    - leere Zeilen ignorieren
    - Zeilen mit # ignorieren
    - alle übrigen eindeutigen Zeilen zählen

    Dadurch werden bei Adblock-Dateien absichtlich auch [Adblock Plus] und
    !-Metadaten so gezählt, wie es der bestehende Repository-Build bereits tut.
    """
    seen: set[str] = set()

    with path.open("r", encoding="utf-8", errors="strict") as handle:
        for raw in handle:
            text = raw.rstrip("\r\n").strip()
            if not text or text.startswith("#"):
                continue
            seen.add(text)

    return len(seen)


def declared_entries_for_file(path: Path) -> int | None:
    with path.open("r", encoding="utf-8", errors="strict") as handle:
        for raw in handle:
            parsed = parse_declared_entries(raw.strip())
            if parsed is not None:
                return parsed
    return None


def normalize_adblock_host(value: str) -> str | None:
    value = value.strip().lower().rstrip(".")
    if not value:
        return None

    try:
        value = value.encode("idna").decode("ascii")
    except (UnicodeError, ValueError):
        return None

    return value if ADBLOCK_HOST_RE.fullmatch(value) else None


def parse_adblock_rule(text: str) -> tuple[str | None, str | None]:
    """
    Validiert DNS-artige Adblock-Regeln wie:
      ||example.com^
      ||actor^
      @@||example.com^
      ||example.com^$important

    Rückgabe: (host, fehler)
    """
    rule = text.strip()

    if rule.startswith("@@"):
        rule = rule[2:]

    if not rule.startswith("||"):
        return None, "nicht unterstützte Adblock-Regel (erwartet ||host^)"

    body = rule[2:]
    if "^" not in body:
        return None, "Adblock-Regel ohne ^-Separator"

    host, suffix = body.split("^", 1)

    # Nach ^ dürfen keine beliebigen Zeichen stehen; Filteroptionen beginnen mit $.
    if suffix and not suffix.startswith("$"):
        return None, f"unerwarteter Inhalt nach ^: {suffix[:80]}"

    host = normalize_adblock_host(host)
    if host is None:
        return None, "ungültiger Host in Adblock-Regel"

    return host, None


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

    try:
        declared = declared_entries_for_file(path)

        for line_no, text in _read_payload(path):
            if parse_declared_entries(text) is not None:
                continue

            if not text or text.startswith(("#", "!")):
                continue

            stats.entries += 1
            domain = normalize_domain(text)

            if not domain:
                stats.invalid += 1
                add_issue(
                    issues,
                    Issue(path, line_no, f"ungültige Domain: {text[:160]}"),
                )
                continue

            if domain in seen:
                stats.duplicates += 1
                add_issue(issues, Issue(path, line_no, f"Duplikat: {domain}"))
            else:
                seen.add(domain)

            if previous is not None and domain < previous:
                stats.unsorted += 1
                add_issue(
                    issues,
                    Issue(
                        path,
                        line_no,
                        f"nicht sortiert: {domain} steht nach {previous}",
                    ),
                )
            previous = domain

            if check_allowlist and fast_is_allowlisted(domain, allowlist):
                stats.allowlist_collisions += 1
                add_issue(
                    issues,
                    Issue(path, line_no, f"Allowlist-Kollision: {domain}"),
                )

        if declared is not None:
            actual_header_count = header_count_non_hash_unique(path)
            if declared != actual_header_count:
                stats.header_errors += 1
                add_issue(
                    issues,
                    Issue(
                        path,
                        None,
                        f"Entries-Header {declared:,} != Build-Zählung {actual_header_count:,}",
                    ),
                )

    except UnicodeDecodeError as exc:
        stats.invalid += 1
        add_issue(
            issues,
            Issue(path, None, f"Datei ist nicht gültiges UTF-8: {exc}"),
        )
    except OSError as exc:
        stats.invalid += 1
        add_issue(
            issues,
            Issue(path, None, f"Datei konnte nicht gelesen werden: {exc}"),
        )

    return issues, stats


def validate_adblock_file(
    path: Path,
    *,
    allowlist: set[str],
) -> tuple[list[Issue], Stats]:
    issues: list[Issue] = []
    stats = Stats(files=1, adblock_files=1)
    seen_rules: set[str] = set()
    previous_rule: str | None = None

    try:
        declared = declared_entries_for_file(path)
        saw_header = False

        for line_no, text in _read_payload(path):
            if parse_declared_entries(text) is not None:
                continue

            if not text or text.startswith("#"):
                continue

            # Adblock-Dateikopf und Metadaten sind gültig, aber keine Filterregel.
            if text.lower() in {"[adblock plus]", "[adblock]"}:
                saw_header = True
                continue

            if text.startswith("!"):
                continue

            stats.entries += 1

            normalized_rule = text.lower()
            if normalized_rule in seen_rules:
                stats.duplicates += 1
                add_issue(
                    issues,
                    Issue(path, line_no, f"Duplikat-Adblock-Regel: {text[:160]}"),
                )
            else:
                seen_rules.add(normalized_rule)

            host, error = parse_adblock_rule(text)
            if error:
                stats.invalid += 1
                add_issue(
                    issues,
                    Issue(path, line_no, f"ungültige Adblock-Regel: {error}: {text[:160]}"),
                )
                continue

            # Sortierung nur unter tatsächlichen Regeln prüfen.
            if previous_rule is not None and normalized_rule < previous_rule:
                stats.unsorted += 1
                add_issue(
                    issues,
                    Issue(
                        path,
                        line_no,
                        f"Adblock-Regeln nicht sortiert: {text[:120]}",
                    ),
                )
            previous_rule = normalized_rule

            if host and fast_is_allowlisted(host, allowlist):
                stats.allowlist_collisions += 1
                add_issue(
                    issues,
                    Issue(path, line_no, f"Allowlist-Kollision in Adblock-Regel: {host}"),
                )

        if not saw_header:
            stats.invalid += 1
            add_issue(
                issues,
                Issue(path, None, "Adblock-Format erkannt, aber [Adblock Plus]-Header fehlt"),
            )

        if declared is not None:
            actual_header_count = header_count_non_hash_unique(path)
            if declared != actual_header_count:
                stats.header_errors += 1
                add_issue(
                    issues,
                    Issue(
                        path,
                        None,
                        f"Entries-Header {declared:,} != Build-Zählung {actual_header_count:,}",
                    ),
                )

    except UnicodeDecodeError as exc:
        stats.invalid += 1
        add_issue(
            issues,
            Issue(path, None, f"Datei ist nicht gültiges UTF-8: {exc}"),
        )
    except OSError as exc:
        stats.invalid += 1
        add_issue(
            issues,
            Issue(path, None, f"Datei konnte nicht gelesen werden: {exc}"),
        )

    return issues, stats


def validate_ip_file(path: Path) -> tuple[list[Issue], Stats]:
    issues: list[Issue] = []
    stats = Stats(files=1)
    seen: set[str] = set()
    previous: str | None = None

    expected_version: int | None = None
    lower_name = path.name.lower()
    if "ipv4" in lower_name:
        expected_version = 4
    elif "ipv6" in lower_name:
        expected_version = 6

    try:
        declared = declared_entries_for_file(path)

        for line_no, text in _read_payload(path):
            if parse_declared_entries(text) is not None:
                continue

            if not text or text.startswith(("#", "!")):
                continue

            stats.entries += 1

            try:
                address = ipaddress.ip_address(text)
            except ValueError:
                stats.invalid += 1
                add_issue(
                    issues,
                    Issue(path, line_no, f"ungültige IP-Adresse: {text[:160]}"),
                )
                continue

            if expected_version is not None and address.version != expected_version:
                stats.invalid += 1
                add_issue(
                    issues,
                    Issue(
                        path,
                        line_no,
                        f"falsche IP-Version: erwartet IPv{expected_version}, "
                        f"gefunden IPv{address.version}: {text}",
                    ),
                )

            canonical = str(address)

            if canonical in seen:
                stats.duplicates += 1
                add_issue(issues, Issue(path, line_no, f"Duplikat: {canonical}"))
            else:
                seen.add(canonical)

            if previous is not None and canonical < previous:
                stats.unsorted += 1
                add_issue(
                    issues,
                    Issue(
                        path,
                        line_no,
                        f"nicht sortiert: {canonical} steht nach {previous}",
                    ),
                )
            previous = canonical

        if declared is not None:
            actual_header_count = header_count_non_hash_unique(path)
            if declared != actual_header_count:
                stats.header_errors += 1
                add_issue(
                    issues,
                    Issue(
                        path,
                        None,
                        f"Entries-Header {declared:,} != Build-Zählung {actual_header_count:,}",
                    ),
                )

    except UnicodeDecodeError as exc:
        stats.invalid += 1
        add_issue(
            issues,
            Issue(path, None, f"Datei ist nicht gültiges UTF-8: {exc}"),
        )
    except OSError as exc:
        stats.invalid += 1
        add_issue(
            issues,
            Issue(path, None, f"Datei konnte nicht gelesen werden: {exc}"),
        )

    return issues, stats


def validate_regex_pattern(pattern: str) -> str | None:
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

    try:
        declared = declared_entries_for_file(path)

        for line_no, text in _read_payload(path):
            if parse_declared_entries(text) is not None:
                continue

            if not text or text.startswith(("#", "!")):
                continue

            stats.entries += 1

            if text in seen:
                stats.duplicates += 1
                add_issue(
                    issues,
                    Issue(path, line_no, f"Duplikat-RegEx: {text[:160]}"),
                )
            else:
                seen.add(text)

            regex_error = validate_regex_pattern(text)
            if regex_error:
                stats.invalid += 1
                add_issue(
                    issues,
                    Issue(
                        path,
                        line_no,
                        f"ungültige RegEx: {regex_error}: {text[:160]}",
                    ),
                )

        if declared is not None:
            actual_header_count = header_count_non_hash_unique(path)
            if declared != actual_header_count:
                stats.header_errors += 1
                add_issue(
                    issues,
                    Issue(
                        path,
                        None,
                        f"Entries-Header {declared:,} != Build-Zählung {actual_header_count:,}",
                    ),
                )

    except UnicodeDecodeError as exc:
        stats.invalid += 1
        add_issue(
            issues,
            Issue(path, None, f"Datei ist nicht gültiges UTF-8: {exc}"),
        )
    except OSError as exc:
        stats.invalid += 1
        add_issue(
            issues,
            Issue(path, None, f"Datei konnte nicht gelesen werden: {exc}"),
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
    print(f"Dateien:               {stats.files:,}")
    print(f"Geprüfte Einträge:     {stats.entries:,}")

    if scope == "categories" and stats.adblock_files:
        print(f"Adblock-Dateien:        {stats.adblock_files:,}")

    print(f"Duplikate:              {stats.duplicates:,}")
    print(f"Ungültige Einträge:     {stats.invalid:,}")

    if scope != "regex":
        print(f"Sortierungsfehler:      {stats.unsorted:,}")

    if scope in {"categories", "combined"}:
        print(f"Allowlist-Kollisionen:  {stats.allowlist_collisions:,}")

    print(f"Header-Fehler:          {stats.header_errors:,}")


def emit_issue(issue: Issue) -> None:
    print(f"FEHLER: {issue.plain()}")

    if os.environ.get("GITHUB_ACTIONS") == "true":
        rel = issue.path.relative_to(ROOT)
        message = (
            issue.message.replace("%", "%25")
            .replace("\r", "%0D")
            .replace("\n", "%0A")
        )

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
        if scope == "categories":
            category_format = detect_category_format(path)

            if category_format == "adblock":
                print(f"  Adblock-Syntax erkannt: {path.relative_to(ROOT)}")
                issues, stats = validate_adblock_file(
                    path,
                    allowlist=allowlist,
                )
            else:
                issues, stats = validate_domain_file(
                    path,
                    allowlist=allowlist,
                    check_allowlist=True,
                )

        elif scope == "combined":
            # Kombinierte Profile sind weiterhin reine Domainlisten.
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
        help="Alle Dateien des gewählten Scopes prüfen",
    )
    args = parser.parse_args()

    print("====================================================")
    print(" BlackRabbitZ DNS Blocklists - Repository Validator v3")
    print("====================================================")

    displayed_issues: list[Issue] = []
    total_errors = 0

    if args.scope in {"all", "config"}:
        print("\n=== JSON-Konfiguration ===")
        json_issues = check_json()

        if json_issues:
            total_errors += len(json_issues)
            displayed_issues.extend(json_issues)
            print(f"JSON-Fehler: {len(json_issues)}")
        else:
            print("JSON-Konfiguration: OK")

    if args.scope == "config":
        if total_errors:
            for issue in displayed_issues[:MAX_ISSUES_TO_PRINT]:
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
        total_errors += stats.errors

        if len(displayed_issues) < MAX_ISSUES_TO_PRINT:
            remaining = MAX_ISSUES_TO_PRINT - len(displayed_issues)
            displayed_issues.extend(issues[:remaining])

    if total_errors:
        print("\n====================================================")
        print(f"❌ VALIDIERUNG FEHLGESCHLAGEN: {total_errors:,} Fehler")
        print("====================================================")

        for issue in displayed_issues:
            emit_issue(issue)

        if total_errors > len(displayed_issues):
            print(
                f"... nur {len(displayed_issues):,} Fehlerdetails angezeigt; "
                f"{total_errors - len(displayed_issues):,} weitere Fehler wurden gezählt."
            )

        return 1

    print("\n====================================================")
    print("✅ ALLE GEPRÜFTEN BLACKRABBITZ-LISTEN SIND GÜLTIG")
    print("====================================================")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

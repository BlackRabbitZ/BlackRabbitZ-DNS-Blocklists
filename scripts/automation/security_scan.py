#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

from common import ROOT

RULES = [
    (re.compile(r"\beval\s+[\"'$]"), "Shell eval mit dynamischen Daten"),
    (re.compile(r"curl\s+[^\n|]+\|\s*(?:ba)?sh\b"), "Remote-Inhalt wird direkt an eine Shell gepiped"),
    (re.compile(r"wget\s+[^\n|]+\|\s*(?:ba)?sh\b"), "Remote-Inhalt wird direkt an eine Shell gepiped"),
    (re.compile(r"chmod\s+(?:-R\s+)?777\b"), "Weltweit beschreibbare Rechte (chmod 777)"),
    (re.compile(r"urllib\.request\.urlopen\([^\n]*http://"), "Unverschlüsselte HTTP-URL in Python"),
]


def main() -> int:
    findings: list[str] = []
    paths = sorted((ROOT / "scripts").rglob("*.py")) + sorted((ROOT / "scripts").rglob("*.sh"))
    for path in paths:
        if path.name == "security_scan.py":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern, message in RULES:
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                findings.append(f"{path.relative_to(ROOT)}:{line}: {message}")
    if findings:
        for item in findings:
            print(f"SICHERHEIT: {item}")
        return 1
    print("Statischer Sicherheitscheck: keine definierten Hochrisiko-Muster gefunden.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

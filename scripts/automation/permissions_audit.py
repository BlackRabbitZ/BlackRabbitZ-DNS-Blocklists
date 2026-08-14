#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

from common import ROOT

WORKFLOWS = ROOT / ".github" / "workflows"


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []
    for path in sorted(WORKFLOWS.glob("*.y*ml")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        lines = text.splitlines()
        top_permissions = any(re.match(r"^permissions:\s*", line) for line in lines)
        if not top_permissions:
            failures.append(f"{path.name}: keine expliziten top-level permissions")
        if re.search(r"^permissions:\s*write-all\s*$", text, re.MULTILINE):
            failures.append(f"{path.name}: write-all ist nicht zulässig")
        if "pull_request_target:" in text and "actions/checkout@" in text:
            failures.append(f"{path.name}: pull_request_target darf in diesem Projekt keinen PR-Code auschecken")
        if "pull_request:" in text and re.search(r"^\s{2}contents:\s*write\s*$", text, re.MULTILINE):
            warnings.append(f"{path.name}: Pull-Request-Workflow mit contents: write manuell prüfen")
    for warning in warnings:
        print(f"WARNUNG: {warning}")
    if failures:
        for failure in failures:
            print(f"FEHLER: {failure}")
        return 1
    print(f"Permissions-Audit erfolgreich: {len(list(WORKFLOWS.glob('*.y*ml')))} Workflows geprüft.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

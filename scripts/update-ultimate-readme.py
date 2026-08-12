#!/usr/bin/env python3
"""Backward-compatible wrapper for the v2 Ultimate README updater.

README synchronization is now handled generically for all profiles.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    scripts = Path(__file__).resolve().parent
    print("NOTICE: scripts/update-ultimate-readme.py is deprecated; using generic metadata/README generators.")
    rc = subprocess.call([sys.executable, str(scripts / "generate-metadata.py")])
    if rc:
        return rc
    return subprocess.call([sys.executable, str(scripts / "update-readme.py")])


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Backward-compatible wrapper for the v2 Ultimate-only splitter.

New builds use scripts/publish-profile.py through scripts/update-lists.sh.
This wrapper keeps older local maintenance commands from failing during migration.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Deprecated wrapper: publish Ultimate with the generic profile publisher.")
    parser.add_argument("source", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("lists/combined"))
    parser.add_argument("--max-bytes", type=int, default=5 * 1024 * 1024)
    parser.add_argument("--repo-url", default="https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists")
    parser.add_argument("--includes", required=True)
    args = parser.parse_args()

    publisher = Path(__file__).resolve().with_name("publish-profile.py")
    command = [
        sys.executable,
        str(publisher),
        str(args.source),
        "--profile", "ultimate",
        "--output-dir", str(args.output_dir),
        "--max-bytes", str(args.max_bytes),
        "--repo-url", args.repo_url,
        "--includes", args.includes,
        "--split",
    ]
    print("NOTICE: scripts/split-ultimate.py is deprecated; use scripts/update-lists.sh / publish-profile.py.")
    return subprocess.call(command)


if __name__ == "__main__":
    raise SystemExit(main())

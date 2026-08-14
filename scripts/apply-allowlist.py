#!/usr/bin/env python3
"""Apply the BlackRabbitZ safety allowlist to category lists or a generated file.

The allowlist semantics are intentionally strict:
- an exact allowlisted domain is excluded
- every subdomain of an allowlisted domain is excluded

Non-domain lines (headers, comments, Adblock/AdGuard rules, metadata) are preserved.
This makes the script safe to run across the mixed files in lists/categories/.
"""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path

# Reuse the repository's canonical domain and allowlist semantics.
from automation.common import load_allowlist, normalize_domain


def is_allowlisted_fast(domain: str, allowlist: set[str]) -> bool:
    """O(number of labels) suffix lookup instead of scanning the full allowlist."""
    parts = domain.split(".")
    return any(".".join(parts[index:]) in allowlist for index in range(len(parts)))


def filter_file(path: Path, allowlist: set[str]) -> tuple[int, int]:
    """Filter a file atomically. Return (domain_entries_seen, removed_entries)."""
    if not path.exists():
        raise FileNotFoundError(path)

    seen = 0
    removed = 0

    fd, temp_name = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".allowlist.tmp",
        dir=str(path.parent),
        text=True,
    )
    os.close(fd)
    temp_path = Path(temp_name)

    try:
        with path.open("r", encoding="utf-8", errors="strict") as source, temp_path.open(
            "w", encoding="utf-8", newline="\n"
        ) as target:
            for raw in source:
                text = raw.strip()

                # Preserve comments, headers, empty lines and non-domain formats.
                if not text or text.startswith(("#", "!")):
                    target.write(raw.rstrip("\r\n") + "\n")
                    continue

                domain = normalize_domain(text)
                if domain is None:
                    # Examples: [Adblock Plus], ||actor^, RegEx-like metadata.
                    # Those formats are not DNS domain entries and must remain untouched.
                    target.write(raw.rstrip("\r\n") + "\n")
                    continue

                seen += 1
                if is_allowlisted_fast(domain, allowlist):
                    removed += 1
                    print(f"ALLOWLIST REMOVE {path}: {domain}")
                    continue

                target.write(raw.rstrip("\r\n") + "\n")

        os.replace(temp_path, path)
    except Exception:
        temp_path.unlink(missing_ok=True)
        raise

    return seen, removed


def category_files(directory: Path) -> list[Path]:
    if not directory.exists():
        raise FileNotFoundError(directory)
    return sorted(path for path in directory.glob("*.txt") if path.is_file())


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Apply the BlackRabbitZ safety allowlist."
    )
    parser.add_argument(
        "--allowlist",
        type=Path,
        default=Path("config/allowlist.txt"),
        help="Allowlist file (default: config/allowlist.txt)",
    )

    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument(
        "--categories",
        type=Path,
        help="Filter all *.txt files in this category directory",
    )
    target.add_argument(
        "--file",
        type=Path,
        help="Filter one generated/domain file in place",
    )

    args = parser.parse_args()

    allowlist = load_allowlist(args.allowlist)
    if not allowlist:
        raise SystemExit(
            f"ERROR: safety allowlist is missing or empty: {args.allowlist}"
        )

    files = category_files(args.categories) if args.categories else [args.file]

    total_seen = 0
    total_removed = 0
    changed_files = 0

    for path in files:
        seen, removed = filter_file(path, allowlist)
        total_seen += seen
        total_removed += removed
        if removed:
            changed_files += 1

    print("\n=== safety allowlist summary ===")
    print(f"allowlist domains : {len(allowlist):,}")
    print(f"files checked     : {len(files):,}")
    print(f"domain entries    : {total_seen:,}")
    print(f"files changed     : {changed_files:,}")
    print(f"entries removed   : {total_removed:,}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

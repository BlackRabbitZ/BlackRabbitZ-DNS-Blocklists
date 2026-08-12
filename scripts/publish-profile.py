#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

DEFAULT_MAX_BYTES = 50 * 1024 * 1024
HEADER_RESERVE = 4096


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Publish a sorted unique combined profile, optionally as size-bounded parts.")
    p.add_argument("source", type=Path, help="Sorted unique domain file without comments")
    p.add_argument("--profile", required=True)
    p.add_argument("--output-dir", type=Path, default=Path("lists/combined"))
    p.add_argument("--max-bytes", type=int, default=DEFAULT_MAX_BYTES)
    p.add_argument("--repo-url", default="https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists")
    p.add_argument("--includes", required=True, help="Comma-separated category names")
    p.add_argument("--split", action="store_true", help="Always publish as numbered parts")
    return p.parse_args()


def iter_payload_lines(source: Path):
    with source.open("rb") as fh:
        for line in fh:
            if line.strip():
                yield line


def count_entries(source: Path) -> int:
    return sum(1 for _ in iter_payload_lines(source))


def calculate_part_counts(source: Path, payload_limit: int) -> list[int]:
    counts: list[int] = []
    current_bytes = 0
    current_count = 0
    for line in iter_payload_lines(source):
        line_size = len(line)
        if current_count and current_bytes + line_size > payload_limit:
            counts.append(current_count)
            current_bytes = 0
            current_count = 0
        current_bytes += line_size
        current_count += 1
    if current_count:
        counts.append(current_count)
    return counts


def clean_old_outputs(output_dir: Path, profile: str) -> None:
    single = output_dir / f"{profile}.txt"
    if single.exists():
        single.unlink()

    patterns = [
        re.compile(rf"{re.escape(profile)}-part-\d+\.txt"),
        re.compile(rf"{re.escape(profile)}-\d+\.txt"),  # legacy Ultimate naming
    ]
    for path in output_dir.glob(f"{profile}-*.txt"):
        if any(pattern.fullmatch(path.name) for pattern in patterns):
            path.unlink()


def header(
    *,
    repo_url: str,
    profile: str,
    includes: str,
    entries: int,
    total_entries: int | None = None,
    part: int | None = None,
    total_parts: int | None = None,
) -> bytes:
    lines = [
        "# BlackRabbitZ DNS Blocklists",
        f"# Category: combined/{profile}" + (f" (part {part}/{total_parts})" if part is not None else ""),
        "# Author: BlackRabbitZ",
        f"# Repository: {repo_url}",
        "# License: GPL-3.0-only for project-original material; third-party notices: THIRD_PARTY.md",
        f"# Entries: {entries}",
    ]
    if total_entries is not None:
        lines.append(f"# Profile Total Entries: {total_entries}")
    lines += ["#", f"# Includes: {includes}", "#"]
    if part is not None:
        lines += [
            f"# IMPORTANT: This is only one part of the {profile} profile.",
            f"# Add every {profile}-part-NN.txt Raw URL listed in the README for complete coverage.",
            "#",
        ]
    return ("\n".join(lines) + "\n").encode("utf-8")


def write_single(args: argparse.Namespace, total_entries: int) -> None:
    out = args.output_dir / f"{args.profile}.txt"
    with out.open("wb") as dst:
        dst.write(
            header(
                repo_url=args.repo_url,
                profile=args.profile,
                includes=args.includes,
                entries=total_entries,
            )
        )
        for line in iter_payload_lines(args.source):
            dst.write(line)
    print(f"{out}: {total_entries} entries, {out.stat().st_size} bytes")


def write_parts(args: argparse.Namespace) -> None:
    if args.max_bytes <= HEADER_RESERVE:
        raise SystemExit("max-bytes must be larger than the header reserve")

    payload_limit = args.max_bytes - HEADER_RESERVE
    counts = calculate_part_counts(args.source, payload_limit)
    if not counts:
        raise SystemExit(f"{args.profile} source contains no domains; refusing to generate empty parts")

    total_entries = sum(counts)
    total_parts = len(counts)
    width = max(2, len(str(total_parts)))

    src = args.source.open("rb")
    try:
        for idx, part_count in enumerate(counts, start=1):
            out = args.output_dir / f"{args.profile}-part-{idx:0{width}d}.txt"
            with out.open("wb") as dst:
                dst.write(
                    header(
                        repo_url=args.repo_url,
                        profile=args.profile,
                        includes=args.includes,
                        entries=part_count,
                        total_entries=total_entries,
                        part=idx,
                        total_parts=total_parts,
                    )
                )
                written = 0
                while written < part_count:
                    line = src.readline()
                    if not line:
                        raise RuntimeError(f"Unexpected end of source while writing {args.profile} parts")
                    if not line.strip():
                        continue
                    dst.write(line)
                    written += 1
            size = out.stat().st_size
            if size > args.max_bytes:
                raise RuntimeError(f"{out} exceeds configured maximum: {size} > {args.max_bytes} bytes")
            print(f"{out}: {part_count} entries, {size} bytes")
    finally:
        src.close()

    print(f"{args.profile} split complete: {total_entries} entries across {total_parts} parts")


def main() -> int:
    args = parse_args()
    if not args.source.is_file():
        raise SystemExit(f"Source does not exist: {args.source}")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    total_entries = count_entries(args.source)
    if total_entries == 0:
        raise SystemExit(f"{args.profile} source contains no domains; refusing to publish an empty profile")

    clean_old_outputs(args.output_dir, args.profile)
    if args.split:
        write_parts(args)
    else:
        write_single(args, total_entries)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

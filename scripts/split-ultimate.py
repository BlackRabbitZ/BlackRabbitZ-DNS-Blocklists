#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
from pathlib import Path

DEFAULT_MAX_BYTES = 40 * 1024 * 1024  # 40 MiB target per generated file
HEADER_RESERVE = 4096


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description='Split the deduplicated Ultimate profile into size-bounded parts.')
    p.add_argument('source', type=Path, help='Sorted, unique domain file without comments')
    p.add_argument('--output-dir', type=Path, default=Path('lists/combined'))
    p.add_argument('--max-bytes', type=int, default=DEFAULT_MAX_BYTES)
    p.add_argument('--repo-url', default='https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists')
    p.add_argument('--includes', required=True, help='Comma-separated category names')
    return p.parse_args()


def calculate_part_counts(source: Path, payload_limit: int) -> list[int]:
    counts: list[int] = []
    current_bytes = 0
    current_count = 0

    with source.open('rb') as fh:
        for line in fh:
            if not line.strip():
                continue
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


def clean_old_parts(output_dir: Path) -> None:
    legacy = output_dir / 'ultimate.txt'
    if legacy.exists():
        legacy.unlink()
    for path in output_dir.glob('ultimate-*.txt'):
        if re.fullmatch(r'ultimate-\d+\.txt', path.name):
            path.unlink()


def header(repo_url: str, part: int, total_parts: int, part_entries: int, total_entries: int, includes: str) -> bytes:
    text = (
        '# BlackRabbitZ DNS Blocklists\n'
        f'# Category: combined/ultimate (part {part}/{total_parts})\n'
        '# Author: BlackRabbitZ\n'
        f'# Repository: {repo_url}\n'
        '# License: GPL-3.0-only for project-original material; third-party notices: THIRD_PARTY.md\n'
        f'# Entries: {part_entries}\n'
        f'# Ultimate Total Entries: {total_entries}\n'
        '#\n'
        f'# Includes: {includes}\n'
        '#\n'
        '# IMPORTANT: This is only one part of the Ultimate profile.\n'
        '# Add every ultimate-N.txt Raw URL listed in the README for complete coverage.\n'
        '#\n'
    )
    return text.encode('utf-8')


def main() -> int:
    args = parse_args()
    if args.max_bytes <= HEADER_RESERVE:
        raise SystemExit('max-bytes must be larger than the header reserve')
    if not args.source.is_file():
        raise SystemExit(f'Source does not exist: {args.source}')

    args.output_dir.mkdir(parents=True, exist_ok=True)
    payload_limit = args.max_bytes - HEADER_RESERVE
    counts = calculate_part_counts(args.source, payload_limit)
    if not counts:
        raise SystemExit('Ultimate source contains no domains; refusing to generate empty parts.')

    total_entries = sum(counts)
    total_parts = len(counts)
    clean_old_parts(args.output_dir)

    with args.source.open('rb') as src:
        for idx, part_count in enumerate(counts, start=1):
            out = args.output_dir / f'ultimate-{idx}.txt'
            with out.open('wb') as dst:
                dst.write(header(args.repo_url, idx, total_parts, part_count, total_entries, args.includes))
                written = 0
                while written < part_count:
                    line = src.readline()
                    if not line:
                        raise RuntimeError('Unexpected end of source while writing Ultimate parts')
                    if not line.strip():
                        continue
                    dst.write(line)
                    written += 1

            size = out.stat().st_size
            if size > args.max_bytes:
                raise RuntimeError(f'{out} exceeds configured maximum: {size} > {args.max_bytes} bytes')
            print(f'{out}: {part_count} entries, {size} bytes')

    print(f'Ultimate split complete: {total_entries} entries across {total_parts} parts.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

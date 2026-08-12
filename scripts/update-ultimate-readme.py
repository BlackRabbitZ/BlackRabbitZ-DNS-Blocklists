#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / 'README.md'
COMBINED = ROOT / 'lists' / 'combined'
RAW_BASE = 'https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined'
START = '<!-- ULTIMATE_PARTS_START -->'
END = '<!-- ULTIMATE_PARTS_END -->'


def domain_count(path: Path) -> int:
    count = 0
    with path.open('r', encoding='utf-8') as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith('#'):
                count += 1
    return count


def part_number(path: Path) -> int:
    m = re.fullmatch(r'ultimate-(\d+)\.txt', path.name)
    if not m:
        raise ValueError(path)
    return int(m.group(1))


def main() -> int:
    parts = sorted(
        (p for p in COMBINED.glob('ultimate-*.txt') if re.fullmatch(r'ultimate-\d+\.txt', p.name)),
        key=part_number,
    )
    if not parts:
        raise SystemExit('No ultimate-N.txt parts found.')

    counts = [(p, domain_count(p)) for p in parts]
    total = sum(c for _, c in counts)
    text = README.read_text(encoding='utf-8')

    # Replace the Ultimate protection-profile row while keeping the current table layout.
    row_re = re.compile(r'^\| 🔴 \*\*Ultimate\*\* \|.*$', re.MULTILINE)
    new_row = (
        f'| 🔴 **Ultimate** | Maximum | **{total}** | Aggressive filtering | '
        '[Show Parts](#ultimate-parts) | **[Raw Parts](#ultimate-parts)** |'
    )
    if not row_re.search(text):
        raise SystemExit('Could not find the Ultimate row in README.md')
    text = row_re.sub(new_row, text, count=1)

    # Compact two-column layout: two Ultimate parts per README row.
    # This keeps the main README short even when the profile grows to many parts.
    cells = []
    for p, count in counts:
        n = part_number(p)
        mib = p.stat().st_size / (1024 * 1024)
        cells.append(
            f'**Part {n}**  \n'
            f'**{count:,}** entries · {mib:.1f} MiB  \n'
            f'[View](lists/combined/{p.name}) · '
            f'**[Raw]({RAW_BASE}/{p.name})**'
        )

    rows = [
        '| Ultimate Part | Ultimate Part |',
        '|---|---|',
    ]
    for i in range(0, len(cells), 2):
        left = cells[i].replace('\n', '<br>')
        right = cells[i + 1].replace('\n', '<br>') if i + 1 < len(cells) else ''
        rows.append(f'| {left} | {right} |')

    details = (
        '<a id="ultimate-parts"></a>\n'
        '<details>\n'
        f'<summary><strong>🔴 Show Ultimate Parts ({len(parts)} files)</strong></summary>\n\n'
        f'**Total: {total:,} unique domains.** Add **all parts** to Pi-hole / your DNS blocker for complete Ultimate coverage.\n\n'
        + '\n'.join(rows) + '\n\n'
        '</details>'
    )

    block = START + '\n' + details + '\n' + END

    # Remove the older always-visible Ultimate heading/description if present.
    # The collapsible block now carries all of that information itself.
    legacy_section_re = re.compile(
        r'\n## 🔴 Ultimate Parts\n\n'
        r'\*\*Ultimate contains .*?\n\n'
        + re.escape(START),
        flags=re.DOTALL,
    )
    text = legacy_section_re.sub('\n' + START, text, count=1)
    if START in text and END in text:
        text = re.sub(re.escape(START) + r'.*?' + re.escape(END), block, text, flags=re.DOTALL)
    else:
        anchor = '> **Security**, **Family** and especially **Ultimate** are now large merged profiles; review false positives before deploying them to critical networks.'
        if anchor not in text:
            raise SystemExit('Could not find insertion point for Ultimate Parts section.')
        section = (
            '\n\n' + block
        )
        text = text.replace(anchor, anchor + section, 1)

    # Keep repository-structure documentation accurate.
    text = text.replace('    │   └── ultimate.txt', '    │   ├── ultimate-1.txt\n    │   ├── ultimate-2.txt\n    │   └── ultimate-… .txt')
    text = text.replace('    │   └── ultimate-… .txt', '    │   └── ultimate-*.txt')

    README.write_text(text, encoding='utf-8')
    print(f'README Ultimate section updated: {total} entries across {len(parts)} parts.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

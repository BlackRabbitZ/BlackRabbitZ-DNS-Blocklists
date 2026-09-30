#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMBINED = ROOT / 'lists' / 'combined'
RAW_BASE = 'https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined'
START = '<!-- ULTIMATE_PARTS_START -->'
END = '<!-- ULTIMATE_PARTS_END -->'


def domain_count(path: Path) -> int:
    return sum(1 for line in path.read_text(encoding='utf-8').splitlines()
               if line.strip() and not line.lstrip().startswith('#'))


def part_number(path: Path) -> int:
    m = re.fullmatch(r'ultimate-(\d+)\.txt', path.name)
    if not m:
        raise ValueError(path)
    return int(m.group(1))


def fmt_count(value: int, lang: str) -> str:
    value = f'{value:,}'
    return value.replace(',', '.') if lang == 'de' else value


def update_readme(path: Path, parts: list[tuple[Path, int]], total: int, lang: str) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding='utf-8')

    view_label = 'Teile anzeigen' if lang == 'de' else 'Show parts'
    raw_label = 'Raw-Teile' if lang == 'de' else 'Raw parts'
    row_re = re.compile(r'^\| 🔴 \*\*Ultimate\*\* \|.*$', re.MULTILINE)
    new_row = (
        f'| 🔴 **Ultimate** | Maximum | **{fmt_count(total, lang)}** | '
        + ('Aggressive Filterung' if lang == 'de' else 'Aggressive filtering')
        + f' | [{view_label}](#ultimate-parts) | **[{raw_label}](#ultimate-parts)** |'
    )
    if not row_re.search(text):
        raise SystemExit(f'Could not find Ultimate row in {path.name}')
    text = row_re.sub(new_row, text, count=1)

    if lang == 'de':
        rows = ['| Teil | Einträge | Größe | Anzeigen | Raw |', '|---:|---:|---:|:---:|:---:|']
    else:
        rows = ['| Part | Entries | Size | View | Raw |', '|---:|---:|---:|:---:|:---:|']

    for p, count in parts:
        n = part_number(p)
        mib = p.stat().st_size / (1024 * 1024)
        view = 'Anzeigen' if lang == 'de' else 'View'
        rows.append(
            f'| **{n}** | **{fmt_count(count, lang)}** | {mib:.1f} MiB | '
            f'[{view}](lists/combined/{p.name}) | **[Raw]({RAW_BASE}/{p.name})** |'
        )

    block = START + '\n' + '\n'.join(rows) + '\n' + END
    if START not in text or END not in text:
        raise SystemExit(f'Could not find Ultimate marker block in {path.name}')
    text = re.sub(re.escape(START) + r'.*?' + re.escape(END), block, text, flags=re.DOTALL)
    path.write_text(text, encoding='utf-8')
    print(f'{path.name}: Ultimate updated: {total} entries across {len(parts)} parts.')


def main() -> int:
    parts_paths = sorted(
        (p for p in COMBINED.glob('ultimate-*.txt') if re.fullmatch(r'ultimate-\d+\.txt', p.name)),
        key=part_number,
    )
    if not parts_paths:
        raise SystemExit('No ultimate-N.txt parts found.')
    parts = [(p, domain_count(p)) for p in parts_paths]
    total = sum(count for _, count in parts)
    update_readme(ROOT / 'README.md', parts, total, 'de')
    update_readme(ROOT / 'README_EN.md', parts, total, 'en')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

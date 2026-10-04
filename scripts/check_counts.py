from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
for p in sorted(ROOT.rglob('*.txt')):
    if '_base' in p.parts: continue
    n=sum(1 for x in p.read_text(encoding='utf-8',errors='ignore').splitlines() if x.strip() and not x.startswith('#'))
    print(f'{n:>9}  {p.relative_to(ROOT)}')

#!/usr/bin/env python3
"""Repository integrity checks for BlackRabbitZ DNS Blocklists."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORY_DIR = ROOT / "lists" / "categories"
MANUAL_DIR = ROOT / "sources" / "manual"
UPSTREAM_DIR = ROOT / "sources" / "upstream"
CONFIG = ROOT / "scripts" / "upstream-sources.json"
ALLOWLIST = ROOT / "config" / "allowlist.txt"
CRITICAL = ROOT / "config" / "critical-services.txt"
DOMAIN_RE = re.compile(r"^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?$", re.I)


def extract(line: str) -> str | None:
    d=line.strip().lower().rstrip('.')
    if not d or d.startswith(('#','!','@@')): return None
    if d.startswith('||') and '^' in d: d=d[2:].split('^',1)[0]
    if ' #' in d: d=d.split(' #',1)[0].strip()
    if d.startswith('*.'): d=d[2:]
    d=d.split()[0] if d.split() else ''
    return d if DOMAIN_RE.fullmatch(d) else None


def read(path: Path) -> list[str]:
    if not path.exists(): return []
    return [d for line in path.read_text(encoding='utf-8',errors='ignore').splitlines() if (d:=extract(line))]


def suffix(domain: str, roots: set[str]) -> bool:
    return any(domain==r or domain.endswith('.'+r) for r in roots)


def main() -> int:
    errors=[]
    config=json.loads(CONFIG.read_text())
    allow_roots=set(read(ALLOWLIST))
    critical_roots=set(read(CRITICAL))

    # Config validation uses the production parser itself.
    cp=subprocess.run([sys.executable,str(ROOT/'scripts'/'update-upstreams.py'),'--check-config'],capture_output=True,text=True)
    if cp.returncode:
        errors.append(cp.stdout+cp.stderr)

    for path in sorted(CATEGORY_DIR.glob('*.txt')):
        category=path.stem
        entries=read(path)
        if len(entries)!=len(set(entries)):
            errors.append(f'{path.relative_to(ROOT)} contains duplicate domains')
        if entries!=sorted(entries):
            errors.append(f'{path.relative_to(ROOT)} is not sorted')
        settings=config.get('categories',{}).get(category,{})
        bad_allow=[d for d in entries if suffix(d,allow_roots)]
        if bad_allow:
            errors.append(f'{category}: {len(bad_allow)} explicitly allowlisted domains present (example: {bad_allow[0]})')
        if settings.get('protect_critical',False):
            bad=[d for d in entries if suffix(d,critical_roots)]
            if bad:
                errors.append(f'{category}: {len(bad)} critical-service domains present (example: {bad[0]})')
        if not (MANUAL_DIR/f'{category}.txt').exists():
            errors.append(f'missing sources/manual/{category}.txt')

    # Broad/specialised separation must remain enforced.
    def s(name): return set(read(CATEGORY_DIR/f'{name}.txt'))
    tracker_specialised=['telemetry','social-trackers','mobile-tracking','affiliate-tracking','consent-cmp','windows-telemetry','apple-telemetry','android-telemetry','linux-telemetry','nas-telemetry','server-telemetry','native-tracking','smart-tv','iot','gaming-telemetry']
    if (CATEGORY_DIR/'trackers.txt').exists():
        overlap=s('trackers') & set().union(*(s(x) for x in tracker_specialised if (CATEGORY_DIR/f'{x}.txt').exists()))
        if overlap: errors.append(f'trackers overlaps specialised lists by {len(overlap)} domains')
    telemetry_specialised=['mobile-tracking','windows-telemetry','apple-telemetry','android-telemetry','linux-telemetry','nas-telemetry','server-telemetry','smart-tv','iot','gaming-telemetry']
    if (CATEGORY_DIR/'telemetry.txt').exists():
        overlap=s('telemetry') & set().union(*(s(x) for x in telemetry_specialised if (CATEGORY_DIR/f'{x}.txt').exists()))
        if overlap: errors.append(f'telemetry overlaps specialised lists by {len(overlap)} domains')

    # Cache files must also be sorted/unique if present.
    for path in sorted(UPSTREAM_DIR.glob('*/*.txt')):
        entries=read(path)
        if entries!=sorted(set(entries)):
            errors.append(f'{path.relative_to(ROOT)} is not sorted/unique')

    if errors:
        print('VALIDATION FAILED',file=sys.stderr)
        for e in errors: print(' -',e.strip(),file=sys.stderr)
        return 1
    print(f'Validation OK: {len(list(CATEGORY_DIR.glob("*.txt")))} category lists; no critical-service leaks; modular separation intact.')
    return 0

if __name__=='__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)

updater=(ROOT/'scripts'/'update-upstreams.py').read_text(encoding='utf-8')
builder=(ROOT/'scripts'/'build-categories.py').read_text(encoding='utf-8')
workflow=(ROOT/'.github'/'workflows'/'daily-upstream-update.yml').read_text(encoding='utf-8')

require(not ('subprocess.run' in updater and 'build-categories.py' in updater),
        'update-upstreams.py must not build public categories before classification')
require('CLASSIFIED_DIR' in builder and 'folder=CLASSIFIED_DIR/cat' in builder,
        'build-categories.py must consume sources/classified')
require('UPSTREAM_DIR' not in builder,
        'build-categories.py must never consume raw sources/upstream directly')

stages=[
    'python3 ./scripts/update-upstreams.py',
    'python3 ./scripts/classify-upstreams.py',
    'python3 ./scripts/validate-classifier.py',
    'python3 ./scripts/build-categories.py',
]
pos=[workflow.find(s) for s in stages]
require(all(p >= 0 for p in pos), 'daily workflow missing required classified pipeline stage')
require(pos == sorted(pos), 'daily workflow order must be updater -> classifier -> validation -> builder')
print('Pipeline contract OK')

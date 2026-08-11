#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 BlackRabbitZ
"""Validate source datasets and generated lists."""
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
DOMAIN_RE=re.compile(r"^(?=.{1,253}$)(?!-)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$",re.I)

errors=[]
for p in sorted((ROOT/"data").rglob("*.txt")):
    seen=set()
    for i,raw in enumerate(p.read_text(encoding="utf-8").splitlines(),1):
        line=raw.strip().lower()
        if not line or line.startswith("#"): continue
        if line in seen: errors.append(f"{p}:{i}: duplicate: {line}")
        seen.add(line)
        if not DOMAIN_RE.fullmatch(line): errors.append(f"{p}:{i}: invalid domain: {line}")
allow=set((ROOT/"data/allowlist/global.txt").read_text().split())
for p in (ROOT/"data/categories").glob("*.txt"):
    conflicts=allow.intersection(set(p.read_text().split()))
    for d in sorted(conflicts): print(f"INFO allowlist overrides category entry: {d}")
if errors:
    print("\n".join(errors)); sys.exit(1)
print("Validation OK")

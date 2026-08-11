#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 BlackRabbitZ
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
DOMAIN_RE=re.compile(r"^(?=.{1,253}$)(?!-)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$",re.I)
errors=[]
category_names={p.stem for p in (ROOT/"data/categories").glob("*.txt")}
for p in sorted((ROOT/"data").rglob("*.txt")):
    seen=set()
    for i,raw in enumerate(p.read_text(encoding="utf-8").splitlines(),1):
        line=raw.strip().lower().rstrip(".")
        if not line or line.startswith("#"): continue
        if line in seen: errors.append(f"{p}:{i}: duplicate: {line}")
        seen.add(line)
        if not DOMAIN_RE.fullmatch(line): errors.append(f"{p}:{i}: invalid domain: {line}")
cfg=json.loads((ROOT/"config.json").read_text(encoding="utf-8"))
profiles=cfg.get("profiles",{})
for slug,spec in profiles.items():
    for c in spec.get("categories",[]):
        if c not in category_names:
            errors.append(f"config.json: profile {slug!r} references missing category {c!r}")
if errors:
    print("\n".join(errors)); sys.exit(1)
print(f"Validation OK: {len(category_names)} categories, {len(profiles)} profiles")

#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 BlackRabbitZ
"""Build deterministic DNS blocklists from independently maintained local datasets."""
from __future__ import annotations
import argparse, hashlib, ipaddress, json, re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOMAIN_RE = re.compile(
    r"^(?=.{1,253}\.?$)(?!-)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$",
    re.I,
)

def normalize(value: str) -> str | None:
    value = value.strip().lower().rstrip(".")
    if not value or value.startswith("#"):
        return None
    parts = value.split()
    if len(parts) >= 2:
        try:
            ipaddress.ip_address(parts[0])
            value = parts[1].lower().rstrip(".")
        except ValueError:
            pass
    if value.startswith("*."):
        value = value[2:]
    if not DOMAIN_RE.fullmatch(value):
        raise ValueError(f"invalid domain: {value}")
    return value

def load(path: Path) -> set[str]:
    out=set()
    if not path.exists():
        return out
    for n,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
        try:
            d=normalize(line)
        except ValueError as exc:
            raise SystemExit(f"{path}:{n}: {exc}")
        if d:
            out.add(d)
    return out

def header(label: str, count: int, version: str, sha: str) -> str:
    return "\n".join([
        f"# Title: BlackRabbitZ DNS Blocklists - {label}",
        "# Author: BlackRabbitZ",
        "# Homepage: https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists",
        "# License: GPL-3.0-only; see LICENSE, NOTICE and ATTRIBUTION.md",
        "# Format: domain list / DNS sinkhole compatible",
        f"# Version: {version}",
        f"# Entries: {count}",
        f"# Content-SHA256: {sha}",
        "# Generated from independently maintained data/ categories.",
        "",
    ])

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--check",action="store_true")
    args=ap.parse_args()
    cfg=json.loads((ROOT/"config.json").read_text(encoding="utf-8"))
    profiles=cfg.get("profiles", cfg.get("tiers", {}))
    allow=load(ROOT/"data/allowlist/global.txt")
    category_files={p.stem:p for p in (ROOT/"data/categories").glob("*.txt")}
    categories={name:load(path) for name,path in category_files.items()}
    version=datetime.now(timezone.utc).strftime("%Y.%m.%d")
    generated={}
    for slug, spec in profiles.items():
        if isinstance(spec,list):
            names=spec; label=slug.title()
        else:
            names=spec["categories"]; label=spec.get("label",slug.title())
        missing=[n for n in names if n not in categories]
        if missing:
            raise SystemExit(f"profile {slug!r} references missing categories: {', '.join(missing)}")
        domains=set().union(*(categories[n] for n in names)) - allow
        body="\n".join(sorted(domains))
        canonical=(body+"\n") if body else ""
        sha=hashlib.sha256(canonical.encode()).hexdigest()
        generated[ROOT/f"dist/{slug}.txt"]=header(label,len(domains),version,sha)+canonical
        hosts_body="\n".join(f"0.0.0.0 {d}" for d in sorted(domains))
        hosts=(hosts_body+"\n") if hosts_body else ""
        generated[ROOT/f"dist/{slug}-hosts.txt"]=header(label+" Hosts",len(domains),version,sha)+hosts

    expected=set(generated)
    # Remove obsolete generated list formats/profiles so dist remains canonical.
    for p in (ROOT/"dist").glob("*.txt"):
        if p not in expected and not args.check:
            p.unlink()

    changed=[]
    for path,text in generated.items():
        old=path.read_text(encoding="utf-8") if path.exists() else None
        if old != text:
            changed.append(path)
            if not args.check:
                path.write_text(text,encoding="utf-8",newline="\n")
    if args.check and changed:
        print("Generated files are stale:")
        for p in changed: print(" -",p.relative_to(ROOT))
        raise SystemExit(1)
    print(f"Built {len(generated)} files from {len(categories)} categories and {len(profiles)} profiles.")

if __name__=="__main__":
    main()

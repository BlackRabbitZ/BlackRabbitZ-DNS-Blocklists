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
    # Accept hosts-style input as a convenience.
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
    out = set()
    if not path.exists():
        return out
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        try:
            d = normalize(line)
        except ValueError as e:
            raise SystemExit(f"{path}:{n}: {e}")
        if d:
            out.add(d)
    return out

def header(title: str, count: int, version: str, sha: str) -> str:
    return "\n".join([
        f"# Title: BlackRabbitZ DNS Blocklists - {title}",
        "# Author: BlackRabbitZ",
        "# Homepage: https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists",
        "# License: GPL-3.0-only; see LICENSE, NOTICE and ATTRIBUTION.md",
        "# Format: one domain per line (Pi-hole / DNS sinkhole compatible)",
        f"# Version: {version}",
        f"# Entries: {count}",
        f"# Content-SHA256: {sha}",
        "# Generated deterministically from this repository's data/ directory.",
        "",
    ])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if generated files differ")
    args = ap.parse_args()
    cfg = json.loads((ROOT/"config.json").read_text())
    allow = load(ROOT/"data/allowlist/global.txt")
    categories = {p.stem: load(p) for p in (ROOT/"data/categories").glob("*.txt")}
    version = datetime.now(timezone.utc).strftime("%Y.%m.%d")
    generated = {}
    for tier, names in cfg["tiers"].items():
        domains = set().union(*(categories.get(n,set()) for n in names)) - allow
        body = "\n".join(sorted(domains))
        sha = hashlib.sha256((body+"\n").encode()).hexdigest()
        text = header(tier.title(), len(domains), version, sha) + body + ("\n" if body else "")
        generated[ROOT/f"dist/{tier}.txt"] = text
        hosts = header(tier.title()+" Hosts", len(domains), version, sha)
        hosts += "\n".join(f"0.0.0.0 {d}" for d in sorted(domains)) + ("\n" if domains else "")
        generated[ROOT/f"dist/{tier}-hosts.txt"] = hosts

    changed=[]
    for path,text in generated.items():
        old=path.read_text(encoding="utf-8") if path.exists() else None
        if old != text:
            changed.append(path)
            if not args.check:
                path.write_text(text,encoding="utf-8",newline="\n")
    if args.check and changed:
        print("Generated files are stale:")
        for p in changed: print(" -", p.relative_to(ROOT))
        raise SystemExit(1)
    print(f"Built {len(generated)} files.")

if __name__ == "__main__":
    main()

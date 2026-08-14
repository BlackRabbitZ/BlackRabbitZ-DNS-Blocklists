#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import random
from datetime import date
from pathlib import Path

from common import ROOT, category_files, normalize_domain, payload_lines
from dns_tools import check_domains

STATE_PATH = ROOT / "metadata" / "dns-health-state.json"
REPORT_PATH = ROOT / "metadata" / "dns-health.json"


def reservoir_sample(limit: int, seed: str, exclude: set[str]) -> list[str]:
    rng = random.Random(seed)
    sample: list[str] = []
    seen = 0
    for path in category_files():
        for raw in payload_lines(path):
            domain = normalize_domain(raw)
            if not domain or domain in exclude:
                continue
            seen += 1
            if len(sample) < limit:
                sample.append(domain)
            else:
                index = rng.randrange(seen)
                if index < limit:
                    sample[index] = domain
    return sorted(set(sample))


def load_state(path: Path) -> dict:
    if not path.exists():
        return {"version": 1, "candidates": {}}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("version") == 1 and isinstance(data.get("candidates"), dict):
            return data
    except Exception:
        pass
    return {"version": 1, "candidates": {}}


def main() -> int:
    parser = argparse.ArgumentParser(description="Rotierender DNS-Gesundheitscheck für bestehende Blocklist-Domains.")
    parser.add_argument("--sample-size", type=int, default=10000)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--timeout", type=int, default=2)
    parser.add_argument("--state", type=Path, default=STATE_PATH)
    parser.add_argument("--report", type=Path, default=REPORT_PATH)
    args = parser.parse_args()

    today = date.today().isoformat()
    state = load_state(args.state)
    candidates: dict[str, dict] = state["candidates"]
    existing_candidates = set(candidates)
    sample = reservoir_sample(args.sample_size, today, existing_candidates)
    domains = sorted(existing_candidates | set(sample))
    print(f"DNS-Health: {len(existing_candidates):,} bestehende Kandidaten + {len(sample):,} neue Stichprobe")

    results = check_domains(domains, timeout=args.timeout, workers=args.workers)
    counts = {"exists": 0, "nxdomain": 0, "temporary": 0}
    for result in results:
        counts[result.classification] += 1
        domain = result.domain
        record = candidates.get(domain)
        if result.classification == "exists":
            candidates.pop(domain, None)
            continue
        if result.classification == "temporary":
            continue
        if record is None:
            record = {"checks": [], "first_seen": today, "last_seen": today}
            candidates[domain] = record
        checks = [str(item) for item in record.get("checks", []) if item]
        if today not in checks:
            checks.append(today)
        record["checks"] = checks[-8:]
        record["last_seen"] = today
        record.setdefault("first_seen", today)

    confirmed = sorted(domain for domain, rec in candidates.items() if len(set(rec.get("checks", []))) >= 3)
    state_out = {"version": 1, "candidates": dict(sorted(candidates.items()))}
    args.state.parent.mkdir(parents=True, exist_ok=True)
    args.state.write_text(json.dumps(state_out, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    report = {
        "checked": len(results),
        "sampled_new": len(sample),
        "rechecked_candidates": len(existing_candidates),
        "exists": counts["exists"],
        "nxdomain": counts["nxdomain"],
        "temporary": counts["temporary"],
        "tracked_candidates": len(candidates),
        "confirmed_after_3_checks": len(confirmed),
        "confirmed_domains": confirmed[:1000],
    }
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

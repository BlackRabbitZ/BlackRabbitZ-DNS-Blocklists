#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config" / "profiles.json"
BUILD = ROOT / "metadata" / "build.json"
COMBINED = ROOT / "lists" / "combined"


def payload_lines(path: Path):
    with path.open("r", encoding="utf-8", errors="strict") as fh:
        for line in fh:
            text = line.strip()
            if text and not text.startswith("#"):
                yield text


def main() -> int:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    build = json.loads(BUILD.read_text(encoding="utf-8"))
    max_bytes = int(config["split_max_bytes"])
    failures: list[str] = []

    for profile, cfg in config["profiles"].items():
        info = build["profiles"].get(profile)
        if not info:
            failures.append(f"metadata missing profile: {profile}")
            continue

        files = [ROOT / item["file"] for item in info["files"]]
        if cfg.get("split"):
            if (COMBINED / f"{profile}.txt").exists():
                failures.append(f"split profile still has unsplit file: {profile}.txt")
            for path in COMBINED.glob(f"{profile}-*.txt"):
                if re.fullmatch(rf"{re.escape(profile)}-\d+\.txt", path.name):
                    failures.append(f"legacy numbered part still exists: {path.name}")
            for path in files:
                if path.stat().st_size > max_bytes:
                    failures.append(f"part exceeds split limit: {path} ({path.stat().st_size} > {max_bytes})")
        else:
            if len(files) != 1 or files[0].name != f"{profile}.txt":
                failures.append(f"unsplit profile has unexpected output layout: {profile}")

        previous: str | None = None
        counted = 0
        for path in files:
            for domain in payload_lines(path):
                counted += 1
                if previous is not None and domain <= previous:
                    relation = "duplicate" if domain == previous else "out of order"
                    failures.append(f"{profile}: {relation}: {domain} after {previous}")
                    break
                previous = domain
            if failures and failures[-1].startswith(f"{profile}:"):
                break

        if counted != info["entries"]:
            failures.append(f"{profile}: metadata count mismatch ({counted} != {info['entries']})")
        part_sum = sum(int(item["entries"]) for item in info["files"])
        if part_sum != info["entries"]:
            failures.append(f"{profile}: part entry sum mismatch ({part_sum} != {info['entries']})")

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        raise SystemExit(1)

    print("Generated profile validation passed: sorted, unique, size-bounded and metadata-consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

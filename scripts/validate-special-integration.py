#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config" / "special-lists.json"
METADATA = ROOT / "metadata" / "special-lists.json"
CATEGORIES = ROOT / "lists" / "categories"
IPS = ROOT / "lists" / "ips"


def output_dir(kind: str) -> Path:
    return IPS if kind == "ipv4" else CATEGORIES


def main() -> int:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    if not METADATA.is_file():
        raise SystemExit("metadata/special-lists.json is missing")
    metadata = json.loads(METADATA.read_text(encoding="utf-8"))

    expected_revision = int(config.get("integration_revision", 1))
    actual_revision = int(metadata.get("integration_revision", 0) or 0)
    failures: list[str] = []
    if actual_revision != expected_revision:
        failures.append(f"integration revision mismatch: {actual_revision} != {expected_revision}")

    meta_items = metadata.get("items", {})
    for item in config.get("items", []):
        variants_meta = meta_items.get(item["id"], {}).get("variants", {})
        for variant in item.get("variants", []):
            target = variant.get("merge_into")
            if not target:
                continue
            info = variants_meta.get(variant["id"], {})
            if info.get("status") != "merged" or info.get("merge_into") != target:
                failures.append(f"{variant['id']}: not successfully merged into {target}")
            target_file = CATEGORIES / f"{target}.txt"
            if not target_file.is_file():
                failures.append(f"{variant['id']}: merge target missing: {target_file.relative_to(ROOT)}")

            directory = output_dir(variant["kind"])
            stale = [directory / f"{variant['id']}.txt", *directory.glob(f"{variant['id']}-part-*.txt")]
            for path in stale:
                if path.exists():
                    failures.append(f"obsolete parallel output still exists: {path.relative_to(ROOT)}")

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        raise SystemExit(1)

    print("Extended-source integration validation passed: overlapping sources are merged and no parallel outputs remain")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

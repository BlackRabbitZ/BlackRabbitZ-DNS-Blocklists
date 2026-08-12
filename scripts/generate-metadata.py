#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config" / "profiles.json"
CATEGORIES = ROOT / "lists" / "categories"
COMBINED = ROOT / "lists" / "combined"
METADATA = ROOT / "metadata"


def domain_count(path: Path) -> int:
    count = 0
    with path.open("r", encoding="utf-8", errors="strict") as fh:
        for line in fh:
            text = line.strip()
            if text and not text.startswith("#"):
                count += 1
    return count


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def file_info(path: Path) -> dict:
    return {
        "file": path.relative_to(ROOT).as_posix(),
        "entries": domain_count(path),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }


def main() -> int:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    METADATA.mkdir(parents=True, exist_ok=True)

    data: dict = {
        "schema_version": 1,
        "split_max_bytes": config["split_max_bytes"],
        "categories": {},
        "profiles": {},
    }

    for path in sorted(CATEGORIES.glob("*.txt")):
        data["categories"][path.stem] = file_info(path)

    checksum_rows: list[tuple[str, str]] = []
    for item in data["categories"].values():
        checksum_rows.append((item["sha256"], item["file"]))

    for profile, profile_cfg in config["profiles"].items():
        if profile_cfg.get("split"):
            part_re = re.compile(rf"{re.escape(profile)}-part-(\d+)\.txt")
            parts = [p for p in COMBINED.glob(f"{profile}-part-*.txt") if part_re.fullmatch(p.name)]
            parts.sort(key=lambda p: int(part_re.fullmatch(p.name).group(1)))
            if not parts:
                raise SystemExit(f"No generated parts found for split profile: {profile}")
            files = [file_info(p) for p in parts]
        else:
            path = COMBINED / f"{profile}.txt"
            if not path.is_file():
                raise SystemExit(f"Missing generated profile: {path}")
            files = [file_info(path)]

        entries = sum(item["entries"] for item in files)
        data["profiles"][profile] = {
            "label": profile_cfg["label"],
            "group": profile_cfg["group"],
            "split": bool(profile_cfg.get("split")),
            "entries": entries,
            "parts": len(files),
            "files": files,
            "categories": profile_cfg["categories"],
        }
        for item in files:
            checksum_rows.append((item["sha256"], item["file"]))

    (METADATA / "build.json").write_text(
        json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (METADATA / "SHA256SUMS").write_text(
        "".join(f"{digest}  {path}\n" for digest, path in sorted(checksum_rows, key=lambda x: x[1])),
        encoding="utf-8",
    )
    print(f"Wrote {METADATA / 'build.json'} and {METADATA / 'SHA256SUMS'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

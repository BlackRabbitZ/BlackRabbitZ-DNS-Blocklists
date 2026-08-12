#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
CONFIG = ROOT / "config" / "profiles.json"
BUILD = ROOT / "metadata" / "build.json"
RAW_BASE = "https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main"

MARKERS = {
    "main": ("<!-- MAIN_PROFILES_START -->", "<!-- MAIN_PROFILES_END -->"),
    "addons": ("<!-- ADDON_PROFILES_START -->", "<!-- ADDON_PROFILES_END -->"),
    "parts": ("<!-- SPLIT_PROFILES_START -->", "<!-- SPLIT_PROFILES_END -->"),
    "comparison": ("<!-- COMPARISON_START -->", "<!-- COMPARISON_END -->"),
}


def replace_block(text: str, start: str, end: str, body: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    replacement = f"{start}\n{body.rstrip()}\n{end}"
    if not pattern.search(text):
        raise SystemExit(f"README marker block missing: {start} ... {end}")
    return pattern.sub(lambda _: replacement, text, count=1)


def profile_link(profile: str, info: dict) -> tuple[str, str]:
    if info["split"]:
        anchor = f"#{profile}-parts"
        return f"[Show Parts]({anchor})", f"**[Raw Parts]({anchor})**"
    file_path = info["files"][0]["file"]
    return f"[View]({file_path})", f"**[Raw]({RAW_BASE}/{file_path})**"


def profile_table(config: dict, build: dict, group: str) -> str:
    rows = [
        "| Profile | Protection | Entries | Recommended for | View | Raw |",
        "|---|:---:|---:|---|:---:|:---:|",
    ]
    for name, cfg in config["profiles"].items():
        if cfg["group"] != group:
            continue
        info = build["profiles"][name]
        view, raw = profile_link(name, info)
        rows.append(
            f"| {cfg['icon']} **{cfg['label']}** | {cfg['protection']} | **{info['entries']:,}** | "
            f"{cfg['recommended_for']} | {view} | {raw} |"
        )
    return "\n".join(rows)


def parts_block(config: dict, build: dict) -> str:
    chunks: list[str] = []
    for name, cfg in config["profiles"].items():
        info = build["profiles"][name]
        if not info["split"]:
            continue
        files = info["files"]
        chunks += [
            f'<a id="{name}-parts"></a>',
            "<details>",
            f"<summary><strong>{cfg['icon']} Show {cfg['label'].replace(' ⭐', '')} Parts ({len(files)} files)</strong></summary>",
            "",
            f"**Total: {info['entries']:,} unique domains.** Add **all parts** to Pi-hole / your DNS blocker for complete {cfg['label'].replace(' ⭐', '')} coverage.",
            "",
            f"| {cfg['label'].replace(' ⭐', '')} Part | {cfg['label'].replace(' ⭐', '')} Part |",
            "|---|---|",
        ]
        cells: list[str] = []
        for idx, file_info in enumerate(files, start=1):
            path = file_info["file"]
            mib = file_info["bytes"] / (1024 * 1024)
            cells.append(
                f"**Part {idx:02d}**  <br>**{file_info['entries']:,}** entries · {mib:.1f} MiB  <br>"
                f"[View]({path}) · **[Raw]({RAW_BASE}/{path})**"
            )
        for i in range(0, len(cells), 2):
            left = cells[i]
            right = cells[i + 1] if i + 1 < len(cells) else ""
            chunks.append(f"| {left} | {right} |")
        chunks += ["", "</details>", ""]
    return "\n".join(chunks).rstrip()


def comparison_table(config: dict) -> str:
    names = list(config["profiles"].keys())
    labels = [config["profiles"][name]["label"] for name in names]
    rows = [
        "| Feature | " + " | ".join(labels) + " |",
        "|---|" + "|".join(":---:" for _ in names) + "|",
    ]
    for feature in config["comparison_features"]:
        cells = []
        required = set(feature["categories"])
        mode = feature.get("mode", "all")
        for name in names:
            present = set(config["profiles"][name]["categories"])
            enabled = bool(required & present) if mode == "any" else required <= present
            cells.append("✅" if enabled else "—")
        rows.append(f"| {feature['label']} | " + " | ".join(cells) + " |")
    rows.append(
        "| Breakage Risk | "
        + " | ".join(config["profiles"][name]["breakage"] for name in names)
        + " |"
    )
    return "\n".join(rows)


def update_category_counts(text: str, build: dict) -> str:
    for name, info in build["categories"].items():
        target = f"[View](lists/categories/{name}.txt)"
        lines = text.splitlines()
        changed = False
        for idx, line in enumerate(lines):
            if target not in line or not line.startswith("|"):
                continue
            fields = line.split("|")
            if len(fields) >= 4:
                fields[2] = f" {info['entries']:,} "
                lines[idx] = "|".join(fields)
                changed = True
                break
        if changed:
            text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    return text


def main() -> int:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    build = json.loads(BUILD.read_text(encoding="utf-8"))
    text = README.read_text(encoding="utf-8")

    text = replace_block(text, *MARKERS["main"], profile_table(config, build, "main"))
    text = replace_block(text, *MARKERS["addons"], profile_table(config, build, "addon"))
    text = replace_block(text, *MARKERS["parts"], parts_block(config, build))
    text = replace_block(text, *MARKERS["comparison"], comparison_table(config))
    text = update_category_counts(text, build)
    README.write_text(text, encoding="utf-8")
    print("README profile tables, split-part links, comparison matrix and category counts synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

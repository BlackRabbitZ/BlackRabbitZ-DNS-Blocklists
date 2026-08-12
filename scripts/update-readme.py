#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config" / "profiles.json"
I18N = ROOT / "config" / "readme-i18n.json"
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


def number(value: int, language: str) -> str:
    formatted = f"{value:,}"
    return formatted.replace(",", ".") if language == "de" else formatted


def localized_profile(cfg: dict, language_cfg: dict, name: str) -> dict:
    local = language_cfg.get("profiles", {}).get(name, {})
    return {
        "label": cfg["label"],
        "protection": local.get("protection", cfg["protection"]),
        "recommended_for": local.get("recommended_for", cfg["recommended_for"]),
        "breakage": local.get("breakage", cfg["breakage"]),
    }


def profile_link(profile: str, info: dict, language_cfg: dict) -> tuple[str, str]:
    table = language_cfg["table"]
    if info["split"]:
        anchor = f"#{profile}-parts"
        return f"[{table['show_parts']}]({anchor})", f"**[{table['raw_parts']}]({anchor})**"
    file_path = info["files"][0]["file"]
    return f"[{table['view']}]({file_path})", f"**[{table['raw']}]({RAW_BASE}/{file_path})**"


def profile_table(config: dict, build: dict, group: str, language: str, language_cfg: dict) -> str:
    table = language_cfg["table"]
    rows = [
        f"| {table['profile']} | {table['protection']} | {table['entries']} | {table['recommended_for']} | {table['view']} | {table['raw']} |",
        "|---|:---:|---:|---|:---:|:---:|",
    ]
    for name, cfg in config["profiles"].items():
        if cfg["group"] != group:
            continue
        info = build["profiles"][name]
        display = localized_profile(cfg, language_cfg, name)
        view, raw = profile_link(name, info, language_cfg)
        rows.append(
            f"| {cfg['icon']} **{display['label']}** | {display['protection']} | **{number(info['entries'], language)}** | "
            f"{display['recommended_for']} | {view} | {raw} |"
        )
    return "\n".join(rows)


def parts_block(config: dict, build: dict, language: str, language_cfg: dict) -> str:
    chunks: list[str] = []
    p = language_cfg["parts"]
    table = language_cfg["table"]

    for name, cfg in config["profiles"].items():
        info = build["profiles"][name]
        if not info["split"]:
            continue

        files = info["files"]
        label = cfg["label"].replace(" ⭐", "")
        chunks += [
            f'<a id="{name}-parts"></a>',
            "<details>",
            f"<summary><strong>{cfg['icon']} {label}: {p['show']} ({len(files)} {p['files']})</strong></summary>",
            "",
            f"**{p['total']}: {number(info['entries'], language)} {p['unique_domains']}.** {p['instruction']}",
            "",
            f"| {label} {p['part']} | {label} {p['part']} |",
            "|---|---|",
        ]

        cells: list[str] = []
        for idx, file_info in enumerate(files, start=1):
            path = file_info["file"]
            mib = file_info["bytes"] / (1024 * 1024)
            cells.append(
                f"**{p['part']} {idx:02d}**  <br>**{number(file_info['entries'], language)}** {p['entries']} · {mib:.1f} MiB  <br>"
                f"[{table['view']}]({path}) · **[{table['raw']}]({RAW_BASE}/{path})**"
            )

        for i in range(0, len(cells), 2):
            left = cells[i]
            right = cells[i + 1] if i + 1 < len(cells) else ""
            chunks.append(f"| {left} | {right} |")
        chunks += ["", "</details>", ""]

    return "\n".join(chunks).rstrip()


def comparison_table(config: dict, language_cfg: dict) -> str:
    table = language_cfg["table"]
    names = list(config["profiles"].keys())
    labels = [config["profiles"][name]["label"] for name in names]
    rows = [
        f"| {table['feature']} | " + " | ".join(labels) + " |",
        "|---|" + "|".join(":---:" for _ in names) + "|",
    ]

    feature_translations = language_cfg.get("features", {})
    for feature in config["comparison_features"]:
        cells = []
        required = set(feature["categories"])
        mode = feature.get("mode", "all")
        for name in names:
            present = set(config["profiles"][name]["categories"])
            enabled = bool(required & present) if mode == "any" else required <= present
            cells.append("✅" if enabled else "—")
        label = feature_translations.get(feature["label"], feature["label"])
        rows.append(f"| {label} | " + " | ".join(cells) + " |")

    breakage = [localized_profile(config["profiles"][name], language_cfg, name)["breakage"] for name in names]
    rows.append(f"| {table['breakage']} | " + " | ".join(breakage) + " |")
    return "\n".join(rows)


def update_category_counts(text: str, build: dict, language: str) -> str:
    lines = text.splitlines()
    for name, info in build["categories"].items():
        target = f"[View](lists/categories/{name}.txt)" if language == "en" else f"[Anzeigen](lists/categories/{name}.txt)"
        for idx, line in enumerate(lines):
            if target not in line or not line.startswith("|"):
                continue
            fields = line.split("|")
            if len(fields) >= 4:
                fields[2] = f" {number(info['entries'], language)} "
                lines[idx] = "|".join(fields)
            break
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def update_one(readme: Path, language: str, language_cfg: dict, config: dict, build: dict) -> None:
    if not readme.exists():
        raise SystemExit(f"README file missing: {readme.relative_to(ROOT)}")

    text = readme.read_text(encoding="utf-8")
    text = replace_block(text, *MARKERS["main"], profile_table(config, build, "main", language, language_cfg))
    text = replace_block(text, *MARKERS["addons"], profile_table(config, build, "addon", language, language_cfg))
    text = replace_block(text, *MARKERS["parts"], parts_block(config, build, language, language_cfg))
    text = replace_block(text, *MARKERS["comparison"], comparison_table(config, language_cfg))
    text = update_category_counts(text, build, language)
    readme.write_text(text, encoding="utf-8")
    print(f"Synchronized {readme.relative_to(ROOT)}")


def main() -> int:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    i18n = json.loads(I18N.read_text(encoding="utf-8"))
    build = json.loads(BUILD.read_text(encoding="utf-8"))

    for language, language_cfg in i18n["languages"].items():
        update_one(ROOT / language_cfg["readme"], language, language_cfg, config, build)

    print("German and English README profile tables, split-part links, comparison matrix and category counts synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

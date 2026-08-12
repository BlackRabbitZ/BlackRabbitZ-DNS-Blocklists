#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config" / "profiles.json"
I18N = ROOT / "config" / "readme-i18n.json"
BUILD = ROOT / "metadata" / "build.json"
SPECIAL_CONFIG = ROOT / "config" / "special-lists.json"
SPECIAL_BUILD = ROOT / "metadata" / "special-lists.json"
RAW_BASE = "https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main"

MARKERS = {
    "main": ("<!-- MAIN_PROFILES_START -->", "<!-- MAIN_PROFILES_END -->"),
    "addons": ("<!-- ADDON_PROFILES_START -->", "<!-- ADDON_PROFILES_END -->"),
    "parts": ("<!-- SPLIT_PROFILES_START -->", "<!-- SPLIT_PROFILES_END -->"),
    "comparison": ("<!-- COMPARISON_START -->", "<!-- COMPARISON_END -->"),
    "special_ads_tracking": ("<!-- SPECIAL_ADS_TRACKING_START -->", "<!-- SPECIAL_ADS_TRACKING_END -->"),
    "special_security": ("<!-- SPECIAL_SECURITY_START -->", "<!-- SPECIAL_SECURITY_END -->"),
    "special_network": ("<!-- SPECIAL_NETWORK_START -->", "<!-- SPECIAL_NETWORK_END -->"),
    "special_family": ("<!-- SPECIAL_FAMILY_START -->", "<!-- SPECIAL_FAMILY_END -->"),
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


def special_variant_links(variant: dict, info: dict | None, language: str) -> tuple[str, str, str]:
    if language == "de":
        pending = "Noch nicht erzeugt"
        show_parts = "Teile anzeigen"
        view = "Anzeigen"
        raw = "Raw"
    else:
        pending = "Not built yet"
        show_parts = "Show parts"
        view = "View"
        raw = "Raw"

    if not info or not info.get("files"):
        return pending, "—", "—"

    files = info["files"]
    entries = number(int(info.get("entries", 0)), language)
    if len(files) == 1:
        path = files[0]["file"]
        return entries, f"[{view}]({path})", f"**[{raw}]({RAW_BASE}/{path})**"
    anchor = f"#{variant['id']}-parts"
    return entries, f"[{show_parts}]({anchor})", f"**[{show_parts}]({anchor})**"


def special_parts_table(variant: dict, info: dict, language: str) -> str:
    files = info.get("files", [])
    if len(files) <= 1:
        return ""
    label = variant["label_de"] if language == "de" else variant["label_en"]
    part_word = "Teil" if language == "de" else "Part"
    entries_word = "Einträge" if language == "de" else "entries"
    view_word = "Anzeigen" if language == "de" else "View"
    chunks = [
        f'<a id="{variant["id"]}-parts"></a>',
        "<details>",
        f"<summary><strong>{label}: {len(files)} {('Teile' if language == 'de' else 'parts')}</strong></summary>",
        "",
        f"| {part_word} | {part_word} |",
        "|---|---|",
    ]
    cells = []
    for idx, file_info in enumerate(files, start=1):
        path = file_info["file"]
        mib = file_info["bytes"] / (1024 * 1024)
        cells.append(
            f"**{part_word} {idx:02d}**  <br>**{number(file_info['entries'], language)}** {entries_word} · {mib:.1f} MiB  <br>"
            f"[{view_word}]({path}) · **[Raw]({RAW_BASE}/{path})**"
        )
    for i in range(0, len(cells), 2):
        chunks.append(f"| {cells[i]} | {cells[i + 1] if i + 1 < len(cells) else ''} |")
    chunks += ["", "</details>"]
    return "\n".join(chunks)


def special_lists_block(config: dict, metadata: dict, language: str, section: str) -> str:
    chunks: list[str] = []
    metadata_items = metadata.get("items", {}) if metadata else {}
    if language == "de":
        risk_label = "Risiko"
        variant_label = "Variante"
        entries_label = "Einträge"
        format_label = "Format"
        view_label = "Anzeigen / Teile"
        raw_label = "Raw"
        doc_text = "Dokumentation"
        formats = {"domains": "Domains", "ipv4": "IPv4 / Firewall", "raw": "Adblock"}
    else:
        risk_label = "Risk"
        variant_label = "Variant"
        entries_label = "Entries"
        format_label = "Format"
        view_label = "View / Parts"
        raw_label = "Raw"
        doc_text = "Documentation"
        formats = {"domains": "Domains", "ipv4": "IPv4 / firewall", "raw": "Adblock"}

    for item in config.get("items", []):
        if int(item.get("point", 0)) >= 23 or item.get("readme_section") != section:
            continue
        title = item["title_de"] if language == "de" else item["title_en"]
        description = item["description_de"] if language == "de" else item["description_en"]
        risk = item["risk_de"] if language == "de" else item["risk_en"]
        chunks += [
            f'<a id="special-{item["id"]}"></a>',
            "<details>",
            f"<summary><strong>{item['point']}. {item['icon']} {title}</strong> — {description}</summary>",
            "",
            f"**{risk_label}: {risk}**",
            "",
        ]
        variants = item.get("variants", [])
        if not variants:
            doc_path = item.get("documentation_de") if language == "de" else item.get("documentation_en")
            if doc_path and not doc_path.startswith("#"):
                chunks += [f"[{doc_text}]({doc_path})", ""]
            else:
                chunks += [description, ""]
        else:
            chunks += [
                f"| {variant_label} | {entries_label} | {format_label} | {view_label} | {raw_label} |",
                "|---|---:|---|:---:|:---:|",
            ]
            item_meta = metadata_items.get(item["id"], {}).get("variants", {})
            split_sections: list[str] = []
            for variant in variants:
                info = item_meta.get(variant["id"])
                label = variant["label_de"] if language == "de" else variant["label_en"]
                entries, view, raw = special_variant_links(variant, info, language)
                fmt = formats.get(variant.get("kind", "domains"), variant.get("kind", ""))
                chunks.append(f"| **{label}** | {entries} | {fmt} | {view} | {raw} |")
                if info and len(info.get("files", [])) > 1:
                    split_sections.append(special_parts_table(variant, info, language))
            chunks.append("")
            if split_sections:
                chunks += split_sections + [""]
        chunks += ["</details>", ""]
    return "\n".join(chunks).rstrip()

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


def update_one(readme: Path, language: str, language_cfg: dict, config: dict, build: dict, special_config: dict, special_build: dict) -> None:
    if not readme.exists():
        raise SystemExit(f"README file missing: {readme.relative_to(ROOT)}")

    text = readme.read_text(encoding="utf-8")
    text = replace_block(text, *MARKERS["main"], profile_table(config, build, "main", language, language_cfg))
    text = replace_block(text, *MARKERS["addons"], profile_table(config, build, "addon", language, language_cfg))
    text = replace_block(text, *MARKERS["parts"], parts_block(config, build, language, language_cfg))
    text = replace_block(text, *MARKERS["comparison"], comparison_table(config, language_cfg))
    text = replace_block(text, *MARKERS["special_ads_tracking"], special_lists_block(special_config, special_build, language, "ads_tracking"))
    text = replace_block(text, *MARKERS["special_security"], special_lists_block(special_config, special_build, language, "security"))
    text = replace_block(text, *MARKERS["special_network"], special_lists_block(special_config, special_build, language, "network"))
    text = replace_block(text, *MARKERS["special_family"], special_lists_block(special_config, special_build, language, "family"))
    text = update_category_counts(text, build, language)
    readme.write_text(text, encoding="utf-8")
    print(f"Synchronized {readme.relative_to(ROOT)}")


def main() -> int:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    i18n = json.loads(I18N.read_text(encoding="utf-8"))
    build = json.loads(BUILD.read_text(encoding="utf-8"))
    special_config = json.loads(SPECIAL_CONFIG.read_text(encoding="utf-8")) if SPECIAL_CONFIG.is_file() else {"items": []}
    special_build = json.loads(SPECIAL_BUILD.read_text(encoding="utf-8")) if SPECIAL_BUILD.is_file() else {}

    for language, language_cfg in i18n["languages"].items():
        update_one(ROOT / language_cfg["readme"], language, language_cfg, config, build, special_config, special_build)

    print("German and English README profiles, parts, categorized special lists, comparison matrix and category counts synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

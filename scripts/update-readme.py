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
    "ads_tracking_table": ("<!-- ADS_TRACKING_TABLE_START -->", "<!-- ADS_TRACKING_TABLE_END -->"),
    "telemetry_table": ("<!-- TELEMETRY_TABLE_START -->", "<!-- TELEMETRY_TABLE_END -->"),
    "security_table": ("<!-- SECURITY_TABLE_START -->", "<!-- SECURITY_TABLE_END -->"),
    "special_network": ("<!-- SPECIAL_NETWORK_START -->", "<!-- SPECIAL_NETWORK_END -->"),
    "family_table": ("<!-- FAMILY_TABLE_START -->", "<!-- FAMILY_TABLE_END -->"),
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
        view = "Anzeigen"
        raw = "Raw"
        parts = "Teile"
    else:
        pending = "Not built yet"
        view = "View"
        raw = "Raw"
        parts = "Parts"

    if not info or not info.get("files"):
        return pending, "—", "—"

    files = info["files"]
    entries = number(int(info.get("entries", 0)), language)
    if len(files) == 1:
        path = files[0]["file"]
        return entries, f"[{view}]({path})", f"**[{raw}]({RAW_BASE}/{path})**"

    anchor = f"#{variant['id']}-parts"
    # There is no single complete Raw file for a split list. Both cells therefore
    # lead to the complete part overview instead of silently exposing only Part 01.
    return entries, f"[{view}]({anchor})", f"**[{parts}]({anchor})**"


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
        f"<summary><strong>{label}: {len(files)} {('Teile anzeigen' if language == 'de' else 'show parts')}</strong></summary>",
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


def special_variant_row(item: dict, variant: dict, info: dict | None, language: str, first: bool) -> str:
    title = item["title_de"] if language == "de" else item["title_en"]
    description = item["description_de"] if language == "de" else item["description_en"]
    label = variant["label_de"] if language == "de" else variant["label_en"]
    multiple = len(item.get("variants", [])) > 1
    display = f"{item['icon']} **{title}{' – ' + label if multiple else ''}**"
    if first:
        display = f'<a id="list-{item["id"]}"></a>' + display
    entries, view, raw = special_variant_links(variant, info, language)
    return f"| {display} | {entries} | {description} | {view} | {raw} |"


def special_rows(config: dict, metadata: dict, language: str, section: str) -> tuple[list[str], list[str]]:
    rows: list[str] = []
    parts: list[str] = []
    metadata_items = metadata.get("items", {}) if metadata else {}
    for item in config.get("items", []):
        if int(item.get("point", 0)) >= 23 or item.get("readme_section") != section:
            continue
        item_meta = metadata_items.get(item["id"], {}).get("variants", {})
        variants = item.get("variants", [])
        if not variants:
            continue
        for idx, variant in enumerate(variants):
            info = item_meta.get(variant["id"])
            rows.append(special_variant_row(item, variant, info, language, idx == 0))
            if info and len(info.get("files", [])) > 1:
                parts.append(special_parts_table(variant, info, language))
    return rows, parts


BASE_TABLES = {
    "ads_tracking": [
        ("ads", "📣", "Werbung", "Ads", "Große Domain-Sammlung für Werbung und Werbeauslieferung", "Large advertising and ad-delivery domain set"),
        ("trackers", "👁️", "Tracker", "Trackers", "Große Sammlung von Analyse- und Tracking-Infrastruktur", "Large analytics and tracking infrastructure set"),
        ("social-trackers", "👥", "Social Tracker", "Social Trackers", "Tracking- und Analyse-Endpunkte sozialer Netzwerke", "Social-network tracking and analytics endpoints"),
        ("mobile-tracking", "📲", "Mobiles Tracking", "Mobile Tracking", "Mobile Attribution, SDK-Analysen und App-Tracking", "Mobile attribution, SDK analytics and app tracking"),
        ("native-tracking", "🧩", "Natives/App-Tracking", "Native/App Tracking", "Natives Betriebssystem-/Geräte- und Anwendungs-Tracking", "Native OS/device and application tracking"),
        ("affiliate-tracking", "🔗", "Affiliate-Tracking", "Affiliate Tracking", "Affiliate-, Klick-, Referral- und Conversion-Tracking; ab Strict enthalten", "Affiliate, click, referral and conversion tracking; included from Strict upward"),
        ("consent-cmp", "🍪", "Consent / CMP", "Consent / CMP", "Optionales Blocking von Consent-Management/CMP mit erhöhtem Risiko für Website-Fehlfunktionen", "Optional consent-management/CMP blocking with elevated website-breakage risk"),
    ],
    "telemetry": [
        ("telemetry", "📊", "Allgemeine Telemetrie", "General Telemetry", "Breite Produkt-/App-Analysen, Diagnosen und Telemetrie", "Broad product/app analytics, diagnostics and telemetry"),
        ("windows-telemetry", "🪟", "Windows-Telemetrie", "Windows Telemetry", "Windows-Diagnose- und native Telemetrie-Endpunkte", "Windows diagnostics and native telemetry endpoints"),
        ("apple-telemetry", "🍎", "Apple-Telemetrie", "Apple Telemetry", "Native Apple-Telemetrie, Metriken und Diagnosen", "Apple native telemetry, metrics and diagnostics"),
        ("android-telemetry", "🤖", "Android-Telemetrie", "Android Telemetry", "Native Android-/Hersteller-Telemetrie und Tracking", "Android/vendor native telemetry and tracking"),
        ("linux-telemetry", "🐧", "Linux-Telemetrie", "Linux Telemetry", "Telemetrie, Diagnosen und Nutzungsberichte von Linux-Distributionen", "Linux distribution telemetry, diagnostics and usage reporting"),
        ("nas-telemetry", "💾", "NAS-Telemetrie", "NAS Telemetry", "NAS-Telemetrie und Nutzungsberichte (Synology, TrueNAS und weitere)", "NAS telemetry and usage reporting (Synology, TrueNAS and others)"),
        ("server-telemetry", "🖥️", "Server-Telemetrie", "Server Telemetry", "Server-, Red-Hat-Insights- und Management-Telemetrie", "Server, Red Hat Insights and management telemetry"),
        ("smart-tv", "📺", "Smart-TV", "Smart TV", "Smart-TV-Werbung, ACR, Diagnosen und Telemetrie", "Smart-TV ads, ACR, diagnostics and telemetry"),
        ("iot", "🏠", "IoT", "IoT", "Telemetrie-/Tracking-Endpunkte von IoT- und verbundenen Geräten", "Telemetry/tracking endpoints for IoT and connected devices"),
    ],
    "security": [
        ("malware", "🦠", "Malware", "Malware", "Sehr große Sammlung von Malware-, Ransomware- und aktiven Malware-Hosts", "Massive malware, ransomware and active malware-host set"),
        ("phishing", "🎣", "Phishing", "Phishing", "Sehr große Sammlung aktiver und kuratierter Phishing-Domains", "Massive active and curated phishing-domain set"),
        ("scam", "💰", "Scam", "Scam", "Sehr große Sammlung von Betrugs-, Fraud- und täuschenden Plattform-Domains", "Massive scam, fraud and deceptive-platform domain set"),
        ("fake-shops", "🛒", "Fake-Shops", "Fake Shops", "Aggressive Sammlung potenzieller Fake-Shops und täuschender Shops", "Aggressive fake-shop/deceptive-store candidate set"),
        ("cryptomining", "⛏️", "Kryptomining", "Cryptomining", "Browser-/Remote-Mining-Infrastruktur; allgemeine Börsen sind ausgeschlossen", "Browser/remote mining infrastructure (generic exchanges excluded)"),
    ],
    "family": [
        ("adult", "🔞", "Erwachsene Inhalte", "Adult", "Sehr große Domain-Sammlung für Erwachsenen-Inhalte und Pornografie", "Massive adult-content and pornography domain set"),
        ("gambling", "🎰", "Glücksspiel", "Gambling", "Sehr große Domain-Sammlung für Wetten, Casinos und Glücksspiel", "Massive betting, casino and gambling domain set"),
    ],
}


def integrated_table(build: dict, special_config: dict, special_build: dict, language: str, section: str) -> str:
    if language == "de":
        headers = ("Liste", "Einträge", "Beschreibung", "Anzeigen", "Raw")
        view_word = "Anzeigen"
    else:
        headers = ("List", "Entries", "Description", "View", "Raw")
        view_word = "View"
    rows = [f"| {headers[0]} | {headers[1]} | {headers[2]} | {headers[3]} | {headers[4]} |", "|---|---:|---|:---:|:---:|"]
    for cat, icon, de_name, en_name, de_desc, en_desc in BASE_TABLES[section]:
        info = build.get("categories", {}).get(cat, {})
        entries = number(int(info.get("entries", 0)), language)
        name = de_name if language == "de" else en_name
        desc = de_desc if language == "de" else en_desc
        path = f"lists/categories/{cat}.txt"
        rows.append(f"| {icon} **{name}** | {entries} | {desc} | [{view_word}]({path}) | [Raw]({RAW_BASE}/{path}) |")
    ext_rows, split_parts = special_rows(special_config, special_build, language, section)
    rows.extend(ext_rows)
    if split_parts:
        rows += [""] + split_parts
    return "\n".join(rows).rstrip()


def network_table(config: dict, metadata: dict, language: str) -> str:
    if language == "de":
        headers=("Liste","Einträge","Beschreibung","Anzeigen","Raw"); doc="Dokumentation"
    else:
        headers=("List","Entries","Description","View","Raw"); doc="Documentation"
    rows=[f"| {headers[0]} | {headers[1]} | {headers[2]} | {headers[3]} | {headers[4]} |", "|---|---:|---|:---:|:---:|"]
    metadata_items = metadata.get("items", {}) if metadata else {}
    split_parts=[]
    for item in config.get("items", []):
        if int(item.get("point", 0)) >= 23 or item.get("readme_section") != "network":
            continue
        variants=item.get("variants",[])
        if not variants:
            title=item["title_de"] if language=="de" else item["title_en"]
            desc=item["description_de"] if language=="de" else item["description_en"]
            doc_path=item.get("documentation_de") if language=="de" else item.get("documentation_en")
            link=f"[{doc}]({doc_path})" if doc_path and not doc_path.startswith("#") else "—"
            rows.append(f'| <a id="list-{item["id"]}"></a>{item["icon"]} **{title}** | — | {desc} | {link} | — |')
            continue
        item_meta=metadata_items.get(item["id"],{}).get("variants",{})
        for idx, variant in enumerate(variants):
            info=item_meta.get(variant["id"])
            rows.append(special_variant_row(item, variant, info, language, idx==0))
            if info and len(info.get("files",[]))>1:
                split_parts.append(special_parts_table(variant, info, language))
    if split_parts:
        rows += [""] + split_parts
    return "\n".join(rows).rstrip()


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
    text = replace_block(text, *MARKERS["ads_tracking_table"], integrated_table(build, special_config, special_build, language, "ads_tracking"))
    text = replace_block(text, *MARKERS["telemetry_table"], integrated_table(build, special_config, special_build, language, "telemetry"))
    text = replace_block(text, *MARKERS["security_table"], integrated_table(build, special_config, special_build, language, "security"))
    text = replace_block(text, *MARKERS["special_network"], network_table(special_config, special_build, language))
    text = replace_block(text, *MARKERS["family_table"], integrated_table(build, special_config, special_build, language, "family"))
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

    print("German and English README profiles, 50-MiB parts, functionally integrated extended lists, comparison matrix and category counts synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Advanced Protection & Functional Lists

**🌐 Language / Sprache:** [🇩🇪 Deutsch](SPECIAL_LISTS.md) · 🇬🇧 **English**

BlackRabbitZ extends its existing categories with selected HaGeZi DNS blocklists. Data is **merged by function**: when a suitable BlackRabbitZ list already exists, additional domains are merged into it, normalized, deduplicated and filtered through the central allowlist. Only genuinely new functionality remains as a separate optional list or variant group.

## Primary source

The HaGeZi GitLab mirror is used for DNS blocklists:

```text
https://gitlab.com/hagezi/mirror/-/tree/main/dns-blocklists
```

Raw data is downloaded from:

```text
https://gitlab.com/hagezi/mirror/-/raw/main/dns-blocklists/
```

Original project / license reference:

```text
https://github.com/hagezi/dns-blocklists
```

## Outage behaviour

If the GitLab mirror is temporarily unavailable:

- the affected source is skipped for that run after bounded retries,
- previously generated BlackRabbitZ data is preserved,
- the remaining build continues,
- Security, Family and Ultimate are still generated,
- large profiles are split into **parts of at most 50 MiB**,
- a later workflow run retries the source automatically.

## Functional merging

| HaGeZi function | BlackRabbitZ target |
|---|---|
| Fake / Internet Fraud | existing `scam.txt` |
| Pop-Up Ads | existing `ads.txt` |
| Gambling Full | existing `gambling.txt` |
| NSFW | existing `adult.txt` |
| Native Apple | existing `apple-telemetry.txt` |
| Native Windows / Office | existing `windows-telemetry.txt` |
| Native Huawei / Samsung / Vivo / OPPO / Realme / Xiaomi | existing `android-telemetry.txt` |
| Native TikTok | existing `mobile-tracking.txt` |
| Native LG webOS / Roku | existing `smart-tv.txt` |
| Native Amazon | existing `iot.txt` |

Only functionality without a suitable existing BlackRabbitZ category remains standalone, such as Threat Intelligence, Dynamic DNS, Badware Hoster, DNS Bypass, SafeSearch, Anti Piracy, Social Network Blocking or URL Shortener.

## NRD / DGA

HaGeZi maintains NRD/DGA in a **separate `nrd` repository**, which is not part of the supplied `dns-blocklists` path in the GitLab mirror. Those sources therefore remain separately configured. If that source is unavailable, the same skip/fallback mechanism applies.

## Maintenance

All source URLs are centrally maintained in `config/special-lists.json`. Generated lists and metadata are then processed by the normal BlackRabbitZ build.

# Third-party material

**🌐 Language / Sprache:** [🇩🇪 Deutsch](THIRD_PARTY.md) · 🇬🇧 **English**

This repository contains merged and deduplicated domain indicators from third-party blocklist and threat-intelligence projects in addition to BlackRabbitZ-original entries.

The upstream projects remain authoritative. Their data can change more frequently than the snapshots committed here. Copyright, database rights, trademarks and license terms remain with their respective upstream owners.

## Imported / derived sources

- **The Block List Project** — Ads, Tracking, Malware, Ransomware, Phishing, Scam, Fraud, Porn, Gambling and Smart-TV data. The upstream repository currently identifies its project license as Unlicense; generated list headers in the downloaded snapshot also carry upstream license metadata. Preserve upstream notices when redistributing.
  - https://github.com/blocklistproject/Lists
- **Phishing.Database** — active phishing domains. MIT licensed upstream.
  - https://github.com/Phishing-Database/Phishing.Database
- **AnudeepND blacklist** — advertising/tracking and CoinMiner sources. MIT licensed upstream.
  - https://github.com/anudeepND/blacklist
- **NextDNS native-tracking-domains / click-tracking-domains** — native platform/device tracking and affiliate/click tracking domains. Native Tracking repository is MIT licensed upstream.
  - https://github.com/nextdns/native-tracking-domains
  - https://github.com/nextdns/click-tracking-domains
- **Perflyst PiHoleBlocklist** — Android, Smart-TV and Amazon Fire TV tracking/telemetry sources. MIT licensed upstream.
  - https://github.com/Perflyst/PiHoleBlocklist
- **HaGeZi DNS Blocklists** — Apple native tracking, LG webOS and Gambling sources. Preserve the upstream GPL/license notices and attribution.
  - https://github.com/hagezi/dns-blocklists
- **StevenBlack/hosts** — porn-only extension used for the Adult category. MIT licensed upstream.
  - https://github.com/StevenBlack/hosts
- **NoCoin** — browser cryptomining domains. MIT licensed upstream.
  - https://github.com/hoshsadiq/adblock-nocoin-list
- **DurableNapkin Scam Blocklist** — scam indicators; MIT licensed upstream.
  - https://github.com/durablenapkin/scamblocklist
- **URLhaus (abuse.ch / Spamhaus)** — active malware-distribution hosts.
  - https://urlhaus.abuse.ch/
  - https://urlhaus.abuse.ch/downloads/hostfile/
- **BaFin** — curated public consumer warnings retained from the prior Scam list.
  - https://www.bafin.de/DE/verbraucherinnen-verbraucher/news-warnungen/news-warnungen_node.html
- **Verbraucherzentrale / Fakeshop-Finder** — curated public fake-shop warnings retained from the prior Fake Shops list.
  - https://www.verbraucherzentrale.de/fakeshopfinder-71560
- **Vendor documentation** (Canonical/Debian, Synology/TrueNAS/QNAP, Red Hat, Dell, HPE) — small telemetry endpoint sets used for Linux, NAS and Server categories.


## HaGeZi upstream data for extended functional lists

BlackRabbitZ uses the HaGeZi GitLab mirror as the primary technical download source for DNS blocklists.

- GitLab mirror: `https://gitlab.com/hagezi/mirror/-/tree/main/dns-blocklists`
- Original project: `https://github.com/hagezi/dns-blocklists`
- License: GPL-3.0
- Build configuration: `config/special-lists.json`
- Functionally integrated domain lists: `lists/categories/`
- Machine-readable metadata: `metadata/special-lists.json`

Data is normalized, deduplicated, checked against the allowlist and integrated into existing BlackRabbitZ categories by function. Original HaGeZi provenance and licensing remain documented. Temporary source outages do not stop the remaining BlackRabbitZ build.

## Derived subsets

Some categories are derived from broader upstream datasets using category-specific matching:

- `telemetry.txt` — telemetry/analytics/metrics/diagnostics subset of tracking data.
- `social-trackers.txt` — social-platform tracking subset.
- `mobile-tracking.txt` — mobile analytics/attribution SDK subset plus Android tracking data.
- `affiliate-tracking.txt` — affiliate/click/referral subset plus NextDNS click tracking data.
- `consent-cmp.txt` — consent-management/CMP subset.
- `fake-shops.txt` — retail/store-looking subset of scam/fraud intelligence plus curated fake-shop warnings.

Derived categories are intentionally aggressive. A domain's presence in a derived category is a blocking classification, not a legal finding about the domain owner.

## Redistribution

BlackRabbitZ-original material remains under `GPL-3.0-only`. Third-party material remains subject to its applicable upstream license and notices. When redistributing substantial portions of an upstream dataset, preserve that project's required copyright, permission and attribution notices and consult the linked upstream license as the authoritative version.

### Modification notice for HaGeZi-derived data

As of **12 August 2026**, material derived from HaGeZi is normalized, deduplicated, filtered through the global allowlist where applicable, functionally re-categorized, published under BlackRabbitZ file names and split into parts up to 50 MiB when large. Source provenance remains in generated file headers and in this third-party documentation.

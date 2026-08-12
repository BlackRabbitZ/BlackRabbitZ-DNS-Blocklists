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


## Archived special lists (topics 7–22)

BlackRabbitZ can additionally import the HaGeZi special lists documented by the **2 August 2026** Wayback snapshot. The original lists were published under GPL-3.0. Because the original repository is currently not a reliable live upstream, these datasets are **clearly treated as archived third-party sources** and are not presented as current HaGeZi feeds.

- Archived repository page: `https://web.archive.org/web/20260802022304/https://github.com/hagezi/dns-blocklists`
- Original project: `https://github.com/hagezi/dns-blocklists`
- Build configuration: `config/special-lists.json`
- Generated domain lists: `lists/special/`
- Generated IPv4 lists: `lists/ips/`
- Machine-readable provenance/checksums: `metadata/special-lists.json`

The configuration points to the corresponding archived Raw captures. For some files, the 2 August snapshot redirects to the nearest available Wayback capture of that same file. BlackRabbitZ normalizes domain/IP variants and splits large outputs; Adblock-specific syntax is preserved only where it is required for the list to work (for example TLD rules).

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

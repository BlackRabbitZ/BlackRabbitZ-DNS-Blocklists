# Advanced Protection & Special Lists

**🌐 Language / Sprache:** [🇩🇪 Deutsch](SPECIAL_LISTS.md) · 🇬🇧 **English**

BlackRabbitZ maps HaGeZi topics **7 through 24** from the archived repository state dated **2 August 2026**. The actual blocklists from topics 7–22 are built from archived raw data where a static list existed. Topics 23 and 24 were documentation sections, so they are represented as **Recommendations** and **Online DNS Services** in the README.

Archived source page:

```text
https://web.archive.org/web/20260802022304/https://github.com/hagezi/dns-blocklists
```

## Important archive note

These files are **not current HaGeZi feeds**. They are frozen Wayback snapshots at, or as close as practical to, the August 2026 state. BlackRabbitZ:

- preserves source and GPL attribution in `THIRD_PARTY_EN.md`,
- normalizes domain and IPv4 lists,
- removes exact matches from `config/allowlist.txt` from domain variants,
- deduplicates and sorts normal domain/IP variants,
- splits large output files to a maximum of **50 MiB each**,
- keeps archived extended lists separate from normal daily BlackRabbitZ upstream feeds.

## Included areas

| Point | BlackRabbitZ area | Variants / implementation | Risk |
|---:|---|---|---|
| 7 | Fake & Internet Scams | Full | Medium |
| 8 | Pop-Up Ads | Full | Medium |
| 9 | Threat Intelligence Feeds | Full, Medium, Mini, IPv4 | Medium–High |
| 10 | NRD / DGA | five NRD time windows + DGA 7/14/30 days | Very high |
| 11 | DNS Bypass Protection | Full, DoH-only, DoH-IPv4 | High |
| 12 | SafeSearch Not Supported | domain list | High |
| 13 | Dynamic DNS | domain list | High |
| 14 | Badware Hoster | domain list | Very high |
| 15 | URL Shortener | domain list | Very high |
| 16 | Most Abused TLDs | archived Adblock format | Very high |
| 17 | DNS Rebind Protection | Pi-hole/dnsmasq documentation | Configuration |
| 18 | Anti Piracy | domain list | High |
| 19 | Gambling | Full, Medium, Mini | High |
| 20 | Social Networks | domain list | Very high |
| 21 | NSFW | domain list | High |
| 22 | Native Tracker | Amazon, Apple, Huawei, Microsoft, Samsung, TikTok, LG webOS, Roku, Vivo, OPPO/Realme, Xiaomi | Medium–High |
| 23 | Recommendations | README documentation | — |
| 24 | Online DNS Services | README documentation | — |

## Why NRD/DGA is not rebuilt every day

The archived NRD datasets are extremely large. In the HaGeZi snapshot, each of the five NRD weekly windows contained multiple millions of domains, in addition to DGA/entropy variants. These datasets can dramatically increase repository size and DNS-blocker memory use.

Archived extended lists are therefore **not** downloaded by the normal daily upstream refresh. They have a dedicated GitHub Actions workflow:

```text
Actions → Update archived extended lists → Run workflow
```

To build every point-7-through-22 variant, leave **“Build large NRD/DGA lists”** enabled.

## Directories

```text
lists/categories/   # domain/Adblock extended lists and 50-MiB parts
lists/ips/       # IPv4 extended lists
metadata/special-lists.json
```

The README reads `metadata/special-lists.json` and automatically creates counts, View/Raw links and part tables.

## Format notes

### Domain lists

Normal extended lists are published as one domain per line and can be used like other BlackRabbitZ lists.

### IPv4 lists

TIF and DoH IPv4 variants are **not normal Pi-hole Adlists**. They are intended for firewalls or DNS products that explicitly support IP/network lists.

### Most Abused TLDs

The archived TLD variant is preserved in its original **Adblock rule format**. It is not blindly converted to a plain-domain list because doing so would change wildcard and exception semantics.

### DNS rebind protection

HaGeZi's archived rebind list targeted AdGuard/AdGuard Home. Pi-hole has its own rebind mechanisms through FTL/dnsmasq. BlackRabbitZ therefore implements point 17 as configuration documentation rather than an unsuitable static Adlist:

[`DNS_REBIND_PROTECTION_EN.md`](DNS_REBIND_PROTECTION_EN.md)

## Maintenance

Archived raw sources are not expected to change. Rebuilding is useful when:

- the BlackRabbitZ allowlist changes,
- the split limit or normalizer changes,
- a missing Wayback resource is replaced by a better archived snapshot,
- generated files should be regenerated.

New **current** third-party feeds should continue to go through the normal BlackRabbitZ upstream review process and must not silently be presented as “current HaGeZi”.

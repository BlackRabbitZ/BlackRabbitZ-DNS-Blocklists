# Advanced Protection & Functional Lists

**🌐 Language / Sprache:** [🇩🇪 Deutsch](SPECIAL_LISTS.md) · 🇬🇧 **English**

BlackRabbitZ integrates additional HaGeZi functional lists **by function** into the existing BlackRabbitZ sections. Overlapping data is not published as duplicate parallel lists. Only functionality for which BlackRabbitZ has no suitable existing list remains as a separate optional list or compact variant group.

## Upstream behaviour

The update configuration uses **no Wayback/archive URL as a data source**. It attempts to fetch the original live/CDN/raw upstream sources directly.

If a source is temporarily unavailable:

- it is skipped for that run after bounded retries,
- already generated BlackRabbitZ data is preserved,
- the remaining list build continues,
- Security, Family and Ultimate can still be rebuilt and split into **parts of at most 50 MiB**,
- a later workflow run retries the unavailable source automatically.

Original project:

```text
https://github.com/hagezi/dns-blocklists
```

## Included areas

| Point | BlackRabbitZ area | Variants / implementation | Risk |
|---:|---|---|---|
| 7 | Scam & Internet Fraud | merged into existing `scam.txt` | Medium |
| 8 | Ads | merged into existing `ads.txt` | Medium |
| 9 | Threat Intelligence Feeds | Full, Medium, Mini, IPv4 | Medium–High |
| 10 | NRD / DGA | five NRD time windows + DGA 7/14/30 days | Very high |
| 11 | DNS Bypass Protection | Full, DoH-only, DoH-IPv4 | High |
| 12 | SafeSearch Not Supported | domain list | High |
| 13 | Dynamic DNS | domain list | High |
| 14 | Badware Hoster | domain list | Very high |
| 15 | URL Shortener | domain list | Very high |
| 16 | Most Abused TLDs | Adblock format | Very high |
| 17 | DNS Rebind Protection | Pi-hole/dnsmasq documentation | Configuration |
| 18 | Anti Piracy | domain list | High |
| 19 | Gambling | Full merged into `gambling.txt`; Medium/Mini optional | High |
| 20 | Social Networks | domain list | Very high |
| 21 | NSFW | merged into existing `adult.txt` | High |
| 22 | Native Tracker | merged into Apple/Windows/Android/Smart-TV/IoT/Mobile Tracking lists | Medium–High |
| 23 | Recommendations | README documentation | — |
| 24 | Online DNS Services | README documentation | — |

## Directories

```text
lists/categories/   # existing categories + functionally new optional lists/parts
lists/ips/          # optional IPv4 variants
metadata/special-lists.json
```

The README reads `metadata/special-lists.json` and automatically generates counts, View/Raw links and part tables.

## Maintenance

Source URLs are maintained centrally in `config/special-lists.json`. Temporary upstream outages are **non-fatal** and do not stop the normal BlackRabbitZ build.

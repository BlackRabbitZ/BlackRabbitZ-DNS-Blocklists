# Migration to v3.3.3

This release fixes two aspects of the previous integration:

1. **Profile parts are actually rebuilt at up to 50 MiB.** Legacy 5-MiB Security, Family and Ultimate parts are deleted before publishing, and validation detects stale undersized parts afterwards.
2. **Overlapping extended sources no longer create parallel lists.** They are merged and deduplicated into existing BlackRabbitZ functional categories.

## Automatic routing

| Extended source | BlackRabbitZ target |
|---|---|
| Fake / Internet Scam | `scam.txt` |
| Pop-Up Ads | `ads.txt` |
| Gambling Full | `gambling.txt` |
| NSFW | `adult.txt` |
| Apple Native Tracker | `apple-telemetry.txt` |
| Microsoft/Windows/Office Native Tracker | `windows-telemetry.txt` |
| Huawei, Samsung, Vivo, OPPO/Realme, Xiaomi | `android-telemetry.txt` |
| TikTok Native Tracker | `mobile-tracking.txt` |
| LG webOS, Roku | `smart-tv.txt` |
| Amazon | `iot.txt` |

Threat Intelligence, NRD/DGA, DNS Bypass, Dynamic DNS, Badware Hoster, URL Shortener, TLD rules, SafeSearch, Anti-Piracy and Social-Network blocking remain optional standalone functions because no equivalent existing BlackRabbitZ category exists.

## First run

After the commit, **Update blocklists** starts automatically. The workflow:

1. migrates already generated parallel files into their functional targets or downloads the archived source when only a placeholder exists,
2. removes legacy parallel outputs only after a successful merge,
3. deletes legacy 5-MiB profile parts,
4. rebuilds Security, Family and Ultimate with at most 50 MiB per part,
5. regenerates metadata, checksums and both READMEs.

After the bot commit, use **Fetch origin** in GitHub Desktop before making more local changes.

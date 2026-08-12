<div align="center">

# 🐇 BlackRabbitZ DNS Blocklists
### Privacy • Security • Ads • Trackers • Telemetry

[![License: GPL-3.0-only](https://img.shields.io/badge/License-GPL--3.0--only-blue.svg)](LICENSE)
![Pi-hole](https://img.shields.io/badge/Pi--hole-Compatible-brightgreen)
![Static Lists](https://img.shields.io/badge/Lists-Static-success)
![Maintainer](https://img.shields.io/badge/Maintainer-BlackRabbitZ-black)
![End Users](https://img.shields.io/badge/End%20Users-No%20Python-success)
[![Update blocklists](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/actions/workflows/update-lists.yml/badge.svg)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/actions/workflows/update-lists.yml)

**Static, transparent DNS blocklists for Pi-hole and compatible DNS filtering solutions.**

</div>

---

## ⚡ Quick Start

### ⭐ Recommended: Balanced

For most users, **Balanced** is the best starting point. It blocks advertising, general trackers and social tracking while deliberately leaving affiliate/referral infrastructure out of the default profile to reduce avoidable breakage.

```text
https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/balanced.txt
```

**Pi-hole**

1. Open the Pi-hole web interface.
2. Go to **Lists / Adlists**.
3. Add the Raw URL above.
4. Save.
5. Update Gravity.

---

# 🚀 Privacy Protection Profiles

These are the main protection levels. Start with **Balanced** and move to **Strict** or **Ultimate** only when you intentionally want more aggressive privacy filtering.

<!-- MAIN_PROFILES_START -->
| Profile | Protection | Entries | Recommended for | View | Raw |
|---|:---:|---:|---|:---:|:---:|
| 🟢 **Light** | Low | **234,038** | Basic ad blocking | [View](lists/combined/light.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/light.txt)** |
| 🔵 **Balanced ⭐** | Medium | **371,660** | Most users | [View](lists/combined/balanced.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/balanced.txt)** |
| 🟠 **Strict** | High | **372,540** | Privacy-focused setups | [View](lists/combined/strict.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/strict.txt)** |
| 🔴 **Ultimate** | Maximum | **5,169,019** | Aggressive filtering | [Show Parts](#ultimate-parts) | **[Raw Parts](#ultimate-parts)** |
<!-- MAIN_PROFILES_END -->

> **Balanced** is recommended for most installations.  
> **Strict** adds affiliate tracking, telemetry, device telemetry and native/app tracking.  
> **Ultimate** is intentionally aggressive and can affect telemetry-dependent features, Smart-TV functions, app analytics, gaming telemetry and cloud-backed services. **Consent/CMP remains an optional standalone category instead of being forced into Ultimate.**

---

# 🧩 Optional Protection Modules

These profiles solve a different problem than the privacy tiers above. They are best treated as **add-ons**, not as “stronger versions” of Balanced or Strict.

<!-- ADDON_PROFILES_START -->
| Profile | Protection | Entries | Recommended for | View | Raw |
|---|:---:|---:|---|:---:|:---:|
| 🛡️ **Security** | Security | **3,458,013** | Security-focused filtering | [Show Parts](#security-parts) | **[Raw Parts](#security-parts)** |
| 👨‍👩‍👧 **Family** | Family | **1,788,212** | Family networks | [Show Parts](#family-parts) | **[Raw Parts](#family-parts)** |
<!-- ADDON_PROFILES_END -->

- **Security** focuses on malware, phishing, scams, fake shops and cryptomining. It can be combined with Balanced or Strict.
- **Family** adds advertising/tracking protection plus adult and gambling filtering.
- **Gaming Privacy**, **Consent/CMP** and other category lists remain separately selectable below so users can add only what they actually want.

---

# 📦 Large Profile Parts

Large combined profiles are generated as deterministic, size-bounded files. Add **every part** of a split profile for complete coverage. Parts use zero-padded names such as `security-part-01.txt` and target a maximum of **5 MiB per file**.

Upgrading from the previous `security.txt` / `family.txt` / `ultimate-N.txt` layout? See [`docs/MIGRATION_V3.md`](docs/MIGRATION_V3.md).

<!-- SPLIT_PROFILES_START -->
> Split profile links are generated automatically by `scripts/update-readme.py` during the first rebuild.
<!-- SPLIT_PROFILES_END -->

---

# 🎚️ Protection Comparison

<!-- COMPARISON_START -->
| Feature | Light | Balanced ⭐ | Strict | Security | Family | Ultimate |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Advertising | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| General Trackers | — | ✅ | ✅ | — | ✅ | ✅ |
| Social Tracking | — | ✅ | ✅ | — | ✅ | ✅ |
| Affiliate Tracking | — | — | ✅ | — | — | ✅ |
| General Telemetry | — | — | ✅ | — | — | ✅ |
| Gaming Telemetry | — | — | — | — | — | ✅ |
| Windows Telemetry | — | — | ✅ | — | — | ✅ |
| Apple Telemetry | — | — | ✅ | — | — | ✅ |
| Android Telemetry | — | — | ✅ | — | — | ✅ |
| Linux Telemetry | — | — | ✅ | — | — | ✅ |
| NAS Telemetry | — | — | ✅ | — | — | ✅ |
| Server Telemetry | — | — | ✅ | — | — | ✅ |
| Mobile/App Tracking | — | — | ✅ | — | — | ✅ |
| Smart-TV / IoT | — | — | ✅ | — | — | ✅ |
| Cryptomining | — | — | — | ✅ | — | ✅ |
| Malware / Phishing / Scam / Fake Shops | — | — | — | ✅ | — | ✅ |
| Consent / CMP | — | — | — | — | — | — |
| Adult | — | — | — | — | ✅ | ✅ |
| Gambling | — | — | — | — | ✅ | ✅ |
| Breakage Risk | 🟢 Low | 🔵 Low–Medium | 🟠 Higher | 🟡 Medium | 🟠 Higher | 🔴 Highest |
<!-- COMPARISON_END -->

---

# 📢 Ads & Tracking

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 📣 **Ads** | 234,038 | Large advertising and ad-delivery domain set | [View](lists/categories/ads.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/ads.txt) |
| 👁️ **Trackers** | 143,941 | Large analytics and tracking infrastructure set | [View](lists/categories/trackers.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/trackers.txt) |
| 👥 **Social Trackers** | 99 | Social-network tracking and analytics endpoints | [View](lists/categories/social-trackers.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/social-trackers.txt) |
| 📲 **Mobile Tracking** | 202 | Mobile attribution, SDK analytics and app tracking | [View](lists/categories/mobile-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/mobile-tracking.txt) |
| 🧩 **Native/App Tracking** | 1,466 | Native OS/device and application tracking | [View](lists/categories/native-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/native-tracking.txt) |
| 🔗 **Affiliate Tracking** | 643 | Affiliate, click, referral and conversion tracking; included from Strict upward | [View](lists/categories/affiliate-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/affiliate-tracking.txt) |
| 🍪 **Consent / CMP** | 44 | Optional consent-management/CMP blocking with elevated website-breakage risk | [View](lists/categories/consent-cmp.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/consent-cmp.txt) |

> **Consent/CMP is deliberately not included in the combined protection profiles.** DNS-level blocking of consent infrastructure can interfere with page loading, consent state and site functionality.

---

# 📡 Telemetry & Devices

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 📊 **General Telemetry** | 29,289 | Broad product/app analytics, diagnostics and telemetry | [View](lists/categories/telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/telemetry.txt) |
| 🪟 **Windows Telemetry** | 425 | Windows diagnostics and native telemetry endpoints | [View](lists/categories/windows-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/windows-telemetry.txt) |
| 🍎 **Apple Telemetry** | 119 | Apple native telemetry, metrics and diagnostics | [View](lists/categories/apple-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/apple-telemetry.txt) |
| 🤖 **Android Telemetry** | 1,310 | Android/vendor native telemetry and tracking | [View](lists/categories/android-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/android-telemetry.txt) |
| 🐧 **Linux Telemetry** | 3 | Linux distribution telemetry, diagnostics and usage reporting | [View](lists/categories/linux-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/linux-telemetry.txt) |
| 💾 **NAS Telemetry** | 12 | NAS telemetry and usage reporting (Synology, TrueNAS and others) | [View](lists/categories/nas-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/nas-telemetry.txt) |
| 🖥️ **Server Telemetry** | 10 | Server, Red Hat Insights and management telemetry | [View](lists/categories/server-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/server-telemetry.txt) |
| 📺 **Smart TV** | 556 | Smart-TV advertising, ACR, diagnostics and telemetry | [View](lists/categories/smart-tv.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/smart-tv.txt) |
| 🏠 **IoT** | 85 | IoT and connected-device telemetry/tracking endpoints | [View](lists/categories/iot.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/iot.txt) |

> Device-specific lists may disable recommendations, diagnostics, usage reporting, ACR, advertising or other cloud-backed features.

---

# 🎮 Gaming Privacy

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 🎮 **Gaming Telemetry** | 38 | Recommended game, launcher, analytics and crash-reporting endpoints with lower breakage risk | [View](lists/categories/gaming-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gaming-telemetry.txt) |
| ⚠️ **Gaming Telemetry – Aggressive** | 62 | Optional additional endpoints with increased launcher, login and gameplay breakage risk | [View](lists/categories/gaming-telemetry-aggressive.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gaming-telemetry-aggressive.txt) |
| 🧩 **Gaming RegEx Rules** | 5 | Dynamic Pi-hole deny patterns; import individually, not as a normal Adlist | [View](lists/regex/gaming-telemetry-regex.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regex/gaming-telemetry-regex.txt) |

> Start with **Gaming Telemetry**. The aggressive list and RegEx rules can interfere with Battle.net, Epic, Rockstar, Riot, EA and individual games. Test them in a separate Pi-hole group first.

---

# 🛡️ Security Lists

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 🦠 **Malware** | 2,710,231 | Massive malware, ransomware and active malware-host set | [View](lists/categories/malware.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/malware.txt) |
| 🎣 **Phishing** | 572,332 | Massive active and curated phishing-domain set | [View](lists/categories/phishing.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/phishing.txt) |
| 💰 **Scam** | 266,444 | Massive scam, fraud and deceptive-platform domain set | [View](lists/categories/scam.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/scam.txt) |
| 🛒 **Fake Shops** | 11,380 | Aggressive fake-shop/deceptive-store candidate set | [View](lists/categories/fake-shops.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/fake-shops.txt) |
| ⛏️ **Cryptomining** | 6,121 | Browser/remote mining infrastructure (generic exchanges excluded) | [View](lists/categories/cryptomining.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/cryptomining.txt) |

> Security lists are intentionally **large and aggressive** and merge multiple upstream intelligence sources. Threat data changes quickly, so false positives are possible and upstream snapshots should be refreshed regularly.

---

# 👨‍👩‍👧 Family Lists

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 🔞 **Adult** | 999,123 | Massive adult-content and pornography domain set | [View](lists/categories/adult.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/adult.txt) |
| 🎰 **Gambling** | 420,536 | Massive betting, casino and gambling domain set | [View](lists/categories/gambling.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gambling.txt) |

> Future parental-control modules such as SafeSearch or DNS-bypass protection should be added only after their data sources and breakage behavior are independently validated. They are intentionally not fabricated or enabled by default here.

---

# 🌐 Upstream Sources & Build Transparency

The large category lists merge and deduplicate selected upstream DNS/threat-intelligence datasets. Source and license details are documented in [`THIRD_PARTY.md`](THIRD_PARTY.md).

- Category files are published as plain domains, one domain per line.
- `.github/workflows/daily-upstream-update.yml` checks configured upstream feeds every day and additively imports newly published domains.
- `scripts/update-upstreams.py` validates, normalizes, deduplicates and safety-checks upstream data before category files are changed.
- `config/profiles.json` is the single source of truth for profile composition, display metadata and split behavior.
- `scripts/update-lists.sh` rebuilds all combined profiles, metadata, checksums and README values after category changes.
- Upstream URLs and per-source safety thresholds remain in [`scripts/upstream-sources.json`](scripts/upstream-sources.json).
- [`metadata/build.json`](metadata/build.json) contains machine-readable counts, part files, sizes and SHA-256 hashes.
- [`metadata/SHA256SUMS`](metadata/SHA256SUMS) provides checksums for all published category and combined list files.

See [`docs/AUTOMATIC_UPDATES.md`](docs/AUTOMATIC_UPDATES.md) for the complete update and fail-safe behavior.

---

# 📂 Repository Structure

```text
BlackRabbitZ-DNS-Blocklists/
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── false-positive.yml
│   │   ├── domain-request.yml
│   │   └── upstream-source.yml
│   └── workflows/
│       ├── update-lists.yml
│       └── daily-upstream-update.yml
├── config/
│   ├── allowlist.txt
│   └── profiles.json
├── docs/
│   ├── AUTOMATIC_UPDATES.md
│   └── MIGRATION_V3.md
├── metadata/
│   ├── build.json
│   └── SHA256SUMS
├── scripts/
│   ├── update-lists.sh
│   ├── publish-profile.py
│   ├── generate-metadata.py
│   ├── update-readme.py
│   ├── validate-generated.py
│   ├── update-upstreams.py
│   └── upstream-sources.json
├── README.md
├── CHANGELOG.md
├── LICENSE
├── NOTICE
├── ATTRIBUTION.md
├── THIRD_PARTY.md
│
└── lists/
    ├── combined/
    │   ├── light.txt
    │   ├── balanced.txt
    │   ├── strict.txt
    │   ├── security-part-01.txt
    │   ├── family-part-01.txt
    │   ├── ultimate-part-01.txt
    │   └── ... additional numbered parts
    │
    ├── regex/
    │   └── gaming-telemetry-regex.txt
    │
    └── categories/
        └── ... individual category lists
```

Every published blocklist remains a normal **static text file** and can be consumed directly by Pi-hole or compatible DNS filters. Repository maintenance uses **Python, Bash and GitHub Actions**; end users still need no Python runtime.

---

# 🔄 Automatic List Updates

Two GitHub Actions keep the repository current:

1. **Daily upstream refresh** runs every day at `03:17 UTC`. It downloads the configured public feeds, normalizes their domains and **adds newly published entries** to the matching category files.
2. **Update blocklists** runs after category, profile-config or build-script changes and keeps generated files synchronized.

The build pipeline:

```text
Upstreams / category edits
        ↓
Normalize + validate + allowlist
        ↓
Category files
        ↓
Profile config
        ↓
Merge + deduplicate + sort
        ↓
Split large profiles (5 MiB parts)
        ↓
Validate ordering / uniqueness / part sizes
        ↓
Generate build.json + SHA256SUMS
        ↓
Synchronize README
```

Automatic upstream imports remain **additive**: the updater can extend the lists automatically, but it does not silently delete existing BlackRabbitZ entries. Specialized gaming/Linux/NAS/server telemetry lists can remain manually curated when no sufficiently trustworthy general-purpose upstream exists.

---

# ➕ Extending the Lists

To add domains to an existing category, edit the corresponding file under:

```text
lists/categories/
```

Add one domain per line. After a category change, the GitHub Action recalculates entry counts and rebuilds every affected combined profile automatically.

To change which categories belong to a profile, edit:

```text
config/profiles.json
```

Do **not** manually edit generated combined profile parts, `metadata/build.json` or `metadata/SHA256SUMS`.

---

# ⚠️ False Positives

Blocking more domains does not automatically mean better protection.

If a list breaks a website, application or device, use the **False positive** issue template and include the affected domain, list/profile, application/device, what stops working and reproduction steps.

The goal is a useful blocklist, not the largest possible number.

---

# 📜 License & Attribution

This repository is licensed under **GNU GPL v3 (`GPL-3.0-only`)**.

**Copyright © 2026 BlackRabbitZ**

Original repository:

```text
https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists
```

See:

- [`LICENSE`](LICENSE)
- [`NOTICE`](NOTICE)
- [`ATTRIBUTION.md`](ATTRIBUTION.md)
- [`THIRD_PARTY.md`](THIRD_PARTY.md)

---

<div align="center">

### 🐇 BlackRabbitZ DNS Blocklists

**Privacy. Security. Control.**

⭐ If this project is useful to you, consider starring the repository.

</div>

<div align="center">

# 🐇 BlackRabbitZ DNS Blocklists

### Privacy • Security • Ads • Trackers • Telemetry

[![License: GPL-3.0-only](https://img.shields.io/badge/License-GPL--3.0--only-blue.svg)](LICENSE)
![Pi-hole](https://img.shields.io/badge/Pi--hole-Compatible-brightgreen)
![Static Lists](https://img.shields.io/badge/Lists-Static-success)
![Maintainer](https://img.shields.io/badge/Maintainer-BlackRabbitZ-black)
![Python](https://img.shields.io/badge/Python-None-success)
[![Update blocklists](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/actions/workflows/update-lists.yml/badge.svg)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/actions/workflows/update-lists.yml)

**Static, transparent DNS blocklists for Pi-hole and compatible DNS filtering solutions.**

</div>

---

## ⚡ Quick Start

### ⭐ Recommended: Balanced

For most users, **Balanced** is the best starting point.

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

# 🚀 Protection Profiles

| Profile | Protection | Entries | Recommended for | View | Raw |
|---|:---:|---:|---|:---:|:---:|
| 🟢 **Light** | Low | **234038** | Basic ad blocking | [View](lists/combined/light.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/light.txt)** |
| 🔵 **Balanced ⭐** | Medium | **371660** | Most users | [View](lists/combined/balanced.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/balanced.txt)** |
| 🟠 **Strict** | High | **371769** | Privacy-focused setups | [View](lists/combined/strict.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/strict.txt)** |
| 🛡️ **Security** | Security | **3408852** | Security-focused filtering | [View](lists/combined/security.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security.txt)** |
| 👨‍👩‍👧 **Family** | Family | **1788212** | Family networks | [View](lists/combined/family.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family.txt)** |
| 🔴 **Ultimate** | Maximum | **5119323** | Aggressive filtering | [View](lists/combined/ultimate.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate.txt)** |

> **Balanced** is recommended for most installations.  
> **Strict** and **Ultimate** may block telemetry-dependent features, Smart-TV functionality, app analytics or other cloud-backed services.  
> **Security**, **Family** and especially **Ultimate** are now large merged profiles; review false positives before deploying them to critical networks.

---

# 🎚️ Protection Comparison

| Feature | Light | Balanced ⭐ | Strict | Security | Family | Ultimate |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Advertising | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| General Trackers | — | ✅ | ✅ | — | ✅ | ✅ |
| Social Tracking | — | ✅ | ✅ | — | ✅ | ✅ |
| Affiliate Tracking | — | ✅ | ✅ | — | — | ✅ |
| General Telemetry | — | — | ✅ | — | — | ✅ |
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
| Consent / CMP | — | — | — | — | — | ✅ |
| Adult | — | — | — | — | ✅ | ✅ |
| Gambling | — | — | — | — | ✅ | ✅ |
| Breakage Risk | 🟢 Low | 🔵 Low–Medium | 🟠 Higher | 🟡 Medium | 🟠 Higher | 🔴 Highest |

---

# 📢 Ads & Tracking

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 📣 **Ads** | 234038 | Large advertising and ad-delivery domain set | [View](lists/categories/ads.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/ads.txt) |
| 👁️ **Trackers** | 143941 | Large analytics and tracking infrastructure set | [View](lists/categories/trackers.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/trackers.txt) |
| 👥 **Social Trackers** | 99 | Social-network tracking and analytics endpoints | [View](lists/categories/social-trackers.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/social-trackers.txt) |
| 📲 **Mobile Tracking** | 202 | Mobile attribution, SDK analytics and app tracking | [View](lists/categories/mobile-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/mobile-tracking.txt) |
| 🧩 **Native/App Tracking** | 628 | Native OS/device and application tracking | [View](lists/categories/native-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/native-tracking.txt) |
| 🔗 **Affiliate Tracking** | 643 | Affiliate, click, referral and conversion tracking | [View](lists/categories/affiliate-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/affiliate-tracking.txt) |
| 🍪 **Consent / CMP** | 44 | Consent-management and CMP infrastructure | [View](lists/categories/consent-cmp.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/consent-cmp.txt) |

---

# 📡 Telemetry & Devices

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 📊 **General Telemetry** | 29289 | Broad product/app analytics, diagnostics and telemetry | [View](lists/categories/telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/telemetry.txt) |
| 🪟 **Windows Telemetry** | 51 | Windows diagnostics and native telemetry endpoints | [View](lists/categories/windows-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/windows-telemetry.txt) |
| 🍎 **Apple Telemetry** | 119 | Apple native telemetry, metrics and diagnostics | [View](lists/categories/apple-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/apple-telemetry.txt) |
| 🤖 **Android Telemetry** | 138 | Android/vendor native telemetry and tracking | [View](lists/categories/android-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/android-telemetry.txt) |
| 🐧 **Linux Telemetry** | 3 | Linux distribution telemetry, diagnostics and usage reporting | [View](lists/categories/linux-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/linux-telemetry.txt) |
| 💾 **NAS Telemetry** | 12 | NAS telemetry and usage reporting (Synology, TrueNAS and others) | [View](lists/categories/nas-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/nas-telemetry.txt) |
| 🖥️ **Server Telemetry** | 10 | Server, Red Hat Insights and management telemetry | [View](lists/categories/server-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/server-telemetry.txt) |
| 📺 **Smart TV** | 556 | Smart-TV advertising, ACR, diagnostics and telemetry | [View](lists/categories/smart-tv.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/smart-tv.txt) |
| 🏠 **IoT** | 85 | IoT and connected-device telemetry/tracking endpoints | [View](lists/categories/iot.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/iot.txt) |

> Device-specific lists may disable recommendations, diagnostics, usage reporting, ACR, advertising or other cloud-backed features.

---

# 🛡️ Security Lists

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 🦠 **Malware** | 2656445 | Massive malware, ransomware and active malware-host set | [View](lists/categories/malware.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/malware.txt) |
| 🎣 **Phishing** | 577791 | Massive active and curated phishing-domain set | [View](lists/categories/phishing.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/phishing.txt) |
| 💰 **Scam** | 265330 | Massive scam, fraud and deceptive-platform domain set | [View](lists/categories/scam.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/scam.txt) |
| 🛒 **Fake Shops** | 10964 | Aggressive fake-shop/deceptive-store candidate set | [View](lists/categories/fake-shops.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/fake-shops.txt) |
| ⛏️ **Cryptomining** | 6121 | Browser/remote mining infrastructure (generic exchanges excluded) | [View](lists/categories/cryptomining.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/cryptomining.txt) |

> Security lists are intentionally **large and aggressive** and merge multiple upstream intelligence sources. Threat data changes quickly, so false positives are possible and upstream snapshots should be refreshed regularly.

---

# 👨‍👩‍👧 Family Lists

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 🔞 **Adult** | 999123 | Massive adult-content and pornography domain set | [View](lists/categories/adult.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/adult.txt) |
| 🎰 **Gambling** | 420536 | Massive betting, casino and gambling domain set | [View](lists/categories/gambling.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gambling.txt) |

---

# 🌐 Upstream Sources & Large Lists

The large category lists merge and deduplicate selected upstream DNS/threat-intelligence datasets. Source and license details are documented in [`THIRD_PARTY.md`](THIRD_PARTY.md).

- Category files are published as plain domains, one domain per line.
- `.github/workflows/daily-upstream-update.yml` checks configured upstream feeds every day and additively imports newly published domains.
- `scripts/update-upstreams.py` validates, normalizes, deduplicates and safety-checks upstream data before category files are changed.
- `scripts/update-lists.sh` rebuilds all combined profiles and synchronizes README entry counts after category changes.
- Upstream URLs and per-source safety thresholds are maintained in [`scripts/upstream-sources.json`](scripts/upstream-sources.json).
- The `Ultimate` profile is extremely large. The build script checks GitHub regular-file size limits before generated changes can be committed.
- For very large initial uploads, use Git/GitHub Desktop instead of the GitHub browser uploader.

See [`docs/AUTOMATIC_UPDATES.md`](docs/AUTOMATIC_UPDATES.md) for the complete update and fail-safe behavior.

---

# 📂 Repository Structure

```text
BlackRabbitZ-DNS-Blocklists/
│
├── .github/
│   └── workflows/
│       ├── update-lists.yml
│       └── daily-upstream-update.yml
├── config/
│   └── allowlist.txt
├── docs/
│   └── AUTOMATIC_UPDATES.md
├── scripts/
│   ├── update-lists.sh
│   ├── update-upstreams.py
│   └── upstream-sources.json
├── README.md
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
    │   ├── security.txt
    │   ├── family.txt
    │   └── ultimate.txt
    │
    └── categories/
        ├── ads.txt
        ├── trackers.txt
        ├── telemetry.txt
        ├── social-trackers.txt
        ├── mobile-tracking.txt
        ├── native-tracking.txt
        ├── affiliate-tracking.txt
        ├── consent-cmp.txt
        ├── windows-telemetry.txt
        ├── apple-telemetry.txt
        ├── android-telemetry.txt
        ├── linux-telemetry.txt
        ├── nas-telemetry.txt
        ├── server-telemetry.txt
        ├── smart-tv.txt
        ├── iot.txt
        ├── cryptomining.txt
        ├── malware.txt
        ├── phishing.txt
        ├── scam.txt
        ├── fake-shops.txt
        ├── adult.txt
        └── gambling.txt
```

Every published blocklist remains a normal **static text file** and can be consumed directly by Pi-hole or compatible DNS filters.
Repository maintenance is automated with **Python, Bash and GitHub Actions**. End users still consume normal static text files and require no Python runtime.

---

# 🔄 Automatic List Updates

Two GitHub Actions keep the repository current:

1. **Daily upstream refresh** runs every day at `03:17 UTC`. It downloads the configured public feeds, normalizes their domains and **adds newly published entries** to the matching category files.
2. **Update blocklists** runs after manual category changes and keeps all generated files synchronized.

The automatic updater:

- downloads only explicitly configured HTTPS sources from `scripts/upstream-sources.json`
- supports plain-domain, hosts, URL, AdGuard/ABP and wildcard-style source formats
- rejects invalid domains, IP addresses and duplicates
- excludes critical domains listed in `config/allowlist.txt` from new automatic imports
- rejects suspiciously small upstream responses
- stops on implausibly large one-run growth instead of blindly committing it
- preserves the last working category when an upstream is unavailable
- updates the `# Entries:` count inside category files
- rebuilds all files under `lists/combined/` from their configured source categories
- removes duplicate domains from combined profiles
- updates all **Entries** values in this README
- commits generated changes back to `main` only after all checks pass

Automatic upstream imports are **additive**: the updater can extend the lists automatically, but it does not silently delete existing BlackRabbitZ entries. `linux-telemetry.txt`, `nas-telemetry.txt` and `server-telemetry.txt` remain manually curated because those vendor-specific endpoints do not have a single trustworthy general-purpose upstream feed.

The profile definitions in `scripts/update-lists.sh` remain the single source of truth for which categories are included in **Light**, **Balanced**, **Strict**, **Security**, **Family** and **Ultimate**. Full details are in [`docs/AUTOMATIC_UPDATES.md`](docs/AUTOMATIC_UPDATES.md).

---

# ➕ Extending the Lists

Adding more domains is intentionally simple.

Open the category you want to extend:

```text
lists/categories/ads.txt
```

Add one domain per line:

```text
ads.example.net
tracker.example.net
```

For a new category, create a new static file:

```text
lists/categories/gaming-telemetry.txt
```

After adding or removing domains, commit and push the category file. The GitHub Action recalculates the entry count and rebuilds every affected combined profile automatically.

To include a **new category** in a combined profile, add its category name to the appropriate `build_combined` definition in:

```text
scripts/update-lists.sh
```

For a completely new combined profile, add another `build_combined` definition and then add its View/Raw links to this README.

---

# ⚠️ False Positives

Blocking more domains does not automatically mean better protection.

If a list breaks a website, application or device, open an issue and include:

- affected domain
- affected list
- application/device
- what stops working
- reproduction steps

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

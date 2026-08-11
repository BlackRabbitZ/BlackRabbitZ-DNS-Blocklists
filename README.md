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
| 🟢 **Light** | Low | **128** | Basic ad blocking | [View](lists/combined/light.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/light.txt)** |
| 🔵 **Balanced ⭐** | Medium | **291** | Most users | [View](lists/combined/balanced.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/balanced.txt)** |
| 🟠 **Strict** | High | **433** | Privacy-focused setups | [View](lists/combined/strict.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/strict.txt)** |
| 🛡️ **Security** | Security | **58** | Security-focused filtering | [View](lists/combined/security.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security.txt)** |
| 👨‍👩‍👧 **Family** | Family | **307** | Family networks | [View](lists/combined/family.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family.txt)** |
| 🔴 **Ultimate** | Maximum | **538** | Aggressive filtering | [View](lists/combined/ultimate.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate.txt)** |

> **Balanced** is recommended for most installations.  
> **Strict** and **Ultimate** may block telemetry-dependent features, Smart-TV functionality, app analytics or other non-essential services.

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
| Breakage Risk | 🟢 Low | 🔵 Low–Medium | 🟠 Higher | 🟢 Low | 🟡 Medium | 🔴 Highest |

---

# 📢 Ads & Tracking

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 📣 **Ads** | 128 | Advertising and ad delivery endpoints | [View](lists/categories/ads.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/ads.txt) |
| 👁️ **Trackers** | 136 | Analytics and tracking infrastructure | [View](lists/categories/trackers.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/trackers.txt) |
| 👥 **Social Trackers** | 35 | Social-network tracking endpoints | [View](lists/categories/social-trackers.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/social-trackers.txt) |
| 📲 **Mobile Tracking** | 56 | Mobile attribution and analytics | [View](lists/categories/mobile-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/mobile-tracking.txt) |
| 🧩 **Native/App Tracking** | 22 | SDK and application telemetry/tracking | [View](lists/categories/native-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/native-tracking.txt) |
| 🔗 **Affiliate Tracking** | 18 | Affiliate and conversion tracking | [View](lists/categories/affiliate-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/affiliate-tracking.txt) |
| 🍪 **Consent / CMP** | 15 | Consent-management platforms | [View](lists/categories/consent-cmp.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/consent-cmp.txt) |

---

# 📡 Telemetry & Devices

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 📊 **General Telemetry** | 40 | Generic product/app telemetry | [View](lists/categories/telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/telemetry.txt) |
| 🪟 **Windows Telemetry** | 31 | Windows diagnostics and telemetry endpoints | [View](lists/categories/windows-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/windows-telemetry.txt) |
| 🍎 **Apple Telemetry** | 11 | Apple telemetry and diagnostics | [View](lists/categories/apple-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/apple-telemetry.txt) |
| 🤖 **Android Telemetry** | 15 | Android/Firebase telemetry | [View](lists/categories/android-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/android-telemetry.txt) |
| 🐧 **Linux Telemetry** | 3 | Linux distribution telemetry, diagnostics and usage reporting | [View](lists/categories/linux-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/linux-telemetry.txt) |
| 💾 **NAS Telemetry** | 6 | NAS telemetry and usage reporting (Synology, TrueNAS and others) | [View](lists/categories/nas-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/nas-telemetry.txt) |
| 🖥️ **Server Telemetry** | 4 | Server, hypervisor and server-management telemetry | [View](lists/categories/server-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/server-telemetry.txt) |
| 📺 **Smart TV** | 39 | Smart-TV advertising, ACR and telemetry | [View](lists/categories/smart-tv.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/smart-tv.txt) |
| 🏠 **IoT** | 15 | IoT telemetry endpoints | [View](lists/categories/iot.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/iot.txt) |

> Device-specific lists may disable recommendations, diagnostics, usage reporting, ACR, advertising or other cloud-backed features.

---

# 🛡️ Security Lists

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 🦠 **Malware** | 10 | Verified malicious infrastructure | [View](lists/categories/malware.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/malware.txt) |
| 🎣 **Phishing** | 10 | Verified phishing infrastructure | [View](lists/categories/phishing.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/phishing.txt) |
| 💰 **Scam** | 12 | BaFin-warned suspicious financial/trading platforms | [View](lists/categories/scam.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/scam.txt) |
| 🛒 **Fake Shops** | 10 | Consumer-warning fake-shop domains | [View](lists/categories/fake-shops.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/fake-shops.txt) |
| ⛏️ **Cryptomining** | 16 | Browser/remote mining infrastructure | [View](lists/categories/cryptomining.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/cryptomining.txt) |

> Live threat intelligence becomes stale quickly. Security categories are intentionally conservative instead of being inflated with unverified or copied feeds.

---

# 👨‍👩‍👧 Family Lists

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 🔞 **Adult** | 16 | Adult-content and pornography domains | [View](lists/categories/adult.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/adult.txt) |
| 🎰 **Gambling** | 16 | Betting, casino and gambling domains | [View](lists/categories/gambling.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gambling.txt) |

---

# 📂 Repository Structure

```text
BlackRabbitZ-DNS-Blocklists/
│
├── .github/
│   └── workflows/
│       └── update-lists.yml
├── scripts/
│   └── update-lists.sh
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
Repository maintenance is automated with **Bash + GitHub Actions**; no Python or runtime dependency is required by users.

---

# 🔄 Automatic List Updates

The repository automatically keeps generated data in sync. When a category file under `lists/categories/` changes on the `main` branch, the `Update blocklists` GitHub Action runs `scripts/update-lists.sh`.

It automatically:

- updates the `# Entries:` count inside category files
- rebuilds all files under `lists/combined/` from their configured source categories
- removes duplicate domains from combined profiles
- updates all **Entries** values in this README
- commits the generated changes back to `main` when something changed

The profile definitions in `scripts/update-lists.sh` are the single source of truth for which categories are included in **Light**, **Balanced**, **Strict**, **Security**, **Family** and **Ultimate**.

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

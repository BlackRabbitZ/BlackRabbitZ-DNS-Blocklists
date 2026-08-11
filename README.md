<div align="center">

# 🐇 BlackRabbitZ DNS Blocklists

### Privacy • Security • Ads • Trackers • Telemetry

[![License: GPL-3.0-only](https://img.shields.io/badge/License-GPL--3.0--only-blue.svg)](LICENSE)
[![Pi-hole](https://img.shields.io/badge/Pi--hole-compatible-96060C?logo=pi-hole&logoColor=white)](https://pi-hole.net/)
[![Lists](https://img.shields.io/badge/Lists-23-2ea44f)](#-available-lists)
[![Maintained by BlackRabbitZ](https://img.shields.io/badge/Maintainer-BlackRabbitZ-black)](https://github.com/BlackRabbitZ)

**Clean, transparent DNS blocklists for Pi-hole and other DNS filtering systems.**  
Choose a ready-made protection profile or combine individual category lists yourself.

</div>

---

## ⚡ Quick Start

### Recommended for most users: **Balanced** 🟦

**Pi-hole URL:**

```text
https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/balanced.txt
```

1. Open **Pi-hole**.
2. Go to your **Lists / Adlists** management.
3. Add the URL above.
4. Update Gravity.
5. Done.

> **Private repository?** The `View` links below work for authorized GitHub users. Public `raw.githubusercontent.com` URLs are intended for use once the repository is public.

---

# 🚀 Recommended Protection Profiles

| Profile | Level | Best for | Entries | View | Pi-hole Raw |
|---|:---:|---|---:|:---:|:---:|
| **Light** | 🟢 | Very conservative ad blocking | 12 | [View](lists/combined/light.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/light.txt)** |
| **Balanced** ⭐ | 🟦 | Ads + common tracking | 23 | [View](lists/combined/balanced.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/balanced.txt)** |
| **Strict** | 🟧 | Privacy + telemetry blocking | 28 | [View](lists/combined/strict.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/strict.txt)** |
| **Security** | 🛡️ | Malware, phishing, scams | 0* | [View](lists/combined/security.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security.txt)** |
| **Family** | 👨‍👩‍👧 | Balanced + family categories | 23 | [View](lists/combined/family.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family.txt)** |
| **Ultimate** | 🔴 | Maximum enabled protection | 28 | [View](lists/combined/ultimate.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate.txt)** |

\* Specialist feeds start conservatively and grow only with curated entries.

### Which profile should I use?

| Feature | Light | Balanced ⭐ | Strict | Security | Family | Ultimate |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Advertising | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| General trackers | — | ✅ | ✅ | — | ✅ | ✅ |
| General telemetry | — | — | ✅ | — | — | ✅ |
| Device / platform telemetry | — | — | ✅ | — | — | ✅ |
| Malware / phishing / scams | — | — | — | ✅ | — | ✅ |
| Adult / gambling | — | — | — | — | ✅ | ✅ |
| Breakage risk | 🟢 Low | 🟦 Low | 🟧 Medium | 🟢 Low | 🟨 Medium | 🔴 Highest |

> Start with **Balanced**. Move to **Strict** if you want stronger privacy filtering. Use **Ultimate** only if you are comfortable troubleshooting occasional false positives.

---

# 📚 Available Lists

## 📢 Ads & Tracking

| List | Description | Entries | View | Raw |
|---|---|---:|:---:|:---:|
| 📣 **Advertising** | Advertising and ad-delivery endpoints | 12 | [View](lists/categories/ads.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/ads.txt)** |
| 👁️ **Trackers** | Analytics and tracking endpoints | 11 | [View](lists/categories/trackers.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/trackers.txt)** |
| 👥 **Social Trackers** | Social-media tracking and measurement | 2 | [View](lists/categories/social-trackers.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/social-trackers.txt)** |
| 📱 **Mobile Tracking** | Mobile application tracking endpoints | 1 | [View](lists/categories/mobile-tracking.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/mobile-tracking.txt)** |

## 📡 Telemetry & Devices

| List | Description | Entries | View | Raw |
|---|---|---:|:---:|:---:|
| 📊 **General Telemetry** | Non-essential telemetry endpoints | 5 | [View](lists/categories/telemetry.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/telemetry.txt)** |
| 🪟 **Windows Telemetry** | Windows telemetry endpoints | 3 | [View](lists/categories/windows-telemetry.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/windows-telemetry.txt)** |
| 🍎 **Apple Telemetry** | Apple platform telemetry endpoints | 1 | [View](lists/categories/apple-telemetry.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/apple-telemetry.txt)** |
| 🤖 **Android Telemetry** | Android platform telemetry endpoints | 0 | [View](lists/categories/android-telemetry.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/android-telemetry.txt)** |
| 📺 **Smart TV** | Smart-TV telemetry and tracking | 0 | [View](lists/categories/smart-tv.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/smart-tv.txt)** |
| 🏠 **IoT Devices** | IoT telemetry and tracking | 0 | [View](lists/categories/iot.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/iot.txt)** |

## 🛡️ Security

| List | Description | Entries | View | Raw |
|---|---|---:|:---:|:---:|
| 🎣 **Phishing** | Credential theft and phishing infrastructure | 0 | [View](lists/categories/phishing.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/phishing.txt)** |
| 🦠 **Malware** | Known malicious delivery / command infrastructure | 0 | [View](lists/categories/malware.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/malware.txt)** |
| 💸 **Scam / Fraud** | Scam and fraudulent domains | 0 | [View](lists/categories/scam.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/scam.txt)** |
| ⛏️ **Cryptomining** | Mining and cryptojacking endpoints | 0 | [View](lists/categories/cryptomining.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/cryptomining.txt)** |
| 🛒 **Fake Shops** | Fraudulent shopping domains | 0 | [View](lists/categories/fake-shops.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/fake-shops.txt)** |

## 👨‍👩‍👧 Family Filters

| List | Description | Entries | View | Raw |
|---|---|---:|:---:|:---:|
| 🔞 **Adult** | Adult-content domains | 0 | [View](lists/categories/adult.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/adult.txt)** |
| 🎰 **Gambling** | Gambling and betting domains | 0 | [View](lists/categories/gambling.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gambling.txt)** |

---

# 🧱 Repository Structure

```text
BlackRabbitZ-DNS-Blocklists/
│
├── lists/
│   ├── combined/
│   │   ├── light.txt
│   │   ├── balanced.txt
│   │   ├── strict.txt
│   │   ├── security.txt
│   │   ├── family.txt
│   │   └── ultimate.txt
│   │
│   └── categories/
│       ├── ads.txt
│       ├── trackers.txt
│       ├── telemetry.txt
│       ├── windows-telemetry.txt
│       ├── apple-telemetry.txt
│       ├── android-telemetry.txt
│       ├── smart-tv.txt
│       ├── iot.txt
│       ├── mobile-tracking.txt
│       ├── social-trackers.txt
│       ├── phishing.txt
│       ├── malware.txt
│       ├── scam.txt
│       ├── cryptomining.txt
│       ├── fake-shops.txt
│       ├── adult.txt
│       └── gambling.txt
│
├── README.md
├── LICENSE
├── NOTICE
├── ATTRIBUTION.md
└── CONTRIBUTING.md
```

There is **no installer, no Python dependency and no runtime code**. The repository contains plain-text DNS lists and documentation only.

---

# ➕ Extending the Lists

The repository is intentionally easy to expand.

### Add a new category

Create another text file under:

```text
lists/categories/
```

Example:

```text
lists/categories/gaming-telemetry.txt
```

Then add a matching `View` and `Raw` link to this README.

### Extend a combined profile

Edit the appropriate file directly under:

```text
lists/combined/
```

For example:

```text
lists/combined/strict.txt
```

Each entry should be one domain per line.

---

# ⚠️ False Positives

DNS blocking can occasionally break login systems, videos, apps, smart devices or other functionality.

If a domain causes unexpected breakage:

1. Temporarily allow the domain in Pi-hole.
2. Confirm that the domain is responsible.
3. Open a GitHub issue with the domain and affected service.

A smaller, reliable list is more useful than a huge list with unnecessary breakage.

---

# 🤝 Contributions

Contributions are welcome for:

- new independently verified domains,
- false positives,
- new categories,
- documentation improvements.

Please include enough context to explain why a domain belongs in a specific category.

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

# ⚖️ License & Attribution

This repository's original documentation and curated list collection are licensed under **GPL-3.0-only**.

**Copyright © 2026 BlackRabbitZ**

Original repository:

```text
https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists
```

See:

- [LICENSE](LICENSE)
- [NOTICE](NOTICE)
- [ATTRIBUTION.md](ATTRIBUTION.md)
- [THIRD_PARTY.md](THIRD_PARTY.md)

---

<div align="center">

### 🐇 BlackRabbitZ DNS Blocklists

**Privacy • Security • Control**

</div>

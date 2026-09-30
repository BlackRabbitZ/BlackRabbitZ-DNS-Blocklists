<div align="center">

# 🐇 BlackRabbitZ DNS Blocklists

### Privacy • Security • Ads • Trackers • Telemetry

[![License: GPL-3.0-only](https://img.shields.io/badge/License-GPL--3.0--only-blue.svg)](LICENSE)
![Pi-hole compatible](https://img.shields.io/badge/Pi--hole-Compatible-brightgreen)
![Static Lists](https://img.shields.io/badge/Lists-Static-success)
![Maintainer](https://img.shields.io/badge/Maintainer-BlackRabbitZ-black)
![End users](https://img.shields.io/badge/End%20users-No%20Python-success)
[![Validate blocklists](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/actions/workflows/update-lists.yml/badge.svg)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/actions/workflows/update-lists.yml)

**Static, transparent DNS blocklists for Pi-hole and compatible DNS filtering solutions.**

</div>

<div align="center">

**🌐 Language / Sprache:** [🇩🇪 Deutsch](README.md) · 🇬🇧 **English**

</div>

---

<a id="why-dns-blocklists"></a>
## 🛡️ Why DNS blocklists?

DNS blocklists stop unwanted connections during name resolution. This allows **ads, trackers, telemetry and known malicious domains to be filtered centrally for the entire network** without installing additional software on every device.

This corrected repository version deliberately separates **manually curated domains**, **automatically retrieved upstream data**, and **uncertain candidates**. External feeds are no longer appended forever to the public lists. Every feed has its own cache; successful refreshes replace that cache, while failed refreshes retain the last known-good state.

---

<a id="contents"></a>
## 📑 Table of contents

- [Why DNS blocklists?](#why-dns-blocklists)
- [Quick start](#quick-start)
- [Privacy profiles](#protection-profiles)
- [Protection comparison](#protection-comparison)
- [Optional protection modules](#optional-protection-modules)
- [Ultimate parts](#ultimate-parts)
- [Ads & tracking](#ads-tracking)
- [Telemetry & devices](#telemetry-devices)
- [Security lists](#security-lists)
- [Family lists](#family-lists)
- [Recommendations](#recommendations)
- [Online DNS services](#online-dns-services)
- [Upstream sources & build transparency](#upstream-sources)
- [Repository structure](#repository-structure)
- [Automatic list updates](#automatic-updates)
- [Extending the lists](#extending-lists)
- [False positives](#false-positives)
- [License & attribution](#license-attribution)

---

<a id="quick-start"></a>
## ⚡ Quick start

### ⭐ Recommended: Balanced

For most users, **Balanced** is the best starting point. It combines ad blocking with general tracker protection without forcing device- and operating-system-specific telemetry lists into the default setup.

```text
https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/balanced.txt
```

**Pi-hole**

1. Open the Pi-hole web interface.
2. Go to **Lists / Adlists**.
3. Add the Raw URL above.
4. Save.
5. Update Gravity.

> Test new or aggressive lists in a separate Pi-hole group first.

---

<a id="protection-profiles"></a>
# 🚀 Protection profiles

The combined profiles are designed for different use cases. **Blocking more does not automatically mean better protection** – device, telemetry and cloud endpoints may have functional dependencies.

| Profile | Protection | Entries | Recommended for | View | Raw |
|---|:---:|---:|---|:---:|:---:|
| 🟢 **Light** | Low | **234036** | Basic ad blocking | [View](lists/combined/light.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/light.txt)** |
| 🔵 **Balanced ⭐** | Medium | **342195** | Most users | [View](lists/combined/balanced.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/balanced.txt)** |
| 🟠 **Strict** | High | **371736** | Privacy-focused setups | [View](lists/combined/strict.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/strict.txt)** |
| 🛡️ **Security** | Security | **3408844** | Security-focused filtering | [View](lists/combined/security.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security.txt)** |
| 👨‍👩‍👧 **Family** | Family | **1758872** | Family networks | [View](lists/combined/family.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family.txt)** |
| 🔴 **Ultimate** | Maximum | **5,119,302** | Aggressive filtering | [Show parts](#ultimate-parts) | **[Raw parts](#ultimate-parts)** |

> **Balanced** is recommended for most installations. **Strict** adds general and device-specific telemetry plus native/app tracking. **Security** and **Family** are focused add-on profiles. **Ultimate** is intentionally aggressive and should not be deployed to critical networks without testing.

---

<a id="protection-comparison"></a>
# 🎚️ Protection comparison

| Feature | Light | Balanced ⭐ | Strict | Security | Family | Ultimate |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Advertising | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| General trackers | — | ✅ | ✅ | — | ✅ | ✅ |
| Social tracking | — | ✅ | ✅ | — | ✅ | ✅ |
| Affiliate tracking | — | — | ✅ | — | — | ✅ |
| General telemetry | — | — | ✅ | — | — | ✅ |
| Windows telemetry | — | — | ✅ | — | — | ✅ |
| Apple telemetry | — | — | ✅ | — | — | ✅ |
| Android telemetry | — | — | ✅ | — | — | ✅ |
| Linux/NAS/server telemetry | — | — | ✅ | — | — | ✅ |
| Mobile/app tracking | — | — | ✅ | — | — | ✅ |
| Smart TV / IoT | — | — | ✅ | — | — | ✅ |
| Cryptomining | — | — | — | ✅ | — | ✅ |
| Malware / phishing / scam / fake shops | — | — | — | ✅ | — | ✅ |
| Adult content | — | — | — | — | ✅ | ✅ |
| Gambling | — | — | — | — | ✅ | ✅ |
| Breakage risk | 🟢 Low | 🔵 Low–Medium | 🟠 Higher | 🟡 Medium | 🟠 Higher | 🔴 Very high |

<a id="optional-protection-modules"></a>
## 🧩 Optional protection modules

**Security** and **Family** are not simply stronger versions of Balanced or Strict; they are focused add-on profiles:

- **Security** combines malware, phishing, scam, fake-shop and cryptomining protection.
- **Family** adds adult-content and gambling filters to ad/tracker protection.
- **Consent/CMP** remains a separate category because DNS-level blocking of consent infrastructure can break websites.

---

<a id="ultimate-parts"></a>
## 📦 Ultimate parts

Ultimate is large and is therefore split automatically into multiple files. Add **every part** for complete Ultimate coverage.

<!-- ULTIMATE_PARTS_START -->
| Part | Entries | Size | View | Raw |
|---:|---:|---:|:---:|:---:|
| **1** | **2,090,381** | 40.0 MiB | [View](lists/combined/ultimate-1.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-1.txt)** |
| **2** | **2,125,750** | 40.0 MiB | [View](lists/combined/ultimate-2.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-2.txt)** |
| **3** | **903,171** | 17.9 MiB | [View](lists/combined/ultimate-3.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-3.txt)** |
<!-- ULTIMATE_PARTS_END -->

---

<a id="ads-tracking"></a>
# 📢 Ads & tracking

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 📣 **Ads** | 234036 | Advertising, ad-delivery and ad infrastructure | [View](lists/categories/ads.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/ads.txt) |
| 👁️ **Trackers** | 113609 | General analytics and tracking infrastructure | [View](lists/categories/trackers.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/trackers.txt) |
| 👥 **Social trackers** | 99 | Social-network tracking and analytics endpoints | [View](lists/categories/social-trackers.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/social-trackers.txt) |
| 📲 **Mobile tracking** | 201 | Mobile attribution, SDK analytics and app tracking | [View](lists/categories/mobile-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/mobile-tracking.txt) |
| 🧩 **Native/app tracking** | 628 | Operating-system, device and application tracking | [View](lists/categories/native-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/native-tracking.txt) |
| 🔗 **Affiliate tracking** | 643 | Affiliate, click, referral and conversion tracking | [View](lists/categories/affiliate-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/affiliate-tracking.txt) |
| 🍪 **Consent / CMP** | 44 | Consent-management/CMP infrastructure; higher breakage risk | [View](lists/categories/consent-cmp.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/consent-cmp.txt) |

> **Consent/CMP is intentionally not included in the normal privacy profiles.** These domains can be directly involved in page loading and consent-state handling.

---

<a id="telemetry-devices"></a>
# 📡 Telemetry & devices

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 📊 **General telemetry** | 29169 | Product/app analytics, diagnostics and telemetry | [View](lists/categories/telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/telemetry.txt) |
| 🪟 **Windows telemetry** | 51 | Windows/Microsoft diagnostics and telemetry | [View](lists/categories/windows-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/windows-telemetry.txt) |
| 🍎 **Apple telemetry** | 119 | Apple metrics, diagnostics and telemetry | [View](lists/categories/apple-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/apple-telemetry.txt) |
| 🤖 **Android telemetry** | 135 | Android/vendor telemetry and native tracking | [View](lists/categories/android-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/android-telemetry.txt) |
| 🐧 **Linux telemetry** | 3 | Linux telemetry and usage reporting | [View](lists/categories/linux-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/linux-telemetry.txt) |
| 💾 **NAS telemetry** | 12 | NAS telemetry and usage reporting | [View](lists/categories/nas-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/nas-telemetry.txt) |
| 🖥️ **Server telemetry** | 10 | Server and management telemetry | [View](lists/categories/server-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/server-telemetry.txt) |
| 📺 **Smart TV** | 556 | Smart-TV advertising, ACR, diagnostics and telemetry | [View](lists/categories/smart-tv.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/smart-tv.txt) |
| 🏠 **IoT** | 85 | IoT and connected-device telemetry/tracking | [View](lists/categories/iot.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/iot.txt) |

> Device-specific lists can interfere with recommendations, diagnostics, usage reporting, ACR, ads or other cloud features. The corrected upstream pipeline therefore protects known update, login, push, certificate and firmware endpoints from automatic privacy/device imports.

---

<a id="security-lists"></a>
# 🛡️ Security lists

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 🦠 **Malware** | 2656445 | Malware, ransomware and active malware hosts | [View](lists/categories/malware.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/malware.txt) |
| 🎣 **Phishing** | 577783 | Active and curated phishing domains | [View](lists/categories/phishing.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/phishing.txt) |
| 💰 **Scam / fraud** | 265330 | Scam, fraud and deceptive-platform domains | [View](lists/categories/scam.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/scam.txt) |
| 🛒 **Fake shops** | 10964 | Potential fake shops and deceptive stores | [View](lists/categories/fake-shops.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/fake-shops.txt) |
| ⛏️ **Cryptomining** | 6121 | Browser/remote mining infrastructure | [View](lists/categories/cryptomining.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/cryptomining.txt) |

> Security lists use different classification rules than privacy/device lists. Functional-looking tokens such as `login` or `update` do not automatically allow a security indicator because malicious domains can contain those words too.

---

<a id="family-lists"></a>
# 👨‍👩‍👧 Family lists

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 🔞 **Adult / NSFW** | 999120 | Adult-content and pornography domains | [View](lists/categories/adult.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/adult.txt) |
| 🎰 **Gambling** | 420536 | Betting, casino and gambling domains | [View](lists/categories/gambling.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gambling.txt) |

---

<a id="recommendations"></a>
# ✅ Recommendations

| Goal | Recommendation |
|---|---|
| Basic ad blocking | **Light** |
| Everyday/home network | **Balanced** |
| More privacy | **Strict** – test first |
| Malware/phishing protection | **Balanced + Security** |
| Family network | **Balanced + Family** |
| Maximum filtering | **Ultimate** – only after testing and with your own allowlist |

**Recommended approach:** start with Balanced, observe the query log, then add only the categories you actually need. This reduces breakage compared with enabling everything at once.

---

<a id="online-dns-services"></a>
# 🌍 Online DNS services and mobile use

The files in this repository are normal domain lists primarily intended for **Pi-hole** and comparable self-managed DNS filters. Many hosted DNS providers either do not support custom lists or apply their own format and size limits.

For mobile devices outside your home network, consider a VPN/DNS tunnel back to your own Pi-hole or a service that supports custom blocklists. Pi-hole regex rules and local group assignments are not automatically portable to external DNS services.

---

<a id="upstream-sources"></a>
# 🌐 Upstream sources & build transparency

The corrected repository deliberately separates the data flow into multiple layers:

```text
Manually curated domains
sources/manual/
        │
        ├──────────────┐
        │              │
External feeds         │
sources/upstream/      │
one cache per feed     │
        │              │
        └──────┬───────┘
               ▼
      scripts/build-categories.py
               │
               ▼
      lists/categories/
               │
               ▼
      scripts/update-lists.sh
               │
               ▼
      lists/combined/
```

### What changed from the old additive importer

- **No endless additive accumulation:** a successful feed refresh replaces only that feed's cache.
- **Last known-good state on outages:** a temporary upstream failure cannot empty a category.
- **Manual data stays separate:** `sources/manual/` is independent from automated upstream data.
- **Critical-service protection:** `config/critical-services.txt` protects known update, authentication, push, certificate and firmware infrastructure in privacy/device categories.
- **Quarantine:** functional-looking or uncertain candidates can be written to `review/quarantine/` instead of being published automatically.
- **Allowlist:** `config/allowlist.txt` is an explicit exclusion for published lists.
- **NXDOMAIN checks:** newly cached domains can be checked in batches for confirmed NXDOMAIN before publication.
- **Plausibility guards:** unexpectedly small, large or rapidly changing feeds are not accepted blindly.
- **Review instead of direct push:** the daily upstream refresh creates or updates a Pull Request.

Source and license information is documented in [`THIRD_PARTY.md`](THIRD_PARTY.md), attribution in [`ATTRIBUTION.md`](ATTRIBUTION.md). Workflow details are in [`docs/AUTOMATIC_UPDATES.md`](docs/AUTOMATIC_UPDATES.md) and [`MIGRATION_WORKFLOW_FIX.md`](MIGRATION_WORKFLOW_FIX.md).

---

<a id="repository-structure"></a>
# 📂 Repository structure

```text
BlackRabbitZ-DNS-Blocklists/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── false-positive.yml
│   └── workflows/
│       ├── update-lists.yml
│       └── daily-upstream-update.yml
├── config/
│   ├── allowlist.txt
│   ├── critical-services.txt
│   └── functional-guard-tokens.txt
├── docs/
│   └── AUTOMATIC_UPDATES.md
├── metadata/
│   └── cleanup-report.json
├── review/
│   └── quarantine/
├── scripts/
│   ├── automation/new_domain_check.py
│   ├── build-categories.py
│   ├── reclassify-existing.py
│   ├── update-upstreams.py
│   ├── upstream-sources.json
│   ├── validate-repository.py
│   ├── split-ultimate.py
│   ├── update-ultimate-readme.py
│   └── update-lists.sh
├── sources/
│   ├── manual/
│   └── upstream/
├── lists/
│   ├── categories/
│   └── combined/
├── README.md
├── README_EN.md
├── MIGRATION_WORKFLOW_FIX.md
├── LICENSE
├── NOTICE
├── ATTRIBUTION.md
└── THIRD_PARTY.md
```

All published blocklists remain normal static text files. Python/Bash/GitHub Actions are required only for repository maintenance, not for Pi-hole end users.

---

<a id="automatic-updates"></a>
# 🔄 Automatic list updates

The repository uses two separate workflows:

### 1. `daily-upstream-update.yml`

Runs on schedule at **03:17 UTC** or manually. It:

1. validates the upstream configuration,
2. refreshes the individual feed caches,
3. performs an NXDOMAIN check on newly cached domains when practical,
4. rebuilds categories and combined profiles,
5. validates the repository,
6. creates or updates the `automation/upstream-refresh` branch,
7. opens or updates a **review Pull Request**.

Third-party changes therefore **no longer get pushed directly to `main` without review**.

### 2. `update-lists.yml`

This workflow has **read-only repository permission** and verifies integrity. It rebuilds all generated files locally and fails if committed generated files do not match their sources.

### Safety principle

```text
Upstream → cache → guard rules → build → validation → Pull Request → human review → merge
```

---

<a id="extending-lists"></a>
# ➕ Extending the lists

Manual domains are **no longer maintained directly in `lists/categories/`**. Those files are generated outputs.

For an existing category, edit for example:

```text
sources/manual/ads.txt
```

One domain per line:

```text
ads.example.net
tracker.example.net
```

Then rebuild and validate locally:

```bash
python3 ./scripts/build-categories.py
bash ./scripts/update-lists.sh
python3 ./scripts/validate-repository.py
```

### New upstream source

New external feeds are configured in `scripts/upstream-sources.json`. Add only sources whose purpose, format, license and breakage risk are understood.

### New category

1. Create `sources/manual/<category>.txt`.
2. Include the category in the build.
3. Add mapping in `upstream-sources.json` if automated feeds are desired.
4. Add the category to `scripts/update-lists.sh` if it belongs in a combined profile.
5. Add links to README/README_EN.
6. Run the validator.

---

<a id="false-positives"></a>
# ⚠️ False positives

Blocking more domains does not automatically mean better security or privacy.

If a list breaks a website, app or device, please include:

- affected domain,
- affected list/profile,
- application/device/operating system,
- what stops working,
- whether disabling the list restores the feature,
- reproducible steps.

Permanent explicit exclusions belong in `config/allowlist.txt`. Known functional infrastructure that should be specially protected during automatic privacy/device imports belongs in `config/critical-services.txt`.

The goal is a **useful and understandable blocklist**, not the largest possible number of domains.

---

<a id="license-attribution"></a>
# 📜 License & attribution

This repository is licensed under **GNU GPL v3 (`GPL-3.0-only`)**.

Copyright © 2026 BlackRabbitZ

Original repository:

```text
https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists
```

See also:

- [`LICENSE`](LICENSE)
- [`NOTICE`](NOTICE)
- [`ATTRIBUTION.md`](ATTRIBUTION.md)
- [`THIRD_PARTY.md`](THIRD_PARTY.md)
- [`SECURITY.md`](SECURITY.md)
- [`CONTRIBUTING.md`](CONTRIBUTING.md)

---

<div align="center">

### 🐇 BlackRabbitZ DNS Blocklists

**Privacy. Security. Control.**

⭐ If this project is useful to you, consider starring the repository.

</div>

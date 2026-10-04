<p align="right">

<a href="README.md">🇩🇪 Deutsch</a> · 🇬🇧 <strong>English</strong>

</p>

<a id="top"></a>

<div align="center">

# 🐇 BlackRabbitZ DNS Blocklists

### Privacy • Device Isolation • App Blocking • Security • Family • Network Control

[![Pi-hole](https://img.shields.io/badge/Pi--hole-Compatible-96060C?logo=pihole&logoColor=white)](https://pi-hole.net/)
[![AdGuard Home](https://img.shields.io/badge/AdGuard%20Home-Compatible-67B279?logo=adguard&logoColor=white)](https://github.com/AdguardTeam/AdGuardHome)
[![Unbound](https://img.shields.io/badge/Unbound-Compatible-5B6770)](https://nlnetlabs.nl/projects/unbound/about/)
![Format](https://img.shields.io/badge/Format-Plain%20Domains-2EA44F)
![Profiles](https://img.shields.io/badge/Profile-Light%20%7C%20Normal%20%7C%20Pro%20%7C%20Pro%2B%2B%20%7C%20Ultimate-3178C6)
![Catalog](https://img.shields.io/badge/Catalog-100%20Categories-0088CC)

[![Validate](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/actions/workflows/validate.yml/badge.svg)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/actions/workflows/validate.yml)
[![License](https://img.shields.io/github/license/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists?label=License)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/blob/main/LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists?label=Last%20commit)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/commits/main)
[![Issues](https://img.shields.io/github/issues/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/issues)
[![Repo Size](https://img.shields.io/github/repo-size/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists?label=Repo%20size)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists)
[![Stars](https://img.shields.io/github/stars/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists?style=flat&label=Stars)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/stargazers)

**Modular DNS blocklists with clearly separated protection levels for privacy, devices, apps, security, family and network control.**

</div>

---
<a id="projekt-navigation"></a>
## 📘 1. Table of Contents – Project & Usage

- [🚀 Quick Start](#schnellstart)
- [🧭 Which blocking mode do I need?](#wirkungsarten)
- [📊 Global main lists at a glance](#hauptlisten)
- [🎚️ Privacy protection levels](#schutzstufen)

---
<a id="kinderschutz-navigation"></a>
## 👨‍👩‍👧 Dedicated Table of Contents – Family & Child Protection

- [👨‍👩‍👧 Family & Content](#family)
- [🧒 Kids Allow-Only](#kids-allow-only)
- [📚 Kids allowlist files](#kids-dateien)
- [🛠️ Pi-hole v6 guide](#kids-anleitung)

---
<a id="blocklisten-navigation"></a>
## 🧱 2. Table of Contents – Blocklists

### [🛡️ General Privacy Lists](#privacy-group)
- [🕵️ Privacy & Tracking](#privacy)
- [🧩 Software & Hardware Telemetry](#software-hardware)
- [🤖 AI, Bots & Crawlers](#automation)

### [🔌 Devices & Vendors — Privacy / Restrict / Isolate](#devices-group)
- [📺 Smart TV](#smart-tv)
- [📱 Smartphones & Mobile](#mobile)
- [💻 Operating Systems](#betriebssysteme)
- [🏠 IoT & Smart Home](#iot)
- [🎙️ Voice Assistants](#voice)
- [🚗 Automotive / Connected Cars](#automotive)
- [💾 NAS & Server](#nas-server)
- [🌐 Routers & Network Devices](#network-devices)
- [📡 ISP / Providers](#providers)
- [🏢 Google, Microsoft, Apple & Amazon](#ecosystems)
- [🏭 Vendor Lists](#manufacturers)

### [📱 Apps & Services — Privacy / Block All](#apps-group)
- [📺 Streaming](#streaming)
- [🎮 Gaming](#gaming)
- [💬 Social Media](#social-media)
- [☁️ Cloud, Server & Development](#cloud-dev)

### [🛡️ Full Protection / Control Lists](#protection-group)
- [👨‍👩‍👧 Family & Content](#family)
- [🛡️ Security & Threat Intelligence](#security)
- [🔐 DNS, Network & Bypass Control](#network)
- [🧰 Special Lists](#speziallisten)
- [🌍 Regional Lists](#regional)

### 📚 Project & Documentation
- [🧩 List model](#listenmodell)
- [🗺️ 100-category catalog](#katalog100)
- [📂 Repository structure](#repo-struktur)
- [✅ Quality assurance](#qualitaet)
- [⚠️ Notes & technical limitations](#grenzen)
- [📜 Sources & license](#lizenz)

---
# 📘 Part 1 – Project & Usage


<a id="wirkungsarten"></a>
## 🧭 Which blocking mode do I need?

> **Compatibility:** All existing repository paths and RAW URLs remain unchanged. The new `device-control` and `service-blocking` lists are added **in addition**; existing lists were not moved or reordered.

| What do you want to achieve? | Use this list |
|---|---|
| Reduce ads, trackers, analytics, telemetry and fingerprinting | 🛡️ **Privacy** |
| Keep using the device normally while reducing vendor tracking | 🔌 Vendor/device → **Privacy** |
| Also restrict optional vendor/cloud functionality | ⚠️ Vendor/device → **Restrict** |
| Disconnect the device from the vendor as completely as possible | 🚫 Vendor/device → **Isolate** |
| Keep using an app/service while reducing tracking | 📱 App/service → **Privacy** |
| Completely block an app/web service | 🚫 App/service → **Block All** |
| Block malware/phishing/ransomware/scam | 🛡️ **Security** |
| Block NSFW/gambling/drugs/violence/weapons, etc. | 👨‍👩‍👧 **Family** |
| Block DoH/VPN/proxy/bypass endpoints | 🔐 **Network Control** |

### 🔌 Devices & Vendors

Each supported device or vendor gets:

```text
privacy.txt
restrict.txt
isolate.txt
updates.txt
```

**Privacy** = privacy/tracking endpoints only.  
**Restrict** = additionally blocks optional vendor, cloud, marketing and recommendation services.  
**Isolate** = blocks as much known vendor communication as possible, including account, store, cloud, APIs and updates.  
**Updates** = update infrastructure can be controlled separately.

### 📱 Apps & Services

Each supported service gets:

```text
privacy.txt
block-all.txt
```

**Privacy** = reduce tracking/analytics/telemetry.  
**Block All** = block functional service hosts so the service no longer works.

### 🛡️ Security and 👨‍👩‍👧 Family

Here, an entry generally means:

> **The listed domain should not be reachable.**

---

<a id="schnellstart"></a>
## 🚀 Quick Start

For the entire network, choose **exactly one** global main list:

```text
profiles/light.txt
profiles/normal.txt
profiles/pro.txt
profiles/pro-plus.txt
profiles/ultimate.txt
```

The levels are cumulative. There is **no part/MiB splitting** – each logical profile is exactly **one file and one URL**.

---
<a id="hauptlisten"></a>
## 📊 Global Main Lists at a Glance

| Profile | Entries | Blocking | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 234,013 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/light.txt) |
| 🟦 **Normal** | 342,238 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/normal.txt) |
| 🟨 **Pro** | 370,387 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/pro.txt) |
| 🟧 **Pro++** | 382,467 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/pro-plus.txt) |
| 🟥 **Ultimate** | 5,118,112 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/ultimate.txt) |


The five profiles build on each other. For normal use, choose **exactly one** level.

> **What is included in the global main lists?** `Ultimate` contains the union of all area-specific `Ultimate` main lists in the repository. The smaller global levels (`Light`, `Normal`, `Pro`, `Pro++`) are deliberately curated, cumulative subsets and **not** simply a 1:1 union of all same-named area lists.

---
<a id="schutzstufen"></a>
## 🎚️ Privacy Protection Levels from Light to Ultimate

| Profile | Typical Content | Risk |
|---|---|:---:|
| 🟩 **Light** | Ads + especially safe trackers | Minimal |
| 🟦 **Normal** | Light + Tracking/Analytics | Low |
| 🟨 **Pro** | Normal + telemetry, diagnostics, native/device tracking | Low–Medium |
| 🟧 **Pro++** | Pro + aggressiveere Vendor-/Cloud-Endpunkte + Security-Basis | Medium |
| 🟥 **Ultimate** | maximum privacy/tracking dataset; no intentional Block All/Isolate behavior | High |

Depending on the area, `Ultimate` may affect cloud functionality, logins, stores, updates or other online features.

---
<a id="listenmodell"></a>
## 🧩 Main Lists & Full Lists

Every major area follows the same model:

```text
Light ⊂ Normal ⊂ Pro ⊂ Pro++ ⊂ Ultimate
```

The **main lists** aggregate entire areas.

For individual targets, the intended behavior is made explicit by the filename:

| Area | Files |
|---|---|
| Devices / vendors | `privacy.txt` · `restrict.txt` · `isolate.txt` · `updates.txt` |
| Apps / services | `privacy.txt` · `block-all.txt` |
| Security | full protection lists |
| Family | full content-blocking lists |
| Network Control | full policy/bypass-blocking lists |

**Status:** ✅ = contains entries. 🟡 = the path/category is fully prepared, but the current static source snapshot lacks reliable domain entries. In file headers, `Data method` indicates whether a list was taken directly from a source, generated as a tier, or conservatively reclassified from existing domains.

---
<a id="katalog100"></a>
## 🗺️ 100-Category Catalog

All **100 categories** from the BRZ Pi-hole DNS lists & child-protection handbook are mapped to concrete repository paths in [`docs/CATALOG_100.md`](docs/CATALOG_100.md). This also keeps it visible which special classes are already populated and which are only prepared.

---
<a id="repo-struktur"></a>
## 📂 Repository Structure – Final Layout

### Smartphones & Mobile

<details>
<summary><strong>📂 Show Smartphones & Mobile</strong></summary>


```text
lists/device-control/mobile/
├── apple-ios/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── google-android/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── google-pixel/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── huawei/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── motorola/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── oneplus/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── oppo-realme/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── samsung/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── shared-other/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── vivo/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── xiaomi/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
```

</details>

### Smart TV

<details>
<summary><strong>📂 Show Smart TV</strong></summary>


```text
lists/device-control/smart-tv/
├── amazon-fire-tv/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── google-android-tv/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── google-tv/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── hisense-vidaa/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── lg-webos/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── panasonic/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── philips/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── roku/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── samsung/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── shared-other/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── sony-bravia/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── tcl/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
```

</details>

### Operating Systems

<details>
<summary><strong>📂 Show Operating Systems</strong></summary>


```text
lists/device-control/operating-systems/
├── android/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── apple/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── chromeos/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── ios/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── linux/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── macos/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
├── windows/
│   ├── privacy.txt
│   ├── restrict.txt
│   ├── isolate.txt
│   └── updates.txt
```

</details>

### Social Media

<details>
<summary><strong>📂 Show Social Media</strong></summary>


```text
lists/service-blocking/social-media/
├── discord/
│   ├── privacy.txt
│   └── block-all.txt
├── facebook-meta/
│   ├── privacy.txt
│   └── block-all.txt
├── instagram/
│   ├── privacy.txt
│   └── block-all.txt
├── linkedin/
│   ├── privacy.txt
│   └── block-all.txt
├── pinterest/
│   ├── privacy.txt
│   └── block-all.txt
├── reddit/
│   ├── privacy.txt
│   └── block-all.txt
├── snapchat/
│   ├── privacy.txt
│   └── block-all.txt
├── telegram/
│   ├── privacy.txt
│   └── block-all.txt
├── threads/
│   ├── privacy.txt
│   └── block-all.txt
├── tiktok/
│   ├── privacy.txt
│   └── block-all.txt
├── whatsapp/
│   ├── privacy.txt
│   └── block-all.txt
├── x-twitter/
│   ├── privacy.txt
│   └── block-all.txt
```

</details>

### Streaming

<details>
<summary><strong>📂 Show Streaming</strong></summary>


```text
lists/service-blocking/streaming/
├── apple-tv/
│   ├── privacy.txt
│   └── block-all.txt
├── dazn/
│   ├── privacy.txt
│   └── block-all.txt
├── disney-plus/
│   ├── privacy.txt
│   └── block-all.txt
├── emby/
│   ├── privacy.txt
│   └── block-all.txt
├── jellyfin/
│   ├── privacy.txt
│   └── block-all.txt
├── netflix/
│   ├── privacy.txt
│   └── block-all.txt
├── paramount/
│   ├── privacy.txt
│   └── block-all.txt
├── plex/
│   ├── privacy.txt
│   └── block-all.txt
├── prime-video/
│   ├── privacy.txt
│   └── block-all.txt
├── spotify/
│   ├── privacy.txt
│   └── block-all.txt
├── twitch/
│   ├── privacy.txt
│   └── block-all.txt
├── youtube/
│   ├── privacy.txt
│   └── block-all.txt
```

</details>

### Gaming

<details>
<summary><strong>📂 Show Gaming</strong></summary>


```text
lists/service-blocking/gaming/
├── battle-net/
│   ├── privacy.txt
│   └── block-all.txt
├── ea-origin/
│   ├── privacy.txt
│   └── block-all.txt
├── epic-games/
│   ├── privacy.txt
│   └── block-all.txt
├── mobile-games/
│   ├── privacy.txt
│   └── block-all.txt
├── nintendo/
│   ├── privacy.txt
│   └── block-all.txt
├── playstation/
│   ├── privacy.txt
│   └── block-all.txt
├── riot-games/
│   ├── privacy.txt
│   └── block-all.txt
├── rockstar/
│   ├── privacy.txt
│   └── block-all.txt
├── steam/
│   ├── privacy.txt
│   └── block-all.txt
├── ubisoft/
│   ├── privacy.txt
│   └── block-all.txt
├── xbox/
│   ├── privacy.txt
│   └── block-all.txt
```

</details>

### Security / Family / Network Control

<details>
<summary><strong>📂 Show Security / Family / Network Control</strong></summary>


```text
lists/security/
family/content/
lists/network/
```

These three areas remain full protection/blocking lists.

---

</details>
<a id="qualitaet"></a>
## ✅ Quality Assurance

- Plain-domain format, one domain per line
- sorted and deduplicated
- cumulative main profiles
- 100-category mapping
- SHA-256 checksums
- no part files
- no automatic third-party list synchronization
- transparent labeling of prepared and derived lists

```bash
python3 scripts/validate.py
```

---
<a id="grenzen"></a>
## ⚠️ Notes & Technical Limitations

DNS blocking filters domains, not individual URL paths. Missing source classes are not guessed: they remain visible as prepared lists until a reliable source is added. AI/crawler lists do not replace WAF/web-server/`robots.txt` rules. DNS rebinding protection lives under `policies/` because it is resolver/firewall configuration rather than a normal domain list.

---
# 🧱 Part 2 – List Catalog

> The order of this catalog now matches the blocklist table of contents **1:1**.

---
<a id="privacy-group"></a>
## 🛡️ General Privacy Lists

Only **background and privacy endpoints** are blocked here. Websites, apps and devices should generally continue to work.

<a id="privacy"></a>
### 🕵️ Privacy & Tracking

#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 31,392 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/light.txt) |
| 🟦 **Normal** | 55,932 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/normal.txt) |
| 🟨 **Pro** | 83,565 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/pro.txt) |
| 🟧 **Pro++** | 344,214 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/pro-plus.txt) |
| 🟥 **Ultimate** | 348,192 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/ultimate.txt) |

> **Privacy & Tracking – Ultimate:** This level contains the union of all full/special lists in the **Privacy & Tracking** area. Lower levels are cumulative, risk-based subsets.

#### Full / Special Lists

<details>
<summary><strong>📂 Show full/special lists</strong></summary>

| List | Entries | Status | Full List |
| --- | ---: | :---: | --- |
| **Ads (Advertising)** | 218,123 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/ads.txt) |
| **Pop-Up Ads** | 512 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/pop-up-ads.txt) |
| **Affiliate Tracking** | 608 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/affiliate-tracking.txt) |
| **Aggressive Privacy** | 625 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/aggressive-privacy.txt) |
| **Analytics** | 34,728 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/analytics.txt) |
| **Captcha Antibot** | 378 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/captcha-antibot.txt) |
| **Cdn Tracking** | 19 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/cdn-tracking.txt) |
| **Chat Support** | 49 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/chat-support.txt) |
| **Consent Cmp** | 41 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/consent-cmp.txt) |
| **Crash Reporting** | 85 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/crash-reporting.txt) |
| **Crm** | 106 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/crm.txt) |
| **Ecommerce** | 42 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/ecommerce.txt) |
| **External Fonts** | 3 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/external-fonts.txt) |
| **Fingerprinting** | 10 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/fingerprinting.txt) |
| **Marketing** | 2,004 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/marketing.txt) |
| **Mobile Tracking** | 208 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/mobile-tracking.txt) |
| **Native Tracking** | 587 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/native-tracking.txt) |
| **Newsletter Tracking** | 156 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/newsletter-tracking.txt) |
| **Payment Tracking** | 17 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/payment-tracking.txt) |
| **Push Notifications** | 73 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/push-notifications.txt) |
| **Recommendations** | 360 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/recommendations.txt) |
| **Search Tracking** | 1 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/search-tracking.txt) |
| **Seo Tracking** | 115 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/seo-tracking.txt) |
| **Session Replay** | 195 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/session-replay.txt) |
| **Social Tracking** | 29 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/social-tracking.txt) |
| **Telemetry** | 27,984 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/telemetry.txt) |
| **Trackers** | 106,915 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/trackers.txt) |
| **Tracking Pixels** | 866 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/tracking-pixels.txt) |
| **Tracking Redirects** | 306 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/tracking-redirects.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="software-hardware"></a>
### 🧩 Software & Hardware Telemetry

#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 73 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/light.txt) |
| 🟦 **Normal** | 73 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/normal.txt) |
| 🟨 **Pro** | 78 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/pro.txt) |
| 🟧 **Pro++** | 78 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/pro-plus.txt) |
| 🟥 **Ultimate** | 83 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/ultimate.txt) |

<details>
<summary><strong>📂 Show vendor behavior lists</strong></summary>


| Device / Vendor | Entries | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
| --- | :---: | --- | --- | --- | --- |
| **Adobe** | 354 | **34 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/adobe/privacy.txt) | **38 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/adobe/restrict.txt) | **354 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/adobe/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/adobe/updates.txt) |
| **AMD** | 5 | **1 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/amd/privacy.txt) | **2 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/amd/restrict.txt) | **5 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/amd/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/amd/updates.txt) |
| **Autodesk** | 15 | **7 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/autodesk/privacy.txt) | **7 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/autodesk/restrict.txt) | **15 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/autodesk/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/autodesk/updates.txt) |
| **Corsair** | 2 | **2 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/corsair/privacy.txt) | **2 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/corsair/restrict.txt) | **2 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/corsair/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/corsair/updates.txt) |
| **Intel** | 4 | **3 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/intel/privacy.txt) | **3 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/intel/restrict.txt) | **4 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/intel/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/intel/updates.txt) |
| **Logitech** | 15 | **4 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/logitech/privacy.txt) | **4 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/logitech/restrict.txt) | **15 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/logitech/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/logitech/updates.txt) |
| **Nvidia** | 19 | **9 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/nvidia/privacy.txt) | **9 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/nvidia/restrict.txt) | **19 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/nvidia/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/nvidia/updates.txt) |
| **Razer** | 8 | **3 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/razer/privacy.txt) | **3 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/razer/restrict.txt) | **8 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/razer/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/razer/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="automation"></a>
### 🤖 AI, Bots & Crawlers

#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 13 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/light.txt) |
| 🟦 **Normal** | 28 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/normal.txt) |
| 🟨 **Pro** | 33 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/pro.txt) |
| 🟧 **Pro++** | 50 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/pro-plus.txt) |
| 🟥 **Ultimate** | 301 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/ultimate.txt) |

#### Full / Special Lists

<details>
<summary><strong>📂 Show full/special lists</strong></summary>

| List | Entries | Status | Full List |
| --- | ---: | :---: | --- |
| **Aggressive Crawlers** | 15 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/aggressive-crawlers.txt) |
| **Ai Crawlers** | 10 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/ai-crawlers.txt) |
| **Ai Scrapers** | 3 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/ai-scrapers.txt) |
| **Ai Telemetry** | 36 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/ai-telemetry.txt) |
| **Ai Tracking** | 44 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/ai-tracking.txt) |
| **Llm Crawlers** | 188 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/llm-crawlers.txt) |
| **Malicious Bots** | 1 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/malicious-bots.txt) |
| **Seo Bots** | 5 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/seo-bots.txt) |
| **Training Bots** | 6 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/training-bots.txt) |
| **Web Crawlers** | 62 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/web-crawlers.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>


---
<a id="devices-group"></a>
## 🔌 Devices & Vendors — Privacy / Restrict / Isolate

Devices and vendors use separate behavior levels: **Privacy** for tracking/telemetry, **Restrict** for additional optional vendor services, and **Isolate** for as much vendor communication as possible.

<a id="smart-tv"></a>
### 📺 Smart TV

#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 344 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/light.txt) |
| 🟦 **Normal** | 359 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/normal.txt) |
| 🟨 **Pro** | 451 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/pro.txt) |
| 🟧 **Pro++** | 622 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/pro-plus.txt) |
| 🟥 **Ultimate** | 634 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | Entries | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
| --- | :---: | --- | --- | --- | --- |
| **Amazon Fire TV** | 776 | **159 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/amazon-fire-tv/privacy.txt) | **170 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/amazon-fire-tv/restrict.txt) | **776 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/amazon-fire-tv/isolate.txt) | **4 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/amazon-fire-tv/updates.txt) |
| **Google Android TV** | 14,479 | **13,438 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/google-android-tv/privacy.txt) | **13,440 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/google-android-tv/restrict.txt) | **14,479 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/google-android-tv/isolate.txt) | **11 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/google-android-tv/updates.txt) |
| **Google TV** | 14,479 | **13,438 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/google-tv/privacy.txt) | **13,440 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/google-tv/restrict.txt) | **14,479 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/google-tv/isolate.txt) | **11 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/google-tv/updates.txt) |
| **Hisense VIDAA** | 11 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/hisense-vidaa/privacy.txt) | **0 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/hisense-vidaa/restrict.txt) | **11 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/hisense-vidaa/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/hisense-vidaa/updates.txt) |
| **LG webOS** | 620 | **332 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/lg-webos/privacy.txt) | **332 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/lg-webos/restrict.txt) | **620 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/lg-webos/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/lg-webos/updates.txt) |
| **Panasonic** | 15 | **8 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/panasonic/privacy.txt) | **8 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/panasonic/restrict.txt) | **15 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/panasonic/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/panasonic/updates.txt) |
| **Philips** | 73 | **63 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/philips/privacy.txt) | **63 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/philips/restrict.txt) | **73 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/philips/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/philips/updates.txt) |
| **Roku** | 13 | **5 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/roku/privacy.txt) | **5 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/roku/restrict.txt) | **13 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/roku/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/roku/updates.txt) |
| **Samsung** | 347 | **113 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/samsung/privacy.txt) | **114 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/samsung/restrict.txt) | **347 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/samsung/isolate.txt) | **1 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/samsung/updates.txt) |
| **Shared / Other** | 104 | **15 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/shared-other/privacy.txt) | **16 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/shared-other/restrict.txt) | **104 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/shared-other/isolate.txt) | **1 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/shared-other/updates.txt) |
| **Sony Bravia** | 147 | **26 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/sony-bravia/privacy.txt) | **26 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/sony-bravia/restrict.txt) | **147 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/sony-bravia/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/sony-bravia/updates.txt) |
| **TCL** | 2 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/tcl/privacy.txt) | **0 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/tcl/restrict.txt) | **2 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/tcl/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/tcl/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="mobile"></a>
### 📱 Smartphones & Mobile

#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 391 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/light.txt) |
| 🟦 **Normal** | 442 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/normal.txt) |
| 🟨 **Pro** | 518 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/pro.txt) |
| 🟧 **Pro++** | 939 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/pro-plus.txt) |
| 🟥 **Ultimate** | 945 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | Entries | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
| --- | :---: | --- | --- | --- | --- |
| **Apple iOS** | 340 | **52 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/apple-ios/privacy.txt) | **53 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/apple-ios/restrict.txt) | **340 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/apple-ios/isolate.txt) | **7 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/apple-ios/updates.txt) |
| **Google Android** | 14,488 | **13,440 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/google-android/privacy.txt) | **13,442 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/google-android/restrict.txt) | **14,488 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/google-android/isolate.txt) | **11 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/google-android/updates.txt) |
| **Google Pixel** | 14,488 | **13,440 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/google-pixel/privacy.txt) | **13,442 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/google-pixel/restrict.txt) | **14,488 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/google-pixel/isolate.txt) | **11 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/google-pixel/updates.txt) |
| **Huawei** | 75 | **16 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/huawei/privacy.txt) | **16 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/huawei/restrict.txt) | **75 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/huawei/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/huawei/updates.txt) |
| **Motorola** | 31 | **2 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/motorola/privacy.txt) | **3 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/motorola/restrict.txt) | **31 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/motorola/isolate.txt) | **1 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/motorola/updates.txt) |
| **Oneplus** | 8 | **1 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/oneplus/privacy.txt) | **1 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/oneplus/restrict.txt) | **8 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/oneplus/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/oneplus/updates.txt) |
| **Oppo / Realme** | 161 | **39 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/oppo-realme/privacy.txt) | **39 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/oppo-realme/restrict.txt) | **161 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/oppo-realme/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/oppo-realme/updates.txt) |
| **Samsung** | 308 | **111 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/samsung/privacy.txt) | **112 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/samsung/restrict.txt) | **308 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/samsung/isolate.txt) | **1 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/samsung/updates.txt) |
| **Shared / Other** | 582 | **232 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/shared-other/privacy.txt) | **237 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/shared-other/restrict.txt) | **582 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/shared-other/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/shared-other/updates.txt) |
| **Vivo** | 53 | **4 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/vivo/privacy.txt) | **4 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/vivo/restrict.txt) | **53 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/vivo/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/vivo/updates.txt) |
| **Xiaomi** | 582 | **121 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/xiaomi/privacy.txt) | **126 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/xiaomi/restrict.txt) | **582 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/xiaomi/isolate.txt) | **7 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/xiaomi/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="betriebssysteme"></a>
### 💻 Operating Systems

#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 20 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/light.txt) |
| 🟦 **Normal** | 45 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/normal.txt) |
| 🟨 **Pro** | 89 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/pro.txt) |
| 🟧 **Pro++** | 244 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/pro-plus.txt) |
| 🟥 **Ultimate** | 249 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | Entries | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
| --- | :---: | --- | --- | --- | --- |
| **Android** | 14,598 | **13,464 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/android/privacy.txt) | **13,467 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/android/restrict.txt) | **14,598 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/android/isolate.txt) | **11 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/android/updates.txt) |
| **Apple** | 358 | **61 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/apple/privacy.txt) | **62 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/apple/restrict.txt) | **358 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/apple/isolate.txt) | **7 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/apple/updates.txt) |
| **Chromeos** | 14,480 | **13,438 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/chromeos/privacy.txt) | **13,440 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/chromeos/restrict.txt) | **14,480 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/chromeos/isolate.txt) | **11 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/chromeos/updates.txt) |
| **Ios** | 341 | **52 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/ios/privacy.txt) | **53 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/ios/restrict.txt) | **341 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/ios/isolate.txt) | **7 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/ios/updates.txt) |
| **Linux** | 3 | **1 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/linux/privacy.txt) | **1 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/linux/restrict.txt) | **3 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/linux/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/linux/updates.txt) |
| **Macos** | 340 | **52 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/macos/privacy.txt) | **53 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/macos/restrict.txt) | **340 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/macos/isolate.txt) | **7 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/macos/updates.txt) |
| **Windows** | 793 | **204 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/windows/privacy.txt) | **225 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/windows/restrict.txt) | **793 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/windows/isolate.txt) | **21 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/windows/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="iot"></a>
### 🏠 IoT & Smart Home

#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 2 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/light.txt) |
| 🟦 **Normal** | 11 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/normal.txt) |
| 🟨 **Pro** | 26 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/pro.txt) |
| 🟧 **Pro++** | 79 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/pro-plus.txt) |
| 🟥 **Ultimate** | 82 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | Entries | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
| --- | :---: | --- | --- | --- | --- |
| **Amazon Alexa** | 771 | **159 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/amazon-alexa/privacy.txt) | **170 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/amazon-alexa/restrict.txt) | **771 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/amazon-alexa/isolate.txt) | **4 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/amazon-alexa/updates.txt) |
| **Huawei** | 75 | **16 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/huawei/privacy.txt) | **16 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/huawei/restrict.txt) | **75 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/huawei/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/huawei/updates.txt) |
| **Samsung SmartThings** | 307 | **111 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/samsung-smartthings/privacy.txt) | **112 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/samsung-smartthings/restrict.txt) | **307 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/samsung-smartthings/isolate.txt) | **1 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/samsung-smartthings/updates.txt) |
| **Shared / Other** | 20 | **10 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/shared-other/privacy.txt) | **10 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/shared-other/restrict.txt) | **20 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/shared-other/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/shared-other/updates.txt) |
| **Sonos** | 2 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/sonos/privacy.txt) | **0 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/sonos/restrict.txt) | **2 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/sonos/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/sonos/updates.txt) |
| **Xiaomi** | 582 | **121 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/xiaomi/privacy.txt) | **126 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/xiaomi/restrict.txt) | **582 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/xiaomi/isolate.txt) | **7 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/xiaomi/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="voice"></a>
### 🎙️ Voice Assistants

#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 7 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/light.txt) |
| 🟦 **Normal** | 16 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/normal.txt) |
| 🟨 **Pro** | 37 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/pro.txt) |
| 🟧 **Pro++** | 103 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/pro-plus.txt) |
| 🟥 **Ultimate** | 108 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | Entries | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
| --- | :---: | --- | --- | --- | --- |
| **Alexa** | 768 | **159 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/alexa/privacy.txt) | **170 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/alexa/restrict.txt) | **768 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/alexa/isolate.txt) | **4 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/alexa/updates.txt) |
| **Cortana** | 774 | **194 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/cortana/privacy.txt) | **215 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/cortana/restrict.txt) | **774 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/cortana/isolate.txt) | **21 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/cortana/updates.txt) |
| **Google Assistant** | 14,481 | **13,438 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/google-assistant/privacy.txt) | **13,441 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/google-assistant/restrict.txt) | **14,481 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/google-assistant/isolate.txt) | **11 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/google-assistant/updates.txt) |
| **Siri** | 362 | **55 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/siri/privacy.txt) | **56 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/siri/restrict.txt) | **362 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/siri/isolate.txt) | **8 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/siri/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="automotive"></a>
### 🚗 Automotive / Connected Cars

#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 42 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/light.txt) |
| 🟦 **Normal** | 102 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/normal.txt) |
| 🟨 **Pro** | 177 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/pro.txt) |
| 🟧 **Pro++** | 617 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/pro-plus.txt) |
| 🟥 **Ultimate** | 619 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | Entries | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
| --- | :---: | --- | --- | --- | --- |
| **Audi** | 491 | **71 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/audi/privacy.txt) | **72 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/audi/restrict.txt) | **491 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/audi/isolate.txt) | **4 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/audi/updates.txt) |
| **Bmw** | 53 | **10 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/bmw/privacy.txt) | **10 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/bmw/restrict.txt) | **53 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/bmw/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/bmw/updates.txt) |
| **Ford** | 31 | **3 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/ford/privacy.txt) | **3 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/ford/restrict.txt) | **31 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/ford/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/ford/updates.txt) |
| **Mercedes** | 33 | **22 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/mercedes/privacy.txt) | **22 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/mercedes/restrict.txt) | **33 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/mercedes/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/mercedes/updates.txt) |
| **Tesla** | 12 | **2 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/tesla/privacy.txt) | **2 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/tesla/restrict.txt) | **12 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/tesla/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/tesla/updates.txt) |
| **VW** | 45 | **6 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/vw/privacy.txt) | **6 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/vw/restrict.txt) | **45 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/vw/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/vw/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="nas-server"></a>
### 💾 NAS & Server

#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 1 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/light.txt) |
| 🟦 **Normal** | 3 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/normal.txt) |
| 🟨 **Pro** | 11 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/pro.txt) |
| 🟧 **Pro++** | 53 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/pro-plus.txt) |
| 🟥 **Ultimate** | 55 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | Entries | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
| --- | :---: | --- | --- | --- | --- |
| **Docker** | 16 | **2 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/docker/privacy.txt) | **2 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/docker/restrict.txt) | **16 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/docker/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/docker/updates.txt) |
| **HPE / Dell** | 5 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/hpe-dell/privacy.txt) | **1 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/hpe-dell/restrict.txt) | **5 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/hpe-dell/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/hpe-dell/updates.txt) |
| **Kubernetes** | 25 | **3 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/kubernetes/privacy.txt) | **4 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/kubernetes/restrict.txt) | **25 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/kubernetes/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/kubernetes/updates.txt) |
| **QNAP** | 6 | **6 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/qnap/privacy.txt) | **6 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/qnap/restrict.txt) | **6 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/qnap/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/qnap/updates.txt) |
| **Red Hat / OpenShift** | 5 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/redhat-openshift/privacy.txt) | **1 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/redhat-openshift/restrict.txt) | **5 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/redhat-openshift/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/redhat-openshift/updates.txt) |
| **Synology** | 3 | **2 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/synology/privacy.txt) | **2 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/synology/restrict.txt) | **3 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/synology/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/synology/updates.txt) |
| **Truenas** | 3 | **1 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/truenas/privacy.txt) | **1 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/truenas/restrict.txt) | **3 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/truenas/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/truenas/updates.txt) |
| **Unraid** | 2 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/unraid/privacy.txt) | **0 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/unraid/restrict.txt) | **2 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/unraid/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/unraid/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="network-devices"></a>
### 🌐 Routers & Network Devices

#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 11 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/light.txt) |
| 🟦 **Normal** | 48 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/normal.txt) |
| 🟨 **Pro** | 73 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/pro.txt) |
| 🟧 **Pro++** | 370 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/pro-plus.txt) |
| 🟥 **Ultimate** | 396 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | Entries | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
| --- | :---: | --- | --- | --- | --- |
| **Asus** | 29 | **2 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/asus/privacy.txt) | **3 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/asus/restrict.txt) | **29 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/asus/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/asus/updates.txt) |
| **AVM / FRITZ!Box** | 1 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/avm-fritzbox/privacy.txt) | **0 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/avm-fritzbox/restrict.txt) | **1 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/avm-fritzbox/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/avm-fritzbox/updates.txt) |
| **Cisco** | 29 | **5 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/cisco/privacy.txt) | **5 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/cisco/restrict.txt) | **29 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/cisco/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/cisco/updates.txt) |
| **Huawei** | 58 | **12 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/huawei/privacy.txt) | **12 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/huawei/restrict.txt) | **58 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/huawei/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/huawei/updates.txt) |
| **Mikrotik** | 1 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/mikrotik/privacy.txt) | **0 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/mikrotik/restrict.txt) | **1 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/mikrotik/isolate.txt) | **1 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/mikrotik/updates.txt) |
| **Netgear** | 4 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/netgear/privacy.txt) | **0 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/netgear/restrict.txt) | **4 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/netgear/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/netgear/updates.txt) |
| **TP-Link** | 17 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/tp-link/privacy.txt) | **6 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/tp-link/restrict.txt) | **17 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/tp-link/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/tp-link/updates.txt) |
| **Ubiquiti** | 301 | **38 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/ubiquiti/privacy.txt) | **41 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/ubiquiti/restrict.txt) | **301 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/ubiquiti/isolate.txt) | **2 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/ubiquiti/updates.txt) |
| **Zyxel** | 1 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/zyxel/privacy.txt) | **0 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/zyxel/restrict.txt) | **1 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/zyxel/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/zyxel/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="providers"></a>
### 📡 ISP / Providers

#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 5 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/light.txt) |
| 🟦 **Normal** | 39 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/normal.txt) |
| 🟨 **Pro** | 71 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/pro.txt) |
| 🟧 **Pro++** | 166 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/pro-plus.txt) |
| 🟥 **Ultimate** | 166 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | Entries | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
| --- | :---: | --- | --- | --- | --- |
| **1&1** | 7 | **2 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/1und1/privacy.txt) | **2 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/1und1/restrict.txt) | **7 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/1und1/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/1und1/updates.txt) |
| **Deutsche Glasfaser** | 6 | **6 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/deutsche-glasfaser/privacy.txt) | **6 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/deutsche-glasfaser/restrict.txt) | **6 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/deutsche-glasfaser/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/deutsche-glasfaser/updates.txt) |
| **O2** | 18 | **3 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/o2/privacy.txt) | **4 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/o2/restrict.txt) | **18 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/o2/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/o2/updates.txt) |
| **Telekom** | 61 | **6 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/telekom/privacy.txt) | **6 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/telekom/restrict.txt) | **61 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/telekom/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/telekom/updates.txt) |
| **Unitymedia** | 4 | **4 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/unitymedia/privacy.txt) | **4 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/unitymedia/restrict.txt) | **4 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/unitymedia/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/unitymedia/updates.txt) |
| **Vodafone** | 81 | **22 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/vodafone/privacy.txt) | **22 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/vodafone/restrict.txt) | **81 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/vodafone/isolate.txt) | **3 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/vodafone/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="ecosystems"></a>
### 🏢 Google, Microsoft, Apple & Amazon

#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 11,912 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/light.txt) |
| 🟦 **Normal** | 12,074 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/normal.txt) |
| 🟨 **Pro** | 12,357 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/pro.txt) |
| 🟧 **Pro++** | 15,410 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/pro-plus.txt) |
| 🟥 **Ultimate** | 15,462 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | Entries | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
| --- | :---: | --- | --- | --- | --- |
| **Amazon** | 777 | **159 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/amazon/privacy.txt) | **170 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/amazon/restrict.txt) | **777 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/amazon/isolate.txt) | **4 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/amazon/updates.txt) |
| **Apple** | 340 | **52 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/apple/privacy.txt) | **53 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/apple/restrict.txt) | **340 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/apple/isolate.txt) | **7 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/apple/updates.txt) |
| **Google** | 14,481 | **13,438 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/google/privacy.txt) | **13,440 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/google/restrict.txt) | **14,481 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/google/isolate.txt) | **11 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/google/updates.txt) |
| **Microsoft** | 779 | **202 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/microsoft/privacy.txt) | **223 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/microsoft/restrict.txt) | **779 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/microsoft/isolate.txt) | **21 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/microsoft/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="manufacturers"></a>
### 🏭 Vendor Lists

This overview shows the concrete behavior lists for **every vendor currently present**.

| Device / Vendor | Entries | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
| --- | :---: | --- | --- | --- | --- |
| **Adobe** | 354 | **34 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/adobe/privacy.txt) | **38 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/adobe/restrict.txt) | **354 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/adobe/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/adobe/updates.txt) |
| **Amazon** | 770 | **159 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/amazon/privacy.txt) | **170 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/amazon/restrict.txt) | **770 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/amazon/isolate.txt) | **4 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/amazon/updates.txt) |
| **AMD** | 5 | **1 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/amd/privacy.txt) | **2 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/amd/restrict.txt) | **5 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/amd/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/amd/updates.txt) |
| **Apple** | 337 | **51 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/apple/privacy.txt) | **52 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/apple/restrict.txt) | **337 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/apple/isolate.txt) | **7 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/apple/updates.txt) |
| **Autodesk** | 15 | **7 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/autodesk/privacy.txt) | **7 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/autodesk/restrict.txt) | **15 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/autodesk/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/autodesk/updates.txt) |
| **Ea** | 298 | **37 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/ea/privacy.txt) | **39 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/ea/restrict.txt) | **298 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/ea/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/ea/updates.txt) |
| **Epic** | 8 | **5 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/epic/privacy.txt) | **5 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/epic/restrict.txt) | **8 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/epic/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/epic/updates.txt) |
| **Google** | 14,479 | **13,438 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/google/privacy.txt) | **13,440 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/google/restrict.txt) | **14,479 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/google/isolate.txt) | **11 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/google/updates.txt) |
| **Huawei** | 58 | **12 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/huawei/privacy.txt) | **12 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/huawei/restrict.txt) | **58 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/huawei/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/huawei/updates.txt) |
| **LG** | 601 | **329 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/lg/privacy.txt) | **329 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/lg/restrict.txt) | **601 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/lg/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/lg/updates.txt) |
| **Logitech** | 15 | **4 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/logitech/privacy.txt) | **4 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/logitech/restrict.txt) | **15 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/logitech/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/logitech/updates.txt) |
| **Meta** | 111 | **12 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/meta/privacy.txt) | **13 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/meta/restrict.txt) | **111 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/meta/isolate.txt) | **2 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/meta/updates.txt) |
| **Microsoft** | 764 | **196 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/microsoft/privacy.txt) | **217 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/microsoft/restrict.txt) | **764 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/microsoft/isolate.txt) | **21 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/microsoft/updates.txt) |
| **Nintendo** | 10 | **3 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/nintendo/privacy.txt) | **4 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/nintendo/restrict.txt) | **10 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/nintendo/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/nintendo/updates.txt) |
| **Nvidia** | 18 | **8 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/nvidia/privacy.txt) | **8 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/nvidia/restrict.txt) | **18 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/nvidia/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/nvidia/updates.txt) |
| **Philips** | 73 | **63 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/philips/privacy.txt) | **63 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/philips/restrict.txt) | **73 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/philips/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/philips/updates.txt) |
| **Razer** | 8 | **3 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/razer/privacy.txt) | **3 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/razer/restrict.txt) | **8 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/razer/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/razer/updates.txt) |
| **Samsung** | 308 | **111 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/samsung/privacy.txt) | **112 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/samsung/restrict.txt) | **308 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/samsung/isolate.txt) | **1 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/samsung/updates.txt) |
| **Sony** | 143 | **26 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/sony/privacy.txt) | **26 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/sony/restrict.txt) | **143 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/sony/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/sony/updates.txt) |
| **Ubisoft** | 6 | **6 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/ubisoft/privacy.txt) | **6 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/ubisoft/restrict.txt) | **6 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/ubisoft/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/ubisoft/updates.txt) |
| **Valve / Steam** | 49 | **4 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/valve-steam/privacy.txt) | **4 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/valve-steam/restrict.txt) | **49 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/valve-steam/isolate.txt) | **0 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/valve-steam/updates.txt) |
| **Xiaomi** | 582 | **121 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/xiaomi/privacy.txt) | **126 entries**<br>[Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/xiaomi/restrict.txt) | **582 entries**<br>[Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/xiaomi/isolate.txt) | **7 entries**<br>[Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/xiaomi/updates.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>


---
<a id="apps-group"></a>
## 📱 Apps & Services — Privacy / Block All

For apps and services, **Privacy** and **Block All** are separate. Privacy reduces tracking/analytics/telemetry; Block All is intended to completely block the service.

<a id="streaming"></a>
### 📺 Streaming

#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 7 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/light.txt) |
| 🟦 **Normal** | 13 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/normal.txt) |
| 🟨 **Pro** | 27 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/pro.txt) |
| 🟧 **Pro++** | 39 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/pro-plus.txt) |
| 🟥 **Ultimate** | 44 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** the service should continue to work; tracking/analytics/telemetry are reduced.  
> 🚫 **Block All:** the service should be completely blocked.

| App / Service | Entries | 🛡️ Privacy | 🚫 Block All |
| --- | :---: | --- | --- |
| **Apple TV** | 15 | **4 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/apple-tv/privacy.txt) | **15 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/apple-tv/block-all.txt) |
| **Dazn** | 5 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/dazn/privacy.txt) | **5 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/dazn/block-all.txt) |
| **Disney+** | 9 | **1 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/disney-plus/privacy.txt) | **9 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/disney-plus/block-all.txt) |
| **Emby** | 2 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/emby/privacy.txt) | **2 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/emby/block-all.txt) |
| **Jellyfin** | 2 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/jellyfin/privacy.txt) | **2 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/jellyfin/block-all.txt) |
| **Netflix** | 25 | **12 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/netflix/privacy.txt) | **25 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/netflix/block-all.txt) |
| **Paramount** | 9 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/paramount/privacy.txt) | **9 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/paramount/block-all.txt) |
| **Plex** | 7 | **2 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/plex/privacy.txt) | **7 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/plex/block-all.txt) |
| **Prime Video** | 4 | **1 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/prime-video/privacy.txt) | **4 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/prime-video/block-all.txt) |
| **Spotify** | 132 | **17 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/spotify/privacy.txt) | **132 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/spotify/block-all.txt) |
| **Twitch** | 18 | **4 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/twitch/privacy.txt) | **18 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/twitch/block-all.txt) |
| **Youtube** | 17 | **4 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/youtube/privacy.txt) | **17 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/youtube/block-all.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="gaming"></a>
### 🎮 Gaming

#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 2 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/light.txt) |
| 🟦 **Normal** | 30 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/normal.txt) |
| 🟨 **Pro** | 42 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/pro.txt) |
| 🟧 **Pro++** | 46 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/pro-plus.txt) |
| 🟥 **Ultimate** | 50 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/ultimate.txt) |

<details>
<summary><strong>📂 Show platform behavior lists</strong></summary>


| App / Service | Entries | 🛡️ Privacy | 🚫 Block All |
| --- | :---: | --- | --- |
| **Battle.net** | 8 | **3 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/battle-net/privacy.txt) | **8 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/battle-net/block-all.txt) |
| **EA / Origin** | 20 | **1 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/ea-origin/privacy.txt) | **20 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/ea-origin/block-all.txt) |
| **Epic Games** | 11 | **5 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/epic-games/privacy.txt) | **11 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/epic-games/block-all.txt) |
| **Mobile Games** | 7 | **2 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/mobile-games/privacy.txt) | **7 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/mobile-games/block-all.txt) |
| **Nintendo** | 7 | **1 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/nintendo/privacy.txt) | **7 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/nintendo/block-all.txt) |
| **Playstation** | 13 | **4 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/playstation/privacy.txt) | **13 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/playstation/block-all.txt) |
| **Riot Games** | 6 | **3 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/riot-games/privacy.txt) | **6 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/riot-games/block-all.txt) |
| **Rockstar** | 5 | **2 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/rockstar/privacy.txt) | **5 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/rockstar/block-all.txt) |
| **Steam** | 7 | **2 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/steam/privacy.txt) | **7 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/steam/block-all.txt) |
| **Ubisoft** | 4 | **2 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/ubisoft/privacy.txt) | **4 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/ubisoft/block-all.txt) |
| **Xbox** | 11 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/xbox/privacy.txt) | **11 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/xbox/block-all.txt) |

</details>

#### Privacy Special Lists

| Special List | 🛡️ Privacy |
|---|---|
| **Anti-Cheat Telemetry** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/anti-cheat-telemetry/privacy.txt) |
| **Game Analytics** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/game-analytics/privacy.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="social-media"></a>
### 💬 Social Media

#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 14 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/light.txt) |
| 🟦 **Normal** | 26 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/normal.txt) |
| 🟨 **Pro** | 30 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/pro.txt) |
| 🟧 **Pro++** | 47 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/pro-plus.txt) |
| 🟥 **Ultimate** | 47 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** the service should continue to work; tracking/analytics/telemetry are reduced.  
> 🚫 **Block All:** the service should be completely blocked.

| App / Service | Entries | 🛡️ Privacy | 🚫 Block All |
| --- | :---: | --- | --- |
| **Discord** | 12 | **2 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/discord/privacy.txt) | **12 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/discord/block-all.txt) |
| **Facebook / Meta** | 47 | **7 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/facebook-meta/privacy.txt) | **47 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/facebook-meta/block-all.txt) |
| **Instagram** | 10 | **1 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/instagram/privacy.txt) | **10 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/instagram/block-all.txt) |
| **Linkedin** | 16 | **8 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/linkedin/privacy.txt) | **16 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/linkedin/block-all.txt) |
| **Pinterest** | 13 | **4 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/pinterest/privacy.txt) | **13 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/pinterest/block-all.txt) |
| **Reddit** | 26 | **13 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/reddit/privacy.txt) | **26 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/reddit/block-all.txt) |
| **Snapchat** | 15 | **6 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/snapchat/privacy.txt) | **15 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/snapchat/block-all.txt) |
| **Telegram** | 5 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/telegram/privacy.txt) | **5 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/telegram/block-all.txt) |
| **Threads** | 8 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/threads/privacy.txt) | **8 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/threads/block-all.txt) |
| **Tiktok** | 58 | **21 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/tiktok/privacy.txt) | **58 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/tiktok/block-all.txt) |
| **Whatsapp** | 6 | **1 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/whatsapp/privacy.txt) | **6 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/whatsapp/block-all.txt) |
| **X / Twitter** | 25 | **9 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/x-twitter/privacy.txt) | **25 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/x-twitter/block-all.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="cloud-dev"></a>
### ☁️ Cloud, Server & Development

#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 65 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/light.txt) |
| 🟦 **Normal** | 165 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/normal.txt) |
| 🟨 **Pro** | 301 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/pro.txt) |
| 🟧 **Pro++** | 1,486 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/pro-plus.txt) |
| 🟥 **Ultimate** | 1,491 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** the service should continue to work; tracking/analytics/telemetry are reduced.  
> 🚫 **Block All:** the service should be completely blocked.

| App / Service | Entries | 🛡️ Privacy | 🚫 Block All |
| --- | :---: | --- | --- |
| **AWS** | 440 | **125 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/aws/privacy.txt) | **440 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/aws/block-all.txt) |
| **Azure** | 186 | **16 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/azure/privacy.txt) | **186 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/azure/block-all.txt) |
| **Cicd** | 2 | **0 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/cicd/privacy.txt) | **2 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/cicd/block-all.txt) |
| **Cloud Storage** | 12 | **4 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/cloud-storage/privacy.txt) | **12 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/cloud-storage/block-all.txt) |
| **Cloudflare** | 33 | **8 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/cloudflare/privacy.txt) | **33 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/cloudflare/block-all.txt) |
| **Github** | 18 | **3 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/github/privacy.txt) | **18 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/github/block-all.txt) |
| **Gitlab** | 3 | **1 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/gitlab/privacy.txt) | **3 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/gitlab/block-all.txt) |
| **Google Cloud** | 49 | **2 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/google-cloud/privacy.txt) | **49 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/google-cloud/block-all.txt) |
| **Jetbrains** | 1 | **1 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/jetbrains/privacy.txt) | **1 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/jetbrains/block-all.txt) |
| **Oracle Cloud** | 8 | **3 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/oracle-cloud/privacy.txt) | **8 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/oracle-cloud/block-all.txt) |
| **Visual Studio** | 2 | **1 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/visual-studio/privacy.txt) | **2 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/visual-studio/block-all.txt) |
| **VS Code** | 2 | **1 entries**<br>[Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/vscode/privacy.txt) | **2 entries**<br>[Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/vscode/block-all.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>


---
<a id="protection-group"></a>
## 🛡️ Full Protection / Control Lists

These areas are deliberate **domain-blocking lists**. A match should not be reachable for the assigned Pi-hole group.

<a id="family"></a>
### 👨‍👩‍👧 Family & Content

> 🚫 **Full domain blocking:** Listd adult/NSFW/gambling/drugs/violence/weapons/piracy/torrent domains should not be reachable.


#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 998,924 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/light.txt) |
| 🟦 **Normal** | 1,419,159 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/normal.txt) |
| 🟨 **Pro** | 1,430,117 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/pro.txt) |
| 🟧 **Pro++** | 1,769,650 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/pro-plus.txt) |
| 🟥 **Ultimate** | 2,347,190 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/ultimate.txt) |

#### Full Content Lists

<details>
<summary><strong>📂 Show content lists</strong></summary>

| List | Entries | Status | Link |
| --- | ---: | :---: | --- |
| **Adult** | 998,924 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/adult.txt) |
| **Dating** | 40 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/dating.txt) |
| **Drugs** | 55 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/drugs.txt) |
| **Gambling** | 420,536 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/gambling.txt) |
| **Misinformation** | 0 | 🟡 | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/misinformation.txt) |
| **Piracy** | 58 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/piracy.txt) |
| **Sexual Content** | 998,924 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/sexual-content.txt) |
| **Torrents** | 44 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/torrents.txt) |
| **Violence Gore** | 53 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/violence-gore.txt) |
| **Weapons** | 89 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/weapons.txt) |

> `Misinformation` deliberately remains optional and is not automatically treated as an objective security category.

</details>

<p align="right"><a href="#kinderschutz-navigation">⬆️ Family table of contents</a></p>

---

<a id="kids-allow-only"></a>
### 🧒 Kids Allow-Only

`Kids Allow-Only` is not a normal denylist profile. In a dedicated Pi-hole group, everything is blocked by default; only explicitly allowed domains work.

<a id="kids-dateien"></a>
#### 📚 Kids Allowlist Files

| Datei | Entries | Purpose | List |
| --- | ---: | --- | --- |
| `kids-de.txt` | 39 | Basis-Allowlist | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-de.txt) |
| `kids-education-de.txt` | 17 | Learning, school, STEM, history | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-education-de.txt) |
| `kids-media-de.txt` | 16 | Children's TV, audio, news | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-media-de.txt) |
| `kids-games-de.txt` | 18 | verified children's games | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-games-de.txt) |
| `kids-runtime-de.txt` | 9 | required technical hosts | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-runtime-de.txt) |


The base allowlist includes, among others, fragFINN, Blinde Kuh, Seitenstark, Internet-ABC, KiKA, Kikaninchen, WDR Maus, Kindernetz, Kinderfilmwelt, HanisauLand, Kinderzeitmaschine, LegaKids, Meine Forscherwelt, Klassewasser, Abenteuer Regenwald, Naturdetektive, Ohrka and Auditorix.

<a id="kids-anleitung"></a>
<details>
<summary><strong>🛠️ Pi-hole v6+: Set up Kids Allow Only</strong></summary>

> **Principle:** Create a dedicated Pi-hole group for children's devices.  
> This group receives a **Regex Deny rule `.*`**, which blocks everything by default.  
> Then add **exactly one Kids Allow Only list as a subscribed allowlist**.  
> This means only explicitly allowed domains are reachable.

### 1. Give the child device a stable identity

Use a **static IP address or DHCP reservation** whenever possible so Pi-hole can always assign the device to the correct group.

Example:

`192.168.178.50` → child's tablet

### 2. Create a dedicated Pi-hole group

In Pi-hole:

**Group Management → Groups → Add Group**

Example name:

`Kids-Allow-Only`

### 3. Assign the child device to the group

Go to:

**Group Management → Clients**

Add the device and assign it only to the **Kids-Allow-Only** group.

> **Recommendation:** Remove the device from the `Default` group so normal network rules do not unexpectedly interfere with the Allow Only profile.

### 4. Choose the Kids allowlist

Use the appropriate list from this section.

Open the desired list on GitHub, click **Raw**, and copy the Raw URL.

### 5. Add the list as a subscribed allowlist

In **Pi-hole v6+**, add the copied Raw URL as a **Subscribed Allowlist**.

Important:

- Type: **Allow**
- Group: **only `Kids-Allow-Only`**
- do not assign it to the normal `Default` group

### 6. Block everything else

Go to:

**Group Management → Domains**

Create a new **Regex Denylist** entry:

```text
.*
```

Assign this rule **only** to the `Kids-Allow-Only` group.

> ⚠️ **Never assign `.*` to the `Default` group by mistake.**  
> Otherwise, you will effectively block the entire internet for every device using that group.

### 7. Update Gravity

Refresh Pi-hole's lists after making the changes.

Using the Pi-hole web interface or from the terminal:

```bash
pihole updateGravity
```

### 8. Test the setup

On the child device, test:

- a domain from the allowlist → **must work**
- a domain that is not allowed → **must be blocked**

Use the **Query Log** to see which domains were allowed or blocked.

### 9. If an allowed website does not work completely

Many websites require additional domains for images, video, login, APIs, or CDNs.

If an allowed website does not load correctly:

1. Open the website.
2. Watch the Pi-hole **Query Log**.
3. Check which required domains are being blocked.
4. Allow only domains that are clearly necessary.
5. Add those domains to the appropriate Kids list or runtime allowlist.

> Do not broadly allow complete CDN or cloud zones. Doing so can weaken the Allow Only model.

### 10. Prevent bypassing

Kids Allow Only only works reliably if the device **actually uses Pi-hole as its DNS resolver**.

For more tightly controlled child devices, also consider:

- blocking external DNS at the router/firewall
- restricting DoH / DoT / Private DNS
- restricting VPN / proxy bypass methods
- covering both IPv4 **and** IPv6

DNS filtering alone is not a complete replacement for firewall, device-management, or parental-control policies.

### Pi-hole v5

Direct subscription to external **allowlists** was introduced with **Pi-hole v6**.  
With Pi-hole v5, allowed domains must be added individually or imported using a separate mechanism.

</details>

<p align="right"><a href="#kinderschutz-navigation">⬆️ Family table of contents</a></p>

---
# 🧱 Part 3 – Blocklist Catalog

---

<a id="security"></a>
### 🛡️ Security & Threat Intelligence

> 🚫 **Full domain blocking:** Malware, phishing, ransomware, C2, scam and other security targets should not be reachable.


#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 10,960 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/light.txt) |
| 🟦 **Normal** | 17,081 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/normal.txt) |
| 🟨 **Pro** | 594,410 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/pro.txt) |
| 🟧 **Pro++** | 844,669 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/pro-plus.txt) |
| 🟥 **Ultimate** | 3,408,596 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/ultimate.txt) |

#### Full / Special Lists

<details>
<summary><strong>📂 Show full/special lists</strong></summary>

| List | Entries | Status | Full List |
| --- | ---: | :---: | --- |
| **Abuse** | 116,920 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/abuse.txt) |
| **Brand Impersonation** | 53,975 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/brand-impersonation.txt) |
| **Command Control** | 53 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/command-control.txt) |
| **Cryptocurrency** | 63 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/cryptocurrency.txt) |
| **Cryptomining** | 6,121 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/cryptomining.txt) |
| **Data Exfiltration** | 13 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/data-exfiltration.txt) |
| **Ddos** | 15 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/ddos.txt) |
| **Disposable Email** | 30 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/disposable-email.txt) |
| **Dns Security** | 386 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/dns-security.txt) |
| **Dynamic Dns** | 74 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/dynamic-dns.txt) |
| **Expired Domains** | 0 | 🟡 | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/expired-domains.txt) |
| **Exploits** | 38 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/exploits.txt) |
| **Badware Hosters** | 24 | ✅⚠️ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/badware-hosters.txt) |
| **Fake Shops** | 10,960 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/fake-shops.txt) |
| **Fake Software** | 229 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/fake-software.txt) |
| **Malicious Extensions** | 0 | 🟡 | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/malicious-extensions.txt) |
| **Malicious Redirects** | 83 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/malicious-redirects.txt) |
| **Malvertising** | 51,883 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/malvertising.txt) |
| **Malware** | 2,656,377 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/malware.txt) |
| **Newly Registered Domains** | 15,000 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/newly-registered-domains.txt) |
| **Nft** | 1,758 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/nft.txt) |
| **Parked Domains** | 25 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/parked-domains.txt) |
| **Phishing** | 577,332 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/phishing.txt) |
| **Pup Pua** | 33 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/pup-pua.txt) |
| **Ransomware** | 53 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/ransomware.txt) |
| **Remote Access** | 23 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/remote-access.txt) |
| **Scam** | 265,246 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/scam.txt) |
| **Scanners** | 143 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/scanners.txt) |
| **Spam** | 32 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/spam.txt) |
| **Surveillance** | 16 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/surveillance.txt) |
| **Suspicious Tlds** | 6,490 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/suspicious-tlds.txt) |
| **Typosquatting** | 53,975 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/typosquatting.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="network"></a>
### 🔐 DNS, Network & Bypass Control

> 🚫 **Network Control:** Listd DoH/DoT/VPN/proxy/Tor/DDNS/bypass endpoints should deliberately not be reachable.


#### Main Lists

| Profile | Entries | Protection | Risk | List |
| --- | ---: | --- | :---: | --- |
| 🟩 **Light** | 31 | conservative | Minimal | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/light.txt) |
| 🟦 **Normal** | 49 | balanced | Low | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/normal.txt) |
| 🟨 **Pro** | 66 | privacy | Low–Medium | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/pro.txt) |
| 🟧 **Pro++** | 311 | aggressive | Medium | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/pro-plus.txt) |
| 🟥 **Ultimate** | 947 | maximum | High | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/ultimate.txt) |

#### Full / Special Lists

<details>
<summary><strong>📂 Show full/special lists</strong></summary>

| List | Entries | Status | Full List |
| --- | ---: | :---: | --- |
| **Adblock Bypass** | 88 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/adblock-bypass.txt) |
| **Dns Attacks** | 9 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/dns-attacks.txt) |
| **Dns Bypass** | 314 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/dns-bypass.txt) |
| **Doh** | 3 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/doh.txt) |
| **Dot** | 99 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/dot.txt) |
| **Dynamic Dns** | 74 | ✅⚠️ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/dynamic-dns.txt) |
| **Private Dns** | 102 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/private-dns.txt) |
| **Proxy** | 142 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/proxy.txt) |
| **Tor** | 7 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/tor.txt) |
| **Url Shorteners** | 255 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/url-shorteners.txt) |
| **Vpn** | 63 | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/vpn.txt) |
| **SafeSearch not supported** | 205 | ✅⚠️ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/safesearch-not-supported.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="speziallisten"></a>
### 🧰 Special Lists

These lists are **optional add-on modules** and do not replace the normal Light/Normal/Pro/Pro++/Ultimate profiles. Test especially aggressivee special lists in a test group first.

> **⚠️ Note:** `Dynamic DNS`, `Badware Hosters`, `Most Abused TLDs`, `SafeSearch not supported` and bypass lists can significantly restrict legitimate services. `Most Abused TLDs` deliberately uses **Adblock syntax** and is not a normal plain-domain list.

| Special List | Entries | Purpose | List |
| --- | ---: | --- | --- |
| **Fake / Scam / Trap Sites** | 265,318 | Scam + fake shops + fake software in one list | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/special/fake.txt) |
| **Pop-Up Ads** | 512 | Pop-up/pop-under ad networks from BRZ Ads | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/pop-up-ads.txt) |
| **Threat Intelligence Mini** | 594,410 | compact BRZ TI tier | [Mini](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/threat-intelligence/mini.txt) |
| **Threat Intelligence Medium** | 844,669 | medium BRZ TI tier | [Medium](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/threat-intelligence/medium.txt) |
| **Threat Intelligence Full** | 3,408,596 | complete BRZ Security Ultimate dataset as a standalone list | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/threat-intelligence/full.txt) |
| **Dynamic DNS** | 74 | known DynDNS providers; very aggressivee | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/dynamic-dns.txt) |
| **Badware Hoster** | 24 | risky hosting/site-builder roots with a high malware concentration | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/badware-hosters.txt) |
| **Most Abused TLDs** | **130** | entire risky TLDs/suffixes; Adblock format | [Adblock](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/policies/adblock/most-abused-tlds.adblock) |
| **DNS Rebind Protection** | – | resolver policy instead of a normal domain list | [dnsmasq Policy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/policies/dnsmasq/rebind.conf) |
| **DoH/VPN/Tor/Proxy Bypass** | 314 | combined local bypass list | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/special/doh-vpn-tor-proxy-bypass.txt) |
| **Encrypted DNS Only** | 102 | DoH + DoT + Private DNS | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/special/encrypted-dns-only.txt) |
| **SafeSearch not supported** | 205 | search engines without SafeSearch support | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/safesearch-not-supported.txt) |
| **URL Shortener** | 255 | known URL-shortening services | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/url-shorteners.txt) |
| **Anti Piracy** | 58 | piracy/illegal streaming | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/piracy.txt) |
| **Gambling Full** | 420,536 | complete BRZ gambling dataset | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/gambling.txt) |
| **Social Networks** | 47 | combined social-network list | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/special/social-networks.txt) |
| **NSFW** | 998,924 | Adult/NSFW special list | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/nsfw.txt) |
| **Native Tracker** | 587 | integrated trackers from operating systems, apps and devices | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/native-tracking.txt) |

#### Manually Updatable Live Variants

For very large or rapidly changing lists (e.g. **NRD/DGA, TIF IP addresses, DoH IP addresses, Anti-Piracy, Gambling Medium/Mini**), there is deliberately **no automatic GitHub workflow**. The sources are stored in `config/special-upstreams.json` and can be updated manually when needed:

```bash
python3 scripts/update-special-lists.py --list
python3 scripts/update-special-lists.py hagezi_anti_piracy hagezi_gambling_medium hagezi_gambling_mini
```

The updater writes only the explicitly selected files. Details: [`docs/SPECIAL_LISTS.md`](docs/SPECIAL_LISTS.md).

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="regional"></a>
### 🌍 Regional Lists

The paths are prepared. They are not artificially populated using the pattern “TLD = region”, because that would be technically unreliable.

| List | Entries | Status | Link |
| --- | ---: | :---: | --- |
| **Cn** | 5,896 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/cn.txt) |
| **De** | 3,304 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/de.txt) |
| **Es** | 1,698 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/es.txt) |
| **Eu** | 31,996 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/eu.txt) |
| **Fr** | 2,123 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/fr.txt) |
| **It** | 2,307 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/it.txt) |
| **Jp** | 625 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/jp.txt) |
| **Kr** | 479 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/kr.txt) |
| **Ru** | 15,374 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/ru.txt) |
| **Uk** | 7,416 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/uk.txt) |
| **Us** | 6,302 | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/us.txt) |


---
<a id="lizenz"></a>
## 📜 Sources & License

The repository is licensed under **GPL-3.0-only**. The domain base comes from the static BlackRabbitZ snapshot and its documented sources, including Block List Project, AnudeepND, NextDNS Native Tracking Protection, Perflyst, URLhaus, Phishing.Database and HaGeZi-derived data.

HaGeZi is additionally used as a reference for cumulative main levels and separate native/special lists. There is **no automatic live synchronization**.

See [`THIRD_PARTY.md`](THIRD_PARTY.md), [`docs/SOURCES.md`](docs/SOURCES.md) and the `# Sources:` headers in the lists.

<p align="right"><a href="#top">⬆️ Back to top</a></p>

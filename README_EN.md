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

| Profile | Blocking | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **234,013** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/light.txt) |
| 🟦 **Normal** | balanced | Low | **342,238** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **370,387** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **382,467** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **5,118,112** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/ultimate.txt) |


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

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **31,392** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **55,932** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **83,565** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **344,214** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **348,192** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/ultimate.txt) |

> **Privacy & Tracking – Ultimate:** This level contains the union of all full/special lists in the **Privacy & Tracking** area. Lower levels are cumulative, risk-based subsets.

#### Full / Special Lists

<details>
<summary><strong>📂 Show full/special lists</strong></summary>

| List | Entries | Status | Full List |
|---|---:|:---:|---|
| **Ads (Advertising)** | **218,123** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/ads.txt) |
| **Pop-Up Ads** | **512** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/pop-up-ads.txt) |
| **Affiliate Tracking** | **608** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/affiliate-tracking.txt) |
| **Aggressive Privacy** | **652** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/aggressivee-privacy.txt) |
| **Analytics** | **34,728** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/analytics.txt) |
| **Captcha Antibot** | **378** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/captcha-antibot.txt) |
| **Cdn Tracking** | **19** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/cdn-tracking.txt) |
| **Chat Support** | **49** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/chat-support.txt) |
| **Consent Cmp** | **41** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/consent-cmp.txt) |
| **Crash Reporting** | **85** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/crash-reporting.txt) |
| **Crm** | **106** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/crm.txt) |
| **Ecommerce** | **42** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/ecommerce.txt) |
| **External Fonts** | **3** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/external-fonts.txt) |
| **Fingerprinting** | **10** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/fingerprinting.txt) |
| **Marketing** | **2,004** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/marketing.txt) |
| **Mobile Tracking** | **208** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/mobile-tracking.txt) |
| **Native Tracking** | **587** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/native-tracking.txt) |
| **Newsletter Tracking** | **156** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/newsletter-tracking.txt) |
| **Payment Tracking** | **17** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/payment-tracking.txt) |
| **Push Notifications** | **73** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/push-notifications.txt) |
| **Recommendations** | **360** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/recommendations.txt) |
| **Search Tracking** | **1** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/search-tracking.txt) |
| **Seo Tracking** | **115** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/seo-tracking.txt) |
| **Session Replay** | **195** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/session-replay.txt) |
| **Social Tracking** | **29** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/social-tracking.txt) |
| **Telemetry** | **27,984** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/telemetry.txt) |
| **Trackers** | **106,915** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/trackers.txt) |
| **Tracking Pixels** | **866** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/tracking-pixels.txt) |
| **Tracking Redirects** | **306** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/tracking-redirects.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="software-hardware"></a>
### 🧩 Software & Hardware Telemetry

#### Main Lists

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **73** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **73** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **78** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **78** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **83** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/ultimate.txt) |

<details>
<summary><strong>📂 Show vendor behavior lists</strong></summary>


| Device / Vendor | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
|---|---|---|---|---|
| **Adobe** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/adobe/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/adobe/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/adobe/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/adobe/updates.txt) |
| **AMD** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/amd/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/amd/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/amd/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/amd/updates.txt) |
| **Autodesk** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/autodesk/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/autodesk/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/autodesk/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/autodesk/updates.txt) |
| **Corsair** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/corsair/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/corsair/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/corsair/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/corsair/updates.txt) |
| **Intel** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/intel/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/intel/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/intel/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/intel/updates.txt) |
| **Logitech** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/logitech/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/logitech/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/logitech/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/logitech/updates.txt) |
| **Nvidia** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/nvidia/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/nvidia/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/nvidia/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/nvidia/updates.txt) |
| **Razer** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/razer/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/razer/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/razer/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/software-hardware/razer/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="automation"></a>
### 🤖 AI, Bots & Crawlers

#### Main Lists

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **13** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **28** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **33** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **50** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **301** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/ultimate.txt) |

#### Full / Special Lists

<details>
<summary><strong>📂 Show full/special lists</strong></summary>

| List | Entries | Status | Full List |
|---|---:|:---:|---|
| **Aggressive Crawlers** | **15** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/aggressivee-crawlers.txt) |
| **Ai Crawlers** | **10** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/ai-crawlers.txt) |
| **Ai Scrapers** | **3** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/ai-scrapers.txt) |
| **Ai Telemetry** | **36** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/ai-telemetry.txt) |
| **Ai Tracking** | **44** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/ai-tracking.txt) |
| **Llm Crawlers** | **188** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/llm-crawlers.txt) |
| **Malicious Bots** | **1** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/malicious-bots.txt) |
| **Seo Bots** | **5** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/seo-bots.txt) |
| **Training Bots** | **6** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/training-bots.txt) |
| **Web Crawlers** | **62** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/web-crawlers.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>


---
<a id="devices-group"></a>
## 🔌 Devices & Vendors — Privacy / Restrict / Isolate

Devices and vendors use separate behavior levels: **Privacy** for tracking/telemetry, **Restrict** for additional optional vendor services, and **Isolate** for as much vendor communication as possible.

<a id="smart-tv"></a>
### 📺 Smart TV

#### Main Lists

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **344** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **359** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **451** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **622** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **634** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
|---|---|---|---|---|
| **Amazon Fire TV** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/amazon-fire-tv/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/amazon-fire-tv/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/amazon-fire-tv/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/amazon-fire-tv/updates.txt) |
| **Google Android TV** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/google-android-tv/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/google-android-tv/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/google-android-tv/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/google-android-tv/updates.txt) |
| **Google TV** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/google-tv/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/google-tv/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/google-tv/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/google-tv/updates.txt) |
| **Hisense VIDAA** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/hisense-vidaa/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/hisense-vidaa/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/hisense-vidaa/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/hisense-vidaa/updates.txt) |
| **LG webOS** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/lg-webos/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/lg-webos/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/lg-webos/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/lg-webos/updates.txt) |
| **Panasonic** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/panasonic/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/panasonic/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/panasonic/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/panasonic/updates.txt) |
| **Philips** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/philips/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/philips/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/philips/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/philips/updates.txt) |
| **Roku** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/roku/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/roku/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/roku/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/roku/updates.txt) |
| **Samsung** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/samsung/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/samsung/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/samsung/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/samsung/updates.txt) |
| **Shared / Other** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/shared-other/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/shared-other/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/shared-other/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/shared-other/updates.txt) |
| **Sony Bravia** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/sony-bravia/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/sony-bravia/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/sony-bravia/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/sony-bravia/updates.txt) |
| **TCL** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/tcl/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/tcl/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/tcl/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/smart-tv/tcl/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="mobile"></a>
### 📱 Smartphones & Mobile

#### Main Lists

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **391** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **442** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **518** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **939** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **945** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
|---|---|---|---|---|
| **Apple iOS** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/apple-ios/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/apple-ios/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/apple-ios/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/apple-ios/updates.txt) |
| **Google Android** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/google-android/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/google-android/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/google-android/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/google-android/updates.txt) |
| **Google Pixel** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/google-pixel/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/google-pixel/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/google-pixel/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/google-pixel/updates.txt) |
| **Huawei** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/huawei/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/huawei/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/huawei/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/huawei/updates.txt) |
| **Motorola** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/motorola/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/motorola/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/motorola/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/motorola/updates.txt) |
| **Oneplus** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/oneplus/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/oneplus/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/oneplus/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/oneplus/updates.txt) |
| **Oppo / Realme** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/oppo-realme/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/oppo-realme/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/oppo-realme/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/oppo-realme/updates.txt) |
| **Samsung** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/samsung/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/samsung/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/samsung/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/samsung/updates.txt) |
| **Shared / Other** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/shared-other/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/shared-other/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/shared-other/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/shared-other/updates.txt) |
| **Vivo** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/vivo/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/vivo/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/vivo/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/vivo/updates.txt) |
| **Xiaomi** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/xiaomi/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/xiaomi/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/xiaomi/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/mobile/xiaomi/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="betriebssysteme"></a>
### 💻 Operating Systems

#### Main Lists

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **20** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **45** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **89** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **244** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **249** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
|---|---|---|---|---|
| **Android** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/android/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/android/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/android/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/android/updates.txt) |
| **Apple** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/apple/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/apple/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/apple/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/apple/updates.txt) |
| **Chromeos** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/chromeos/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/chromeos/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/chromeos/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/chromeos/updates.txt) |
| **Ios** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/ios/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/ios/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/ios/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/ios/updates.txt) |
| **Linux** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/linux/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/linux/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/linux/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/linux/updates.txt) |
| **Macos** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/macos/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/macos/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/macos/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/macos/updates.txt) |
| **Windows** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/windows/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/windows/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/windows/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/windows/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="iot"></a>
### 🏠 IoT & Smart Home

#### Main Lists

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **2** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **11** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **26** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **79** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **82** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
|---|---|---|---|---|
| **Amazon Alexa** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/amazon-alexa/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/amazon-alexa/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/amazon-alexa/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/amazon-alexa/updates.txt) |
| **Huawei** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/huawei/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/huawei/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/huawei/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/huawei/updates.txt) |
| **Samsung SmartThings** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/samsung-smartthings/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/samsung-smartthings/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/samsung-smartthings/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/samsung-smartthings/updates.txt) |
| **Shared / Other** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/shared-other/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/shared-other/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/shared-other/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/shared-other/updates.txt) |
| **Sonos** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/sonos/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/sonos/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/sonos/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/sonos/updates.txt) |
| **Xiaomi** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/xiaomi/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/xiaomi/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/xiaomi/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/xiaomi/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="voice"></a>
### 🎙️ Voice Assistants

#### Main Lists

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **7** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **16** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **37** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **103** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **108** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
|---|---|---|---|---|
| **Alexa** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/alexa/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/alexa/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/alexa/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/alexa/updates.txt) |
| **Cortana** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/cortana/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/cortana/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/cortana/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/cortana/updates.txt) |
| **Google Assistant** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/google-assistant/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/google-assistant/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/google-assistant/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/google-assistant/updates.txt) |
| **Siri** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/siri/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/siri/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/siri/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/siri/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="automotive"></a>
### 🚗 Automotive / Connected Cars

#### Main Lists

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **42** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **102** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **177** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **617** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **619** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
|---|---|---|---|---|
| **Audi** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/audi/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/audi/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/audi/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/audi/updates.txt) |
| **Bmw** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/bmw/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/bmw/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/bmw/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/bmw/updates.txt) |
| **Ford** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/ford/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/ford/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/ford/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/ford/updates.txt) |
| **Mercedes** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/mercedes/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/mercedes/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/mercedes/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/mercedes/updates.txt) |
| **Tesla** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/tesla/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/tesla/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/tesla/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/tesla/updates.txt) |
| **VW** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/vw/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/vw/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/vw/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/vw/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="nas-server"></a>
### 💾 NAS & Server

#### Main Lists

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **1** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **3** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **11** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **53** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **55** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
|---|---|---|---|---|
| **Docker** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/docker/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/docker/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/docker/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/docker/updates.txt) |
| **HPE / Dell** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/hpe-dell/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/hpe-dell/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/hpe-dell/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/hpe-dell/updates.txt) |
| **Kubernetes** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/kubernetes/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/kubernetes/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/kubernetes/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/kubernetes/updates.txt) |
| **QNAP** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/qnap/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/qnap/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/qnap/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/qnap/updates.txt) |
| **Red Hat / OpenShift** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/redhat-openshift/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/redhat-openshift/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/redhat-openshift/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/redhat-openshift/updates.txt) |
| **Synology** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/synology/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/synology/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/synology/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/synology/updates.txt) |
| **Truenas** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/truenas/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/truenas/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/truenas/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/truenas/updates.txt) |
| **Unraid** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/unraid/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/unraid/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/unraid/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/nas-server/unraid/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="network-devices"></a>
### 🌐 Routers & Network Devices

#### Main Lists

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **11** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **48** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **73** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **370** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **396** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
|---|---|---|---|---|
| **Asus** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/asus/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/asus/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/asus/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/asus/updates.txt) |
| **AVM / FRITZ!Box** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/avm-fritzbox/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/avm-fritzbox/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/avm-fritzbox/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/avm-fritzbox/updates.txt) |
| **Cisco** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/cisco/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/cisco/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/cisco/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/cisco/updates.txt) |
| **Huawei** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/huawei/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/huawei/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/huawei/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/huawei/updates.txt) |
| **Mikrotik** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/mikrotik/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/mikrotik/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/mikrotik/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/mikrotik/updates.txt) |
| **Netgear** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/netgear/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/netgear/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/netgear/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/netgear/updates.txt) |
| **TP-Link** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/tp-link/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/tp-link/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/tp-link/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/tp-link/updates.txt) |
| **Ubiquiti** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/ubiquiti/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/ubiquiti/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/ubiquiti/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/ubiquiti/updates.txt) |
| **Zyxel** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/zyxel/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/zyxel/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/zyxel/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/network-devices/zyxel/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="providers"></a>
### 📡 ISP / Providers

#### Main Lists

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **5** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **39** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **71** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **166** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **166** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
|---|---|---|---|---|
| **1&1** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/1und1/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/1und1/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/1und1/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/1und1/updates.txt) |
| **Deutsche Glasfaser** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/deutsche-glasfaser/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/deutsche-glasfaser/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/deutsche-glasfaser/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/deutsche-glasfaser/updates.txt) |
| **O2** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/o2/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/o2/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/o2/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/o2/updates.txt) |
| **Telekom** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/telekom/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/telekom/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/telekom/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/telekom/updates.txt) |
| **Unitymedia** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/unitymedia/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/unitymedia/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/unitymedia/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/unitymedia/updates.txt) |
| **Vodafone** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/vodafone/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/vodafone/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/vodafone/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/vodafone/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="ecosystems"></a>
### 🏢 Google, Microsoft, Apple & Amazon

#### Main Lists

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **11,912** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **12,074** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **12,357** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **15,410** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **15,462** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** tracking/ads/analytics/telemetry/diagnostics only  
> ⚠️ **Restrict:** Privacy + optional vendor/cloud/recommendation services  
> 🚫 **Isolate:** as much vendor communication as possible  
> 🔄 **Updates:** update infrastructure can be controlled separately

| Device / Vendor | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
|---|---|---|---|---|
| **Amazon** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/amazon/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/amazon/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/amazon/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/amazon/updates.txt) |
| **Apple** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/apple/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/apple/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/apple/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/apple/updates.txt) |
| **Google** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/google/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/google/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/google/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/google/updates.txt) |
| **Microsoft** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/microsoft/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/microsoft/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/microsoft/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/microsoft/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="manufacturers"></a>
### 🏭 Vendor Lists

This overview shows the concrete behavior lists for **every vendor currently present**.

| Device / Vendor | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
|---|---|---|---|---|
| **Adobe** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/adobe/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/adobe/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/adobe/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/adobe/updates.txt) |
| **Amazon** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/amazon/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/amazon/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/amazon/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/amazon/updates.txt) |
| **AMD** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/amd/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/amd/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/amd/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/amd/updates.txt) |
| **Apple** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/apple/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/apple/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/apple/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/apple/updates.txt) |
| **Autodesk** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/autodesk/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/autodesk/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/autodesk/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/autodesk/updates.txt) |
| **Ea** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/ea/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/ea/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/ea/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/ea/updates.txt) |
| **Epic** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/epic/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/epic/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/epic/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/epic/updates.txt) |
| **Google** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/google/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/google/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/google/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/google/updates.txt) |
| **Huawei** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/huawei/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/huawei/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/huawei/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/huawei/updates.txt) |
| **LG** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/lg/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/lg/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/lg/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/lg/updates.txt) |
| **Logitech** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/logitech/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/logitech/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/logitech/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/logitech/updates.txt) |
| **Meta** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/meta/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/meta/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/meta/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/meta/updates.txt) |
| **Microsoft** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/microsoft/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/microsoft/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/microsoft/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/microsoft/updates.txt) |
| **Nintendo** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/nintendo/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/nintendo/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/nintendo/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/nintendo/updates.txt) |
| **Nvidia** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/nvidia/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/nvidia/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/nvidia/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/nvidia/updates.txt) |
| **Philips** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/philips/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/philips/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/philips/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/philips/updates.txt) |
| **Razer** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/razer/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/razer/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/razer/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/razer/updates.txt) |
| **Samsung** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/samsung/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/samsung/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/samsung/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/samsung/updates.txt) |
| **Sony** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/sony/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/sony/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/sony/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/sony/updates.txt) |
| **Ubisoft** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/ubisoft/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/ubisoft/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/ubisoft/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/ubisoft/updates.txt) |
| **Valve / Steam** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/valve-steam/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/valve-steam/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/valve-steam/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/valve-steam/updates.txt) |
| **Xiaomi** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/xiaomi/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/xiaomi/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/xiaomi/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/manufacturers/xiaomi/updates.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>


---
<a id="apps-group"></a>
## 📱 Apps & Services — Privacy / Block All

For apps and services, **Privacy** and **Block All** are separate. Privacy reduces tracking/analytics/telemetry; Block All is intended to completely block the service.

<a id="streaming"></a>
### 📺 Streaming

#### Main Lists

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **7** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **13** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **27** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **39** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **44** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** the service should continue to work; tracking/analytics/telemetry are reduced.  
> 🚫 **Block All:** the service should be completely blocked.

| App / Service | 🛡️ Privacy | 🚫 Block All |
|---|---|---|
| **Apple TV** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/apple-tv/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/apple-tv/block-all.txt) |
| **Dazn** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/dazn/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/dazn/block-all.txt) |
| **Disney+** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/disney-plus/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/disney-plus/block-all.txt) |
| **Emby** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/emby/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/emby/block-all.txt) |
| **Jellyfin** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/jellyfin/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/jellyfin/block-all.txt) |
| **Netflix** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/netflix/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/netflix/block-all.txt) |
| **Paramount** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/paramount/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/paramount/block-all.txt) |
| **Plex** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/plex/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/plex/block-all.txt) |
| **Prime Video** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/prime-video/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/prime-video/block-all.txt) |
| **Spotify** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/spotify/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/spotify/block-all.txt) |
| **Twitch** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/twitch/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/twitch/block-all.txt) |
| **Youtube** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/youtube/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/streaming/youtube/block-all.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="gaming"></a>
### 🎮 Gaming

#### Main Lists

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **2** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **30** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **42** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **46** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **50** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/ultimate.txt) |

<details>
<summary><strong>📂 Show platform behavior lists</strong></summary>


| App / Service | 🛡️ Privacy | 🚫 Block All |
|---|---|---|
| **Battle.net** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/battle-net/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/battle-net/block-all.txt) |
| **EA / Origin** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/ea-origin/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/ea-origin/block-all.txt) |
| **Epic Games** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/epic-games/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/epic-games/block-all.txt) |
| **Mobile Games** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/mobile-games/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/mobile-games/block-all.txt) |
| **Nintendo** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/nintendo/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/nintendo/block-all.txt) |
| **Playstation** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/playstation/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/playstation/block-all.txt) |
| **Riot Games** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/riot-games/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/riot-games/block-all.txt) |
| **Rockstar** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/rockstar/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/rockstar/block-all.txt) |
| **Steam** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/steam/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/steam/block-all.txt) |
| **Ubisoft** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/ubisoft/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/ubisoft/block-all.txt) |
| **Xbox** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/xbox/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/xbox/block-all.txt) |

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

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **14** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **26** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **30** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **47** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **47** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** the service should continue to work; tracking/analytics/telemetry are reduced.  
> 🚫 **Block All:** the service should be completely blocked.

| App / Service | 🛡️ Privacy | 🚫 Block All |
|---|---|---|
| **Discord** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/discord/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/discord/block-all.txt) |
| **Facebook / Meta** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/facebook-meta/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/facebook-meta/block-all.txt) |
| **Instagram** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/instagram/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/instagram/block-all.txt) |
| **Linkedin** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/linkedin/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/linkedin/block-all.txt) |
| **Pinterest** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/pinterest/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/pinterest/block-all.txt) |
| **Reddit** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/reddit/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/reddit/block-all.txt) |
| **Snapchat** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/snapchat/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/snapchat/block-all.txt) |
| **Telegram** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/telegram/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/telegram/block-all.txt) |
| **Threads** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/threads/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/threads/block-all.txt) |
| **Tiktok** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/tiktok/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/tiktok/block-all.txt) |
| **Whatsapp** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/whatsapp/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/whatsapp/block-all.txt) |
| **X / Twitter** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/x-twitter/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/social-media/x-twitter/block-all.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="cloud-dev"></a>
### ☁️ Cloud, Server & Development

#### Main Lists

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **65** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **165** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **301** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **1,486** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **1,491** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/ultimate.txt) |

<details>
<summary><strong>📂 Show behavior lists</strong></summary>


> 🛡️ **Privacy:** the service should continue to work; tracking/analytics/telemetry are reduced.  
> 🚫 **Block All:** the service should be completely blocked.

| App / Service | 🛡️ Privacy | 🚫 Block All |
|---|---|---|
| **AWS** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/aws/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/aws/block-all.txt) |
| **Azure** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/azure/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/azure/block-all.txt) |
| **Cicd** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/cicd/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/cicd/block-all.txt) |
| **Cloud Storage** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/cloud-storage/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/cloud-storage/block-all.txt) |
| **Cloudflare** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/cloudflare/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/cloudflare/block-all.txt) |
| **Github** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/github/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/github/block-all.txt) |
| **Gitlab** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/gitlab/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/gitlab/block-all.txt) |
| **Google Cloud** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/google-cloud/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/google-cloud/block-all.txt) |
| **Jetbrains** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/jetbrains/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/jetbrains/block-all.txt) |
| **Oracle Cloud** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/oracle-cloud/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/oracle-cloud/block-all.txt) |
| **Visual Studio** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/visual-studio/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/visual-studio/block-all.txt) |
| **VS Code** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/vscode/privacy.txt) | [Block All](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/cloud-development/vscode/block-all.txt) |

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

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **998,924** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **1,419,159** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **1,430,117** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **1,769,650** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **2,347,190** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/ultimate.txt) |

#### Full Content Lists

<details>
<summary><strong>📂 Show content lists</strong></summary>

| List | Entries | Status | Link |
|---|---:|:---:|---|
| **Adult** | **998,924** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/adult.txt) |
| **Dating** | **40** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/dating.txt) |
| **Drugs** | **55** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/drugs.txt) |
| **Gambling** | **420,536** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/gambling.txt) |
| **Misinformation** | **0** | 🟡 | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/misinformation.txt) |
| **Piracy** | **58** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/piracy.txt) |
| **Sexual Content** | **998,924** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/sexual-content.txt) |
| **Torrents** | **44** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/torrents.txt) |
| **Violence Gore** | **53** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/violence-gore.txt) |
| **Weapons** | **89** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/weapons.txt) |

> `Misinformation` deliberately remains optional and is not automatically treated as an objective security category.

</details>

<p align="right"><a href="#kinderschutz-navigation">⬆️ Family table of contents</a></p>

---

<a id="kids-allow-only"></a>
### 🧒 Kids Allow-Only

`Kids Allow-Only` is not a normal denylist profile. In a dedicated Pi-hole group, everything is blocked by default; only explicitly allowed domains work.

<a id="kids-dateien"></a>
#### 📚 Kids Allowlist Files

| Datei | Purpose | Entries | List |
|---|---|---:|---|
| `kids-de.txt` | Basis-Allowlist | **39** | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-de.txt) |
| `kids-education-de.txt` | Learning, school, STEM, history | **17** | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-education-de.txt) |
| `kids-media-de.txt` | Children's TV, audio, news | **16** | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-media-de.txt) |
| `kids-games-de.txt` | verified children's games | **18** | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-games-de.txt) |
| `kids-runtime-de.txt` | required technical hosts | **9** | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-runtime-de.txt) |


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

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **10,960** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **17,081** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **594,410** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **844,669** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **3,408,596** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/ultimate.txt) |

#### Full / Special Lists

<details>
<summary><strong>📂 Show full/special lists</strong></summary>

| List | Entries | Status | Full List |
|---|---:|:---:|---|
| **Abuse** | **116,920** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/abuse.txt) |
| **Brand Impersonation** | **53,975** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/brand-impersonation.txt) |
| **Command Control** | **53** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/command-control.txt) |
| **Cryptocurrency** | **63** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/cryptocurrency.txt) |
| **Cryptomining** | **6,121** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/cryptomining.txt) |
| **Data Exfiltration** | **13** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/data-exfiltration.txt) |
| **Ddos** | **15** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/ddos.txt) |
| **Disposable Email** | **30** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/disposable-email.txt) |
| **Dns Security** | **386** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/dns-security.txt) |
| **Dynamic Dns** | **74** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/dynamic-dns.txt) |
| **Expired Domains** | **0** | 🟡 | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/expired-domains.txt) |
| **Exploits** | **38** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/exploits.txt) |
| **Badware Hosters** | **24** | ✅⚠️ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/badware-hosters.txt) |
| **Fake Shops** | **10,960** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/fake-shops.txt) |
| **Fake Software** | **229** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/fake-software.txt) |
| **Malicious Extensions** | **0** | 🟡 | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/malicious-extensions.txt) |
| **Malicious Redirects** | **83** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/malicious-redirects.txt) |
| **Malvertising** | **51,883** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/malvertising.txt) |
| **Malware** | **2,656,377** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/malware.txt) |
| **Newly Registered Domains** | **15,000** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/newly-registered-domains.txt) |
| **Nft** | **1,758** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/nft.txt) |
| **Parked Domains** | **25** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/parked-domains.txt) |
| **Phishing** | **577,332** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/phishing.txt) |
| **Pup Pua** | **33** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/pup-pua.txt) |
| **Ransomware** | **53** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/ransomware.txt) |
| **Remote Access** | **23** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/remote-access.txt) |
| **Scam** | **265,246** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/scam.txt) |
| **Scanners** | **143** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/scanners.txt) |
| **Spam** | **32** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/spam.txt) |
| **Surveillance** | **16** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/surveillance.txt) |
| **Suspicious Tlds** | **6,490** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/suspicious-tlds.txt) |
| **Typosquatting** | **53,975** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/typosquatting.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="network"></a>
### 🔐 DNS, Network & Bypass Control

> 🚫 **Network Control:** Listd DoH/DoT/VPN/proxy/Tor/DDNS/bypass endpoints should deliberately not be reachable.


#### Main Lists

| Profile | Protection | Risk | Entries | List |
|---|---|:---:|---:|---|
| 🟩 **Light** | conservative | Minimal | **31** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/light.txt) |
| 🟦 **Normal** | balanced | Low | **49** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/normal.txt) |
| 🟨 **Pro** | privacy | Low–Medium | **66** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/pro.txt) |
| 🟧 **Pro++** | aggressive | Medium | **311** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximum | High | **947** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/ultimate.txt) |

#### Full / Special Lists

<details>
<summary><strong>📂 Show full/special lists</strong></summary>

| List | Entries | Status | Full List |
|---|---:|:---:|---|
| **Adblock Bypass** | **88** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/adblock-bypass.txt) |
| **Dns Attacks** | **9** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/dns-attacks.txt) |
| **Dns Bypass** | **314** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/dns-bypass.txt) |
| **Doh** | **3** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/doh.txt) |
| **Dot** | **99** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/dot.txt) |
| **Dynamic Dns** | **74** | ✅⚠️ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/dynamic-dns.txt) |
| **Private Dns** | **102** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/private-dns.txt) |
| **Proxy** | **142** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/proxy.txt) |
| **Tor** | **7** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/tor.txt) |
| **Url Shorteners** | **255** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/url-shorteners.txt) |
| **Vpn** | **63** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/vpn.txt) |
| **SafeSearch not supported** | **205** | ✅⚠️ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/safesearch-not-supported.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklist table of contents</a></p>

---

<a id="speziallisten"></a>
### 🧰 Special Lists

These lists are **optional add-on modules** and do not replace the normal Light/Normal/Pro/Pro++/Ultimate profiles. Test especially aggressivee special lists in a test group first.

> **⚠️ Note:** `Dynamic DNS`, `Badware Hosters`, `Most Abused TLDs`, `SafeSearch not supported` and bypass lists can significantly restrict legitimate services. `Most Abused TLDs` deliberately uses **Adblock syntax** and is not a normal plain-domain list.

| Special List | Purpose | Entries | List |
|---|---|---:|---|
| **Fake / Scam / Trap Sites** | Scam + fake shops + fake software in one list | **265,318** | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/special/fake.txt) |
| **Pop-Up Ads** | Pop-up/pop-under ad networks from BRZ Ads | **512** | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/pop-up-ads.txt) |
| **Threat Intelligence Mini** | compact BRZ TI tier | **594,410** | [Mini](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/threat-intelligence/mini.txt) |
| **Threat Intelligence Medium** | medium BRZ TI tier | **844,669** | [Medium](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/threat-intelligence/medium.txt) |
| **Threat Intelligence Full** | complete BRZ Security Ultimate dataset as a standalone list | **3,408,596** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/threat-intelligence/full.txt) |
| **Dynamic DNS** | known DynDNS providers; very aggressivee | **74** | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/dynamic-dns.txt) |
| **Badware Hoster** | risky hosting/site-builder roots with a high malware concentration | **24** | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/badware-hosters.txt) |
| **Most Abused TLDs** | entire risky TLDs/suffixes; Adblock format | **130** | [Adblock](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/policies/adblock/most-abused-tlds.adblock) |
| **DNS Rebind Protection** | resolver policy instead of a normal domain list | – | [dnsmasq Policy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/policies/dnsmasq/rebind.conf) |
| **DoH/VPN/Tor/Proxy Bypass** | combined local bypass list | **314** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/special/doh-vpn-tor-proxy-bypass.txt) |
| **Encrypted DNS Only** | DoH + DoT + Private DNS | **102** | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/special/encrypted-dns-only.txt) |
| **SafeSearch not supported** | search engines without SafeSearch support | **205** | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/safesearch-not-supported.txt) |
| **URL Shortener** | known URL-shortening services | **255** | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/url-shorteners.txt) |
| **Anti Piracy** | piracy/illegal streaming | current BRZ snapshot / optional upstream | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/piracy.txt) |
| **Gambling Full** | complete BRZ gambling dataset | **420,536** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/gambling.txt) |
| **Social Networks** | combined social-network list | **47** | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/special/social-networks.txt) |
| **NSFW** | Adult/NSFW special list | **998,924** | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/nsfw.txt) |
| **Native Tracker** | integrated trackers from operating systems, apps and devices | **587** | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/native-tracking.txt) |

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
|---|---:|:---:|---|
| **Cn** | **5,896** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/cn.txt) |
| **De** | **3,304** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/de.txt) |
| **Es** | **1,698** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/es.txt) |
| **Eu** | **31,996** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/eu.txt) |
| **Fr** | **2,123** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/fr.txt) |
| **It** | **2,307** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/it.txt) |
| **Jp** | **625** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/jp.txt) |
| **Kr** | **479** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/kr.txt) |
| **Ru** | **15,374** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/ru.txt) |
| **Uk** | **7,416** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/uk.txt) |
| **Us** | **6,302** | ✅ | [List](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/us.txt) |


---
<a id="lizenz"></a>
## 📜 Sources & License

The repository is licensed under **GPL-3.0-only**. The domain base comes from the static BlackRabbitZ snapshot and its documented sources, including Block List Project, AnudeepND, NextDNS Native Tracking Protection, Perflyst, URLhaus, Phishing.Database and HaGeZi-derived data.

HaGeZi is additionally used as a reference for cumulative main levels and separate native/special lists. There is **no automatic live synchronization**.

See [`THIRD_PARTY.md`](THIRD_PARTY.md), [`docs/SOURCES.md`](docs/SOURCES.md) and the `# Sources:` headers in the lists.

<p align="right"><a href="#top">⬆️ Back to top</a></p>

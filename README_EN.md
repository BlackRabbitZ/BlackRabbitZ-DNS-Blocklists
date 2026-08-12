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

<div align="center">

**🌐 Language / Sprache:** [🇩🇪 Deutsch](README.md) · 🇬🇧 **English**

</div>

<a id="why-dns-blocklists"></a>
## 🛡️ Why use DNS blocklists?

DNS blocklists stop unwanted connections during name resolution. This allows **ads, trackers, telemetry and known malicious domains to be filtered centrally for the whole network** without installing extra software on every device.

---

<a id="contents"></a>
## 📑 Table of Contents

- [Why DNS blocklists?](#why-dns-blocklists) — why network-wide DNS blocking is useful
- [Quick Start](#quick-start) — recommended default list and fast Pi-hole setup
- [Privacy Profiles](#protection-profiles) — Light, Balanced, Strict and Ultimate protection levels
- [Protection Comparison](#protection-comparison) — profile features and breakage risk
  - [Optional Protection Modules](#optional-protection-modules) — Security and Family as targeted add-ons
  - [Large Profile Parts](#large-profile-parts) — automatically generated Raw parts; up to 50 MiB per file going forward
- [Ads & Tracking](#ads-tracking) — ads, trackers, affiliate tracking and pop-up ads
- [Telemetry & Devices](#telemetry-devices) — OS, device, Smart-TV, IoT and native-tracker lists
- [Gaming Privacy](#gaming-privacy) — gaming telemetry and optional RegEx rules
- [Security Lists](#security-lists) — malware, phishing, scam, fake, threat intelligence, NRD/DGA, DynDNS, hoster and TLD protection
- [DNS, Web & Bypass Protection](#dns-web-protection) — DoH/VPN/TOR/proxy bypass, URL shorteners and DNS rebind protection
- [Family Lists](#family-lists) — Adult/NSFW, gambling, SafeSearch, anti-piracy and social-network blocking
- [Recommendations](#recommendations) — sensible profile and add-on combinations
- [Online DNS Services](#online-dns-services) — guidance for external DNS providers and mobile use
- [Upstream Sources & Build Transparency](#upstream-sources) — sources, archive snapshots, metadata and checksums
- [Repository Structure](#repository-structure) — folders, configs, scripts and generated lists
- [Automatic List Updates](#automatic-updates) — daily feeds and the extended-list builder
- [Extending Lists](#extending-lists) — add categories, profiles and extended lists
- [False Positives](#false-positives) — report false blocks and use the allowlist
- [License & Attribution](#license-attribution) — GPL-3.0, third-party sources and attribution

---

<a id="quick-start"></a>
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

<a id="protection-profiles"></a>
# 🚀 Privacy Protection Profiles

These are the main protection levels. Start with **Balanced** and move to **Strict** or **Ultimate** only when you intentionally want more aggressive privacy filtering.

<!-- MAIN_PROFILES_START -->
| Profile | Protection | Entries | Recommended for | View | Raw |
|---|:---:|---:|---|:---:|:---:|
| 🟢 **Light** | Low | **235,630** | Basic ad blocking | [View](lists/combined/light.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/light.txt)** |
| 🔵 **Balanced ⭐** | Medium | **373,134** | Most users | [View](lists/combined/balanced.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/balanced.txt)** |
| 🟠 **Strict** | High | **374,914** | Privacy-focused setups | [View](lists/combined/strict.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/strict.txt)** |
| 🔴 **Ultimate** | Maximum | **5,212,373** | Aggressive filtering | [Show Parts](#ultimate-parts) | **[Raw Parts](#ultimate-parts)** |
<!-- MAIN_PROFILES_END -->

> **Balanced** is recommended for most installations.
> **Strict** adds affiliate tracking, telemetry, device telemetry and native/app tracking.
> **Ultimate** is intentionally aggressive and can affect telemetry-dependent features, Smart-TV functions, app analytics, gaming telemetry and cloud-backed services. **Consent/CMP remains an optional standalone category instead of being forced into Ultimate.**

---

<a id="protection-comparison"></a>
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

<a id="optional-protection-modules"></a>
## 🧩 Optional Protection Modules

These profiles solve a different problem than the privacy tiers above. They are best treated as **add-ons**, not as “stronger versions” of Balanced or Strict.

<!-- ADDON_PROFILES_START -->
| Profile | Protection | Entries | Recommended for | View | Raw |
|---|:---:|---:|---|:---:|:---:|
| 🛡️ **Security** | Security | **3,457,982** | Security-focused filtering | [Show Parts](#security-parts) | **[Raw Parts](#security-parts)** |
| 👨‍👩‍👧 **Family** | Family | **1,831,225** | Family networks | [Show Parts](#family-parts) | **[Raw Parts](#family-parts)** |
<!-- ADDON_PROFILES_END -->

- **Security** focuses on malware, phishing, scams, fake shops and cryptomining. It can be combined with Balanced or Strict.
- **Family** adds advertising/tracking protection plus adult and gambling filtering.
- **Gaming Privacy**, **Consent/CMP** and other category lists remain separately selectable below so users can add only what they actually want.

<a id="large-profile-parts"></a>
## 📦 Large Profile Parts

Large combined profiles are generated as deterministic, size-bounded files. Add **every part** of a split profile for complete coverage. Parts use zero-padded names such as `security-part-01.txt` and now target a maximum of **50 MiB per file**. On the first build after this upgrade, the previous smaller parts are automatically merged and regenerated.

Upgrading from the previous `security.txt` / `family.txt` / `ultimate-N.txt` layout? See [`docs/MIGRATION_V3_EN.md`](docs/MIGRATION_V3_EN.md).

<!-- SPLIT_PROFILES_START -->
<a id="security-parts"></a>
<details>
<summary><strong>🛡️ Security: Show Parts (2 files)</strong></summary>

**Total: 3,457,982 unique domains.** Add all parts to Pi-hole or your DNS blocker for complete profile coverage.

| Security Part | Security Part |
|---|---|
| **Part 01**  <br>**2,578,738** entries · 50.0 MiB  <br>[View](lists/combined/security-part-01.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-01.txt)** | **Part 02**  <br>**879,244** entries · 17.5 MiB  <br>[View](lists/combined/security-part-02.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-02.txt)** |

</details>

<a id="family-parts"></a>
<details>
<summary><strong>👨‍👩‍👧 Family: Show Parts (1 files)</strong></summary>

**Total: 1,831,225 unique domains.** Add all parts to Pi-hole or your DNS blocker for complete profile coverage.

| Family Part | Family Part |
|---|---|
| **Part 01**  <br>**1,831,225** entries · 33.3 MiB  <br>[View](lists/combined/family-part-01.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family-part-01.txt)** |  |

</details>

<a id="ultimate-parts"></a>
<details>
<summary><strong>🔴 Ultimate: Show Parts (2 files)</strong></summary>

**Total: 5,212,373 unique domains.** Add all parts to Pi-hole or your DNS blocker for complete profile coverage.

| Ultimate Part | Ultimate Part |
|---|---|
| **Part 01**  <br>**2,632,290** entries · 50.0 MiB  <br>[View](lists/combined/ultimate-part-01.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-01.txt)** | **Part 02**  <br>**2,580,083** entries · 49.6 MiB  <br>[View](lists/combined/ultimate-part-02.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-02.txt)** |

</details>
<!-- SPLIT_PROFILES_END -->



---

<a id="ads-tracking"></a>
# 📢 Ads & Tracking

<!-- ADS_TRACKING_TABLE_START -->
| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 📣 **Ads** | 235,630 | Large advertising, ad-delivery and integrated pop-up-ad domain set | [View](lists/categories/ads.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/ads.txt) |
| 👁️ **Trackers** | 143,941 | Large analytics and tracking infrastructure set | [View](lists/categories/trackers.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/trackers.txt) |
| 👥 **Social Trackers** | 99 | Social-network tracking and analytics endpoints | [View](lists/categories/social-trackers.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/social-trackers.txt) |
| 📲 **Mobile Tracking** | 808 | Mobile attribution, SDK analytics, app tracking and integrated TikTok native trackers | [View](lists/categories/mobile-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/mobile-tracking.txt) |
| 🧩 **Native/App Tracking** | 1,466 | Native OS/device and application tracking | [View](lists/categories/native-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/native-tracking.txt) |
| 🔗 **Affiliate Tracking** | 643 | Affiliate, click, referral and conversion tracking; included from Strict upward | [View](lists/categories/affiliate-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/affiliate-tracking.txt) |
| 🍪 **Consent / CMP** | 44 | Optional consent-management/CMP blocking with elevated website-breakage risk | [View](lists/categories/consent-cmp.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/consent-cmp.txt) |
<!-- ADS_TRACKING_TABLE_END -->

> **Consent/CMP is deliberately not included in any combined protection profile.** DNS-level consent blocking can interfere with page loading, consent state and site functionality.

---

<a id="telemetry-devices"></a>
# 📡 Telemetry & Devices

<!-- TELEMETRY_TABLE_START -->
| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 📊 **General Telemetry** | 29,289 | Broad product/app analytics, diagnostics and telemetry | [View](lists/categories/telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/telemetry.txt) |
| 🪟 **Windows Telemetry** | 425 | Windows/Office diagnostics, telemetry and integrated Microsoft native trackers | [View](lists/categories/windows-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/windows-telemetry.txt) |
| 🍎 **Apple Telemetry** | 119 | Apple telemetry, metrics, diagnostics and integrated native trackers | [View](lists/categories/apple-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/apple-telemetry.txt) |
| 🤖 **Android Telemetry** | 1,511 | Android/vendor telemetry including Huawei, Samsung, Vivo, OPPO/Realme and Xiaomi | [View](lists/categories/android-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/android-telemetry.txt) |
| 🐧 **Linux Telemetry** | 3 | Linux distribution telemetry, diagnostics and usage reporting | [View](lists/categories/linux-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/linux-telemetry.txt) |
| 💾 **NAS Telemetry** | 12 | NAS telemetry and usage reporting (Synology, TrueNAS and others) | [View](lists/categories/nas-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/nas-telemetry.txt) |
| 🖥️ **Server Telemetry** | 10 | Server, Red Hat Insights and management telemetry | [View](lists/categories/server-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/server-telemetry.txt) |
| 📺 **Smart TV** | 622 | Smart-TV ads, ACR, diagnostics, telemetry and integrated LG webOS/Roku trackers | [View](lists/categories/smart-tv.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/smart-tv.txt) |
| 🏠 **IoT** | 437 | Telemetry/tracking endpoints for IoT, connected and Amazon devices/services | [View](lists/categories/iot.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/iot.txt) |
<!-- TELEMETRY_TABLE_END -->

> Device-specific lists and native trackers can disable recommendations, diagnostics, usage reporting, ACR, ads or other cloud-backed features.

---

<a id="gaming-privacy"></a>
# 🎮 Gaming Privacy

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 🎮 **Gaming Telemetry** | 38 | Recommended game, launcher, analytics and crash-reporting endpoints with lower breakage risk | [View](lists/categories/gaming-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gaming-telemetry.txt) |
| ⚠️ **Gaming Telemetry – Aggressive** | 62 | Optional additional endpoints with increased launcher, login and gameplay breakage risk | [View](lists/categories/gaming-telemetry-aggressive.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gaming-telemetry-aggressive.txt) |
| 🧩 **Gaming RegEx Rules** | 5 | Dynamic Pi-hole deny patterns; import individually, not as a normal Adlist | [View](lists/regex/gaming-telemetry-regex.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regex/gaming-telemetry-regex.txt) |

> Start with **Gaming Telemetry**. The aggressive list and RegEx rules can interfere with Battle.net, Epic, Rockstar, Riot, EA and individual games. Test them in a separate Pi-hole group first.

---

<a id="security-lists"></a>
# 🛡️ Security Lists

<!-- SECURITY_TABLE_START -->
| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 🦠 **Malware** | 2,710,235 | Massive malware, ransomware and active malware-host set | [View](lists/categories/malware.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/malware.txt) |
| 🎣 **Phishing** | 572,332 | Massive active and curated phishing-domain set | [View](lists/categories/phishing.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/phishing.txt) |
| 💰 **Scam & Internet Fraud** | 283,956 | Scam, fraud, fake-offer, trap and deceptive-platform domains | [View](lists/categories/scam.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/scam.txt) |
| 🛒 **Fake Shops** | 11,380 | Aggressive fake-shop/deceptive-store candidate set | [View](lists/categories/fake-shops.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/fake-shops.txt) |
| ⛏️ **Cryptomining** | 6,121 | Browser/remote mining infrastructure (generic exchanges excluded) | [View](lists/categories/cryptomining.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/cryptomining.txt) |
| <a id="list-threat-intelligence"></a>🔐 **Threat Intelligence Feeds** | 4 variants | Additional malware, phishing, scam, spam, cryptojacking and C2 indicators in multiple sizes. | [Variants](#list-threat-intelligence-variants) | — |
| <a id="list-nrd-dga"></a>🆕 **Newly Registered Domains / NRD & DGA** | 8 variants | Time-window lists for newly registered domains and high-entropy DGA domains; very large and especially aggressive. | [Variants](#list-nrd-dga-variants) | — |
| <a id="list-dynamic-dns"></a>🔏 **Dynamic DNS** | 1,524 | Blocks known dynamic-DNS services that can be abused in phishing or malware campaigns. | [View](lists/categories/dynamic-dns.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/dynamic-dns.txt)** |
| <a id="list-badware-hoster"></a>💻 **Badware Hoster** | 1,258 | Blocks hosting-provider root domains repeatedly abused for malicious content; high false-positive risk. | [View](lists/categories/badware-hoster.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/badware-hoster.txt)** |
| <a id="list-most-abused-tlds"></a>🔮 **Most Abused TLDs** | 147 | Aggressive rules blocking entire frequently abused top-level domains; archived in Pi-hole-compatible Adblock format. | [View](lists/categories/most-abused-tlds.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/most-abused-tlds.txt)** |

<a id="list-threat-intelligence-variants"></a>
<details>
<summary><strong>🔐 Threat Intelligence Feeds: Show variants</strong></summary>

| Variant | Entries | View | Raw |
|---|---:|:---:|:---:|
| **Full** | 1,742,603 | [View](lists/categories/threat-intelligence-full.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/threat-intelligence-full.txt)** |
| **Medium** | 388,528 | [View](lists/categories/threat-intelligence-medium.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/threat-intelligence-medium.txt)** |
| **Mini** | 290,044 | [View](lists/categories/threat-intelligence-mini.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/threat-intelligence-mini.txt)** |
| **IPv4** | 55,692 | [View](lists/ips/threat-intelligence-ipv4.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ips/threat-intelligence-ipv4.txt)** |

</details>
<a id="list-nrd-dga-variants"></a>
<details>
<summary><strong>🆕 Newly Registered Domains / NRD & DGA: Show variants</strong></summary>

| Variant | Entries | View | Raw |
|---|---:|:---:|:---:|
| **NRD days 1–7** | 2,474,849 | [View](lists/categories/nrd-01-07.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/nrd-01-07.txt)** |
| **NRD days 8–14** | 2,628,672 | [View](lists/categories/nrd-08-14.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/nrd-08-14.txt)** |
| **NRD days 15–21** | 2,428,426 | [View](lists/categories/nrd-15-21.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/nrd-15-21.txt)** |
| **NRD days 22–28** | 2,922,658 | [View](lists/categories/nrd-22-28.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/nrd-22-28.txt)** |
| **NRD days 29–35** | 2,298,771 | [View](lists/categories/nrd-29-35.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/nrd-29-35.txt)** |
| **DGA 7 days** | 539,743 | [View](lists/categories/dga-7.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/dga-7.txt)** |
| **DGA 14 days** | 1,125,605 | [View](lists/categories/dga-14.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/dga-14.txt)** |
| **DGA 30 days** | Not built yet | — | — |

</details>
<!-- SECURITY_TABLE_END -->

> Security and threat-intelligence lists can be very large and aggressive. **NRD/DGA, badware-hoster and TLD rules** carry particularly high false-positive risk and should be enabled deliberately.

---

<a id="dns-web-protection"></a>
# 🌐 DNS, Web & Bypass Protection

These optional modules target **DNS bypass, DNS rebinding and obfuscated redirects**. They are not part of the normal privacy profiles and should be enabled deliberately.

<!-- SPECIAL_NETWORK_START -->
| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| <a id="list-dns-bypass"></a>📤 **DoH/VPN/TOR/Proxy Bypass** | 3 variants | Blocks known encrypted-DNS, VPN, TOR and proxy endpoints that can bypass local DNS filtering. | [Variants](#list-dns-bypass-variants) | — |
| <a id="list-url-shortener"></a>📲 **URL Shortener** | 9,904 | Blocks known link/URL shorteners; intentionally marked very aggressive for normal home networks. | [View](lists/categories/url-shortener.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/url-shortener.txt)** |
| <a id="list-dns-rebind-protection"></a>🛡️ **DNS Rebind Protection** | — | Pi-hole/dnsmasq configuration against DNS rebinding; not a normal static domain Adlist. | [Documentation](docs/DNS_REBIND_PROTECTION_EN.md) | — |

<a id="list-dns-bypass-variants"></a>
<details>
<summary><strong>📤 DoH/VPN/TOR/Proxy Bypass: Show variants</strong></summary>

| Variant | Entries | View | Raw |
|---|---:|:---:|:---:|
| **Full** | 16,965 | [View](lists/categories/dns-bypass-full.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/dns-bypass-full.txt)** |
| **DoH only** | 3,384 | [View](lists/categories/doh-only.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/doh-only.txt)** |
| **DoH IPv4** | 1,395 | [View](lists/ips/doh-ipv4.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ips/doh-ipv4.txt)** |

</details>
<!-- SPECIAL_NETWORK_END -->

---

<a id="family-lists"></a>
# 👨‍👩‍👧 Family Lists

<!-- FAMILY_TABLE_START -->
| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 🔞 **Adult / NSFW** | 1,028,639 | Massive adult/NSFW-content and pornography domain set | [View](lists/categories/adult.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/adult.txt) |
| 🎰 **Gambling** | 432,555 | Massive betting, casino and gambling domain set · [optional variants](#list-gambling-variants) | [View](lists/categories/gambling.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gambling.txt) |
| <a id="list-safesearch-unsupported"></a>🔍 **SafeSearch Unsupported** | 206 | Blocks search engines that do not support SafeSearch. | [View](lists/categories/safesearch-unsupported.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/safesearch-unsupported.txt)** |
| <a id="list-anti-piracy"></a>💀 **Anti Piracy** | 39,740 | Blocks domains and services mainly used for unauthorized distribution of copyrighted content. | [View](lists/categories/anti-piracy.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/anti-piracy.txt)** |
| <a id="list-social-networks"></a>💬 **Social Networks** | 898 | Blocks access to traditional social networks; messaging and streaming are not automatically treated the same way. | [View](lists/categories/social-networks.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/social-networks.txt)** |

<a id="list-gambling-variants"></a>
<details>
<summary><strong>🎰 Gambling: Show variants</strong></summary>

| Variant | Entries | View | Raw |
|---|---:|:---:|:---:|
| **Medium** | 142,337 | [View](lists/categories/gambling-medium.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gambling-medium.txt)** |
| **Mini** | 93,306 | [View](lists/categories/gambling-mini.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gambling-mini.txt)** |

</details>
<!-- FAMILY_TABLE_END -->

> Family and content filters deliberately remain optional so Adult/NSFW, gambling, SafeSearch, social networks and anti-piracy can be combined to match your network.

---

<a id="recommendations"></a>
# 💡 Recommendations

BlackRabbitZ separates **privacy profiles**, **protection modules** and **aggressive extended lists** so every feature does not have to be forced into one giant all-in-one profile.

| Goal | Recommendation |
|---|---|
| Reduce ads/tracking with minimal breakage | **Balanced ⭐** |
| More privacy and telemetry blocking | **Strict** |
| Additional threat protection | **Balanced or Strict + Security** |
| Family network | **Family** plus selected SafeSearch/social/bypass modules as needed |
| Maximum integrated blocking | **Ultimate**, only if you can troubleshoot false positives yourself |
| Additional threat intelligence | start with **TIF Mini/Medium**; use Full only with sufficient resources |
| NRD/DGA, badware hosters, URL shorteners, TLD blocking | only for deliberately aggressive or particularly sensitive environments |

DNS blocking can catch a great deal of advertising, tracking and known malicious infrastructure, but it **cannot replace browser-side content filtering**. A good content blocker is still useful for page elements.

---

<a id="online-dns-services"></a>
# 🏬 Online DNS Services

BlackRabbitZ primarily targets **self-managed DNS filters** such as Pi-hole. The published plain-domain lists can also be used by other products when the service supports custom blocklists.

| Use case | Recommendation |
|---|---|
| Home network / full control | Pi-hole or a comparable self-hosted DNS filter |
| Mobile away from home | reach your own DNS via VPN/tunnel or use an external DNS service that accepts custom lists |
| IPv4 extended lists | use only in products/firewalls that explicitly support IP/network lists |
| DNS rebind protection | use the resolver's built-in rebind feature; see the [documentation](docs/DNS_REBIND_PROTECTION_EN.md) |

> Support for custom lists at external DNS providers can change. BlackRabbitZ therefore does not claim permanently valid provider availability here and instead publishes portable Raw lists.

---

<a id="upstream-sources"></a>
# 🌐 Upstream Sources & Build Transparency

The large category lists merge and deduplicate selected upstream DNS/threat-intelligence datasets. Source and license details are documented in [`THIRD_PARTY_EN.md`](THIRD_PARTY_EN.md).

- Category files are published as plain domains, one domain per line.
- `.github/workflows/daily-upstream-update.yml` checks configured upstream feeds every day and additively imports newly published domains.
- `scripts/update-upstreams.py` validates, normalizes, deduplicates and safety-checks upstream data before category files are changed.
- `config/profiles.json` is the single source of truth for profile composition, display metadata and split behavior.
- `scripts/update-lists.sh` rebuilds all combined profiles, metadata, checksums and README values after category changes.
- Upstream URLs and per-source safety thresholds remain in [`scripts/upstream-sources.json`](scripts/upstream-sources.json).
- [`metadata/build.json`](metadata/build.json) contains machine-readable counts, part files, sizes and SHA-256 hashes.
- [`metadata/SHA256SUMS`](metadata/SHA256SUMS) provides checksums for all published category and combined list files.

See [`docs/AUTOMATIC_UPDATES_EN.md`](docs/AUTOMATIC_UPDATES_EN.md) for the complete update and fail-safe behavior.

---

<a id="repository-structure"></a>
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
│   ├── profiles.json
│   └── readme-i18n.json
├── docs/
│   ├── AUTOMATIC_UPDATES.md
│   ├── AUTOMATIC_UPDATES_EN.md
│   ├── MIGRATION_V3.md
│   └── MIGRATION_V3_EN.md
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
├── README_EN.md
├── CHANGELOG.md
├── CHANGELOG_EN.md
├── CONTRIBUTING.md
├── CONTRIBUTING_EN.md
├── SECURITY.md
├── SECURITY_EN.md
├── LICENSE
├── NOTICE
├── ATTRIBUTION.md
├── ATTRIBUTION_EN.md
├── THIRD_PARTY.md
├── THIRD_PARTY_EN.md
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

<a id="automatic-updates"></a>
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
Split large profiles (max. 50 MiB parts)
        ↓
Validate ordering / uniqueness / part sizes
        ↓
Generate build.json + SHA256SUMS
        ↓
Synchronize README files
```

Automatic upstream imports remain **additive**: the updater can extend the lists automatically, but it does not silently delete existing BlackRabbitZ entries. Specialized gaming/Linux/NAS/server telemetry lists can remain manually curated when no sufficiently trustworthy general-purpose upstream exists.

---

<a id="extending-lists"></a>
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

<a id="false-positives"></a>
# ⚠️ False Positives

Blocking more domains does not automatically mean better protection.

If a list breaks a website, application or device, use the **False positive** issue template and include the affected domain, list/profile, application/device, what stops working and reproduction steps.

The goal is a useful blocklist, not the largest possible number.

---

<a id="license-attribution"></a>
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
- [`ATTRIBUTION_EN.md`](ATTRIBUTION_EN.md)
- [`THIRD_PARTY_EN.md`](THIRD_PARTY_EN.md)

---

<div align="center">

### 🐇 BlackRabbitZ DNS Blocklists

**Privacy. Security. Control.**

⭐ If this project is useful to you, consider starring the repository.

</div>

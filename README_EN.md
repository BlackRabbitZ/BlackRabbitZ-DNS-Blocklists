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

- [Why use DNS blocklists?](#why-dns-blocklists) — a short explanation of network-wide DNS filtering
- [Quick Start](#quick-start) — recommended default list and fast Pi-hole setup
- [Privacy Protection Profiles](#protection-profiles) — Light, Balanced, Strict and Ultimate as graduated profiles
- [Protection Comparison](#protection-comparison) — feature coverage and breakage risk
  - [Optional Protection Modules](#optional-protection-modules) — Security and Family as targeted add-ons
  - [Large Profile Parts](#large-profile-parts) — all Raw parts for Security, Family and Ultimate
- [Ads & Tracking](#ads-tracking) — ads, trackers, affiliate tracking, pop-ups and native trackers
  - [8. Pop-Up Ads](#special-popup-ads) — annoying and potentially malicious pop-up domains
  - [22. Native Tracker](#special-native-tracker-archive) — device- and service-specific tracking
- [Telemetry & Devices](#telemetry-devices) — OS, device, Smart TV, IoT and server telemetry
- [Gaming Privacy](#gaming-privacy) — gaming telemetry and optional RegEx rules
- [Security Lists](#security-lists) — malware, phishing, scams, fake shops and advanced threat intelligence
  - [7. Fake & Internet Scams](#special-fake) — fake shops, traps and fraudulent offers
  - [9. Threat Intelligence Feeds](#special-threat-intelligence) — Full, Medium, Mini and IPv4 indicators
  - [10. Newly Registered Domains / NRD & DGA](#special-nrd-dga) — new and high-entropy domains; very aggressive
  - [13. Dynamic DNS](#special-dynamic-dns) — DynDNS services with elevated abuse risk
  - [14. Badware Hoster](#special-badware-hoster) — hosting infrastructure with elevated abuse risk
  - [16. Most Abused TLDs](#special-most-abused-tlds) — aggressive TLD-based protection rules
- [DNS, Web & Bypass Protection](#dns-web-protection) — DNS bypass, rebinding and obfuscated short links
  - [11. DoH/VPN/TOR/Proxy Bypass](#special-dns-bypass) — endpoints that can bypass local DNS filtering
  - [15. URL Shortener](#special-url-shortener) — known link/URL shorteners
  - [17. DNS Rebind Protection](#special-dns-rebind-protection) — resolver configuration against DNS rebinding
- [Family Lists](#family-lists) — adult content, gambling and optional parental-control modules
  - [12. SafeSearch not supported](#special-safesearch-unsupported) — search engines without SafeSearch support
  - [18. Anti Piracy](#special-anti-piracy) — domains used for unauthorized content distribution
  - [19. Gambling variants](#special-gambling-archive) — Full, Medium and Mini
  - [20. Block Social Networks](#special-social-networks) — block access to social-network platforms
  - [21. NSFW](#special-nsfw-archive) — additional adult/NSFW coverage
- [23. Recommendations](#recommendations) — sensible profile and add-on combinations
- [24. Online DNS Services](#online-dns-services) — notes for external DNS providers and mobile use
- [Upstream Sources & Build Transparency](#upstream-sources) — sources, archive snapshots, metadata and checksums
- [Repository Structure](#repository-structure) — directories, configuration, scripts and generated lists
- [Automatic List Updates](#automatic-updates) — daily feeds and the separate special-list builder
- [Extending Lists](#extending-lists) — add categories, profiles and special lists
- [False Positives](#false-positives) — report incorrect blocks and use the allowlist
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
| 🟢 **Light** | Low | **234,038** | Basic ad blocking | [View](lists/combined/light.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/light.txt)** |
| 🔵 **Balanced ⭐** | Medium | **371,544** | Most users | [View](lists/combined/balanced.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/balanced.txt)** |
| 🟠 **Strict** | High | **372,540** | Privacy-focused setups | [View](lists/combined/strict.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/strict.txt)** |
| 🔴 **Ultimate** | Maximum | **5,169,014** | Aggressive filtering | [Show Parts](#ultimate-parts) | **[Raw Parts](#ultimate-parts)** |
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
| 🛡️ **Security** | Security | **3,458,013** | Security-focused filtering | [Show Parts](#security-parts) | **[Raw Parts](#security-parts)** |
| 👨‍👩‍👧 **Family** | Family | **1,788,212** | Family networks | [Show Parts](#family-parts) | **[Raw Parts](#family-parts)** |
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
<summary><strong>🛡️ Security: Show Parts (14 files)</strong></summary>

**Total: 3,458,013 unique domains.** Add all parts to Pi-hole or your DNS blocker for complete profile coverage.

| Security Part | Security Part |
|---|---|
| **Part 01**  <br>**264,378** entries · 5.0 MiB  <br>[View](lists/combined/security-part-01.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-01.txt)** | **Part 02**  <br>**232,052** entries · 5.0 MiB  <br>[View](lists/combined/security-part-02.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-02.txt)** |
| **Part 03**  <br>**247,129** entries · 5.0 MiB  <br>[View](lists/combined/security-part-03.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-03.txt)** | **Part 04**  <br>**259,204** entries · 5.0 MiB  <br>[View](lists/combined/security-part-04.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-04.txt)** |
| **Part 05**  <br>**263,085** entries · 5.0 MiB  <br>[View](lists/combined/security-part-05.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-05.txt)** | **Part 06**  <br>**263,525** entries · 5.0 MiB  <br>[View](lists/combined/security-part-06.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-06.txt)** |
| **Part 07**  <br>**270,072** entries · 5.0 MiB  <br>[View](lists/combined/security-part-07.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-07.txt)** | **Part 08**  <br>**260,007** entries · 5.0 MiB  <br>[View](lists/combined/security-part-08.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-08.txt)** |
| **Part 09**  <br>**256,986** entries · 5.0 MiB  <br>[View](lists/combined/security-part-09.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-09.txt)** | **Part 10**  <br>**260,279** entries · 5.0 MiB  <br>[View](lists/combined/security-part-10.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-10.txt)** |
| **Part 11**  <br>**280,775** entries · 5.0 MiB  <br>[View](lists/combined/security-part-11.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-11.txt)** | **Part 12**  <br>**242,092** entries · 5.0 MiB  <br>[View](lists/combined/security-part-12.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-12.txt)** |
| **Part 13**  <br>**221,927** entries · 5.0 MiB  <br>[View](lists/combined/security-part-13.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-13.txt)** | **Part 14**  <br>**136,502** entries · 2.6 MiB  <br>[View](lists/combined/security-part-14.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-14.txt)** |

</details>

<a id="family-parts"></a>
<details>
<summary><strong>👨‍👩‍👧 Family: Show Parts (7 files)</strong></summary>

**Total: 1,788,212 unique domains.** Add all parts to Pi-hole or your DNS blocker for complete profile coverage.

| Family Part | Family Part |
|---|---|
| **Part 01**  <br>**287,739** entries · 5.0 MiB  <br>[View](lists/combined/family-part-01.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family-part-01.txt)** | **Part 02**  <br>**267,873** entries · 5.0 MiB  <br>[View](lists/combined/family-part-02.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family-part-02.txt)** |
| **Part 03**  <br>**268,779** entries · 5.0 MiB  <br>[View](lists/combined/family-part-03.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family-part-03.txt)** | **Part 04**  <br>**274,756** entries · 5.0 MiB  <br>[View](lists/combined/family-part-04.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family-part-04.txt)** |
| **Part 05**  <br>**269,955** entries · 5.0 MiB  <br>[View](lists/combined/family-part-05.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family-part-05.txt)** | **Part 06**  <br>**266,287** entries · 5.0 MiB  <br>[View](lists/combined/family-part-06.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family-part-06.txt)** |
| **Part 07**  <br>**152,823** entries · 2.7 MiB  <br>[View](lists/combined/family-part-07.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family-part-07.txt)** |  |

</details>

<a id="ultimate-parts"></a>
<details>
<summary><strong>🔴 Ultimate: Show Parts (20 files)</strong></summary>

**Total: 5,169,014 unique domains.** Add all parts to Pi-hole or your DNS blocker for complete profile coverage.

| Ultimate Part | Ultimate Part |
|---|---|
| **Part 01**  <br>**295,375** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-01.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-01.txt)** | **Part 02**  <br>**244,555** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-02.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-02.txt)** |
| **Part 03**  <br>**228,569** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-03.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-03.txt)** | **Part 04**  <br>**264,308** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-04.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-04.txt)** |
| **Part 05**  <br>**260,070** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-05.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-05.txt)** | **Part 06**  <br>**263,024** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-06.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-06.txt)** |
| **Part 07**  <br>**263,058** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-07.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-07.txt)** | **Part 08**  <br>**267,351** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-08.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-08.txt)** |
| **Part 09**  <br>**261,856** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-09.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-09.txt)** | **Part 10**  <br>**279,239** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-10.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-10.txt)** |
| **Part 11**  <br>**258,822** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-11.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-11.txt)** | **Part 12**  <br>**268,354** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-12.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-12.txt)** |
| **Part 13**  <br>**266,309** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-13.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-13.txt)** | **Part 14**  <br>**258,896** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-14.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-14.txt)** |
| **Part 15**  <br>**262,296** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-15.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-15.txt)** | **Part 16**  <br>**264,670** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-16.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-16.txt)** |
| **Part 17**  <br>**278,829** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-17.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-17.txt)** | **Part 18**  <br>**241,849** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-18.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-18.txt)** |
| **Part 19**  <br>**222,191** entries · 5.0 MiB  <br>[View](lists/combined/ultimate-part-19.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-19.txt)** | **Part 20**  <br>**219,393** entries · 4.0 MiB  <br>[View](lists/combined/ultimate-part-20.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-20.txt)** |

</details>
<!-- SPLIT_PROFILES_END -->



---

<a id="ads-tracking"></a>
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

## 🧩 Additional Ads & Tracking Lists

The following optional lists extend the normal BlackRabbitZ categories. They come from the documented HaGeZi state and remain separate from the standard profiles.

<!-- SPECIAL_ADS_TRACKING_START -->
| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| <a id="special-popup-ads"></a>🎉 **8. Pop-Up Ads** | Not built yet | Blocks annoying and potentially malicious pop-up advertising domains. | — | — |
| <a id="special-native-tracker-archive"></a>📲 **22. Native Tracker – Devices & Services – Amazon** | Not built yet | Device- and service-specific tracker lists for Amazon, Apple, Huawei, Microsoft, Samsung, TikTok, LG webOS, Roku, Vivo, OPPO/Realme and Xiaomi. | — | — |
| 📲 **22. Native Tracker – Devices & Services – Apple** | Not built yet | Device- and service-specific tracker lists for Amazon, Apple, Huawei, Microsoft, Samsung, TikTok, LG webOS, Roku, Vivo, OPPO/Realme and Xiaomi. | — | — |
| 📲 **22. Native Tracker – Devices & Services – Huawei** | Not built yet | Device- and service-specific tracker lists for Amazon, Apple, Huawei, Microsoft, Samsung, TikTok, LG webOS, Roku, Vivo, OPPO/Realme and Xiaomi. | — | — |
| 📲 **22. Native Tracker – Devices & Services – Microsoft / Windows / Office** | Not built yet | Device- and service-specific tracker lists for Amazon, Apple, Huawei, Microsoft, Samsung, TikTok, LG webOS, Roku, Vivo, OPPO/Realme and Xiaomi. | — | — |
| 📲 **22. Native Tracker – Devices & Services – Samsung** | Not built yet | Device- and service-specific tracker lists for Amazon, Apple, Huawei, Microsoft, Samsung, TikTok, LG webOS, Roku, Vivo, OPPO/Realme and Xiaomi. | — | — |
| 📲 **22. Native Tracker – Devices & Services – TikTok** | Not built yet | Device- and service-specific tracker lists for Amazon, Apple, Huawei, Microsoft, Samsung, TikTok, LG webOS, Roku, Vivo, OPPO/Realme and Xiaomi. | — | — |
| 📲 **22. Native Tracker – Devices & Services – TikTok – Aggressive** | Not built yet | Device- and service-specific tracker lists for Amazon, Apple, Huawei, Microsoft, Samsung, TikTok, LG webOS, Roku, Vivo, OPPO/Realme and Xiaomi. | — | — |
| 📲 **22. Native Tracker – Devices & Services – LG webOS** | Not built yet | Device- and service-specific tracker lists for Amazon, Apple, Huawei, Microsoft, Samsung, TikTok, LG webOS, Roku, Vivo, OPPO/Realme and Xiaomi. | — | — |
| 📲 **22. Native Tracker – Devices & Services – Roku** | Not built yet | Device- and service-specific tracker lists for Amazon, Apple, Huawei, Microsoft, Samsung, TikTok, LG webOS, Roku, Vivo, OPPO/Realme and Xiaomi. | — | — |
| 📲 **22. Native Tracker – Devices & Services – Vivo** | Not built yet | Device- and service-specific tracker lists for Amazon, Apple, Huawei, Microsoft, Samsung, TikTok, LG webOS, Roku, Vivo, OPPO/Realme and Xiaomi. | — | — |
| 📲 **22. Native Tracker – Devices & Services – OPPO / Realme** | Not built yet | Device- and service-specific tracker lists for Amazon, Apple, Huawei, Microsoft, Samsung, TikTok, LG webOS, Roku, Vivo, OPPO/Realme and Xiaomi. | — | — |
| 📲 **22. Native Tracker – Devices & Services – Xiaomi** | Not built yet | Device- and service-specific tracker lists for Amazon, Apple, Huawei, Microsoft, Samsung, TikTok, LG webOS, Roku, Vivo, OPPO/Realme and Xiaomi. | — | — |
<!-- SPECIAL_ADS_TRACKING_END -->

---

<a id="telemetry-devices"></a>
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

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 🦠 **Malware** | 2,710,231 | Massive malware, ransomware and active malware-host set | [View](lists/categories/malware.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/malware.txt) |
| 🎣 **Phishing** | 572,332 | Massive active and curated phishing-domain set | [View](lists/categories/phishing.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/phishing.txt) |
| 💰 **Scam** | 266,444 | Massive scam, fraud and deceptive-platform domain set | [View](lists/categories/scam.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/scam.txt) |
| 🛒 **Fake Shops** | 11,380 | Aggressive fake-shop/deceptive-store candidate set | [View](lists/categories/fake-shops.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/fake-shops.txt) |
| ⛏️ **Cryptomining** | 6,121 | Browser/remote mining infrastructure (generic exchanges excluded) | [View](lists/categories/cryptomining.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/cryptomining.txt) |

> Security lists are intentionally **large and aggressive** and merge multiple upstream intelligence sources. Threat data changes quickly, so false positives are possible and upstream snapshots should be refreshed regularly.

## 🧩 Advanced Security Lists

Additional threat-intelligence, NRD/DGA, DynDNS, hoster and TLD lists are available for higher-security environments. These modules are more aggressive and can cause more false positives.

<!-- SPECIAL_SECURITY_START -->
| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| <a id="special-fake"></a>🎭 **7. Fake & Internet Scams** | Not built yet | Protection against fake shops, rip-offs, traps and fraudulent fake offers. | — | — |
| <a id="special-threat-intelligence"></a>🔐 **9. Threat Intelligence Feeds – Full** | Not built yet | Additional malware, phishing, scam, spam, cryptojacking and C2 indicators in multiple sizes. | — | — |
| 🔐 **9. Threat Intelligence Feeds – Medium** | Not built yet | Additional malware, phishing, scam, spam, cryptojacking and C2 indicators in multiple sizes. | — | — |
| 🔐 **9. Threat Intelligence Feeds – Mini** | Not built yet | Additional malware, phishing, scam, spam, cryptojacking and C2 indicators in multiple sizes. | — | — |
| 🔐 **9. Threat Intelligence Feeds – IPv4** | Not built yet | Additional malware, phishing, scam, spam, cryptojacking and C2 indicators in multiple sizes. | — | — |
| <a id="special-nrd-dga"></a>🆕 **10. Newly Registered Domains / NRD & DGA – NRD days 1–7** | Not built yet | Time-window lists for newly registered domains and high-entropy DGA domains; very large and especially aggressive. | — | — |
| 🆕 **10. Newly Registered Domains / NRD & DGA – NRD days 8–14** | Not built yet | Time-window lists for newly registered domains and high-entropy DGA domains; very large and especially aggressive. | — | — |
| 🆕 **10. Newly Registered Domains / NRD & DGA – NRD days 15–21** | Not built yet | Time-window lists for newly registered domains and high-entropy DGA domains; very large and especially aggressive. | — | — |
| 🆕 **10. Newly Registered Domains / NRD & DGA – NRD days 22–28** | Not built yet | Time-window lists for newly registered domains and high-entropy DGA domains; very large and especially aggressive. | — | — |
| 🆕 **10. Newly Registered Domains / NRD & DGA – NRD days 29–35** | Not built yet | Time-window lists for newly registered domains and high-entropy DGA domains; very large and especially aggressive. | — | — |
| 🆕 **10. Newly Registered Domains / NRD & DGA – DGA 7 days** | Not built yet | Time-window lists for newly registered domains and high-entropy DGA domains; very large and especially aggressive. | — | — |
| 🆕 **10. Newly Registered Domains / NRD & DGA – DGA 14 days** | Not built yet | Time-window lists for newly registered domains and high-entropy DGA domains; very large and especially aggressive. | — | — |
| 🆕 **10. Newly Registered Domains / NRD & DGA – DGA 30 days** | Not built yet | Time-window lists for newly registered domains and high-entropy DGA domains; very large and especially aggressive. | — | — |
| <a id="special-dynamic-dns"></a>🔏 **13. Dynamic DNS** | Not built yet | Blocks known dynamic-DNS services that can be abused in phishing or malware campaigns. | — | — |
| <a id="special-badware-hoster"></a>💻 **14. Badware Hoster** | Not built yet | Blocks hosting-provider root domains repeatedly abused for malicious content; high false-positive risk. | — | — |
| <a id="special-most-abused-tlds"></a>🔮 **16. Most Abused TLDs** | Not built yet | Aggressive rules blocking entire frequently abused top-level domains; archived in Pi-hole-compatible Adblock format. | — | — |
<!-- SPECIAL_SECURITY_END -->

---

<a id="dns-web-protection"></a>
# 🌐 DNS, Web & Bypass Protection

These optional modules target **DNS bypass, DNS rebinding and obfuscated redirects**. They are not part of the normal privacy profiles and should be enabled deliberately.

<!-- SPECIAL_NETWORK_START -->
| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| <a id="special-dns-bypass"></a>📤 **11. DoH/VPN/TOR/Proxy Bypass – Full** | Not built yet | Blocks known encrypted-DNS, VPN, TOR and proxy endpoints that can bypass local DNS filtering. | — | — |
| 📤 **11. DoH/VPN/TOR/Proxy Bypass – DoH only** | Not built yet | Blocks known encrypted-DNS, VPN, TOR and proxy endpoints that can bypass local DNS filtering. | — | — |
| 📤 **11. DoH/VPN/TOR/Proxy Bypass – DoH IPv4** | Not built yet | Blocks known encrypted-DNS, VPN, TOR and proxy endpoints that can bypass local DNS filtering. | — | — |
| <a id="special-url-shortener"></a>📲 **15. URL Shortener** | Not built yet | Blocks known link/URL shorteners; intentionally marked very aggressive for normal home networks. | — | — |
| <a id="special-dns-rebind-protection"></a>🛡️ **17. DNS Rebind Protection** | — | Pi-hole/dnsmasq configuration against DNS rebinding; not a normal static domain Adlist. | [Documentation](docs/DNS_REBIND_PROTECTION_EN.md) | — |
<!-- SPECIAL_NETWORK_END -->

---

<a id="family-lists"></a>
# 👨‍👩‍👧 Family Lists

| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| 🔞 **Adult** | 999,123 | Massive adult-content and pornography domain set | [View](lists/categories/adult.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/adult.txt) |
| 🎰 **Gambling** | 420,536 | Massive betting, casino and gambling domain set | [View](lists/categories/gambling.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gambling.txt) |

> **These add-on filters deliberately remain optional and are not automatically added to the Family profile.** This lets you tailor parental controls and content filtering to your network.

## 🧩 Additional Family & Content Filters

In addition to the normal Adult and Gambling categories, optional SafeSearch, anti-piracy, social-network and NSFW lists are available. These filters can block wanted content or entire services.

<!-- SPECIAL_FAMILY_START -->
| List | Entries | Description | View | Raw |
|---|---:|---|:---:|:---:|
| <a id="special-safesearch-unsupported"></a>🔍 **12. SafeSearch Unsupported** | Not built yet | Blocks search engines that do not support SafeSearch. | — | — |
| <a id="special-anti-piracy"></a>💀 **18. Anti Piracy** | Not built yet | Blocks domains and services mainly used for unauthorized distribution of copyrighted content. | — | — |
| <a id="special-gambling-archive"></a>🎰 **19. Gambling – HaGeZi Variants – Full** | Not built yet | Archived full, medium and mini variants in addition to the existing BlackRabbitZ gambling list. | — | — |
| 🎰 **19. Gambling – HaGeZi Variants – Medium** | Not built yet | Archived full, medium and mini variants in addition to the existing BlackRabbitZ gambling list. | — | — |
| 🎰 **19. Gambling – HaGeZi Variants – Mini** | Not built yet | Archived full, medium and mini variants in addition to the existing BlackRabbitZ gambling list. | — | — |
| <a id="special-social-networks"></a>💬 **20. Social Networks** | Not built yet | Blocks access to traditional social networks; messaging and streaming are not automatically treated the same way. | — | — |
| <a id="special-nsfw-archive"></a>🔞 **21. NSFW / Adult Content – HaGeZi** | Not built yet | Archived HaGeZi NSFW list in addition to the existing BlackRabbitZ Adult category. | — | — |
<!-- SPECIAL_FAMILY_END -->

---

<a id="recommendations"></a>
# 💡 23. Recommendations

BlackRabbitZ separates **privacy profiles**, **protection modules** and **aggressive special lists** so every feature does not have to be forced into one giant all-in-one profile.

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
# 🏬 24. Online DNS Services

BlackRabbitZ primarily targets **self-managed DNS filters** such as Pi-hole. The published plain-domain lists can also be used by other products when the service supports custom blocklists.

| Use case | Recommendation |
|---|---|
| Home network / full control | Pi-hole or a comparable self-hosted DNS filter |
| Mobile away from home | reach your own DNS via VPN/tunnel or use an external DNS service that accepts custom lists |
| IPv4 special lists | use only in products/firewalls that explicitly support IP/network lists |
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
Split large profiles (5 MiB parts)
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

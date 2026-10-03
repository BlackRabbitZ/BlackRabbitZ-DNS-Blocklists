<p align="right">🇩🇪 <strong>Deutsch</strong> · <a href="README_EN.md">🇬🇧 English</a></p>

<a id="top"></a>

<div align="center">

# 🐇 BlackRabbitZ DNS Blocklists

### Privacy • Geräte-Isolation • App-Blocking • Security • Family • Network Control

![Pi-hole](https://img.shields.io/badge/Pi--hole-kompatibel-96060C?logo=pihole&logoColor=white)
![Format](https://img.shields.io/badge/Format-Plain%20Domains-2ea44f)
![Profiles](https://img.shields.io/badge/Profile-Light%20%7C%20Normal%20%7C%20Pro%20%7C%20Pro%2B%2B%20%7C%20Ultimate-3178C6)
![Catalog](https://img.shields.io/badge/Katalog-100%20Kategorien-informational)

**DNS-Blocklisten mit klar definierter Wirkung:**

🛡️ **Privacy** – Werbung, Tracking, Analytics, Telemetrie und Fingerprinting blockieren, ohne den Dienst absichtlich abzuschalten  
⚠️ **Restrict** – Geräte und Hersteller stärker einschränken, optionale Online-/Cloudfunktionen reduzieren  
🚫 **Isolate** – Geräte möglichst vollständig von der Hersteller-Infrastruktur trennen  
🚫 **Block All** – Apps und Webdienste vollständig sperren  
🛡️ **Security** – Malware, Phishing, C2, Ransomware und Scam vollständig blockieren  
👨‍👩‍👧 **Family** – NSFW, Gambling, Drugs, Violence/Gore, Weapons usw. vollständig blockieren

</div>

---
<a id="projekt-navigation"></a>
## 📘 1. Inhaltsverzeichnis – Projekt & Nutzung

- [🚀 Schnellstart](#schnellstart)
- [🧭 Welche Wirkungsart brauche ich?](#wirkungsarten)
- [📊 Globale Hauptlisten auf einen Blick](#hauptlisten)
- [🎚️ Privacy-Schutzstufen](#schutzstufen)

---
<a id="kinderschutz-navigation"></a>
## 👨‍👩‍👧 Besonderes Inhaltsverzeichnis – Family & Kinderschutz

- [👨‍👩‍👧 Family & Content](#family)
- [🧒 Kids Allow-Only](#kids-allow-only)
- [📚 Kids-Allowlist-Dateien](#kids-dateien)
- [🛠️ Pi-hole-v6-Anleitung](#kids-anleitung)

---
<a id="blocklisten-navigation"></a>
## 🧱 2. Inhaltsverzeichnis – Blocklisten

### [🛡️ Allgemeine Privacy-Listen](#privacy-group)
- [🕵️ Privacy & Tracking](#privacy)
- [🧩 Software & Hardware Telemetrie](#software-hardware)
- [🤖 KI, Bots & Crawler](#automation)

### [🔌 Geräte & Hersteller — Privacy / Restrict / Isolate](#devices-group)
- [📺 Smart TV](#smart-tv)
- [📱 Smartphones & Mobile](#mobile)
- [💻 Betriebssysteme](#betriebssysteme)
- [🏠 IoT & Smart Home](#iot)
- [🎙️ Sprachassistenten](#voice)
- [🚗 Automotive / Connected Cars](#automotive)
- [💾 NAS & Server](#nas-server)
- [🌐 Router & Netzwerkgeräte](#network-devices)
- [📡 ISP / Provider](#providers)
- [🏢 Google, Microsoft, Apple & Amazon](#ecosystems)
- [🏭 Herstellerlisten](#manufacturers)

### [📱 Apps & Dienste — Privacy / Block All](#apps-group)
- [📺 Streaming](#streaming)
- [🎮 Gaming](#gaming)
- [💬 Social Media](#social-media)
- [☁️ Cloud, Server & Development](#cloud-dev)

### [🛡️ Vollständige Schutz-/Kontrolllisten](#protection-group)
- [👨‍👩‍👧 Family & Content](#family)
- [🛡️ Security & Threat Intelligence](#security)
- [🔐 DNS, Netzwerk & Umgehung](#network)
- [🧰 Speziallisten](#speziallisten)
- [🌍 Regionale Listen](#regional)

### 📚 Projekt & Dokumentation
- [🧩 Listenmodell](#listenmodell)
- [🗺️ 100-Kategorien-Katalog](#katalog100)
- [📂 Repository-Struktur](#repo-struktur)
- [✅ Qualitätssicherung](#qualitaet)
- [⚠️ Hinweise & technische Grenzen](#grenzen)
- [📜 Quellen & Lizenz](#lizenz)

---
# 📘 Teil 1 – Projekt & Nutzung


<a id="wirkungsarten"></a>
## 🧭 Welche Wirkungsart brauche ich?

> **Kompatibilität:** Alle bisherigen Repo-Pfade und RAW-URLs bleiben erhalten. Die neuen `device-control`- und `service-blocking`-Listen kommen **zusätzlich** hinzu; vorhandene Listen wurden nicht verschoben oder umsortiert.

| Was möchtest du erreichen? | Richtige Liste |
|---|---|
| Werbung, Tracker, Analytics, Telemetrie, Fingerprinting reduzieren | 🛡️ **Privacy** |
| Gerät normal nutzen, Herstellertracking reduzieren | 🔌 Hersteller/Gerät → **Privacy** |
| Optionale Hersteller-/Cloudfunktionen zusätzlich einschränken | ⚠️ Hersteller/Gerät → **Restrict** |
| Gerät möglichst komplett vom Hersteller trennen | 🚫 Hersteller/Gerät → **Isolate** |
| App/Dienst weiter nutzen, aber Tracking reduzieren | 📱 App/Dienst → **Privacy** |
| App/Webdienst vollständig sperren | 🚫 App/Dienst → **Block All** |
| Malware/Phishing/Ransomware/Scam blockieren | 🛡️ **Security** |
| NSFW/Gambling/Drugs/Violence/Weapons usw. sperren | 👨‍👩‍👧 **Family** |
| DoH/VPN/Proxy/Bypass-Endpunkte sperren | 🔐 **Network Control** |

### 🔌 Geräte & Hersteller

Jedes unterstützte Gerät bzw. jeder Hersteller erhält:

```text
privacy.txt
restrict.txt
isolate.txt
updates.txt
```

**Privacy** = nur Datenschutz-/Tracking-Endpunkte.  
**Restrict** = zusätzlich optionale Hersteller-, Cloud-, Marketing- und Recommendation-Dienste.  
**Isolate** = möglichst gesamte bekannte Herstellerkommunikation inklusive Account, Store, Cloud, APIs und Updates.  
**Updates** = Update-Infrastruktur separat steuerbar.

### 📱 Apps & Dienste

Jeder unterstützte Dienst erhält:

```text
privacy.txt
block-all.txt
```

**Privacy** = Tracking/Analytics/Telemetry reduzieren.  
**Block All** = funktionale Servicehosts sperren, sodass der Dienst nicht mehr funktioniert.

### 🛡️ Security und 👨‍👩‍👧 Family

Hier bedeutet ein Eintrag grundsätzlich:

> **Die gelistete Domain soll nicht erreichbar sein.**

---

<a id="schnellstart"></a>
## 🚀 Schnellstart

Für das gesamte Netzwerk wählst du **genau eine** globale Hauptliste:

```text
profiles/light.txt
profiles/normal.txt
profiles/pro.txt
profiles/pro-plus.txt
profiles/ultimate.txt
```

Die Stufen sind kumulativ. Es gibt **keine Part-/MiB-Aufteilung** – jedes logische Profil ist genau **eine Datei und eine URL**.

---
<a id="hauptlisten"></a>
## 📊 Globale Hauptlisten auf einen Blick

| Profil | Blockierung | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **234.010** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **342.229** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **371.530** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **383.637** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **5.119.284** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/ultimate.txt) |


Die fünf Profile bauen aufeinander auf. Für den normalen Einsatz wird **genau eine** Stufe gewählt.

> **Was steckt in den globalen Hauptlisten?** `Ultimate` enthält die Vereinigung aller bereichsspezifischen `Ultimate`-Hauptlisten im Repository. Die kleineren globalen Stufen (`Light`, `Normal`, `Pro`, `Pro++`) sind dagegen bewusst kuratierte, kumulative Teilmengen und **nicht** einfach die 1:1-Vereinigung aller gleichnamigen Bereichslisten.

---
<a id="schutzstufen"></a>
## 🎚️ Privacy-Schutzstufen Light bis Ultimate

| Profil | Typischer Inhalt | Risiko |
|---|---|:---:|
| 🟩 **Light** | Werbung + besonders sichere Tracker | Minimal |
| 🟦 **Normal** | Light + Tracking/Analytics | Niedrig |
| 🟨 **Pro** | Normal + Telemetrie, Diagnostics, Native-/Device-Tracking | Niedrig–Mittel |
| 🟧 **Pro++** | Pro + aggressivere Hersteller-/Cloud-Endpunkte + Security-Basis | Mittel |
| 🟥 **Ultimate** | maximaler Privacy-/Tracking-Bestand; keine absichtliche Block-All-/Isolate-Wirkung | Hoch |

`Ultimate` kann je nach Bereich Cloudfunktionen, Logins, Stores, Updates oder andere Onlinefunktionen beeinträchtigen.

---
<a id="listenmodell"></a>
## 🧩 Hauptlisten & Full-Listen

Jeder große Bereich folgt demselben Modell:

```text
Light ⊂ Normal ⊂ Pro ⊂ Pro++ ⊂ Ultimate
```

Die **Hauptlisten** bündeln ganze Bereiche.

Für einzelne Ziele wird die Wirkung über den Dateinamen eindeutig:

| Bereich | Dateien |
|---|---|
| Geräte / Hersteller | `privacy.txt` · `restrict.txt` · `isolate.txt` · `updates.txt` |
| Apps / Dienste | `privacy.txt` · `block-all.txt` |
| Security | vollständige Schutzlisten |
| Family | vollständige Inhalts-Sperrlisten |
| Network Control | vollständige Policy-/Umgehungs-Sperrlisten |

**Status:** ✅ = enthält Einträge. 🟡 = Pfad/Kategorie ist vollständig vorbereitet, aber im aktuellen statischen Quellstand fehlen belastbare Domain-Einträge. In den Datei-Headern zeigt `Data method`, ob eine Liste direkt aus einer Quelle übernommen, als Tier erzeugt oder konservativ aus bestehenden Domains neu einsortiert wurde.

---
<a id="katalog100"></a>
## 🗺️ 100-Kategorien-Katalog

Alle **100 Kategorien** des BRZ Pi-hole DNS-Listen & Kinderschutz-Handbuchs sind in [`docs/CATALOG_100.md`](docs/CATALOG_100.md) auf konkrete Repo-Pfade gemappt. Damit bleibt auch sichtbar, welche Spezialklassen bereits befüllt und welche nur vorbereitet sind.

---
<a id="repo-struktur"></a>
## 📂 Repository-Struktur – fertige Ansicht

### Smartphones & Mobile

<details>
<summary><strong>📂 Smartphones & Mobile anzeigen</strong></summary>


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
<summary><strong>📂 Smart TV anzeigen</strong></summary>


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

### Betriebssysteme

<details>
<summary><strong>📂 Betriebssysteme anzeigen</strong></summary>


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
<summary><strong>📂 Social Media anzeigen</strong></summary>


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
<summary><strong>📂 Streaming anzeigen</strong></summary>


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
<summary><strong>📂 Gaming anzeigen</strong></summary>


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
<summary><strong>📂 Security / Family / Network Control anzeigen</strong></summary>


```text
lists/security/
family/content/
lists/network/
```

Diese drei Bereiche bleiben vollständige Schutz-/Sperrlisten.

---

</details>
<a id="qualitaet"></a>
## ✅ Qualitätssicherung

- Plain-Domain-Format, eine Domain pro Zeile
- sortiert und dedupliziert
- kumulative Hauptprofile
- 100-Kategorien-Mapping
- SHA-256-Prüfsummen
- keine Part-Dateien
- keine automatische Fremdlisten-Synchronisation
- transparente Kennzeichnung vorbereiteter und abgeleiteter Listen

```bash
python3 scripts/validate.py
```

---
<a id="grenzen"></a>
## ⚠️ Hinweise & technische Grenzen

DNS-Blocking filtert Domains, keine einzelnen URL-Pfade. Fehlende Quellklassen werden nicht geraten: sie bleiben als vorbereitete Liste sichtbar, bis eine belastbare Quelle aufgenommen wird. KI-/Crawler-Listen ersetzen keine WAF-/Webserver-/`robots.txt`-Regeln. DNS-Rebind-Schutz liegt unter `policies/`, weil er Resolver-/Firewall-Konfiguration und keine normale Domainliste ist.

---
# 🧱 Teil 2 – Listen-Katalog

> Die Reihenfolge dieses Katalogs entspricht jetzt **1:1 dem Blocklisten-Inhaltsverzeichnis**.

---
<a id="privacy-group"></a>
## 🛡️ Allgemeine Privacy-Listen

Hier werden **nur Hintergrund- und Datenschutz-Endpunkte** geblockt. Webseiten, Apps und Geräte sollen grundsätzlich weiter funktionieren.

<a id="privacy"></a>
### 🕵️ Privacy & Tracking

#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **32.546** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **57.859** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **86.962** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **367.459** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **371.597** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/ultimate.txt) |

> **Privacy & Tracking – Ultimate:** Diese Stufe enthält die Vereinigung aller Full-/Speziallisten aus dem Bereich **Privacy & Tracking**. Die Stufen darunter sind kumulative, risikobasierte Teilmengen.

#### Full-/Speziallisten

<details>
<summary><strong>📂 Full-/Speziallisten anzeigen</strong></summary>

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Ads (Werbung)** | **234.017** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/ads.txt) |
| **Pop-Up Ads** | **517** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/pop-up-ads.txt) |
| **Affiliate Tracking** | **643** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/affiliate-tracking.txt) |
| **Aggressive Privacy** | **652** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/aggressive-privacy.txt) |
| **Analytics** | **35.898** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/analytics.txt) |
| **Captcha Antibot** | **379** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/captcha-antibot.txt) |
| **Cdn Tracking** | **20** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/cdn-tracking.txt) |
| **Chat Support** | **64** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/chat-support.txt) |
| **Consent Cmp** | **45** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/consent-cmp.txt) |
| **Crash Reporting** | **98** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/crash-reporting.txt) |
| **Crm** | **121** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/crm.txt) |
| **Ecommerce** | **44** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/ecommerce.txt) |
| **External Fonts** | **3** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/external-fonts.txt) |
| **Fingerprinting** | **14** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/fingerprinting.txt) |
| **Marketing** | **2.060** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/marketing.txt) |
| **Mobile Tracking** | **235** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/mobile-tracking.txt) |
| **Native Tracking** | **628** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/native-tracking.txt) |
| **Newsletter Tracking** | **166** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/newsletter-tracking.txt) |
| **Payment Tracking** | **17** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/payment-tracking.txt) |
| **Push Notifications** | **74** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/push-notifications.txt) |
| **Recommendations** | **362** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/recommendations.txt) |
| **Search Tracking** | **1** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/search-tracking.txt) |
| **Seo Tracking** | **115** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/seo-tracking.txt) |
| **Session Replay** | **212** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/session-replay.txt) |
| **Social Tracking** | **99** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/social-tracking.txt) |
| **Telemetry** | **29.181** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/telemetry.txt) |
| **Trackers** | **113.609** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/trackers.txt) |
| **Tracking Pixels** | **927** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/tracking-pixels.txt) |
| **Tracking Redirects** | **377** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/tracking-redirects.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="software-hardware"></a>
### 🧩 Software & Hardware Telemetrie

#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **75** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **28** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **73** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **76** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **84** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/ultimate.txt) |

<details>
<summary><strong>📂 Hersteller-Wirkungslisten anzeigen</strong></summary>


| Gerät / Hersteller | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
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

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="automation"></a>
### 🤖 KI, Bots & Crawler

#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **13** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **28** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **33** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **49** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **300** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/ultimate.txt) |

#### Full-/Speziallisten

<details>
<summary><strong>📂 Full-/Speziallisten anzeigen</strong></summary>

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Aggressive Crawlers** | **15** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/aggressive-crawlers.txt) |
| **Ai Crawlers** | **10** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/ai-crawlers.txt) |
| **Ai Scrapers** | **3** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/ai-scrapers.txt) |
| **Ai Telemetry** | **36** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/ai-telemetry.txt) |
| **Ai Tracking** | **43** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/ai-tracking.txt) |
| **Llm Crawlers** | **188** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/llm-crawlers.txt) |
| **Malicious Bots** | **1** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/malicious-bots.txt) |
| **Seo Bots** | **5** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/seo-bots.txt) |
| **Training Bots** | **6** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/training-bots.txt) |
| **Web Crawlers** | **62** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/web-crawlers.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>


---
<a id="devices-group"></a>
## 🔌 Geräte & Hersteller — Privacy / Restrict / Isolate

Geräte und Hersteller erhalten getrennte Wirkungsstufen: **Privacy** für Tracking/Telemetrie, **Restrict** für zusätzliche optionale Herstellerdienste und **Isolate** für möglichst vollständige Herstellerkommunikation.

<a id="smart-tv"></a>
### 📺 Smart TV

#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **346** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **362** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **454** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **636** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **648** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/ultimate.txt) |

<details>
<summary><strong>📂 Wirkungslisten anzeigen</strong></summary>


> 🛡️ **Privacy:** nur Tracking/Ads/Analytics/Telemetry/Diagnostics  
> ⚠️ **Restrict:** Privacy + optionale Hersteller-/Cloud-/Recommendation-Dienste  
> 🚫 **Isolate:** möglichst vollständige Herstellerkommunikation  
> 🔄 **Updates:** Update-Infrastruktur separat steuerbar

| Gerät / Hersteller | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
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

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="mobile"></a>
### 📱 Smartphones & Mobile

#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **391** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **445** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **531** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **993** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **1.004** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/ultimate.txt) |

<details>
<summary><strong>📂 Wirkungslisten anzeigen</strong></summary>


> 🛡️ **Privacy:** nur Tracking/Ads/Analytics/Telemetry/Diagnostics  
> ⚠️ **Restrict:** Privacy + optionale Hersteller-/Cloud-/Recommendation-Dienste  
> 🚫 **Isolate:** möglichst vollständige Herstellerkommunikation  
> 🔄 **Updates:** Update-Infrastruktur separat steuerbar

| Gerät / Hersteller | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
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

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="betriebssysteme"></a>
### 💻 Betriebssysteme

#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **20** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **48** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **104** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **302** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **311** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/ultimate.txt) |

<details>
<summary><strong>📂 Wirkungslisten anzeigen</strong></summary>


> 🛡️ **Privacy:** nur Tracking/Ads/Analytics/Telemetry/Diagnostics  
> ⚠️ **Restrict:** Privacy + optionale Hersteller-/Cloud-/Recommendation-Dienste  
> 🚫 **Isolate:** möglichst vollständige Herstellerkommunikation  
> 🔄 **Updates:** Update-Infrastruktur separat steuerbar

| Gerät / Hersteller | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
|---|---|---|---|---|
| **Android** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/android/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/android/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/android/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/android/updates.txt) |
| **Apple** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/apple/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/apple/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/apple/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/apple/updates.txt) |
| **Chromeos** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/chromeos/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/chromeos/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/chromeos/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/chromeos/updates.txt) |
| **Ios** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/ios/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/ios/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/ios/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/ios/updates.txt) |
| **Linux** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/linux/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/linux/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/linux/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/linux/updates.txt) |
| **Macos** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/macos/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/macos/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/macos/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/macos/updates.txt) |
| **Windows** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/windows/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/windows/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/windows/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/operating-systems/windows/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="iot"></a>
### 🏠 IoT & Smart Home

#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **2** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **13** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **29** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **82** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **85** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/ultimate.txt) |

<details>
<summary><strong>📂 Wirkungslisten anzeigen</strong></summary>


> 🛡️ **Privacy:** nur Tracking/Ads/Analytics/Telemetry/Diagnostics  
> ⚠️ **Restrict:** Privacy + optionale Hersteller-/Cloud-/Recommendation-Dienste  
> 🚫 **Isolate:** möglichst vollständige Herstellerkommunikation  
> 🔄 **Updates:** Update-Infrastruktur separat steuerbar

| Gerät / Hersteller | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
|---|---|---|---|---|
| **Amazon Alexa** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/amazon-alexa/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/amazon-alexa/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/amazon-alexa/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/amazon-alexa/updates.txt) |
| **Huawei** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/huawei/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/huawei/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/huawei/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/huawei/updates.txt) |
| **Samsung SmartThings** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/samsung-smartthings/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/samsung-smartthings/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/samsung-smartthings/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/samsung-smartthings/updates.txt) |
| **Shared / Other** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/shared-other/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/shared-other/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/shared-other/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/shared-other/updates.txt) |
| **Sonos** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/sonos/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/sonos/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/sonos/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/sonos/updates.txt) |
| **Xiaomi** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/xiaomi/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/xiaomi/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/xiaomi/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/iot-smart-home/xiaomi/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="voice"></a>
### 🎙️ Sprachassistenten

#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **7** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **16** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **38** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **107** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **112** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/ultimate.txt) |

<details>
<summary><strong>📂 Wirkungslisten anzeigen</strong></summary>


> 🛡️ **Privacy:** nur Tracking/Ads/Analytics/Telemetry/Diagnostics  
> ⚠️ **Restrict:** Privacy + optionale Hersteller-/Cloud-/Recommendation-Dienste  
> 🚫 **Isolate:** möglichst vollständige Herstellerkommunikation  
> 🔄 **Updates:** Update-Infrastruktur separat steuerbar

| Gerät / Hersteller | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
|---|---|---|---|---|
| **Alexa** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/alexa/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/alexa/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/alexa/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/alexa/updates.txt) |
| **Cortana** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/cortana/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/cortana/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/cortana/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/cortana/updates.txt) |
| **Google Assistant** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/google-assistant/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/google-assistant/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/google-assistant/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/google-assistant/updates.txt) |
| **Siri** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/siri/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/siri/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/siri/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/voice-assistants/siri/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="automotive"></a>
### 🚗 Automotive / Connected Cars

#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **42** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **105** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **188** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **663** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **665** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/ultimate.txt) |

<details>
<summary><strong>📂 Wirkungslisten anzeigen</strong></summary>


> 🛡️ **Privacy:** nur Tracking/Ads/Analytics/Telemetry/Diagnostics  
> ⚠️ **Restrict:** Privacy + optionale Hersteller-/Cloud-/Recommendation-Dienste  
> 🚫 **Isolate:** möglichst vollständige Herstellerkommunikation  
> 🔄 **Updates:** Update-Infrastruktur separat steuerbar

| Gerät / Hersteller | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
|---|---|---|---|---|
| **Audi** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/audi/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/audi/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/audi/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/audi/updates.txt) |
| **Bmw** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/bmw/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/bmw/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/bmw/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/bmw/updates.txt) |
| **Ford** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/ford/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/ford/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/ford/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/ford/updates.txt) |
| **Mercedes** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/mercedes/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/mercedes/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/mercedes/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/mercedes/updates.txt) |
| **Tesla** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/tesla/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/tesla/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/tesla/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/tesla/updates.txt) |
| **VW** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/vw/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/vw/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/vw/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/automotive/vw/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="nas-server"></a>
### 💾 NAS & Server

#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **1** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **3** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **11** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **63** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **65** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/ultimate.txt) |

<details>
<summary><strong>📂 Wirkungslisten anzeigen</strong></summary>


> 🛡️ **Privacy:** nur Tracking/Ads/Analytics/Telemetry/Diagnostics  
> ⚠️ **Restrict:** Privacy + optionale Hersteller-/Cloud-/Recommendation-Dienste  
> 🚫 **Isolate:** möglichst vollständige Herstellerkommunikation  
> 🔄 **Updates:** Update-Infrastruktur separat steuerbar

| Gerät / Hersteller | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
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

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="network-devices"></a>
### 🌐 Router & Netzwerkgeräte

#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **11** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **49** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **75** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **375** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **401** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/ultimate.txt) |

<details>
<summary><strong>📂 Wirkungslisten anzeigen</strong></summary>


> 🛡️ **Privacy:** nur Tracking/Ads/Analytics/Telemetry/Diagnostics  
> ⚠️ **Restrict:** Privacy + optionale Hersteller-/Cloud-/Recommendation-Dienste  
> 🚫 **Isolate:** möglichst vollständige Herstellerkommunikation  
> 🔄 **Updates:** Update-Infrastruktur separat steuerbar

| Gerät / Hersteller | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
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

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="providers"></a>
### 📡 ISP / Provider

#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **5** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **39** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **72** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **171** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **171** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/ultimate.txt) |

<details>
<summary><strong>📂 Wirkungslisten anzeigen</strong></summary>


> 🛡️ **Privacy:** nur Tracking/Ads/Analytics/Telemetry/Diagnostics  
> ⚠️ **Restrict:** Privacy + optionale Hersteller-/Cloud-/Recommendation-Dienste  
> 🚫 **Isolate:** möglichst vollständige Herstellerkommunikation  
> 🔄 **Updates:** Update-Infrastruktur separat steuerbar

| Gerät / Hersteller | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
|---|---|---|---|---|
| **1&1** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/1und1/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/1und1/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/1und1/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/1und1/updates.txt) |
| **Deutsche Glasfaser** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/deutsche-glasfaser/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/deutsche-glasfaser/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/deutsche-glasfaser/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/deutsche-glasfaser/updates.txt) |
| **O2** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/o2/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/o2/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/o2/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/o2/updates.txt) |
| **Telekom** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/telekom/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/telekom/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/telekom/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/telekom/updates.txt) |
| **Unitymedia** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/unitymedia/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/unitymedia/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/unitymedia/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/unitymedia/updates.txt) |
| **Vodafone** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/vodafone/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/vodafone/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/vodafone/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/providers/vodafone/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="ecosystems"></a>
### 🏢 Google, Microsoft, Apple & Amazon

#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **11.912** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **12.074** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **12.354** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **15.407** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **15.459** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/ultimate.txt) |

<details>
<summary><strong>📂 Wirkungslisten anzeigen</strong></summary>


> 🛡️ **Privacy:** nur Tracking/Ads/Analytics/Telemetry/Diagnostics  
> ⚠️ **Restrict:** Privacy + optionale Hersteller-/Cloud-/Recommendation-Dienste  
> 🚫 **Isolate:** möglichst vollständige Herstellerkommunikation  
> 🔄 **Updates:** Update-Infrastruktur separat steuerbar

| Gerät / Hersteller | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
|---|---|---|---|---|
| **Amazon** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/amazon/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/amazon/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/amazon/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/amazon/updates.txt) |
| **Apple** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/apple/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/apple/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/apple/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/apple/updates.txt) |
| **Google** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/google/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/google/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/google/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/google/updates.txt) |
| **Microsoft** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/microsoft/privacy.txt) | [Restrict](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/microsoft/restrict.txt) | [Isolate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/microsoft/isolate.txt) | [Updates](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/device-control/ecosystems/microsoft/updates.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="manufacturers"></a>
### 🏭 Herstellerlisten

Diese Übersicht zeigt für **jeden aktuell vorhandenen Hersteller** die konkreten Wirkungslisten.

| Gerät / Hersteller | 🛡️ Privacy | ⚠️ Restrict | 🚫 Isolate | 🔄 Updates |
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

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>


---
<a id="apps-group"></a>
## 📱 Apps & Dienste — Privacy / Block All

Bei Apps und Diensten wird zwischen **Privacy** und **Block All** unterschieden. Privacy reduziert Tracking/Analytics/Telemetrie; Block All soll den jeweiligen Dienst vollständig sperren.

<a id="streaming"></a>
### 📺 Streaming

#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **12** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **24** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **45** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **280** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **301** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/ultimate.txt) |

<details>
<summary><strong>📂 Wirkungslisten anzeigen</strong></summary>


> 🛡️ **Privacy:** Dienst soll weiter funktionieren; Tracking/Analytics/Telemetry werden reduziert.  
> 🚫 **Block All:** Dienst soll vollständig gesperrt werden.

| App / Dienst | 🛡️ Privacy | 🚫 Block All |
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

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="gaming"></a>
### 🎮 Gaming

#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **23** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **68** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **116** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **372** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **378** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/ultimate.txt) |

<details>
<summary><strong>📂 Plattform-Wirkungslisten anzeigen</strong></summary>


| App / Dienst | 🛡️ Privacy | 🚫 Block All |
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

#### Privacy-Speziallisten

| Spezialliste | 🛡️ Privacy |
|---|---|
| **Anti-Cheat Telemetry** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/anti-cheat-telemetry/privacy.txt) |
| **Game Analytics** | [Privacy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/service-blocking/gaming/game-analytics/privacy.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="social-media"></a>
### 💬 Social Media

#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **1.097** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **1.789** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **3.145** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **21.441** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **21.588** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/ultimate.txt) |

<details>
<summary><strong>📂 Wirkungslisten anzeigen</strong></summary>


> 🛡️ **Privacy:** Dienst soll weiter funktionieren; Tracking/Analytics/Telemetry werden reduziert.  
> 🚫 **Block All:** Dienst soll vollständig gesperrt werden.

| App / Dienst | 🛡️ Privacy | 🚫 Block All |
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

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="cloud-dev"></a>
### ☁️ Cloud, Server & Development

#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **65** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **165** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **301** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **1.486** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **1.491** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/ultimate.txt) |

<details>
<summary><strong>📂 Wirkungslisten anzeigen</strong></summary>


> 🛡️ **Privacy:** Dienst soll weiter funktionieren; Tracking/Analytics/Telemetry werden reduziert.  
> 🚫 **Block All:** Dienst soll vollständig gesperrt werden.

| App / Dienst | 🛡️ Privacy | 🚫 Block All |
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

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>


---
<a id="protection-group"></a>
## 🛡️ Vollständige Schutz-/Kontrolllisten

Diese Bereiche sind bewusste **Domain-Sperrlisten**. Ein Treffer soll für die zugewiesene Pi-hole-Gruppe nicht erreichbar sein.

<a id="family"></a>
### 👨‍👩‍👧 Family & Content

> 🚫 **Vollständige Domain-Sperre:** Gelistete Adult-/NSFW-/Gambling-/Drugs-/Violence-/Weapons-/Piracy-/Torrent-Domains sollen nicht erreichbar sein.


#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **998.924** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **1.419.159** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **1.430.117** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **1.769.650** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **2.347.190** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/ultimate.txt) |

#### Vollständige Content-Listen

<details>
<summary><strong>📂 Content-Listen anzeigen</strong></summary>

| Liste | Einträge | Status | Link |
|---|---:|:---:|---|
| **Adult** | **998.924** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/adult.txt) |
| **Dating** | **40** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/dating.txt) |
| **Drugs** | **55** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/drugs.txt) |
| **Gambling** | **420.536** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/gambling.txt) |
| **Misinformation** | **0** | 🟡 | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/misinformation.txt) |
| **Piracy** | **58** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/piracy.txt) |
| **Sexual Content** | **998.924** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/sexual-content.txt) |
| **Torrents** | **44** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/torrents.txt) |
| **Violence Gore** | **53** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/violence-gore.txt) |
| **Weapons** | **89** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/weapons.txt) |

> `Misinformation` bleibt bewusst optional und wird nicht automatisch als objektive Security-Kategorie behandelt.

</details>

<p align="right"><a href="#kinderschutz-navigation">⬆️ Family-Inhaltsverzeichnis</a></p>

---

<a id="kids-allow-only"></a>
### 🧒 Kids Allow-Only

`Kids Allow-Only` ist kein normales Denylist-Profil. Für eine eigene Pi-hole-Gruppe wird standardmäßig alles blockiert; nur ausdrücklich freigegebene Domains funktionieren.

<a id="kids-dateien"></a>
#### 📚 Kids-Allowlist-Dateien

| Datei | Zweck | Einträge | Liste |
|---|---|---:|---|
| `kids-de.txt` | Basis-Allowlist | **39** | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-de.txt) |
| `kids-education-de.txt` | Lernen, Schule, MINT, Geschichte | **17** | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-education-de.txt) |
| `kids-media-de.txt` | Kinderfernsehen, Audio, Nachrichten | **16** | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-media-de.txt) |
| `kids-games-de.txt` | geprüfte Kinderspiele | **18** | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-games-de.txt) |
| `kids-runtime-de.txt` | notwendige technische Hosts | **9** | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-runtime-de.txt) |


Die Basis-Allowlist enthält unter anderem fragFINN, Blinde Kuh, Seitenstark, Internet-ABC, KiKA, Kikaninchen, WDR Maus, Kindernetz, Kinderfilmwelt, HanisauLand, Kinderzeitmaschine, LegaKids, Meine Forscherwelt, Klassewasser, Abenteuer Regenwald, Naturdetektive, Ohrka und Auditorix.

<a id="kids-anleitung"></a>
#### 🛠️ Pi-hole v6 – Anleitung

1. Gruppe `Kids-AllowOnly` anlegen.
2. Kindergeräte dieser Gruppe zuweisen; die Default-Gruppenzuordnung bewusst prüfen.
3. Die RAW-URL von `family/kids-allow-only/kids-de.txt` als **Subscribed Allowlist** nur der Kids-Gruppe zuweisen.
4. Regex-Denylist `.*` nur derselben Gruppe zuweisen.
5. Gravity/Listen aktualisieren.
6. Eine freigegebene und eine nicht freigegebene Domain testen.
7. Geblockte Zusatzhosts erlaubter Seiten im Query Log prüfen und nur eindeutig notwendige Hosts in `kids-runtime-de.txt` aufnehmen.
8. Keine kompletten CDN-/Cloud-Zonen pauschal freigeben.
9. IPv4, IPv6 und mögliche DoH/DoT/VPN-Umgehung berücksichtigen.

> **Warnung:** `.*` niemals versehentlich der normalen Default-Gruppe zuweisen.

<p align="right"><a href="#kinderschutz-navigation">⬆️ Family-Inhaltsverzeichnis</a></p>

---
# 🧱 Teil 3 – Blocklisten-Katalog

---

<a id="security"></a>
### 🛡️ Security & Threat Intelligence

> 🚫 **Vollständige Domain-Sperre:** Malware-, Phishing-, Ransomware-, C2-, Scam- und andere Security-Ziele sollen nicht erreichbar sein.


#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **10.960** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **17.081** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **594.410** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **844.669** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **3.408.596** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/ultimate.txt) |

#### Full-/Speziallisten

<details>
<summary><strong>📂 Full-/Speziallisten anzeigen</strong></summary>

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Abuse** | **116.920** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/abuse.txt) |
| **Brand Impersonation** | **53.975** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/brand-impersonation.txt) |
| **Command Control** | **53** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/command-control.txt) |
| **Cryptocurrency** | **63** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/cryptocurrency.txt) |
| **Cryptomining** | **6.121** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/cryptomining.txt) |
| **Data Exfiltration** | **13** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/data-exfiltration.txt) |
| **Ddos** | **15** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/ddos.txt) |
| **Disposable Email** | **30** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/disposable-email.txt) |
| **Dns Security** | **386** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/dns-security.txt) |
| **Dynamic Dns** | **74** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/dynamic-dns.txt) |
| **Expired Domains** | **0** | 🟡 | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/expired-domains.txt) |
| **Exploits** | **38** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/exploits.txt) |
| **Badware Hosters** | **24** | ✅⚠️ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/badware-hosters.txt) |
| **Fake Shops** | **10.960** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/fake-shops.txt) |
| **Fake Software** | **229** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/fake-software.txt) |
| **Malicious Extensions** | **0** | 🟡 | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/malicious-extensions.txt) |
| **Malicious Redirects** | **83** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/malicious-redirects.txt) |
| **Malvertising** | **51.883** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/malvertising.txt) |
| **Malware** | **2.656.377** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/malware.txt) |
| **Newly Registered Domains** | **15.000** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/newly-registered-domains.txt) |
| **Nft** | **1.758** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/nft.txt) |
| **Parked Domains** | **25** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/parked-domains.txt) |
| **Phishing** | **577.332** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/phishing.txt) |
| **Pup Pua** | **33** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/pup-pua.txt) |
| **Ransomware** | **53** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/ransomware.txt) |
| **Remote Access** | **23** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/remote-access.txt) |
| **Scam** | **265.246** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/scam.txt) |
| **Scanners** | **143** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/scanners.txt) |
| **Spam** | **32** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/spam.txt) |
| **Surveillance** | **16** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/surveillance.txt) |
| **Suspicious Tlds** | **6.490** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/suspicious-tlds.txt) |
| **Typosquatting** | **53.975** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/typosquatting.txt) |

</details>

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="network"></a>
### 🔐 DNS, Netzwerk & Umgehung

> 🚫 **Network Control:** Gelistete DoH-/DoT-/VPN-/Proxy-/Tor-/DDNS-/Bypass-Endpunkte sollen gezielt nicht erreichbar sein.


#### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **31** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **49** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **64** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **309** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **945** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/ultimate.txt) |

#### Full-/Speziallisten

<details>
<summary><strong>📂 Full-/Speziallisten anzeigen</strong></summary>

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Adblock Bypass** | **88** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/adblock-bypass.txt) |
| **Dns Attacks** | **9** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/dns-attacks.txt) |
| **Dns Bypass** | **312** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/dns-bypass.txt) |
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

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="speziallisten"></a>
### 🧰 Speziallisten

Diese Listen sind **optionale Zusatzmodule** und ersetzen nicht die normalen Light/Normal/Pro/Pro++/Ultimate-Profile. Besonders aggressive Speziallisten zuerst in einer Testgruppe pruefen.

> **⚠️ Hinweis:** `Dynamic DNS`, `Badware Hoster`, `Most Abused TLDs`, `SafeSearch not supported` und Bypass-Listen koennen legitime Dienste deutlich einschraenken. `Most Abused TLDs` ist absichtlich **Adblock-Syntax** und keine normale Plain-Domain-Liste.

| Spezialliste | Zweck | Eintraege | Liste |
|---|---|---:|---|
| **Fake / Scam / Trap Sites** | Scam + Fake Shops + Fake Software als eine Liste | **265.318** | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/special/fake.txt) |
| **Pop-Up Ads** | Pop-up-/Pop-under-Werbenetze aus BRZ Ads | **517** | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/pop-up-ads.txt) |
| **Threat Intelligence Mini** | kompakte BRZ-TI-Stufe | **594.410** | [Mini](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/threat-intelligence/mini.txt) |
| **Threat Intelligence Medium** | mittlere BRZ-TI-Stufe | **844.669** | [Medium](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/threat-intelligence/medium.txt) |
| **Threat Intelligence Full** | kompletter BRZ-Security-Ultimate-Datenbestand als Standalone-Liste | **3.408.596** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/threat-intelligence/full.txt) |
| **Dynamic DNS** | bekannte DynDNS-Provider; sehr aggressiv | **74** | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/dynamic-dns.txt) |
| **Badware Hoster** | riskante Hosting-/Site-Builder-Roots mit hoher Malware-Konzentration | **24** | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/badware-hosters.txt) |
| **Most Abused TLDs** | ganze riskante TLDs/Suffixe; Adblock-Format | **130** | [Adblock](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/policies/adblock/most-abused-tlds.adblock) |
| **DNS Rebind Protection** | Resolver-Policy statt normaler Domainliste | – | [dnsmasq Policy](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/policies/dnsmasq/rebind.conf) |
| **DoH/VPN/Tor/Proxy Bypass** | kombinierte lokale Umgehungsliste | **312** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/special/doh-vpn-tor-proxy-bypass.txt) |
| **Encrypted DNS Only** | DoH + DoT + Private DNS | **102** | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/special/encrypted-dns-only.txt) |
| **SafeSearch not supported** | Suchmaschinen ohne SafeSearch-Unterstuetzung | **205** | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/safesearch-not-supported.txt) |
| **URL Shortener** | bekannte Kurzlink-Dienste | **255** | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/full/url-shorteners.txt) |
| **Anti Piracy** | Piracy/Illegal-Streaming | aktueller BRZ-Stand / optionaler Upstream | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/piracy.txt) |
| **Gambling Full** | kompletter BRZ-Gambling-Datensatz | **420.536** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/gambling.txt) |
| **Social Networks** | Social-Network-Sammelliste | **21.588** | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/special/social-networks.txt) |
| **NSFW** | Adult/NSFW-Spezialliste | **998.924** | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/nsfw.txt) |
| **Native Tracker** | integrierte Tracker von OS, Apps und Geraeten | **628** | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/native-tracking.txt) |

#### Manuell aktualisierbare Live-Varianten

Fuer sehr grosse oder schnell wechselnde Listen (z. B. **NRD/DGA, TIF-IP-Adressen, DoH-IP-Adressen, Anti-Piracy, Gambling Medium/Mini**) liegt bewusst **kein automatischer GitHub-Workflow** bei. Die Quellen sind in `config/special-upstreams.json` hinterlegt und koennen bei Bedarf manuell aktualisiert werden:

```bash
python3 scripts/update-special-lists.py --list
python3 scripts/update-special-lists.py hagezi_anti_piracy hagezi_gambling_medium hagezi_gambling_mini
```

Der Updater schreibt nur die explizit ausgewaehlten Dateien. Details: [`docs/SPECIAL_LISTS.md`](docs/SPECIAL_LISTS.md).

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="regional"></a>
### 🌍 Regionale Listen

Die Pfade sind vorbereitet. Sie werden nicht künstlich nach dem Muster „TLD = Region“ befüllt, weil das fachlich unzuverlässig wäre.

| Liste | Einträge | Status | Link |
|---|---:|:---:|---|
| **Cn** | **5.896** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/cn.txt) |
| **De** | **3.304** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/de.txt) |
| **Es** | **1.698** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/es.txt) |
| **Eu** | **31.996** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/eu.txt) |
| **Fr** | **2.123** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/fr.txt) |
| **It** | **2.307** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/it.txt) |
| **Jp** | **625** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/jp.txt) |
| **Kr** | **479** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/kr.txt) |
| **Ru** | **15.374** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/ru.txt) |
| **Uk** | **7.416** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/uk.txt) |
| **Us** | **6.302** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regional/us.txt) |


---
<a id="lizenz"></a>
## 📜 Quellen & Lizenz

Das Repository steht unter **GPL-3.0-only**. Die Domainbasis stammt aus dem statischen BlackRabbitZ-Snapshot mit seinen dokumentierten Quellen, darunter Block List Project, AnudeepND, NextDNS Native Tracking Protection, Perflyst, URLhaus, Phishing.Database und HaGeZi-Anteile.

HaGeZi dient zusätzlich als Referenz für kumulative Hauptstufen und getrennte Native-/Speziallisten. Es gibt **keine automatische Live-Synchronisation**.

Siehe [`THIRD_PARTY.md`](THIRD_PARTY.md), [`docs/SOURCES.md`](docs/SOURCES.md) und die `# Sources:`-Header der Listen.

<p align="right"><a href="#top">⬆️ Nach oben</a></p>

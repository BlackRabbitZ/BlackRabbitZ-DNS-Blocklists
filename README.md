<a id="top"></a>

<div align="center">

# 🐇 BlackRabbitZ DNS Blocklists

### Datenschutz • Werbung • Tracking • Telemetrie • Security • Geräte • Apps • Family

![Pi-hole](https://img.shields.io/badge/Pi--hole-kompatibel-96060C?logo=pihole&logoColor=white)
![Format](https://img.shields.io/badge/Format-Plain%20Domains-2ea44f)
![Profiles](https://img.shields.io/badge/Profile-Light%20%7C%20Normal%20%7C%20Pro%20%7C%20Pro%2B%2B%20%7C%20Ultimate-3178C6)
![Catalog](https://img.shields.io/badge/Katalog-100%20Kategorien-informational)

**Kumulative Hauptlisten für ganze Bereiche – plus Full-Listen für einzelne Hersteller, Dienste und Spezialklassen.**

</div>

---
<a id="projekt-navigation"></a>
## 📘 1. Inhaltsverzeichnis – Projekt & Nutzung

- [🚀 Schnellstart](#schnellstart)
- [📊 Globale Hauptlisten auf einen Blick](#hauptlisten)
- [🎚️ Schutzstufen Light bis Ultimate](#schutzstufen)
- [🧩 Hauptlisten & Full-Listen](#listenmodell)
- [🗺️ 100-Kategorien-Katalog](#katalog100)
- [📂 Repository-Struktur](#repo-struktur)
- [✅ Qualitätssicherung](#qualitaet)
- [⚠️ Hinweise & technische Grenzen](#grenzen)
- [📜 Quellen & Lizenz](#lizenz)

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

- [🕵️ Privacy & Tracking](#privacy)
- [📺 Smart TV](#smart-tv)
- [📱 Smartphones & Mobile](#mobile)
- [💻 Betriebssysteme](#betriebssysteme)
- [📺 Streaming](#streaming)
- [🎮 Gaming](#gaming)
- [💬 Social Media](#social-media)
- [🏢 Google, Microsoft, Apple & Amazon](#ecosystems)
- [🏠 IoT & Smart Home](#iot)
- [🎙️ Sprachassistenten](#voice)
- [🚗 Automotive / Connected Cars](#automotive)
- [💾 NAS & Server](#nas-server)
- [🌐 Router & Netzwerkgeräte](#network-devices)
- [📡 ISP / Provider](#providers)
- [☁️ Cloud, Server & Development](#cloud-dev)
- [🧩 Software & Hardware Telemetrie](#software-hardware)
- [🛡️ Security & Threat Intelligence](#security)
- [🔐 DNS, Netzwerk & Umgehung](#network)
- [🧰 Speziallisten](#speziallisten)
- [🤖 KI, Bots & Crawler](#automation)
- [🌍 Regionale Listen](#regional)
- [🏭 Herstellerlisten](#manufacturers)

---
# 📘 Teil 1 – Projekt & Nutzung

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
## 🎚️ Schutzstufen Light bis Ultimate

| Profil | Typischer Inhalt | Risiko |
|---|---|:---:|
| 🟩 **Light** | Werbung + besonders sichere Tracker | Minimal |
| 🟦 **Normal** | Light + Tracking/Analytics | Niedrig |
| 🟨 **Pro** | Normal + Telemetrie, Diagnostics, Native-/Device-Tracking | Niedrig–Mittel |
| 🟧 **Pro++** | Pro + aggressivere Hersteller-/Cloud-Endpunkte + Security-Basis | Mittel |
| 🟥 **Ultimate** | vollständige stabil integrierte Datenbestände | Hoch |

`Ultimate` kann je nach Bereich Cloudfunktionen, Logins, Stores, Updates oder andere Onlinefunktionen beeinträchtigen.

---
<a id="listenmodell"></a>
## 🧩 Hauptlisten & Full-Listen

Jeder große Bereich folgt demselben Modell:

```text
Light ⊂ Normal ⊂ Pro ⊂ Pro++ ⊂ Ultimate
```

Die **Hauptlisten** bündeln alle unterstützten Hersteller/Dienste eines Bereichs. **Full-Listen** sind Speziallisten für einzelne Hersteller, Dienste oder Schutztypen.

**Status:** ✅ = enthält Einträge. 🟡 = Pfad/Kategorie ist vollständig vorbereitet, aber im aktuellen statischen Quellstand fehlen belastbare Domain-Einträge. In den Datei-Headern zeigt `Data method`, ob eine Liste direkt aus einer Quelle übernommen, als Tier erzeugt oder konservativ aus bestehenden Domains neu einsortiert wurde.

---
<a id="katalog100"></a>
## 🗺️ 100-Kategorien-Katalog

Alle **100 Kategorien** des BRZ Pi-hole DNS-Listen & Kinderschutz-Handbuchs sind in [`docs/CATALOG_100.md`](docs/CATALOG_100.md) auf konkrete Repo-Pfade gemappt. Damit bleibt auch sichtbar, welche Spezialklassen bereits befüllt und welche nur vorbereitet sind.

---
<a id="repo-struktur"></a>
## 📂 Repository-Struktur

```text
profiles/
family/{main,content,kids-allow-only}/
allowlists/
policies/
lists/
├── privacy/
├── platforms/
│   ├── smart-tv/
│   ├── mobile/
│   ├── operating-systems/
│   ├── streaming/
│   ├── iot-smart-home/
│   ├── voice-assistants/
│   ├── automotive/
│   ├── nas-server/
│   ├── network-devices/
│   ├── providers/
│   └── software-hardware-telemetry/
├── apps/{gaming,social-media}/
├── ecosystems/
├── infrastructure/cloud-development/
├── security/
├── network/
├── automation/
├── regional/
└── manufacturers/
config/
docs/
metadata/
scripts/
```

---
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
# 👨‍👩‍👧 Teil 2 – Family & Kinderschutz

<a id="family"></a>
## 👨‍👩‍👧 Family & Content

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **998.924** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **1.419.159** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **1.430.117** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **1.769.650** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **2.347.190** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/ultimate.txt) |

### Vollständige Content-Listen

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

<p align="right"><a href="#kinderschutz-navigation">⬆️ Family-Inhaltsverzeichnis</a></p>

---
<a id="kids-allow-only"></a>
## 🧒 Kids Allow-Only

`Kids Allow-Only` ist kein normales Denylist-Profil. Für eine eigene Pi-hole-Gruppe wird standardmäßig alles blockiert; nur ausdrücklich freigegebene Domains funktionieren.

<a id="kids-dateien"></a>
### 📚 Kids-Allowlist-Dateien

| Datei | Zweck | Einträge | Liste |
|---|---|---:|---|
| `kids-de.txt` | Basis-Allowlist | **39** | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-de.txt) |
| `kids-education-de.txt` | Lernen, Schule, MINT, Geschichte | **17** | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-education-de.txt) |
| `kids-media-de.txt` | Kinderfernsehen, Audio, Nachrichten | **16** | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-media-de.txt) |
| `kids-games-de.txt` | geprüfte Kinderspiele | **0** | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-games-de.txt) |
| `kids-runtime-de.txt` | notwendige technische Hosts | **0** | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/kids-runtime-de.txt) |


Die Basis-Allowlist enthält unter anderem fragFINN, Blinde Kuh, Seitenstark, Internet-ABC, KiKA, Kikaninchen, WDR Maus, Kindernetz, Kinderfilmwelt, HanisauLand, Kinderzeitmaschine, LegaKids, Meine Forscherwelt, Klassewasser, Abenteuer Regenwald, Naturdetektive, Ohrka und Auditorix.

<a id="kids-anleitung"></a>
### 🛠️ Pi-hole v6 – Anleitung

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

<a id="privacy"></a>
## 🕵️ Privacy & Tracking

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **32.546** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **57.859** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **86.962** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **367.459** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **371.597** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/ultimate.txt) |

> **Privacy & Tracking – Ultimate:** Diese Stufe enthält die Vereinigung aller Full-/Speziallisten aus dem Bereich **Privacy & Tracking**. Die Stufen darunter sind kumulative, risikobasierte Teilmengen.

### Full-/Speziallisten

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

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="smart-tv"></a>
## 📺 Smart TV

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **346** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **362** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **454** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **636** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **648** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/ultimate.txt) |

### Full-/Speziallisten

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Amazon Fire Tv** | **19** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/amazon-fire-tv.txt) |
| **Google Android Tv** | **2** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/google-android-tv.txt) |
| **Google Tv** | **2** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/google-tv.txt) |
| **Hisense Vidaa** | **11** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/hisense-vidaa.txt) |
| **Lg Webos** | **355** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/lg-webos.txt) |
| **Panasonic** | **15** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/panasonic.txt) |
| **Philips** | **73** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/philips.txt) |
| **Roku** | **13** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/roku.txt) |
| **Samsung** | **51** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/samsung.txt) |
| **Shared Other** | **103** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/shared-other.txt) |
| **Sony Bravia** | **4** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/sony-bravia.txt) |
| **Tcl** | **2** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/tcl.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="mobile"></a>
## 📱 Smartphones & Mobile

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **391** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **445** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **531** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **993** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **1.004** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/ultimate.txt) |

### Full-/Speziallisten

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Apple Ios** | **121** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/full/apple-ios.txt) |
| **Google Android** | **18** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/full/google-android.txt) |
| **Google Pixel** | **18** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/full/google-pixel.txt) |
| **Huawei** | **38** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/full/huawei.txt) |
| **Motorola** | **31** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/full/motorola.txt) |
| **Oneplus** | **8** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/full/oneplus.txt) |
| **Oppo Realme** | **161** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/full/oppo-realme.txt) |
| **Samsung** | **4** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/full/samsung.txt) |
| **Shared Other** | **582** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/full/shared-other.txt) |
| **Vivo** | **53** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/full/vivo.txt) |
| **Xiaomi** | **9** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/full/xiaomi.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="betriebssysteme"></a>
## 💻 Betriebssysteme

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **20** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **48** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **104** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **302** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **311** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/ultimate.txt) |

### Full-/Speziallisten

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Android** | **135** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/full/android.txt) |
| **Apple** | **119** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/full/apple.txt) |
| **Chromeos** | **1** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/full/chromeos.txt) |
| **Ios** | **92** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/full/ios.txt) |
| **Linux** | **3** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/full/linux.txt) |
| **Macos** | **91** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/full/macos.txt) |
| **Windows** | **54** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/full/windows.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="streaming"></a>
## 📺 Streaming

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **12** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **24** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **45** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **280** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **301** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/main/ultimate.txt) |

### Full-/Speziallisten

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Apple Tv** | **18** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/full/apple-tv.txt) |
| **Dazn** | **3** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/full/dazn.txt) |
| **Disney Plus** | **6** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/full/disney-plus.txt) |
| **Emby** | **2** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/full/emby.txt) |
| **Jellyfin** | **1** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/full/jellyfin.txt) |
| **Netflix** | **25** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/full/netflix.txt) |
| **Paramount** | **9** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/full/paramount.txt) |
| **Plex** | **3** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/full/plex.txt) |
| **Prime Video** | **2** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/full/prime-video.txt) |
| **Spotify** | **185** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/full/spotify.txt) |
| **Twitch** | **22** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/full/twitch.txt) |
| **Youtube** | **25** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/streaming/full/youtube.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="gaming"></a>
## 🎮 Gaming

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **23** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **68** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **116** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **372** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **378** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/ultimate.txt) |

### Full-/Speziallisten

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Anti Cheat Telemetry** | **1** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/anti-cheat-telemetry.txt) |
| **Battle Net** | **5** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/battle-net.txt) |
| **Ea Origin** | **300** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/ea-origin.txt) |
| **Epic Games** | **7** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/epic-games.txt) |
| **Game Analytics** | **27** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/game-analytics.txt) |
| **Mobile Games** | **3** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/mobile-games.txt) |
| **Nintendo** | **5** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/nintendo.txt) |
| **Playstation** | **10** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/playstation.txt) |
| **Riot Games** | **2** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/riot-games.txt) |
| **Rockstar** | **3** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/rockstar.txt) |
| **Steam** | **1** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/steam.txt) |
| **Ubisoft** | **6** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/ubisoft.txt) |
| **Xbox** | **8** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/xbox.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="social-media"></a>
## 💬 Social Media

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **1.097** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **1.789** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **3.145** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **21.441** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **21.588** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/main/ultimate.txt) |

### Full-/Speziallisten

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Discord** | **9** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/full/discord.txt) |
| **Facebook Meta** | **82** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/full/facebook-meta.txt) |
| **Instagram** | **12** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/full/instagram.txt) |
| **Linkedin** | **23** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/full/linkedin.txt) |
| **Pinterest** | **12** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/full/pinterest.txt) |
| **Reddit** | **25** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/full/reddit.txt) |
| **Snapchat** | **11** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/full/snapchat.txt) |
| **Telegram** | **246** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/full/telegram.txt) |
| **Threads** | **10** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/full/threads.txt) |
| **Tiktok** | **61** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/full/tiktok.txt) |
| **Whatsapp** | **20** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/full/whatsapp.txt) |
| **X Twitter** | **21.121** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/full/x-twitter.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="ecosystems"></a>
## 🏢 Google, Microsoft, Apple & Amazon

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **11.912** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **12.074** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **12.354** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **15.407** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **15.459** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/main/ultimate.txt) |

### Full-/Speziallisten

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Amazon** | **775** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/full/amazon.txt) |
| **Apple** | **333** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/full/apple.txt) |
| **Google** | **13.584** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/full/google.txt) |
| **Microsoft** | **769** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ecosystems/full/microsoft.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="iot"></a>
## 🏠 IoT & Smart Home

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **2** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **13** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **29** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **82** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **85** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/main/ultimate.txt) |

### Full-/Speziallisten

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Amazon Alexa** | **13** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/full/amazon-alexa.txt) |
| **Huawei** | **37** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/full/huawei.txt) |
| **Samsung Smartthings** | **4** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/full/samsung-smartthings.txt) |
| **Shared Other** | **20** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/full/shared-other.txt) |
| **Sonos** | **2** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/full/sonos.txt) |
| **Xiaomi** | **9** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/full/xiaomi.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="voice"></a>
## 🎙️ Sprachassistenten

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **7** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **16** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **38** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **107** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **112** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/main/ultimate.txt) |

### Full-/Speziallisten

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Alexa** | **82** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/full/alexa.txt) |
| **Cortana** | **0** | 🟡 | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/full/cortana.txt) |
| **Google Assistant** | **3** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/full/google-assistant.txt) |
| **Siri** | **27** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/voice-assistants/full/siri.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="automotive"></a>
## 🚗 Automotive / Connected Cars

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **42** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **105** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **188** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **663** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **665** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/main/ultimate.txt) |

### Full-/Speziallisten

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Audi** | **491** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/full/audi.txt) |
| **Bmw** | **53** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/full/bmw.txt) |
| **Ford** | **31** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/full/ford.txt) |
| **Mercedes** | **33** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/full/mercedes.txt) |
| **Tesla** | **12** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/full/tesla.txt) |
| **Vw** | **45** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/automotive/full/vw.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="nas-server"></a>
## 💾 NAS & Server

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **1** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **3** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **11** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **63** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **65** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/ultimate.txt) |

### Full-/Speziallisten

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Docker** | **16** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/full/docker.txt) |
| **Hpe Dell** | **5** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/full/hpe-dell.txt) |
| **Kubernetes** | **25** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/full/kubernetes.txt) |
| **Qnap** | **6** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/full/qnap.txt) |
| **Redhat Openshift** | **5** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/full/redhat-openshift.txt) |
| **Synology** | **3** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/full/synology.txt) |
| **Truenas** | **3** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/full/truenas.txt) |
| **Unraid** | **2** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/full/unraid.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="network-devices"></a>
## 🌐 Router & Netzwerkgeräte

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **11** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **49** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **75** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **375** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **401** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/main/ultimate.txt) |

### Full-/Speziallisten

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Asus** | **29** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/full/asus.txt) |
| **Avm Fritzbox** | **1** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/full/avm-fritzbox.txt) |
| **Cisco** | **29** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/full/cisco.txt) |
| **Huawei** | **18** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/full/huawei.txt) |
| **Mikrotik** | **1** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/full/mikrotik.txt) |
| **Netgear** | **4** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/full/netgear.txt) |
| **Tp Link** | **17** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/full/tp-link.txt) |
| **Ubiquiti** | **301** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/full/ubiquiti.txt) |
| **Zyxel** | **1** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/network-devices/full/zyxel.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="providers"></a>
## 📡 ISP / Provider

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **5** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **39** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **72** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **171** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **171** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/main/ultimate.txt) |

### Full-/Speziallisten

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **1Und1** | **7** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/full/1und1.txt) |
| **Deutsche Glasfaser** | **0** | 🟡 | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/full/deutsche-glasfaser.txt) |
| **O2** | **18** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/full/o2.txt) |
| **Telekom** | **61** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/full/telekom.txt) |
| **Unitymedia** | **4** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/full/unitymedia.txt) |
| **Vodafone** | **81** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/providers/full/vodafone.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="cloud-dev"></a>
## ☁️ Cloud, Server & Development

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **65** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **165** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **301** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **1.486** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **1.491** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/main/ultimate.txt) |

### Full-/Speziallisten

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Aws** | **570** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/full/aws.txt) |
| **Azure** | **214** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/full/azure.txt) |
| **Cicd** | **8** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/full/cicd.txt) |
| **Cloud Storage** | **563** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/full/cloud-storage.txt) |
| **Cloudflare** | **42** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/full/cloudflare.txt) |
| **Github** | **24** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/full/github.txt) |
| **Gitlab** | **7** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/full/gitlab.txt) |
| **Google Cloud** | **49** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/full/google-cloud.txt) |
| **Jetbrains** | **2** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/full/jetbrains.txt) |
| **Oracle Cloud** | **8** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/full/oracle-cloud.txt) |
| **Visual Studio** | **3** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/full/visual-studio.txt) |
| **Vscode** | **4** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/infrastructure/cloud-development/full/vscode.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="software-hardware"></a>
## 🧩 Software & Hardware Telemetrie

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **0** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **28** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **73** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **76** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **84** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/main/ultimate.txt) |

### Full-/Speziallisten

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Adobe** | **60** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/full/adobe.txt) |
| **Amd** | **5** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/full/amd.txt) |
| **Autodesk** | **3** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/full/autodesk.txt) |
| **Corsair** | **0** | 🟡 | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/full/corsair.txt) |
| **Intel** | **4** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/full/intel.txt) |
| **Logitech** | **4** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/full/logitech.txt) |
| **Nvidia** | **7** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/full/nvidia.txt) |
| **Razer** | **1** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/software-hardware-telemetry/full/razer.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="security"></a>
## 🛡️ Security & Threat Intelligence

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **10.960** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **17.081** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **594.410** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **844.669** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **3.408.596** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/ultimate.txt) |

### Full-/Speziallisten

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Abuse** | **116.920** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/abuse.txt) |
| **Brand Impersonation** | **53.975** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/brand-impersonation.txt) |
| **Command Control** | **53** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/command-control.txt) |
| **Cryptocurrency** | **63** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/cryptocurrency.txt) |
| **Cryptomining** | **6.121** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/cryptomining.txt) |
| **Data Exfiltration** | **0** | 🟡 | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/data-exfiltration.txt) |
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
| **Newly Registered Domains** | **0** | 🟡 | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/newly-registered-domains.txt) |
| **Nft** | **1.758** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/nft.txt) |
| **Parked Domains** | **25** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/parked-domains.txt) |
| **Phishing** | **577.332** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/phishing.txt) |
| **Pup Pua** | **33** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/pup-pua.txt) |
| **Ransomware** | **53** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/ransomware.txt) |
| **Remote Access** | **23** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/remote-access.txt) |
| **Scam** | **265.246** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/scam.txt) |
| **Scanners** | **143** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/scanners.txt) |
| **Spam** | **32** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/spam.txt) |
| **Surveillance** | **0** | 🟡 | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/surveillance.txt) |
| **Suspicious Tlds** | **6.490** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/suspicious-tlds.txt) |
| **Typosquatting** | **53.975** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/typosquatting.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="network"></a>
## 🔐 DNS, Netzwerk & Umgehung

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **31** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **49** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **64** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **309** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **945** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/network/main/ultimate.txt) |

### Full-/Speziallisten

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

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="speziallisten"></a>
## 🧰 Speziallisten

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
| **Anti Piracy** | Piracy/Illegal-Streaming | **58** | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/piracy.txt) |
| **Gambling Full** | kompletter BRZ-Gambling-Datensatz | **420.536** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/gambling.txt) |
| **Social Networks** | Social-Network-Sammelliste | **21.588** | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/social-media/special/social-networks.txt) |
| **NSFW** | Adult/NSFW-Spezialliste | **998.924** | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/nsfw.txt) |
| **Native Tracker** | integrierte Tracker von OS, Apps und Geraeten | **628** | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/native-tracking.txt) |

### Manuell aktualisierbare Live-Varianten

Fuer sehr grosse oder schnell wechselnde Listen (z. B. **NRD/DGA, TIF-IP-Adressen, DoH-IP-Adressen, Anti-Piracy, Gambling Medium/Mini**) liegt bewusst **kein automatischer GitHub-Workflow** bei. Die Quellen sind in `config/special-upstreams.json` hinterlegt und koennen bei Bedarf manuell aktualisiert werden:

```bash
python3 scripts/update-special-lists.py --list
python3 scripts/update-special-lists.py hagezi_anti_piracy hagezi_gambling_medium hagezi_gambling_mini
```

Der Updater schreibt nur die explizit ausgewaehlten Dateien. Details: [`docs/SPECIAL_LISTS.md`](docs/SPECIAL_LISTS.md).

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="automation"></a>
## 🤖 KI, Bots & Crawler

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **13** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **28** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **33** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **49** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **300** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/main/ultimate.txt) |

### Full-/Speziallisten

| Liste | Einträge | Status | Full-Liste |
|---|---:|:---:|---|
| **Aggressive Crawlers** | **0** | 🟡 | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/aggressive-crawlers.txt) |
| **Ai Crawlers** | **0** | 🟡 | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/ai-crawlers.txt) |
| **Ai Scrapers** | **3** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/ai-scrapers.txt) |
| **Ai Telemetry** | **36** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/ai-telemetry.txt) |
| **Ai Tracking** | **43** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/ai-tracking.txt) |
| **Llm Crawlers** | **188** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/llm-crawlers.txt) |
| **Malicious Bots** | **1** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/malicious-bots.txt) |
| **Seo Bots** | **0** | 🟡 | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/seo-bots.txt) |
| **Training Bots** | **0** | 🟡 | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/training-bots.txt) |
| **Web Crawlers** | **62** | ✅ | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/automation/full/web-crawlers.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---
<a id="regional"></a>
## 🌍 Regionale Listen

Die regionalen Listen enthalten bereits als schädlich klassifizierte Domains mit regionalem ccTLD-Bezug. Sie blockieren **nicht** pauschal eine komplette Länder-TLD; die Zuordnung wird aus dem BRZ-Security-Datenbestand abgeleitet.

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
<a id="manufacturers"></a>
## 🏭 Herstellerlisten

Diese Listen bündeln bereichsübergreifend bereits bekannte Ads-/Tracking-/Telemetrie-Endpunkte eines Herstellers oder Dienstes.

| Liste | Einträge | Status | Link |
|---|---:|:---:|---|
| **Adobe** | **354** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/adobe.txt) |
| **Amazon** | **768** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/amazon.txt) |
| **Amd** | **5** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/amd.txt) |
| **Apple** | **330** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/apple.txt) |
| **Autodesk** | **15** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/autodesk.txt) |
| **Ea** | **298** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/ea.txt) |
| **Epic** | **8** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/epic.txt) |
| **Google** | **14.475** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/google.txt) |
| **Huawei** | **58** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/huawei.txt) |
| **Lg** | **601** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/lg.txt) |
| **Logitech** | **15** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/logitech.txt) |
| **Meta** | **111** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/meta.txt) |
| **Microsoft** | **754** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/microsoft.txt) |
| **Nintendo** | **10** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/nintendo.txt) |
| **Nvidia** | **17** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/nvidia.txt) |
| **Philips** | **73** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/philips.txt) |
| **Razer** | **8** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/razer.txt) |
| **Samsung** | **307** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/samsung.txt) |
| **Sony** | **143** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/sony.txt) |
| **Ubisoft** | **6** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/ubisoft.txt) |
| **Valve Steam** | **49** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/valve-steam.txt) |
| **Xiaomi** | **582** | ✅ | [Liste](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/manufacturers/xiaomi.txt) |

---
<a id="lizenz"></a>
## 📜 Quellen & Lizenz

Das Repository steht unter **GPL-3.0-only**. Die Domainbasis stammt aus dem statischen BlackRabbitZ-Snapshot mit seinen dokumentierten Quellen, darunter Block List Project, AnudeepND, NextDNS Native Tracking Protection, Perflyst, URLhaus, Phishing.Database und HaGeZi-Anteile.

HaGeZi dient zusätzlich als Referenz für kumulative Hauptstufen und getrennte Native-/Speziallisten. Es gibt **keine automatische Live-Synchronisation**.

Siehe [`THIRD_PARTY.md`](THIRD_PARTY.md), [`docs/SOURCES.md`](docs/SOURCES.md) und die `# Sources:`-Header der Listen.

<p align="right"><a href="#top">⬆️ Nach oben</a></p>

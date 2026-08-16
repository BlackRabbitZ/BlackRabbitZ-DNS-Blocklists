<div align="center">

# 🐇 BlackRabbitZ DNS Blocklists
### Datenschutz • Sicherheit • Werbung • Tracking • Telemetrie

[![License: GPL-3.0-only](https://img.shields.io/badge/License-GPL--3.0--only-blue.svg)](LICENSE)
![Pi-hole kompatibel](https://img.shields.io/badge/Pi--hole-Kompatibel-brightgreen)
![Statische Listen](https://img.shields.io/badge/Listen-Statisch-success)
![Maintainer](https://img.shields.io/badge/Maintainer-BlackRabbitZ-black)
![Endnutzer](https://img.shields.io/badge/Endnutzer-Kein%20Python-success)
[![Blocklisten aktualisieren](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/actions/workflows/update-lists.yml/badge.svg)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/actions/workflows/update-lists.yml)

**Statische, transparente DNS-Blocklisten für Pi-hole und kompatible DNS-Filterlösungen.**

</div>

<div align="center">

**🌐 Sprache / Language:** 🇩🇪 **Deutsch** · [🇬🇧 English](README_EN.md)

</div>

<a id="why-dns-blocklists"></a>
## 🛡️ Warum DNS-Blocklisten?

DNS-Blocklisten stoppen unerwünschte Verbindungen bereits bei der Namensauflösung. So lassen sich **Werbung, Tracker, Telemetrie und bekannte schädliche Domains zentral für das gesamte Netzwerk filtern**, ohne auf jedem Gerät zusätzliche Software installieren zu müssen.

---

<a id="contents"></a>
## 📑 Inhaltsverzeichnis

- [Warum DNS-Blocklisten?](#why-dns-blocklists) — kurz erklärt, welchen Nutzen DNS-Blocking im gesamten Netzwerk hat
- [Schnellstart](#quick-start) — empfohlene Standardliste und schnelle Pi-hole-Einrichtung
- [Datenschutzprofile](#protection-profiles) — Light, Balanced, Strict und Ultimate als abgestufte Schutzprofile
- [Schutzvergleich](#protection-comparison) — Funktionsumfang und Fehlfunktionsrisiko der Profile
  - [Optionale Schutzmodule](#optional-protection-modules) — Security und Family als gezielte Ergänzungen
  - [Große Profil-Teile](#large-profile-parts) — automatisch erzeugte Raw-Parts; künftig maximal 50 MiB pro Datei
- [Werbung & Tracking](#ads-tracking) — Werbung, Tracker, Affiliate-Tracking und Pop-Up-Werbung
- [Telemetrie & Geräte](#telemetry-devices) — Betriebssystem-, Geräte-, Smart-TV-, IoT- und Native-Tracker-Listen
- [Gaming-Datenschutz](#gaming-privacy) — Gaming-Telemetrie und optionale RegEx-Regeln
- [Sicherheitslisten](#security-lists) — Malware, Phishing, Scam, Fake, Threat Intelligence, NRD/DGA, DynDNS, Hoster und TLD-Schutz
- [DNS-, Web- & Bypass-Schutz](#dns-web-protection) — DoH/VPN/TOR/Proxy-Bypass, URL-Kürzer und DNS-Rebind-Schutz
- [Familienlisten](#family-lists) — Adult/NSFW, Glücksspiel, SafeSearch, Anti-Piracy und Social-Network-Blocking
- [Empfehlungen](#recommendations) — sinnvolle Kombinationen aus Profilen und Zusatzlisten
- [Online-DNS-Dienste](#online-dns-services) — Hinweise für externe DNS-Anbieter und mobile Nutzung
- [Upstream-Quellen & Build-Transparenz](#upstream-sources) — Quellen, Archiv-Snapshots, Metadaten und Prüfsummen
- [Repository-Struktur](#repository-structure) — Ordner, Konfigurationen, Skripte und erzeugte Listen
- [Automatische Listen-Updates](#automatic-updates) — tägliche Feeds und Builder für erweiterte Listen
- [Listen erweitern](#extending-lists) — Kategorien, Profile und erweiterte Listen ergänzen
- [Fehlblockierungen / False Positives](#false-positives) — Fehlblockierungen melden und Allowlist verwenden
- [Lizenz & Namensnennung](#license-attribution) — GPL-3.0, Drittquellen und Attribution

---

<a id="quick-start"></a>
## ⚡ Schnellstart

### ⭐ Empfehlung: Balanced

Für die meisten Nutzer ist **Balanced** der beste Einstieg. Es blockiert Werbung, allgemeine Tracker und Social-Tracking, lässt Affiliate-/Referral-Infrastruktur aber bewusst aus dem Standardprofil heraus, um vermeidbare Fehlfunktionen zu reduzieren.

```text
https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/balanced.txt
```

**Pi-hole**

1. Öffne die Pi-hole-Weboberfläche.
2. Gehe zu **Lists / Adlists**.
3. Füge die oben angezeigte Raw-URL hinzu.
4. Speichern.
5. Gravity aktualisieren.

---

<a id="protection-profiles"></a>
# 🚀 Datenschutzprofile

Das sind die Haupt-Schutzstufen. Starte mit **Balanced** und wechsle nur dann zu **Strict** oder **Ultimate**, wenn du bewusst aggressiver filtern möchtest.

<!-- MAIN_PROFILES_START -->
| Profil | Schutz | Einträge | Empfohlen für | Anzeigen | Raw |
|---|:---:|---:|---|:---:|:---:|
| 🟢 **Light** | Niedrig | **235.703** | Einfaches Werbeblocking | [Anzeigen](lists/combined/light.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/light.txt)** |
| 🔵 **Balanced ⭐** | Mittel | **373.196** | Die meisten Nutzer | [Anzeigen](lists/combined/balanced.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/balanced.txt)** |
| 🟠 **Strict** | Hoch | **375.065** | Datenschutzorientierte Setups | [Anzeigen](lists/combined/strict.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/strict.txt)** |
| 🔴 **Ultimate** | Maximum | **5.241.049** | Aggressive Filterung | [Teile anzeigen](#ultimate-parts) | **[Raw-Teile](#ultimate-parts)** |
<!-- MAIN_PROFILES_END -->

> **Balanced** wird für die meisten Installationen empfohlen.
> **Strict** ergänzt Affiliate-Tracking, Telemetrie, Geräte-Telemetrie sowie natives/App-Tracking.
> **Ultimate** ist bewusst aggressiv und kann telemetrieabhängige Funktionen, Smart-TV-Funktionen, App-Analysen, Gaming-Telemetrie und cloudgestützte Dienste beeinträchtigen. **Consent/CMP bleibt eine optionale Einzelkategorie und wird nicht in Ultimate erzwungen.**

---

<a id="protection-comparison"></a>
# 🎚️ Schutzvergleich

<!-- COMPARISON_START -->
| Funktion | Light | Balanced ⭐ | Strict | Security | Family | Ultimate |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Werbung | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| Allgemeine Tracker | — | ✅ | ✅ | — | ✅ | ✅ |
| Social-Tracking | — | ✅ | ✅ | — | ✅ | ✅ |
| Affiliate-Tracking | — | — | ✅ | — | — | ✅ |
| Allgemeine Telemetrie | — | — | ✅ | — | — | ✅ |
| Gaming-Telemetrie | — | — | — | — | — | ✅ |
| Windows-Telemetrie | — | — | ✅ | — | — | ✅ |
| Apple-Telemetrie | — | — | ✅ | — | — | ✅ |
| Android-Telemetrie | — | — | ✅ | — | — | ✅ |
| Linux-Telemetrie | — | — | ✅ | — | — | ✅ |
| NAS-Telemetrie | — | — | ✅ | — | — | ✅ |
| Server-Telemetrie | — | — | ✅ | — | — | ✅ |
| Mobil-/App-Tracking | — | — | ✅ | — | — | ✅ |
| Smart-TV / IoT | — | — | ✅ | — | — | ✅ |
| Kryptomining | — | — | — | ✅ | — | ✅ |
| Malware / Phishing / Betrug / Fake-Shops | — | — | — | ✅ | — | ✅ |
| Consent / CMP | — | — | — | — | — | — |
| Erwachsene Inhalte | — | — | — | — | ✅ | ✅ |
| Glücksspiel | — | — | — | — | ✅ | ✅ |
| Fehlfunktionsrisiko | 🟢 Niedrig | 🔵 Niedrig–Mittel | 🟠 Höher | 🟡 Mittel | 🟠 Höher | 🔴 Sehr hoch |
<!-- COMPARISON_END -->

<a id="optional-protection-modules"></a>
## 🧩 Optionale Schutzmodule

Diese Profile lösen andere Aufgaben als die Datenschutzstufen oben. Sie sollten als **Zusatzmodule** verstanden werden und nicht als „stärkere Versionen“ von Balanced oder Strict.

<!-- ADDON_PROFILES_START -->
| Profil | Schutz | Einträge | Empfohlen für | Anzeigen | Raw |
|---|:---:|---:|---|:---:|:---:|
| 🛡️ **Security** | Sicherheit | **3.469.292** | Sicherheitsorientierte Filterung | [Teile anzeigen](#security-parts) | **[Raw-Teile](#security-parts)** |
| 👨‍👩‍👧 **Family** | Familie | **1.848.646** | Familiennetzwerke | [Teile anzeigen](#family-parts) | **[Raw-Teile](#family-parts)** |
<!-- ADDON_PROFILES_END -->

- **Security** konzentriert sich auf Malware, Phishing, Betrug, Fake-Shops und Kryptomining. Es kann mit Balanced oder Strict kombiniert werden.
- **Family** ergänzt Werbe-/Tracking-Schutz um Filter für Erwachsenen-Inhalte und Glücksspiel.
- **Gaming-Datenschutz**, **Consent/CMP** und weitere Kategorielisten bleiben weiter unten separat auswählbar, damit nur das hinzugefügt wird, was tatsächlich gewünscht ist.

<a id="large-profile-parts"></a>
## 📦 Große Profil-Teile

Große kombinierte Profile werden deterministisch in größenbegrenzte Dateien aufgeteilt. Für vollständige Abdeckung müssen **alle Teile** eines gesplitteten Profils hinzugefügt werden. Die Dateinamen sind mit führender Null nummeriert, z. B. `security-part-01.txt`, und zielen künftig auf maximal **50 MiB pro Datei**. Beim ersten Build nach diesem Upgrade werden die bisherigen kleineren Parts automatisch zusammengeführt und neu erzeugt.

Du wechselst vom bisherigen `security.txt` / `family.txt` / `ultimate-N.txt`-Schema? Siehe [`docs/MIGRATION_V3.md`](docs/MIGRATION_V3.md).

<!-- SPLIT_PROFILES_START -->
<a id="security-parts"></a>
<details>
<summary><strong>🛡️ Security: Teile anzeigen (2 Dateien)</strong></summary>

**Gesamt: 3.469.292 eindeutige Domains.** Füge alle Teile zu Pi-hole oder deinem DNS-Blocker hinzu, um die vollständige Abdeckung dieses Profils zu erhalten.

| Security Teil | Security Teil |
|---|---|
| **Teil 01**  <br>**2.579.070** Einträge · 50.0 MiB  <br>[Anzeigen](lists/combined/security-part-01.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-01.txt)** | **Teil 02**  <br>**890.222** Einträge · 17.7 MiB  <br>[Anzeigen](lists/combined/security-part-02.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-02.txt)** |

</details>

<a id="family-parts"></a>
<details>
<summary><strong>👨‍👩‍👧 Family: Teile anzeigen (1 Dateien)</strong></summary>

**Gesamt: 1.848.646 eindeutige Domains.** Füge alle Teile zu Pi-hole oder deinem DNS-Blocker hinzu, um die vollständige Abdeckung dieses Profils zu erhalten.

| Family Teil | Family Teil |
|---|---|
| **Teil 01**  <br>**1.848.646** Einträge · 33.7 MiB  <br>[Anzeigen](lists/combined/family-part-01.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family-part-01.txt)** |  |

</details>

<a id="ultimate-parts"></a>
<details>
<summary><strong>🔴 Ultimate: Teile anzeigen (3 Dateien)</strong></summary>

**Gesamt: 5.241.049 eindeutige Domains.** Füge alle Teile zu Pi-hole oder deinem DNS-Blocker hinzu, um die vollständige Abdeckung dieses Profils zu erhalten.

| Ultimate Teil | Ultimate Teil |
|---|---|
| **Teil 01**  <br>**2.632.856** Einträge · 50.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-01.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-01.txt)** | **Teil 02**  <br>**2.600.402** Einträge · 50.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-02.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-02.txt)** |
| **Teil 03**  <br>**7.791** Einträge · 0.1 MiB  <br>[Anzeigen](lists/combined/ultimate-part-03.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-03.txt)** |  |

</details>
<!-- SPLIT_PROFILES_END -->



---

<a id="ads-tracking"></a>
# 📢 Werbung & Tracking

<!-- ADS_TRACKING_TABLE_START -->
| Liste | Einträge | Beschreibung | Anzeigen | Raw |
|---|---:|---|:---:|:---:|
| 📣 **Werbung** | 235.703 | Große Domain-Sammlung für Werbung, Werbeauslieferung und integrierte Pop-Up-Werbung | [Anzeigen](lists/categories/ads.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/ads.txt) |
| 👁️ **Tracker** | 143.967 | Große Sammlung von Analyse- und Tracking-Infrastruktur | [Anzeigen](lists/categories/trackers.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/trackers.txt) |
| 👥 **Social Tracker** | 99 | Tracking- und Analyse-Endpunkte sozialer Netzwerke | [Anzeigen](lists/categories/social-trackers.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/social-trackers.txt) |
| 📲 **Mobiles Tracking** | 823 | Mobile Attribution, SDK-Analysen, App-Tracking und integrierte TikTok-Native-Tracker | [Anzeigen](lists/categories/mobile-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/mobile-tracking.txt) |
| 🧩 **Natives/App-Tracking** | 1.467 | Natives Betriebssystem-/Geräte- und Anwendungs-Tracking | [Anzeigen](lists/categories/native-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/native-tracking.txt) |
| 🔗 **Affiliate-Tracking** | 643 | Affiliate-, Klick-, Referral- und Conversion-Tracking; ab Strict enthalten | [Anzeigen](lists/categories/affiliate-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/affiliate-tracking.txt) |
| 🍪 **Consent / CMP** | 44 | Optionales Blocking von Consent-Management/CMP mit erhöhtem Risiko für Website-Fehlfunktionen | [Anzeigen](lists/categories/consent-cmp.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/consent-cmp.txt) |
<!-- ADS_TRACKING_TABLE_END -->

> **Consent/CMP ist bewusst in keinem kombinierten Schutzprofil enthalten.** DNS-basiertes Blocking von Consent-Infrastruktur kann Seitenaufbau, Consent-Status und Website-Funktionen beeinträchtigen.

---

<a id="telemetry-devices"></a>
# 📡 Telemetrie & Geräte

<!-- TELEMETRY_TABLE_START -->
| Liste | Einträge | Beschreibung | Anzeigen | Raw |
|---|---:|---|:---:|:---:|
| 📊 **Allgemeine Telemetrie** | 29.324 | Breite Produkt-/App-Analysen, Diagnosen und Telemetrie | [Anzeigen](lists/categories/telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/telemetry.txt) |
| 🪟 **Windows-Telemetrie** | 459 | Windows-/Office-Diagnose, Telemetrie und integrierte Microsoft-Native-Tracker | [Anzeigen](lists/categories/windows-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/windows-telemetry.txt) |
| 🍎 **Apple-Telemetrie** | 135 | Apple-Telemetrie, Metriken, Diagnosen und integrierte Native-Tracker | [Anzeigen](lists/categories/apple-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/apple-telemetry.txt) |
| 🤖 **Android-Telemetrie** | 1.536 | Android-/Hersteller-Telemetrie inkl. Huawei, Samsung, Vivo, OPPO/Realme und Xiaomi | [Anzeigen](lists/categories/android-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/android-telemetry.txt) |
| 🐧 **Linux-Telemetrie** | 65 | Telemetrie, Diagnosen und Nutzungsberichte von Linux-Distributionen | [Anzeigen](lists/categories/linux-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/linux-telemetry.txt) |
| 💾 **NAS-Telemetrie** | 12 | NAS-Telemetrie und Nutzungsberichte (Synology, TrueNAS und weitere) | [Anzeigen](lists/categories/nas-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/nas-telemetry.txt) |
| 🖥️ **Server-Telemetrie** | 10 | Server-, Red-Hat-Insights- und Management-Telemetrie | [Anzeigen](lists/categories/server-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/server-telemetry.txt) |
| 📺 **Smart-TV** | 659 | Smart-TV-Werbung, ACR, Diagnosen, Telemetrie sowie integrierte LG-webOS-/Roku-Tracker | [Anzeigen](lists/categories/smart-tv.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/smart-tv.txt) |
| 🏠 **IoT** | 437 | Telemetrie-/Tracking-Endpunkte von IoT-, verbundenen und Amazon-Geräten/Diensten | [Anzeigen](lists/categories/iot.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/iot.txt) |
<!-- TELEMETRY_TABLE_END -->

> Gerätespezifische Listen und Native-Tracker können Empfehlungen, Diagnosen, Nutzungsberichte, ACR, Werbung oder andere cloudgestützte Funktionen deaktivieren.

---

<a id="gaming-privacy"></a>
# 🎮 Gaming-Datenschutz

| Liste | Einträge | Beschreibung | Anzeigen | Raw |
|---|---:|---|:---:|:---:|
| 🎮 **Gaming-Telemetrie** | 38 | Empfohlene Game-, Launcher-, Analyse- und Crash-Reporting-Endpunkte mit geringerem Fehlfunktionsrisiko | [Anzeigen](lists/categories/gaming-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gaming-telemetry.txt) |
| ⚠️ **Gaming-Telemetrie – Aggressiv** | 62 | Optionale zusätzliche Endpunkte mit höherem Risiko für Launcher-, Login- und Gameplay-Probleme | [Anzeigen](lists/categories/gaming-telemetry-aggressive.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gaming-telemetry-aggressive.txt) |
| 🧩 **Gaming-RegEx-Regeln** | 5 | Dynamische Pi-hole-Deny-Muster; einzeln importieren, nicht als normale Adlist | [Anzeigen](lists/regex/gaming-telemetry-regex.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/regex/gaming-telemetry-regex.txt) |

> Starte mit **Gaming-Telemetrie**. Die aggressive Liste und die RegEx-Regeln können Battle.net, Epic, Rockstar, Riot, EA und einzelne Spiele beeinträchtigen. Teste sie zuerst in einer separaten Pi-hole-Gruppe.

---

<a id="security-lists"></a>
# 🛡️ Sicherheitslisten

<!-- SECURITY_TABLE_START -->
| Liste | Einträge | Beschreibung | Anzeigen | Raw |
|---|---:|---|:---:|:---:|
| 🦠 **Malware** | 2.721.495 | Sehr große Sammlung von Malware-, Ransomware- und aktiven Malware-Hosts | [Anzeigen](lists/categories/malware.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/malware.txt) |
| 🎣 **Phishing** | 572.332 | Sehr große Sammlung aktiver und kuratierter Phishing-Domains | [Anzeigen](lists/categories/phishing.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/phishing.txt) |
| 💰 **Scam & Internet-Betrug** | 284.062 | Betrugs-, Fraud-, Fake-Angebots-, Kostenfallen- und täuschende Plattform-Domains | [Anzeigen](lists/categories/scam.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/scam.txt) |
| 🛒 **Fake-Shops** | 11.389 | Aggressive Sammlung potenzieller Fake-Shops und täuschender Shops | [Anzeigen](lists/categories/fake-shops.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/fake-shops.txt) |
| ⛏️ **Kryptomining** | 6.121 | Browser-/Remote-Mining-Infrastruktur; allgemeine Börsen sind ausgeschlossen | [Anzeigen](lists/categories/cryptomining.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/cryptomining.txt) |
| <a id="list-threat-intelligence"></a>🔐 **Threat Intelligence Feeds** | 4 Varianten | Zusätzliche Malware-, Phishing-, Scam-, Spam-, Kryptojacking- und C2-Indikatoren in mehreren Größen. | [Varianten](#list-threat-intelligence-variants) | — |
| <a id="list-nrd-dga"></a>🆕 **Neu registrierte Domains / NRD & DGA** | 8 Varianten | Zeitfenster für neu registrierte Domains sowie hochentropische DGA-Domains; sehr groß und besonders aggressiv. | [Varianten](#list-nrd-dga-variants) | — |
| <a id="list-dynamic-dns"></a>🔏 **Dynamic DNS** | 1.524 | Blockiert bekannte Dynamic-DNS-Dienste, die in Phishing- oder Malware-Kampagnen missbraucht werden können. | [Anzeigen](lists/categories/dynamic-dns.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/dynamic-dns.txt)** |
| <a id="list-badware-hoster"></a>💻 **Badware-Hoster** | 1.258 | Blockiert ganze Hosting-Anbieter-Domains, die wiederholt für schädliche Inhalte missbraucht wurden; hohes Fehlblockierungsrisiko. | [Anzeigen](lists/categories/badware-hoster.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/badware-hoster.txt)** |
| <a id="list-most-abused-tlds"></a>🔮 **Besonders missbrauchte TLDs** | 147 | Aggressive Regeln zum Sperren ganzer, häufig missbrauchter Top-Level-Domains; im Pi-hole-kompatiblen Adblock-Format archiviert. | [Anzeigen](lists/categories/most-abused-tlds.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/most-abused-tlds.txt)** |

<a id="list-threat-intelligence-variants"></a>
<details>
<summary><strong>🔐 Threat Intelligence Feeds: Varianten anzeigen</strong></summary>

| Variante | Einträge | Anzeigen | Raw |
|---|---:|:---:|:---:|
| **Voll** | 1.742.603 | [Anzeigen](lists/categories/threat-intelligence-full.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/threat-intelligence-full.txt)** |
| **Medium** | 388.528 | [Anzeigen](lists/categories/threat-intelligence-medium.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/threat-intelligence-medium.txt)** |
| **Mini** | 290.044 | [Anzeigen](lists/categories/threat-intelligence-mini.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/threat-intelligence-mini.txt)** |
| **IPv4** | 55.692 | [Anzeigen](lists/ips/threat-intelligence-ipv4.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ips/threat-intelligence-ipv4.txt)** |

</details>
<a id="list-nrd-dga-variants"></a>
<details>
<summary><strong>🆕 Neu registrierte Domains / NRD & DGA: Varianten anzeigen</strong></summary>

| Variante | Einträge | Anzeigen | Raw |
|---|---:|:---:|:---:|
| **NRD 1–7 Tage** | 2.474.849 | [Anzeigen](lists/categories/nrd-01-07.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/nrd-01-07.txt)** |
| **NRD 8–14 Tage** | 2.628.672 | [Anzeigen](lists/categories/nrd-08-14.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/nrd-08-14.txt)** |
| **NRD 15–21 Tage** | 2.428.426 | [Anzeigen](lists/categories/nrd-15-21.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/nrd-15-21.txt)** |
| **NRD 22–28 Tage** | 2.922.658 | [Anzeigen](lists/categories/nrd-22-28.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/nrd-22-28.txt)** |
| **NRD 29–35 Tage** | 2.298.771 | [Anzeigen](lists/categories/nrd-29-35.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/nrd-29-35.txt)** |
| **DGA 7 Tage** | 539.743 | [Anzeigen](lists/categories/dga-7.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/dga-7.txt)** |
| **DGA 14 Tage** | 1.125.605 | [Anzeigen](lists/categories/dga-14.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/dga-14.txt)** |
| **DGA 30 Tage** | 2.461.156 | [Anzeigen](#dga-30-parts) | **[Teile](#dga-30-parts)** |

<a id="dga-30-parts"></a>
<details>
<summary><strong>DGA 30 Tage: 2 Teile anzeigen</strong></summary>

| Teil | Teil |
|---|---|
| **Teil 01**  <br>**2.220.726** Einträge · 50.0 MiB  <br>[Anzeigen](lists/categories/dga-30-part-01.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/dga-30-part-01.txt)** | 2.220.726 |

</details>

</details>
<!-- SECURITY_TABLE_END -->

> Sicherheits- und Threat-Intelligence-Listen können sehr groß und aggressiv sein. **NRD/DGA, Badware-Hoster und TLD-Regeln** haben ein besonders hohes Fehlblockierungsrisiko und sollten gezielt eingesetzt werden.

---

<a id="dns-web-protection"></a>
# 🌐 DNS-, Web- & Bypass-Schutz

Diese optionalen Module richten sich gegen **DNS-Umgehung, DNS-Rebinding und verschleierte Weiterleitungen**. Sie sind nicht Bestandteil der normalen Datenschutzprofile und sollten gezielt eingesetzt werden.

<!-- SPECIAL_NETWORK_START -->
| Liste | Einträge | Beschreibung | Anzeigen | Raw |
|---|---:|---|:---:|:---:|
| <a id="list-dns-bypass"></a>📤 **DoH/VPN/TOR/Proxy-Bypass** | 3 Varianten | Blockiert bekannte verschlüsselte DNS-, VPN-, TOR- und Proxy-Endpunkte, die lokale DNS-Filter umgehen können. | [Varianten](#list-dns-bypass-variants) | — |
| <a id="list-url-shortener"></a>📲 **URL-Kürzer** | 9.904 | Blockiert bekannte Link-/URL-Shortener; für normale Heimnetze bewusst als sehr aggressiv markiert. | [Anzeigen](lists/categories/url-shortener.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/url-shortener.txt)** |
| <a id="list-dns-rebind-protection"></a>🛡️ **DNS-Rebind-Schutz** | — | Pi-hole-/dnsmasq-Konfiguration gegen DNS-Rebinding; keine normale statische Domain-Adlist. | [Dokumentation](docs/DNS_REBIND_PROTECTION.md) | — |

<a id="list-dns-bypass-variants"></a>
<details>
<summary><strong>📤 DoH/VPN/TOR/Proxy-Bypass: Varianten anzeigen</strong></summary>

| Variante | Einträge | Anzeigen | Raw |
|---|---:|:---:|:---:|
| **Voll** | 16.965 | [Anzeigen](lists/categories/dns-bypass-full.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/dns-bypass-full.txt)** |
| **Nur DoH** | 3.384 | [Anzeigen](lists/categories/doh-only.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/doh-only.txt)** |
| **DoH IPv4** | 1.395 | [Anzeigen](lists/ips/doh-ipv4.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/ips/doh-ipv4.txt)** |

</details>
<!-- SPECIAL_NETWORK_END -->

---

<a id="family-lists"></a>
# 👨‍👩‍👧 Familienlisten

<!-- FAMILY_TABLE_START -->
| Liste | Einträge | Beschreibung | Anzeigen | Raw |
|---|---:|---|:---:|:---:|
| 🔞 **Erwachsene Inhalte / NSFW** | 1.028.840 | Sehr große Domain-Sammlung für Erwachsenen-/NSFW-Inhalte und Pornografie | [Anzeigen](lists/categories/adult.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/adult.txt) |
| 🎰 **Glücksspiel** | 449.723 | Sehr große Domain-Sammlung für Wetten, Casinos und Glücksspiel · [optionale Varianten](#list-gambling-variants) | [Anzeigen](lists/categories/gambling.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gambling.txt) |
| <a id="list-safesearch-unsupported"></a>🔍 **Suchmaschinen ohne SafeSearch** | 206 | Blockiert Suchmaschinen, die keine SafeSearch-Funktion unterstützen. | [Anzeigen](lists/categories/safesearch-unsupported.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/safesearch-unsupported.txt)** |
| <a id="list-anti-piracy"></a>💀 **Anti-Piracy** | 39.740 | Blockiert Domains und Dienste, die überwiegend für nicht autorisierte Verbreitung urheberrechtlich geschützter Inhalte genutzt werden. | [Anzeigen](lists/categories/anti-piracy.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/anti-piracy.txt)** |
| <a id="list-social-networks"></a>💬 **Soziale Netzwerke sperren** | 898 | Blockiert den Zugriff auf klassische soziale Netzwerke; Messaging und Streaming sind nicht automatisch gleichbedeutend damit. | [Anzeigen](lists/categories/social-networks.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/social-networks.txt)** |

<a id="list-gambling-variants"></a>
<details>
<summary><strong>🎰 Glücksspiel: Varianten anzeigen</strong></summary>

| Variante | Einträge | Anzeigen | Raw |
|---|---:|:---:|:---:|
| **Medium** | 142.337 | [Anzeigen](lists/categories/gambling-medium.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gambling-medium.txt)** |
| **Mini** | 93.306 | [Anzeigen](lists/categories/gambling-mini.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gambling-mini.txt)** |

</details>
<!-- FAMILY_TABLE_END -->

> Familien- und Inhaltsfilter bleiben bewusst optional. So kannst du Erwachsenen-Inhalte, Glücksspiel, SafeSearch, Social Networks und Anti-Piracy passend zu deinem Netzwerk kombinieren.

---

<a id="recommendations"></a>
# 💡 Empfehlungen

BlackRabbitZ trennt **Datenschutzprofile**, **Schutzmodule** und **aggressive erweiterte Listen**, damit nicht jede Funktion automatisch in einem riesigen All-in-one-Profil landet.

| Ziel | Empfehlung |
|---|---|
| Möglichst problemlos Werbung/Tracking reduzieren | **Balanced ⭐** |
| Mehr Datenschutz und Telemetrie-Blocking | **Strict** |
| Zusätzlicher Bedrohungsschutz | **Balanced oder Strict + Security** |
| Familiennetzwerk | **Family** und bei Bedarf gezielt SafeSearch-/Social-/Bypass-Module |
| Maximales integriertes Blocking | **Ultimate**, nur wenn du Fehlblockierungen selbst beheben kannst |
| Zusätzliche Threat Intelligence | zuerst **TIF Mini/Medium**, Full nur bei ausreichend Ressourcen |
| NRD/DGA, Badware-Hoster, URL-Shortener, TLD-Blocking | nur für bewusst aggressive oder besonders sensible Umgebungen |

DNS-Blocking kann viel Werbung, Tracking und bekannte schädliche Infrastruktur abfangen, aber **nicht jeden Inhalt auf Webseiten ersetzen oder filtern**. Für browserseitige Elemente ist zusätzlich ein guter Content-Blocker sinnvoll.

---

<a id="online-dns-services"></a>
# 🏬 Online-DNS-Dienste

BlackRabbitZ ist in erster Linie für **selbst verwaltete DNS-Filter** wie Pi-hole gedacht. Die veröffentlichten reinen Domainlisten können auch in anderen Produkten verwendet werden, sofern der jeweilige Dienst eigene Blocklisten unterstützt.

| Einsatz | Empfehlung |
|---|---|
| Heimnetz / volle Kontrolle | Pi-hole oder ein vergleichbarer selbst gehosteter DNS-Filter |
| Mobil außerhalb des Heimnetzes | eigener DNS-Zugang per VPN/Tunnel oder ein externer DNS-Dienst mit benutzerdefinierten Listen |
| IPv4-erweiterte Listen | nur in Produkten/Firewalls einsetzen, die IP-/Netzlisten ausdrücklich unterstützen |
| DNS-Rebind-Schutz | integrierte Rebind-Funktion des DNS-Resolvers verwenden; siehe [Dokumentation](docs/DNS_REBIND_PROTECTION.md) |

> Welche externen DNS-Anbieter benutzerdefinierte Listen unterstützen, kann sich ändern. Deshalb behauptet BlackRabbitZ hier keine dauerhaft gültige Verfügbarkeit einzelner Anbieter und veröffentlicht stattdessen portable Raw-Listen.

---

<a id="upstream-sources"></a>
# 🌐 Upstream-Quellen & Build-Transparenz

Die großen Kategorielisten kombinieren und deduplizieren ausgewählte Upstream-DNS-/Threat-Intelligence-Datensätze. Details zu Quellen und Lizenzen sind in [`THIRD_PARTY.md`](THIRD_PARTY.md) dokumentiert.

- Kategoriedateien werden als reine Domains veröffentlicht, eine Domain pro Zeile.
- `.github/workflows/daily-upstream-update.yml` prüft täglich die konfigurierten Upstream-Feeds und importiert neue Domains additiv.
- `scripts/update-upstreams.py` validiert, normalisiert, dedupliziert und prüft Upstream-Daten auf Sicherheitsgrenzen, bevor Kategoriedateien geändert werden.
- `config/profiles.json` ist die zentrale Quelle für Profilzusammensetzung, Anzeigemetadaten und Split-Verhalten.
- `scripts/update-lists.sh` baut nach Kategorieänderungen alle kombinierten Profile, Metadaten, Prüfsummen und README-Werte neu.
- Upstream-URLs und quellenbezogene Sicherheitsgrenzen bleiben in [`scripts/upstream-sources.json`](scripts/upstream-sources.json).
- [`metadata/build.json`](metadata/build.json) enthält maschinenlesbare Zähler, Part-Dateien, Größen und SHA-256-Hashes.
- [`metadata/SHA256SUMS`](metadata/SHA256SUMS) enthält Prüfsummen für alle veröffentlichten Kategorie- und kombinierten Listen.

Siehe [`docs/AUTOMATIC_UPDATES.md`](docs/AUTOMATIC_UPDATES.md) für den vollständigen Update- und Fail-Safe-Ablauf.

---

<a id="repository-structure"></a>
# 📂 Repository-Struktur

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
    │   └── ... weitere nummerierte Teile
    │
    ├── regex/
    │   └── gaming-telemetry-regex.txt
    │
    └── categories/
        └── ... einzelne Kategorielisten
```

Jede veröffentlichte Blockliste bleibt eine normale **statische Textdatei** und kann direkt von Pi-hole oder kompatiblen DNS-Filtern verwendet werden. Die Repository-Pflege nutzt **Python, Bash und GitHub Actions**; Endnutzer benötigen weiterhin keine Python-Laufzeitumgebung.

---

<a id="automatic-updates"></a>
# 🔄 Automatische Listen-Updates

Zwei GitHub Actions halten das Repository aktuell:

1. **Daily upstream refresh** läuft täglich um `03:17 UTC`. Der Workflow lädt die konfigurierten öffentlichen Feeds, normalisiert deren Domains und **fügt neu veröffentlichte Einträge** den passenden Kategoriedateien hinzu.
2. **Update blocklists** läuft nach Änderungen an Kategorien, Profilkonfiguration oder Build-Skripten und hält die generierten Dateien synchron.

Die Build-Pipeline:

```text
Upstreams / Kategorieänderungen
        ↓
Normalisieren + validieren + Allowlist
        ↓
Kategoriedateien
        ↓
Profilkonfiguration
        ↓
Zusammenführen + deduplizieren + sortieren
        ↓
Große Profile aufteilen (max. 50-MiB-Teile)
        ↓
Sortierung / Eindeutigkeit / Part-Größen prüfen
        ↓
build.json + SHA256SUMS erzeugen
        ↓
README-Dateien synchronisieren
```

Automatische Upstream-Importe bleiben **additiv**: Der Updater kann die Listen automatisch erweitern, löscht aber nicht still vorhandene BlackRabbitZ-Einträge. Spezialisierte Gaming-/Linux-/NAS-/Server-Telemetrielisten können manuell kuratiert bleiben, wenn keine ausreichend vertrauenswürdige allgemeine Upstream-Quelle existiert.

---

<a id="extending-lists"></a>
# ➕ Listen erweitern

Um Domains zu einer vorhandenen Kategorie hinzuzufügen, bearbeite die entsprechende Datei unter:

```text
lists/categories/
```

Füge eine Domain pro Zeile hinzu. Nach einer Kategorieänderung berechnet die GitHub Action die Eintragszahlen neu und baut jedes betroffene kombinierte Profil automatisch neu.

Um zu ändern, welche Kategorien zu einem Profil gehören, bearbeite:

```text
config/profiles.json
```

Bearbeite generierte kombinierte Profil-Teile, `metadata/build.json` oder `metadata/SHA256SUMS` **nicht manuell**.

---

<a id="false-positives"></a>
# ⚠️ Fehlblockierungen / False Positives

Mehr blockierte Domains bedeuten nicht automatisch besseren Schutz.

Wenn eine Liste eine Website, Anwendung oder ein Gerät beeinträchtigt, nutze das Issue-Template **False positive** und nenne die betroffene Domain, Liste/das Profil, Anwendung/das Gerät, die konkrete Fehlfunktion und Reproduktionsschritte.

Das Ziel ist eine nützliche Blockliste – nicht die größtmögliche Anzahl an Domains.

---

<a id="license-attribution"></a>
# 📜 Lizenz & Namensnennung

Dieses Repository steht unter der **GNU GPL v3 (`GPL-3.0-only`)**.

**Copyright © 2026 BlackRabbitZ**

Original-Repository:

```text
https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists
```

Siehe:

- [`LICENSE`](LICENSE)
- [`NOTICE`](NOTICE)
- [`ATTRIBUTION.md`](ATTRIBUTION.md)
- [`THIRD_PARTY.md`](THIRD_PARTY.md)

---

<div align="center">

### 🐇 BlackRabbitZ DNS Blocklists

**Datenschutz. Sicherheit. Kontrolle.**

⭐ Wenn dir dieses Projekt hilft, kannst du das Repository mit einem Star unterstützen.

</div>

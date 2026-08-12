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

---

<a id="contents"></a>
## 📑 Inhaltsverzeichnis

- [Schnellstart](#quick-start)
- [Datenschutzprofile](#protection-profiles)
- [Schutzvergleich](#protection-comparison)
  - [Optionale Schutzmodule](#optional-protection-modules)
  - [Große Profil-Teile](#large-profile-parts)
- [Werbung & Tracking](#ads-tracking)
- [Telemetrie & Geräte](#telemetry-devices)
- [Gaming-Datenschutz](#gaming-privacy)
- [Sicherheitslisten](#security-lists)
- [Familienlisten](#family-lists)
- [Upstream-Quellen & Build-Transparenz](#upstream-sources)
- [Repository-Struktur](#repository-structure)
- [Automatische Listen-Updates](#automatic-updates)
- [Listen erweitern](#extending-lists)
- [Fehlblockierungen / False Positives](#false-positives)
- [Lizenz & Namensnennung](#license-attribution)

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
| 🟢 **Light** | Niedrig | **234.038** | Einfaches Werbeblocking | [Anzeigen](lists/combined/light.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/light.txt)** |
| 🔵 **Balanced ⭐** | Mittel | **371.544** | Die meisten Nutzer | [Anzeigen](lists/combined/balanced.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/balanced.txt)** |
| 🟠 **Strict** | Hoch | **372.540** | Datenschutzorientierte Setups | [Anzeigen](lists/combined/strict.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/strict.txt)** |
| 🔴 **Ultimate** | Maximum | **5.169.014** | Aggressive Filterung | [Teile anzeigen](#ultimate-parts) | **[Raw-Teile](#ultimate-parts)** |
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
| 🛡️ **Security** | Sicherheit | **3.458.013** | Sicherheitsorientierte Filterung | [Teile anzeigen](#security-parts) | **[Raw-Teile](#security-parts)** |
| 👨‍👩‍👧 **Family** | Familie | **1.788.212** | Familiennetzwerke | [Teile anzeigen](#family-parts) | **[Raw-Teile](#family-parts)** |
<!-- ADDON_PROFILES_END -->

- **Security** konzentriert sich auf Malware, Phishing, Betrug, Fake-Shops und Kryptomining. Es kann mit Balanced oder Strict kombiniert werden.
- **Family** ergänzt Werbe-/Tracking-Schutz um Filter für Erwachsenen-Inhalte und Glücksspiel.
- **Gaming-Datenschutz**, **Consent/CMP** und weitere Kategorielisten bleiben weiter unten separat auswählbar, damit nur das hinzugefügt wird, was tatsächlich gewünscht ist.

<a id="large-profile-parts"></a>
## 📦 Große Profil-Teile

Große kombinierte Profile werden deterministisch in größenbegrenzte Dateien aufgeteilt. Für vollständige Abdeckung müssen **alle Teile** eines gesplitteten Profils hinzugefügt werden. Die Dateinamen sind mit führender Null nummeriert, z. B. `security-part-01.txt`, und zielen auf maximal **5 MiB pro Datei**.

Du wechselst vom bisherigen `security.txt` / `family.txt` / `ultimate-N.txt`-Schema? Siehe [`docs/MIGRATION_V3.md`](docs/MIGRATION_V3.md).

<!-- SPLIT_PROFILES_START -->
<a id="security-parts"></a>
<details>
<summary><strong>🛡️ Security: Teile anzeigen (14 Dateien)</strong></summary>

**Gesamt: 3.458.013 eindeutige Domains.** Füge alle Teile zu Pi-hole oder deinem DNS-Blocker hinzu, um die vollständige Abdeckung dieses Profils zu erhalten.

| Security Teil | Security Teil |
|---|---|
| **Teil 01**  <br>**264.378** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/security-part-01.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-01.txt)** | **Teil 02**  <br>**232.052** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/security-part-02.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-02.txt)** |
| **Teil 03**  <br>**247.129** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/security-part-03.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-03.txt)** | **Teil 04**  <br>**259.204** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/security-part-04.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-04.txt)** |
| **Teil 05**  <br>**263.085** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/security-part-05.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-05.txt)** | **Teil 06**  <br>**263.525** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/security-part-06.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-06.txt)** |
| **Teil 07**  <br>**270.072** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/security-part-07.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-07.txt)** | **Teil 08**  <br>**260.007** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/security-part-08.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-08.txt)** |
| **Teil 09**  <br>**256.986** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/security-part-09.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-09.txt)** | **Teil 10**  <br>**260.279** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/security-part-10.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-10.txt)** |
| **Teil 11**  <br>**280.775** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/security-part-11.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-11.txt)** | **Teil 12**  <br>**242.092** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/security-part-12.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-12.txt)** |
| **Teil 13**  <br>**221.927** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/security-part-13.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-13.txt)** | **Teil 14**  <br>**136.502** Einträge · 2.6 MiB  <br>[Anzeigen](lists/combined/security-part-14.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security-part-14.txt)** |

</details>

<a id="family-parts"></a>
<details>
<summary><strong>👨‍👩‍👧 Family: Teile anzeigen (7 Dateien)</strong></summary>

**Gesamt: 1.788.212 eindeutige Domains.** Füge alle Teile zu Pi-hole oder deinem DNS-Blocker hinzu, um die vollständige Abdeckung dieses Profils zu erhalten.

| Family Teil | Family Teil |
|---|---|
| **Teil 01**  <br>**287.739** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/family-part-01.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family-part-01.txt)** | **Teil 02**  <br>**267.873** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/family-part-02.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family-part-02.txt)** |
| **Teil 03**  <br>**268.779** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/family-part-03.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family-part-03.txt)** | **Teil 04**  <br>**274.756** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/family-part-04.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family-part-04.txt)** |
| **Teil 05**  <br>**269.955** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/family-part-05.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family-part-05.txt)** | **Teil 06**  <br>**266.287** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/family-part-06.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family-part-06.txt)** |
| **Teil 07**  <br>**152.823** Einträge · 2.7 MiB  <br>[Anzeigen](lists/combined/family-part-07.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family-part-07.txt)** |  |

</details>

<a id="ultimate-parts"></a>
<details>
<summary><strong>🔴 Ultimate: Teile anzeigen (20 Dateien)</strong></summary>

**Gesamt: 5.169.014 eindeutige Domains.** Füge alle Teile zu Pi-hole oder deinem DNS-Blocker hinzu, um die vollständige Abdeckung dieses Profils zu erhalten.

| Ultimate Teil | Ultimate Teil |
|---|---|
| **Teil 01**  <br>**295.375** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-01.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-01.txt)** | **Teil 02**  <br>**244.555** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-02.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-02.txt)** |
| **Teil 03**  <br>**228.569** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-03.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-03.txt)** | **Teil 04**  <br>**264.308** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-04.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-04.txt)** |
| **Teil 05**  <br>**260.070** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-05.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-05.txt)** | **Teil 06**  <br>**263.024** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-06.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-06.txt)** |
| **Teil 07**  <br>**263.058** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-07.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-07.txt)** | **Teil 08**  <br>**267.351** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-08.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-08.txt)** |
| **Teil 09**  <br>**261.856** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-09.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-09.txt)** | **Teil 10**  <br>**279.239** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-10.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-10.txt)** |
| **Teil 11**  <br>**258.822** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-11.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-11.txt)** | **Teil 12**  <br>**268.354** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-12.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-12.txt)** |
| **Teil 13**  <br>**266.309** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-13.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-13.txt)** | **Teil 14**  <br>**258.896** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-14.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-14.txt)** |
| **Teil 15**  <br>**262.296** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-15.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-15.txt)** | **Teil 16**  <br>**264.670** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-16.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-16.txt)** |
| **Teil 17**  <br>**278.829** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-17.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-17.txt)** | **Teil 18**  <br>**241.849** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-18.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-18.txt)** |
| **Teil 19**  <br>**222.191** Einträge · 5.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-19.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-19.txt)** | **Teil 20**  <br>**219.393** Einträge · 4.0 MiB  <br>[Anzeigen](lists/combined/ultimate-part-20.txt) · **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-part-20.txt)** |

</details>
<!-- SPLIT_PROFILES_END -->



---

<a id="ads-tracking"></a>
# 📢 Werbung & Tracking

| Liste | Einträge | Beschreibung | Anzeigen | Raw |
|---|---:|---|:---:|:---:|
| 📣 **Werbung** | 234.038 | Große Domain-Sammlung für Werbung und Werbeauslieferung | [Anzeigen](lists/categories/ads.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/ads.txt) |
| 👁️ **Tracker** | 143.941 | Große Sammlung von Analyse- und Tracking-Infrastruktur | [Anzeigen](lists/categories/trackers.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/trackers.txt) |
| 👥 **Social Tracker** | 99 | Tracking- und Analyse-Endpunkte sozialer Netzwerke | [Anzeigen](lists/categories/social-trackers.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/social-trackers.txt) |
| 📲 **Mobiles Tracking** | 202 | Mobile Attribution, SDK-Analysen und App-Tracking | [Anzeigen](lists/categories/mobile-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/mobile-tracking.txt) |
| 🧩 **Natives/App-Tracking** | 1.466 | Natives Betriebssystem-/Geräte- und Anwendungs-Tracking | [Anzeigen](lists/categories/native-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/native-tracking.txt) |
| 🔗 **Affiliate-Tracking** | 643 | Affiliate-, Klick-, Referral- und Conversion-Tracking; ab Strict enthalten | [Anzeigen](lists/categories/affiliate-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/affiliate-tracking.txt) |
| 🍪 **Consent / CMP** | 44 | Optionales Blocking von Consent-Management/CMP mit erhöhtem Risiko für Website-Fehlfunktionen | [Anzeigen](lists/categories/consent-cmp.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/consent-cmp.txt) |

> **Consent/CMP ist bewusst in keinem kombinierten Schutzprofil enthalten.** DNS-basiertes Blocking von Consent-Infrastruktur kann Seitenaufbau, Consent-Status und Website-Funktionen beeinträchtigen.

---

<a id="telemetry-devices"></a>
# 📡 Telemetrie & Geräte

| Liste | Einträge | Beschreibung | Anzeigen | Raw |
|---|---:|---|:---:|:---:|
| 📊 **Allgemeine Telemetrie** | 29.289 | Breite Produkt-/App-Analysen, Diagnosen und Telemetrie | [Anzeigen](lists/categories/telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/telemetry.txt) |
| 🪟 **Windows-Telemetrie** | 425 | Windows-Diagnose- und native Telemetrie-Endpunkte | [Anzeigen](lists/categories/windows-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/windows-telemetry.txt) |
| 🍎 **Apple-Telemetrie** | 119 | Native Apple-Telemetrie, Metriken und Diagnosen | [Anzeigen](lists/categories/apple-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/apple-telemetry.txt) |
| 🤖 **Android-Telemetrie** | 1.310 | Native Android-/Hersteller-Telemetrie und Tracking | [Anzeigen](lists/categories/android-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/android-telemetry.txt) |
| 🐧 **Linux-Telemetrie** | 3 | Telemetrie, Diagnosen und Nutzungsberichte von Linux-Distributionen | [Anzeigen](lists/categories/linux-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/linux-telemetry.txt) |
| 💾 **NAS-Telemetrie** | 12 | NAS-Telemetrie und Nutzungsberichte (Synology, TrueNAS und weitere) | [Anzeigen](lists/categories/nas-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/nas-telemetry.txt) |
| 🖥️ **Server-Telemetrie** | 10 | Server-, Red-Hat-Insights- und Management-Telemetrie | [Anzeigen](lists/categories/server-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/server-telemetry.txt) |
| 📺 **Smart-TV** | 556 | Smart-TV-Werbung, ACR, Diagnosen und Telemetrie | [Anzeigen](lists/categories/smart-tv.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/smart-tv.txt) |
| 🏠 **IoT** | 85 | Telemetrie-/Tracking-Endpunkte von IoT- und verbundenen Geräten | [Anzeigen](lists/categories/iot.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/iot.txt) |

> Gerätespezifische Listen können Empfehlungen, Diagnosen, Nutzungsberichte, ACR, Werbung oder andere cloudgestützte Funktionen deaktivieren.

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

| Liste | Einträge | Beschreibung | Anzeigen | Raw |
|---|---:|---|:---:|:---:|
| 🦠 **Malware** | 2.710.231 | Sehr große Sammlung von Malware-, Ransomware- und aktiven Malware-Hosts | [Anzeigen](lists/categories/malware.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/malware.txt) |
| 🎣 **Phishing** | 572.332 | Sehr große Sammlung aktiver und kuratierter Phishing-Domains | [Anzeigen](lists/categories/phishing.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/phishing.txt) |
| 💰 **Scam** | 266.444 | Sehr große Sammlung von Betrugs-, Fraud- und täuschenden Plattform-Domains | [Anzeigen](lists/categories/scam.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/scam.txt) |
| 🛒 **Fake-Shops** | 11.380 | Aggressive Sammlung potenzieller Fake-Shops und täuschender Shops | [Anzeigen](lists/categories/fake-shops.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/fake-shops.txt) |
| ⛏️ **Kryptomining** | 6.121 | Browser-/Remote-Mining-Infrastruktur; allgemeine Börsen sind ausgeschlossen | [Anzeigen](lists/categories/cryptomining.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/cryptomining.txt) |

> Sicherheitslisten sind bewusst **groß und aggressiv** und kombinieren mehrere Upstream-Intelligence-Quellen. Bedrohungsdaten ändern sich schnell; Fehlblockierungen sind daher möglich und Upstream-Daten sollten regelmäßig aktualisiert werden.

---

<a id="family-lists"></a>
# 👨‍👩‍👧 Familienlisten

| Liste | Einträge | Beschreibung | Anzeigen | Raw |
|---|---:|---|:---:|:---:|
| 🔞 **Erwachsene Inhalte** | 999.123 | Sehr große Domain-Sammlung für Erwachsenen-Inhalte und Pornografie | [Anzeigen](lists/categories/adult.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/adult.txt) |
| 🎰 **Glücksspiel** | 420.536 | Sehr große Domain-Sammlung für Wetten, Casinos und Glücksspiel | [Anzeigen](lists/categories/gambling.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gambling.txt) |

> Zukünftige Jugendschutzmodule wie SafeSearch oder DNS-Bypass-Schutz sollten erst hinzugefügt werden, nachdem Datenquellen und mögliche Fehlfunktionen unabhängig geprüft wurden. Solche Funktionen werden hier bewusst nicht erfunden oder standardmäßig aktiviert.

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
Große Profile aufteilen (5-MiB-Teile)
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

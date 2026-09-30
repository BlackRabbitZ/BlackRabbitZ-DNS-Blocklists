<div align="center">

# 🐇 BlackRabbitZ DNS Blocklists

### Datenschutz • Sicherheit • Werbung • Tracking • Telemetrie

[![Lizenz: GPL-3.0-only](https://img.shields.io/badge/Lizenz-GPL--3.0--only-blue.svg)](LICENSE)
![Pi-hole kompatibel](https://img.shields.io/badge/Pi--hole-Kompatibel-brightgreen)
![Statische Listen](https://img.shields.io/badge/Listen-Statisch-success)
![Maintainer](https://img.shields.io/badge/Maintainer-BlackRabbitZ-black)
![Endnutzer](https://img.shields.io/badge/Endnutzer-Kein%20Python-success)
[![Blocklisten validieren](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/actions/workflows/update-lists.yml/badge.svg)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/actions/workflows/update-lists.yml)

**Statische, transparente DNS-Blocklisten für Pi-hole und kompatible DNS-Filterlösungen.**

</div>

<div align="center">

**🌐 Sprache / Language:** 🇩🇪 **Deutsch** · [🇬🇧 English](README_EN.md)

</div>

---

<a id="why-dns-blocklists"></a>
## 🛡️ Warum DNS-Blocklisten?

DNS-Blocklisten stoppen unerwünschte Verbindungen bereits bei der Namensauflösung. So lassen sich **Werbung, Tracker, Telemetrie und bekannte schädliche Domains zentral für das gesamte Netzwerk filtern**, ohne auf jedem Gerät zusätzliche Software installieren zu müssen.

Diese korrigierte Repository-Version trennt dabei bewusst **manuell gepflegte Domains**, **automatisch bezogene Upstream-Daten** und **unsichere Kandidaten**. Externe Quellen werden nicht mehr endlos additiv in die öffentlichen Listen geschrieben. Jede Quelle besitzt einen eigenen Cache; bei erfolgreichen Updates wird dieser Cache ersetzt, bei Fehlern bleibt der letzte funktionierende Stand erhalten.

---

<a id="contents"></a>
## 📑 Inhaltsverzeichnis

- [Warum DNS-Blocklisten?](#why-dns-blocklists)
- [Schnellstart](#quick-start)
- [Datenschutzprofile](#protection-profiles)
- [Schutzvergleich](#protection-comparison)
- [Optionale Schutzmodule](#optional-protection-modules)
- [Ultimate-Teile](#ultimate-parts)
- [Werbung & Tracking](#ads-tracking)
- [Telemetrie & Geräte](#telemetry-devices)
- [Sicherheitslisten](#security-lists)
- [Familienlisten](#family-lists)
- [Empfehlungen](#recommendations)
- [Online-DNS-Dienste](#online-dns-services)
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

Für die meisten Nutzer ist **Balanced** der beste Einstieg. Es kombiniert Werbeblocking mit allgemeinem Tracking-Schutz, ohne die geräte- und betriebssystemspezifischen Telemetrielisten standardmäßig zu erzwingen.

```text
https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/balanced.txt
```

**Pi-hole**

1. Öffne die Pi-hole-Weboberfläche.
2. Gehe zu **Lists / Adlists**.
3. Füge die oben angezeigte Raw-URL hinzu.
4. Speichern.
5. Gravity aktualisieren.

> Neue oder aggressivere Listen solltest du zunächst einer separaten Pi-hole-Gruppe zuweisen und testen.

---

<a id="protection-profiles"></a>
# 🚀 Datenschutzprofile

Die kombinierten Profile sind für unterschiedliche Einsatzzwecke gedacht. **Mehr blockieren bedeutet nicht automatisch besseren Schutz** – besonders Geräte-, Telemetrie- und Cloud-Endpunkte können funktionale Abhängigkeiten besitzen.

| Profil | Schutz | Einträge | Empfohlen für | Anzeigen | Raw |
|---|:---:|---:|---|:---:|:---:|
| 🟢 **Light** | Niedrig | **234036** | Einfaches Werbeblocking | [Anzeigen](lists/combined/light.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/light.txt)** |
| 🔵 **Balanced ⭐** | Mittel | **342195** | Die meisten Nutzer | [Anzeigen](lists/combined/balanced.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/balanced.txt)** |
| 🟠 **Strict** | Hoch | **371736** | Datenschutzorientierte Setups | [Anzeigen](lists/combined/strict.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/strict.txt)** |
| 🛡️ **Security** | Sicherheit | **3408844** | Sicherheitsorientierte Filterung | [Anzeigen](lists/combined/security.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security.txt)** |
| 👨‍👩‍👧 **Family** | Familie | **1758872** | Familiennetzwerke | [Anzeigen](lists/combined/family.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family.txt)** |
| 🔴 **Ultimate** | Maximum | **5.119.302** | Aggressive Filterung | [Teile anzeigen](#ultimate-parts) | **[Raw-Teile](#ultimate-parts)** |

> **Balanced** wird für die meisten Installationen empfohlen. **Strict** ergänzt insbesondere allgemeine und gerätespezifische Telemetrie sowie natives/App-Tracking. **Security** und **Family** sind Zusatzprofile mit einem anderen Schwerpunkt. **Ultimate** ist bewusst aggressiv und sollte nicht ungeprüft in kritischen Netzen eingesetzt werden.

---

<a id="protection-comparison"></a>
# 🎚️ Schutzvergleich

| Funktion | Light | Balanced ⭐ | Strict | Security | Family | Ultimate |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Werbung | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| Allgemeine Tracker | — | ✅ | ✅ | — | ✅ | ✅ |
| Social-Tracking | — | ✅ | ✅ | — | ✅ | ✅ |
| Affiliate-Tracking | — | — | ✅ | — | — | ✅ |
| Allgemeine Telemetrie | — | — | ✅ | — | — | ✅ |
| Windows-Telemetrie | — | — | ✅ | — | — | ✅ |
| Apple-Telemetrie | — | — | ✅ | — | — | ✅ |
| Android-Telemetrie | — | — | ✅ | — | — | ✅ |
| Linux-/NAS-/Server-Telemetrie | — | — | ✅ | — | — | ✅ |
| Mobil-/App-Tracking | — | — | ✅ | — | — | ✅ |
| Smart-TV / IoT | — | — | ✅ | — | — | ✅ |
| Kryptomining | — | — | — | ✅ | — | ✅ |
| Malware / Phishing / Betrug / Fake-Shops | — | — | — | ✅ | — | ✅ |
| Erwachsene Inhalte | — | — | — | — | ✅ | ✅ |
| Glücksspiel | — | — | — | — | ✅ | ✅ |
| Fehlfunktionsrisiko | 🟢 Niedrig | 🔵 Niedrig–Mittel | 🟠 Höher | 🟡 Mittel | 🟠 Höher | 🔴 Sehr hoch |

<a id="optional-protection-modules"></a>
## 🧩 Optionale Schutzmodule

**Security** und **Family** sind keine bloß „stärkeren“ Varianten von Balanced oder Strict, sondern thematische Zusatzprofile:

- **Security** bündelt Malware, Phishing, Scam, Fake-Shops und Kryptomining.
- **Family** ergänzt Werbe-/Tracking-Schutz um Erwachsenen-Inhalte und Glücksspiel.
- **Consent/CMP** bleibt eine bewusst separate Kategorie, da DNS-basiertes Blocking von Consent-Infrastruktur Webseiten beeinträchtigen kann.

---

<a id="ultimate-parts"></a>
## 📦 Ultimate-Teile

Ultimate ist groß und wird deshalb automatisch in mehrere Dateien aufgeteilt. Für vollständige Ultimate-Abdeckung müssen **alle Teile** hinzugefügt werden.

<!-- ULTIMATE_PARTS_START -->
| Teil | Einträge | Größe | Anzeigen | Raw |
|---:|---:|---:|:---:|:---:|
| **1** | **2.090.381** | 40.0 MiB | [Anzeigen](lists/combined/ultimate-1.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-1.txt)** |
| **2** | **2.125.750** | 40.0 MiB | [Anzeigen](lists/combined/ultimate-2.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-2.txt)** |
| **3** | **903.171** | 17.9 MiB | [Anzeigen](lists/combined/ultimate-3.txt) | **[Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate-3.txt)** |
<!-- ULTIMATE_PARTS_END -->

---

<a id="ads-tracking"></a>
# 📢 Werbung & Tracking

| Liste | Einträge | Beschreibung | Anzeigen | Raw |
|---|---:|---|:---:|:---:|
| 📣 **Werbung** | 234036 | Werbung, Werbeauslieferung und Werbe-Infrastruktur | [Anzeigen](lists/categories/ads.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/ads.txt) |
| 👁️ **Tracker** | 113609 | Allgemeine Analyse- und Tracking-Infrastruktur | [Anzeigen](lists/categories/trackers.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/trackers.txt) |
| 👥 **Social Tracker** | 99 | Tracking- und Analyse-Endpunkte sozialer Netzwerke | [Anzeigen](lists/categories/social-trackers.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/social-trackers.txt) |
| 📲 **Mobiles Tracking** | 201 | Mobile Attribution, SDK-Analysen und App-Tracking | [Anzeigen](lists/categories/mobile-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/mobile-tracking.txt) |
| 🧩 **Natives/App-Tracking** | 628 | Betriebssystem-, Geräte- und Anwendungs-Tracking | [Anzeigen](lists/categories/native-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/native-tracking.txt) |
| 🔗 **Affiliate-Tracking** | 643 | Affiliate-, Klick-, Referral- und Conversion-Tracking | [Anzeigen](lists/categories/affiliate-tracking.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/affiliate-tracking.txt) |
| 🍪 **Consent / CMP** | 44 | Consent-Management/CMP; erhöhtes Fehlfunktionsrisiko | [Anzeigen](lists/categories/consent-cmp.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/consent-cmp.txt) |

> **Consent/CMP ist bewusst nicht Teil der normalen Datenschutzprofile.** Solche Domains können direkt mit Seitenaufbau und Consent-Status zusammenhängen.

---

<a id="telemetry-devices"></a>
# 📡 Telemetrie & Geräte

| Liste | Einträge | Beschreibung | Anzeigen | Raw |
|---|---:|---|:---:|:---:|
| 📊 **Allgemeine Telemetrie** | 29169 | Produkt-/App-Analysen, Diagnosen und Telemetrie | [Anzeigen](lists/categories/telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/telemetry.txt) |
| 🪟 **Windows-Telemetrie** | 51 | Windows-/Microsoft-Diagnose und Telemetrie | [Anzeigen](lists/categories/windows-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/windows-telemetry.txt) |
| 🍎 **Apple-Telemetrie** | 119 | Apple-Metriken, Diagnosen und Telemetrie | [Anzeigen](lists/categories/apple-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/apple-telemetry.txt) |
| 🤖 **Android-Telemetrie** | 135 | Android-/Hersteller-Telemetrie und Native-Tracking | [Anzeigen](lists/categories/android-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/android-telemetry.txt) |
| 🐧 **Linux-Telemetrie** | 3 | Telemetrie und Nutzungsberichte von Linux-Systemen | [Anzeigen](lists/categories/linux-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/linux-telemetry.txt) |
| 💾 **NAS-Telemetrie** | 12 | NAS-Telemetrie und Nutzungsberichte | [Anzeigen](lists/categories/nas-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/nas-telemetry.txt) |
| 🖥️ **Server-Telemetrie** | 10 | Server-/Management-Telemetrie | [Anzeigen](lists/categories/server-telemetry.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/server-telemetry.txt) |
| 📺 **Smart-TV** | 556 | Smart-TV-Werbung, ACR, Diagnosen und Telemetrie | [Anzeigen](lists/categories/smart-tv.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/smart-tv.txt) |
| 🏠 **IoT** | 85 | IoT- und Connected-Device-Telemetrie/Tracking | [Anzeigen](lists/categories/iot.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/iot.txt) |

> Gerätespezifische Listen können Empfehlungen, Diagnosen, Nutzungsberichte, ACR, Werbung oder andere Cloud-Funktionen beeinträchtigen. Die korrigierte Upstream-Pipeline schützt deshalb bekannte Update-, Login-, Push-, Zertifikats- und Firmware-Endpunkte vor automatischem Import in Privacy-/Device-Kategorien.

---

<a id="security-lists"></a>
# 🛡️ Sicherheitslisten

| Liste | Einträge | Beschreibung | Anzeigen | Raw |
|---|---:|---|:---:|:---:|
| 🦠 **Malware** | 2656445 | Malware-, Ransomware- und aktive Malware-Hosts | [Anzeigen](lists/categories/malware.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/malware.txt) |
| 🎣 **Phishing** | 577783 | Aktive und kuratierte Phishing-Domains | [Anzeigen](lists/categories/phishing.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/phishing.txt) |
| 💰 **Scam & Internet-Betrug** | 265330 | Betrugs-, Fraud- und täuschende Plattform-Domains | [Anzeigen](lists/categories/scam.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/scam.txt) |
| 🛒 **Fake-Shops** | 10964 | Potenzielle Fake-Shops und täuschende Shops | [Anzeigen](lists/categories/fake-shops.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/fake-shops.txt) |
| ⛏️ **Kryptomining** | 6121 | Browser-/Remote-Mining-Infrastruktur | [Anzeigen](lists/categories/cryptomining.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/cryptomining.txt) |

> Sicherheitslisten folgen einer anderen Logik als Privacy-/Device-Listen. Funktionale Begriffe wie `login` oder `update` führen dort nicht automatisch zur Freigabe, weil solche Begriffe auch in schädlichen Domains vorkommen können.

---

<a id="family-lists"></a>
# 👨‍👩‍👧 Familienlisten

| Liste | Einträge | Beschreibung | Anzeigen | Raw |
|---|---:|---|:---:|:---:|
| 🔞 **Adult / NSFW** | 999120 | Erwachsenen-Inhalte und Pornografie | [Anzeigen](lists/categories/adult.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/adult.txt) |
| 🎰 **Glücksspiel** | 420536 | Wett-, Casino- und Glücksspiel-Domains | [Anzeigen](lists/categories/gambling.txt) | [Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gambling.txt) |

---

<a id="recommendations"></a>
# ✅ Empfehlungen

| Ziel | Empfehlung |
|---|---|
| Einfaches Werbeblocking | **Light** |
| Alltag / Heimnetz | **Balanced** |
| Mehr Datenschutz | **Strict** – zunächst testen |
| Schutz vor Malware/Phishing | **Balanced + Security** |
| Familiennetz | **Balanced + Family** |
| Maximale Filterung | **Ultimate** – nur nach Test und mit eigener Allowlist |

**Empfohlene Vorgehensweise:** mit Balanced starten, Query-Log beobachten und anschließend nur die Kategorien ergänzen, die du wirklich brauchst. Das reduziert Fehlblockierungen deutlich gegenüber einem pauschalen „alles an“-Ansatz.

---

<a id="online-dns-services"></a>
# 🌍 Online-DNS-Dienste und mobile Nutzung

Die Dateien in diesem Repository sind normale Domainlisten. Sie sind primär für **Pi-hole** und vergleichbare selbstverwaltete DNS-Filter gedacht. Viele DNS-Dienste akzeptieren eigene Blocklisten jedoch nur eingeschränkt oder überhaupt nicht.

Für mobile Geräte außerhalb des Heimnetzes bieten sich z. B. VPN-/DNS-Tunnel zum eigenen Pi-hole oder Lösungen mit eigener Blocklist-Unterstützung an. Beachte dabei, dass Pi-hole-RegEx-Regeln und lokale Gruppenlogik nicht automatisch auf externe DNS-Anbieter übertragbar sind.

---

<a id="upstream-sources"></a>
# 🌐 Upstream-Quellen & Build-Transparenz

Die korrigierte Version trennt den Datenfluss bewusst in mehrere Ebenen:

```text
Manuell gepflegte Domains
sources/manual/
        │
        ├──────────────┐
        │              │
Externe Quellen        │
sources/upstream/      │
pro Feed eigener Cache │
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

### Was gegenüber dem alten additiven Import geändert wurde

- **Keine endlose additive Vermischung mehr:** ein erfolgreicher Feed ersetzt seinen eigenen Cache.
- **Letzter guter Stand bei Ausfällen:** eine temporär nicht erreichbare Quelle leert keine Kategorie.
- **Manuelle Daten bleiben getrennt:** `sources/manual/` ist unabhängig von automatischen Upstreams.
- **Critical-Service-Schutz:** `config/critical-services.txt` schützt bekannte Update-, Auth-, Push-, Zertifikats- und Firmware-Infrastruktur in Privacy-/Device-Kategorien.
- **Quarantäne:** funktional wirkende oder unsichere Kandidaten können unter `review/quarantine/` landen, statt direkt veröffentlicht zu werden.
- **Allowlist:** `config/allowlist.txt` gilt als expliziter Ausschluss für veröffentlichte Listen.
- **NXDOMAIN-Prüfung:** neu gecachte Domains können vor Veröffentlichung stichproben-/batchweise auf bestätigtes NXDOMAIN geprüft werden.
- **Plausibilitätsgrenzen:** ungewöhnlich kleine, große oder stark veränderte Quellen werden nicht blind übernommen.
- **Review statt Direkt-Push:** das tägliche Upstream-Update erstellt bzw. aktualisiert einen Pull Request.

Quellen- und Lizenzhinweise stehen in [`THIRD_PARTY.md`](THIRD_PARTY.md), Attribution in [`ATTRIBUTION.md`](ATTRIBUTION.md). Details zum Workflow findest du in [`docs/AUTOMATIC_UPDATES.md`](docs/AUTOMATIC_UPDATES.md) und [`MIGRATION_WORKFLOW_FIX.md`](MIGRATION_WORKFLOW_FIX.md).

---

<a id="repository-structure"></a>
# 📂 Repository-Struktur

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

Alle veröffentlichten Blocklisten bleiben normale statische Textdateien. Python/Bash/GitHub Actions werden nur für die Wartung des Repositories benötigt – nicht für Pi-hole-Endnutzer.

---

<a id="automatic-updates"></a>
# 🔄 Automatische Listen-Updates

Das Repository verwendet zwei getrennte Workflows:

### 1. `daily-upstream-update.yml`

Läuft geplant um **03:17 UTC** oder manuell. Der Workflow:

1. prüft die Upstream-Konfiguration,
2. aktualisiert die einzelnen Feed-Caches,
3. führt – soweit sinnvoll – eine NXDOMAIN-Prüfung auf neuen Cache-Domains durch,
4. baut Kategorien und kombinierte Profile neu,
5. validiert das Repository,
6. erstellt oder aktualisiert den Branch `automation/upstream-refresh`,
7. öffnet bzw. aktualisiert einen **Review Pull Request**.

Er pusht Fremdquellen-Änderungen damit **nicht mehr ungeprüft direkt auf `main`**.

### 2. `update-lists.yml`

Dieser Workflow besitzt nur **Read-Zugriff** und dient der Integritätsprüfung. Er baut alle generierten Dateien lokal neu und schlägt fehl, wenn die committed Dateien nicht mit ihren Quellen übereinstimmen.

### Sicherheitsprinzip

```text
Upstream → Cache → Schutzregeln → Build → Validierung → Pull Request → menschlicher Review → Merge
```

---

<a id="extending-lists"></a>
# ➕ Listen erweitern

Manuelle Domains werden **nicht mehr direkt in `lists/categories/` gepflegt**. Diese Dateien sind generierte Ausgaben.

Für eine bestehende Kategorie bearbeitest du stattdessen z. B.:

```text
sources/manual/ads.txt
```

Eine Domain pro Zeile:

```text
ads.example.net
tracker.example.net
```

Danach lokal neu bauen und prüfen:

```bash
python3 ./scripts/build-categories.py
bash ./scripts/update-lists.sh
python3 ./scripts/validate-repository.py
```

### Neue Upstream-Quelle

Neue externe Feeds werden in `scripts/upstream-sources.json` konfiguriert. Füge nur Quellen hinzu, deren Einsatzzweck, Format, Lizenz und Fehlblockierungsrisiko nachvollziehbar sind.

### Neue Kategorie

1. `sources/manual/<kategorie>.txt` anlegen.
2. Kategorie im Build berücksichtigen.
3. Falls automatische Feeds gewünscht sind, Mapping in `upstream-sources.json` ergänzen.
4. Falls die Kategorie in einem Kombiprofil landen soll, `scripts/update-lists.sh` entsprechend ergänzen.
5. README/README_EN verlinken.
6. Validator ausführen.

---

<a id="false-positives"></a>
# ⚠️ Fehlblockierungen / False Positives

Mehr Domains zu blockieren bedeutet nicht automatisch mehr Sicherheit oder Datenschutz.

Wenn eine Liste eine Webseite, App oder ein Gerät beeinträchtigt, melde möglichst:

- betroffene Domain,
- betroffene Liste bzw. Profil,
- Anwendung/Gerät/Betriebssystem,
- welche Funktion ausfällt,
- ob die Funktion nach Deaktivieren der Liste wieder arbeitet,
- reproduzierbare Schritte.

Für dauerhafte Ausnahmen steht `config/allowlist.txt` zur Verfügung. Bekannte funktionale Infrastruktur, die bei automatischen Privacy-/Device-Imports besonders geschützt werden soll, gehört in `config/critical-services.txt`.

Das Ziel ist eine **brauchbare und nachvollziehbare Blocklist**, nicht die größtmögliche Domainzahl.

---

<a id="license-attribution"></a>
# 📜 Lizenz & Namensnennung

Dieses Repository steht unter **GNU GPL v3 (`GPL-3.0-only`)**.

Copyright © 2026 BlackRabbitZ

Original-Repository:

```text
https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists
```

Siehe außerdem:

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

⭐ Wenn dir das Projekt hilft, kannst du das Repository mit einem Stern unterstützen.

</div>

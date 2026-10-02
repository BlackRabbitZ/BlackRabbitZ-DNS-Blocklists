<a id="top"></a>

<div align="center">

# 🐇 BlackRabbitZ DNS Blocklists

### Datenschutz • Werbung • Tracking • Telemetrie • Sicherheit • Geräte • Apps • Family

![Pi-hole](https://img.shields.io/badge/Pi--hole-kompatibel-96060C?logo=pihole&logoColor=white)
![Format](https://img.shields.io/badge/Format-Plain%20Domains-2ea44f)
![Profiles](https://img.shields.io/badge/Profile-Light%20%7C%20Normal%20%7C%20Pro%20%7C%20Pro%2B%2B%20%7C%20Ultimate-3178C6)
![Single URL](https://img.shields.io/badge/1%20Liste-1%20URL-success)
![License](https://img.shields.io/badge/Lizenz-GPL--3.0-orange)

**Eine klare Schutzstufe für ganze Bereiche – und optionale Full-Listen für einzelne Hersteller oder Dienste.**

</div>

---

<a id="projekt-navigation"></a>
## 📘 1. Inhaltsverzeichnis – Projekt & Nutzung

- [🚀 Schnellstart](#schnellstart)
- [📊 Globale Hauptlisten auf einen Blick](#hauptlisten)
- [🎚️ Schutzstufen Light bis Ultimate](#schutzstufen)
- [🧩 Hauptlisten & Full-Listen](#listenmodell)
- [📂 Repository-Struktur](#repo-struktur)
- [✅ Qualitätssicherung](#qualitaet)
- [⚠️ Hinweise & technische Grenzen](#grenzen)
- [📜 Quellen & Lizenz](#lizenz)

---

<a id="kinderschutz-navigation"></a>
## 👨‍👩‍👧 Besonderes Inhaltsverzeichnis – Family & Kinderschutz

- [👨‍👩‍👧 Family & Content](#family)
- [🧒 Kids Allow-Only](#kids-allow-only)

---

<a id="blocklisten-navigation"></a>
## 🧱 2. Inhaltsverzeichnis – Blocklisten

- [🕵️ Privacy & Tracking](#privacy)
- [📺 Smart TV](#smart-tv)
- [📱 Smartphones & Mobile](#mobile)
- [💻 Betriebssysteme](#betriebssysteme)
- [🎮 Gaming](#gaming)
- [💾 NAS & Server](#nas-server)
- [🏠 IoT & Smart Home](#iot)
- [🛡️ Security](#security)

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

Die Stufen sind kumulativ. `Pro` enthält `Normal`, `Normal` enthält `Light` usw. Du musst die niedrigeren Stufen nicht zusätzlich abonnieren.

> **Wichtig:** Es gibt **keine MiB-/Part-Aufteilung**. Jedes logische Profil ist genau **eine Datei und eine URL**.

<p align="right"><a href="#projekt-navigation">⬆️ Projekt-Inhaltsverzeichnis</a></p>

---

<a id="hauptlisten"></a>
## 📊 Globale Hauptlisten auf einen Blick

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **234.003** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **342.216** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **371.516** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **383.624** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **5.118.461** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/profiles/ultimate.txt) |

**Empfehlungslogik:** `Normal` ist der alltagstaugliche Einstieg, `Pro` setzt den Schwerpunkt stärker auf Datenschutz, `Pro++` wird spürbar aggressiver und `Ultimate` ist bewusst maximal.

<p align="right"><a href="#projekt-navigation">⬆️ Projekt-Inhaltsverzeichnis</a></p>

---

<a id="schutzstufen"></a>
## 🎚️ Schutzstufen Light bis Ultimate

| Profil | Schwerpunkt | Typischer Inhalt | Risiko |
|---|---|---|:---:|
| 🟩 **Light** | Grundschutz | Werbung und besonders sichere Werbeendpunkte | 🟢 Minimal |
| 🟦 **Normal** | Alltagsschutz | Light + Tracking, Analytics und weitere Messdienste | 🟢 Niedrig |
| 🟨 **Pro** | Datenschutz | Normal + Telemetrie, Metrics, Diagnostics und Native Tracking | 🟡 Niedrig–Mittel |
| 🟧 **Pro++** | aggressiv | Pro + aggressive Hersteller-/Cloud-/Privacy-Endpunkte und Security-Basis | 🟠 Mittel |
| 🟥 **Ultimate** | maximal | vollständige bekannte Datenbestände der integrierten Bereiche | 🔴 Hoch |

```text
Light ⊂ Normal ⊂ Pro ⊂ Pro++ ⊂ Ultimate
```

`Ultimate` kann abhängig vom Bereich Updates, Cloudfunktionen, Logins, Stores, Aktivierung oder andere Onlinefunktionen beeinträchtigen.

<p align="right"><a href="#projekt-navigation">⬆️ Projekt-Inhaltsverzeichnis</a></p>

---

<a id="listenmodell"></a>
## 🧩 Hauptlisten & Full-Listen

Jeder größere Bereich folgt demselben Modell.

**Hauptlisten** decken alle unterstützten Hersteller/Dienste eines Bereichs gemeinsam ab:

```text
Light ⊂ Normal ⊂ Pro ⊂ Pro++ ⊂ Ultimate
```

**Full-Listen** sind Speziallisten für genau einen Hersteller oder Dienst. Zusätzlich kann ein Bereich eine `Shared / Other`-Liste besitzen, wenn Domains zum Bereich gehören, aber keinem einzelnen Hersteller sicher zugeordnet werden können. `Samsung Full`, `Steam Full` oder `Synology Full` sind deshalb nicht automatisch die empfohlene Standardwahl.

Beispiel Smart TV:

```text
Samsung Full ─────────────┐
LG/webOS Full ─────────────┤
Roku Full ─────────────────┤─> Smart TV Ultimate
Fire TV Full ──────────────┤
Gemeinsame/sonstige Dienste ┘

Aus dem gesamten Bereich werden zusätzlich sichere Teilmengen für
Light → Normal → Pro → Pro++ erzeugt.
```

<p align="right"><a href="#projekt-navigation">⬆️ Projekt-Inhaltsverzeichnis</a></p>

---

<a id="repo-struktur"></a>
## 📂 Repository-Struktur

```text
BlackRabbitZ-DNS-Blocklists/
├── profiles/                       # globale Light–Ultimate-Listen
├── family/
│   ├── main/                       # Family Light–Ultimate
│   ├── content/                    # Adult / Gambling
│   └── kids-allow-only/            # restriktiver Kinderschutz
├── lists/
│   ├── privacy/
│   │   ├── main/
│   │   └── full/
│   ├── platforms/
│   │   ├── smart-tv/
│   │   ├── mobile/
│   │   ├── operating-systems/
│   │   ├── nas-server/
│   │   └── iot-smart-home/
│   ├── apps/gaming/
│   └── security/
├── config/
├── docs/
├── metadata/
└── scripts/
```

<p align="right"><a href="#projekt-navigation">⬆️ Projekt-Inhaltsverzeichnis</a></p>

---

<a id="qualitaet"></a>
## ✅ Qualitätssicherung

- Plain-Domain-Format, eine Domain pro Zeile
- sortiert und dedupliziert
- kumulative Bereichs- und globale Profile
- SHA-256-Prüfsummen
- Validator gegen ungültige Domains und Duplikate
- **keine Part-Dateien**
- **keine automatische Fremdlisten-Synchronisation**

```bash
python3 scripts/validate.py
```

<p align="right"><a href="#projekt-navigation">⬆️ Projekt-Inhaltsverzeichnis</a></p>

---

<a id="grenzen"></a>
## ⚠️ Hinweise & technische Grenzen

DNS-Blocking kann Verbindungen zu Domains unterbinden, aber keine einzelnen Inhalte auf einer bereits erlaubten Domain entfernen. Hersteller nutzen außerdem teilweise dieselben Domains für Telemetrie und notwendige Funktionen. Deshalb steigt mit jeder Schutzstufe das Risiko von Fehlblockierungen.

Für neue Stufen empfiehlt sich zunächst eine eigene Pi-hole-Testgruppe. Projektweite Ausnahmen können in `config/allowlist.txt` dokumentiert werden.

<p align="right"><a href="#projekt-navigation">⬆️ Projekt-Inhaltsverzeichnis</a></p>

---
# 👨‍👩‍👧 Teil 2 – Family & Kinderschutz

<a id="family"></a>
## 👨‍👩‍👧 Family & Content

Die Family-Hauptlisten kombinieren Inhaltsfilter in abgestuften Stufen. Sie sind bewusst separat von den normalen Privacy-Profilen.

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **998.924** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **1.419.159** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **1.430.117** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **1.769.650** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **2.346.905** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/main/ultimate.txt) |

### Vollständige Content-Listen

| Bereich | Beschreibung | Einträge | Liste |
|---|---|---:|---|
| **Adult / NSFW** | Erwachsenen-Inhalte / Pornografie | **998.924** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/adult.txt) |
| **Gambling** | Wett-, Casino- und Glücksspiel-Domains | **420.536** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/content/gambling.txt) |

<p align="right"><a href="#kinderschutz-navigation">⬆️ Family-Inhaltsverzeichnis</a></p>

---

<a id="kids-allow-only"></a>
## 🧒 Kids Allow-Only

`Kids Allow-Only` ist **keine normale Blockliste**, sondern ein striktes Allow-Only-Modell für eine eigene Pi-hole-Gruppe. Für die zugewiesenen Kindergeräte wird standardmäßig **jede Domain blockiert**. Anschließend werden nur bewusst freigegebene Kinder-, Lern- und Medienangebote wieder erlaubt.

> **Wichtig:** Dieses Modell sollte nur für eine eigene Kindergruppe verwendet werden. Nicht ungeprüft auf das gesamte Heimnetz anwenden.

### ✅ Starter-Allowlist

Die folgende Auswahl ist als **Startpunkt** gedacht. Eltern bzw. Administratoren sollten die Einträge selbst prüfen und je nach Alter, Nutzung und gewünschtem Umfang anpassen.

| Angebot | Kategorie | Beschreibung | Hauptdomain |
|---|---|---|---|
| **fragFINN** | Suche | Kindersuchmaschine und geprüfter Surfraum | `fragfinn.de` |
| **Blinde Kuh** | Suche | Suchmaschine für Kinder | `blinde-kuh.de` |
| **Seitenstark** | Kinderportal | Netzwerk und Sammlung von Kinderseiten | `seitenstark.de` |
| **Internet-ABC** | Lernen / Medienkompetenz | Internet, Sicherheit und Medienbildung | `internet-abc.de` |
| **KiKA** | Medien | Kinderfernsehen und Mediathek | `kika.de` |
| **Kikaninchen** | Kinder / Medien | Angebote für jüngere Kinder | `kikaninchen.de` |
| **WDR Maus** | Wissen | Inhalte rund um die Sendung mit der Maus | `wdrmaus.de` |
| **Kindernetz** | Medien / Wissen | SWR-Angebote für Kinder | `kindernetz.de` |
| **Kinderfilmwelt** | Medien | Informationen und Empfehlungen zu Kinderfilmen | `kinderfilmwelt.de` |
| **Duda News** | Nachrichten | Nachrichten und Wissen für Kinder | `duda.news` |
| **HanisauLand** | Politik / Wissen | Politik und Gesellschaft kindgerecht erklärt | `hanisauland.de` |
| **Kinderzeitmaschine** | Geschichte | Geschichte und historische Themen für Kinder | `kinderzeitmaschine.de` |
| **Coollama** | Lernen | Lern- und Wissensinhalte für Kinder | `coollama.de` |
| **LegaKids** | Lernen | Lesen, Schreiben und Rechtschreibung | `legakids.net` |
| **Meine Forscherwelt** | MINT | Forschen und Naturwissenschaften | `meine-forscherwelt.de` |
| **Klassewasser** | Umwelt / Wissen | Wasser, Umwelt und Bildung | `klassewasser.de` |
| **Abenteuer Regenwald** | Umwelt | Regenwald-, Natur- und Umweltthemen | `abenteuer-regenwald.de` |
| **Naturdetektive** | Natur | Natur- und Artenschutz für Kinder | `naturdetektive.bfn.de` |
| **Ohrka** | Audio | Hörspiele und Hörangebote für Kinder | `ohrka.de` |
| **Auditorix** | Audio / Medienbildung | Hören, Hörspiel und Medienkompetenz | `auditorix.de` |

Die zugehörige Repo-Datei enthält zusätzlich übliche `www.`-Varianten, soweit sinnvoll:

**➡️ [approved-sites.txt](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/approved-sites.txt)**

### 📁 Dateien für Kids Allow-Only

| Datei | Zweck |
|---|---|
| [`approved-sites.txt`](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/approved-sites.txt) | Starter-Allowlist mit freigegebenen Kinder-/Lernangeboten |
| [`block-all.regex`](family/kids-allow-only/block-all.regex) | Regex `.*` – blockiert standardmäßig alle übrigen Domains |
| [`README.md`](family/kids-allow-only/README.md) | Kurzbeschreibung direkt im Kids-Allow-Only-Ordner |

### 🧭 Funktionsprinzip

```text
Kindergerät
    ↓
Pi-hole-Gruppe "Kids"
    ↓
block-all.regex = .*
    ↓
standardmäßig wird jede Domain blockiert
    ↓
approved-sites.txt hebt ausgewählte Domains wieder auf
    ↓
benötigte CDN-/Login-/Medien-Domains gezielt ergänzen
```

Pi-hole wertet Allowlist-Einträge mit höherer Priorität als Denylist- und Regex-Denylist-Einträge aus. Dadurch können bewusst freigegebene Domains trotz der globalen `.*`-Regel für die Kindergruppe erreichbar bleiben.

### 🛠️ Einrichtung in Pi-hole

#### 1. Eigene Gruppe für Kindergeräte anlegen

Erstelle in Pi-hole eine eigene Gruppe, z. B.:

```text
Kids
```

oder:

```text
Kinderschutz
```

Die Gruppe sollte ausschließlich für Geräte gedacht sein, auf denen das Allow-Only-Prinzip gelten soll.

#### 2. Kindergeräte der Gruppe zuweisen

Füge die betreffenden Geräte als Clients hinzu und ordne sie der Gruppe `Kids` zu.

Für einen **strikten Allow-Only-Modus** sollte das Kindergerät nicht zusätzlich die normale `Default`-Gruppe verwenden. Andernfalls können Listen oder Freigaben aus anderen Gruppen zusätzlich wirken.

Beispiele für geeignete Client-Zuordnungen:

```text
192.168.178.50   → Kids
192.168.178.51   → Kids
Kinder-Tablet    → Kids
Kinder-PC        → Kids
```

#### 3. Alles standardmäßig blockieren

Füge als **Regex-Denylist** die Regel aus `block-all.regex` hinzu:

```regex
.*
```

Weise diese Regel **nur der Gruppe `Kids`** zu.

> `.*` trifft praktisch auf jede normale Domain zu. Eine falsche Gruppenzuweisung kann deshalb das gesamte Browsing eines Geräts blockieren.

#### 4. Starter-Allowlist einbinden

Für Pi-hole v6 kann die Raw-Datei als externe Allowlist verwendet werden:

```text
https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/family/kids-allow-only/approved-sites.txt
```

Die Allowlist ebenfalls **nur der Gruppe `Kids`** zuweisen.

Alternativ können die gewünschten Domains einzeln als exakte Allowlist-Einträge eingetragen werden.

#### 5. Listen aktualisieren

Nach Änderungen die Pi-hole-Listen neu laden bzw. Gravity aktualisieren.

CLI:

```bash
pihole updateGravity
```

#### 6. Webseiten testen

Jetzt mit einem Kindergerät eine freigegebene Seite öffnen.

Falls die Hauptseite erreichbar ist, aber beispielsweise Bilder, Videos, Login oder andere Funktionen fehlen, im **Pi-hole Query Log** nach blockierten Abhängigkeiten suchen.

Typische zusätzliche Abhängigkeiten können sein:

```text
CDN-Domains
Bild-/Video-Hosts
Login-Domains
API-Endpunkte
Schriftarten-/Asset-Domains
Mediathek-/Streaming-Endpunkte
```

Nur die tatsächlich benötigten Domains gezielt freigeben. Nicht einfach komplette Fremd-CDNs oder große Plattformen pauschal erlauben.

#### 7. Neue Seiten kontrolliert ergänzen

Wenn eine weitere Kinderseite erlaubt werden soll:

1. Hauptdomain prüfen.
2. Hauptdomain zur Allowlist hinzufügen.
3. Seite auf einem Testgerät öffnen.
4. Im Query Log fehlende technische Domains identifizieren.
5. Nur notwendige Abhängigkeiten ergänzen.
6. Funktion erneut testen.

### ⚠️ Wichtige Grenzen

- Eine erlaubte Domain bedeutet nicht automatisch, dass **jeder Inhalt** dieser Website kindgerecht ist.
- DNS-Filter können keine einzelnen Unterseiten oder Inhalte innerhalb einer bereits erlaubten Domain unterscheiden.
- Websites ändern regelmäßig CDNs, APIs und technische Abhängigkeiten.
- Die Starter-Allowlist ist deshalb **kein statischer Jugendschutz-Ersatz**, sondern eine technisch restriktive Grundlage, die gepflegt und getestet werden muss.
- Für Mobilgeräte sollte zusätzlich verhindert werden, dass Apps oder Browser einen eigenen DNS-/DoH-Dienst verwenden und damit Pi-hole umgehen.

### 🔎 Kontrolle und Fehlersuche

Wenn eine erlaubte Website nicht funktioniert:

```text
1. Pi-hole Query Log öffnen
2. nach dem Kindergerät filtern
3. blockierte Domains während des Seitenaufrufs beobachten
4. Domain und Zweck prüfen
5. nur wenn notwendig gezielt erlauben
```

So bleibt das Allow-Only-Prinzip erhalten, ohne durch großflächige Ausnahmen wieder aufgeweicht zu werden.

<p align="right"><a href="#kinderschutz-navigation">⬆️ Family-Inhaltsverzeichnis</a></p>

---
# 🧱 Teil 3 – Blocklisten-Katalog

<a id="privacy"></a>
## 🕵️ Privacy & Tracking

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **234.003** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **342.216** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **371.491** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **371.519** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **371.722** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/main/ultimate.txt) |

### Vollständige Speziallisten

| Liste | Beschreibung | Einträge | Full-Liste |
|---|---|---:|---|
| **Ads** | Werbung und Ad-Delivery | **234.003** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/ads.txt) |
| **Tracker** | allgemeine Tracking-/Measurement-Domains | **113.606** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/trackers.txt) |
| **Social Tracking** | Tracking sozialer Plattformen | **99** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/social-tracking.txt) |
| **Mobile Tracking** | mobile SDK-/Attribution-Endpunkte | **201** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/mobile-tracking.txt) |
| **Affiliate Tracking** | Referral-/Conversion-Tracking | **643** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/affiliate-tracking.txt) |
| **Telemetry** | allgemeine Telemetrie und Diagnostik | **29.163** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/telemetry.txt) |
| **Native Tracking** | Native Tracker aus Geräten, Apps und Betriebssystemen | **628** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/native-tracking.txt) |
| **Consent/CMP** | Consent-Infrastruktur; aggressiv | **44** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/privacy/full/consent-cmp.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="smart-tv"></a>
## 📺 Smart TV

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **346** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **353** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **374** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **544** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **556** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/main/ultimate.txt) |

### Herstellerspezifische Full-Listen

| Hersteller / Plattform | Beschreibung | Einträge | Full-Liste |
|---|---|---:|---|
| **Samsung / Tizen** | Smart-TV-Endpunkte für Samsung/Tizen | **50** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/samsung.txt) |
| **LG / webOS** | LG/webOS Ads, ACR, Tracking und Telemetrie | **355** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/lg-webos.txt) |
| **Sony / Bravia** | Sony-/Bravia-Endpunkte | **4** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/sony-bravia.txt) |
| **Google / Android TV** | Android-TV-/Google-TV-spezifische Endpunkte | **2** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/google-android-tv.txt) |
| **Roku** | Roku Ads/Tracking/Telemetrie | **13** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/roku.txt) |
| **Amazon Fire TV** | Fire-TV-/Amazon-Endpunkte | **19** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/amazon-fire-tv.txt) |
| **Hisense / VIDAA** | Hisense-/VIDAA-Endpunkte | **11** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/hisense-vidaa.txt) |
| **Gemeinsame / sonstige Smart-TV-Dienste** | nicht eindeutig nur einem Hersteller zuordenbare Smart-TV-Endpunkte | **102** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/smart-tv/full/shared-other.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="mobile"></a>
## 📱 Smartphones & Mobile

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **352** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **396** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **470** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **744** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **751** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/main/ultimate.txt) |

### Herstellerspezifische Full-Listen

| Hersteller / Plattform | Beschreibung | Einträge | Full-Liste |
|---|---|---:|---|
| **Apple / iOS** | Apple-/iOS-Telemetrie und Native Tracking | **121** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/full/apple-ios.txt) |
| **Google / Android** | Android-/Google-nahe Tracking-/Telemetrie-Endpunkte | **18** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/full/google-android.txt) |
| **Samsung Mobile** | Samsung-nahe mobile Endpunkte | **4** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/full/samsung.txt) |
| **Xiaomi / MIUI** | Xiaomi-/MIUI-Endpunkte | **9** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/full/xiaomi.txt) |
| **Huawei** | Huawei-/Hicloud-Endpunkte | **38** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/full/huawei.txt) |
| **Gemeinsame / sonstige Mobile-Dienste** | Native-/Mobile-Endpunkte ohne sichere Einzelhersteller-Zuordnung | **582** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/mobile/full/shared-other.txt) |

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
| 🟧 **Pro++** | aggressiv | Mittel | **301** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **307** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/main/ultimate.txt) |

### Full-Listen

| Plattform | Beschreibung | Einträge | Full-Liste |
|---|---|---:|---|
| **Windows** | Windows-/Microsoft-Telemetrie und Diagnostik | **51** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/full/windows.txt) |
| **Apple** | Apple-Telemetrie und Metrics | **119** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/full/apple.txt) |
| **Android** | Android-/Hersteller-Telemetrie | **135** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/full/android.txt) |
| **Linux** | Linux-Distribution-Telemetrie | **3** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/operating-systems/full/linux.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="gaming"></a>
## 🎮 Gaming

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **1** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **5** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **21** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **38** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **40** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/main/ultimate.txt) |

### Plattform-/Dienst-Full-Listen

| Plattform / Dienst | Beschreibung | Einträge | Full-Liste |
|---|---|---:|---|
| **Steam** | explizit Steam zuordenbare Ads-/Tracking-/Telemetrie-Endpunkte | **1** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/steam.txt) |
| **Epic Games** | Epic-Games-Endpunkte | **7** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/epic-games.txt) |
| **Riot Games** | Riot-Games-Endpunkte | **1** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/riot-games.txt) |
| **Battle.net / Blizzard** | Battle.net-/Blizzard-Endpunkte | **5** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/battle-net.txt) |
| **Rockstar Games** | Rockstar-Endpunkte | **3** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/rockstar.txt) |
| **Xbox** | Xbox-Endpunkte | **8** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/xbox.txt) |
| **PlayStation** | PlayStation-/Sony-Entertainment-Endpunkte | **10** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/playstation.txt) |
| **Nintendo** | Nintendo-Endpunkte | **5** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/apps/gaming/full/nintendo.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="nas-server"></a>
## 💾 NAS & Server

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **0** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **0** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **5** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **22** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **22** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/main/ultimate.txt) |

### Hersteller-/Plattform-Full-Listen

| Hersteller / Plattform | Beschreibung | Einträge | Full-Liste |
|---|---|---:|---|
| **Synology** | Synology-Telemetrie/Services | **3** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/full/synology.txt) |
| **QNAP** | QNAP-/myQNAPcloud-Endpunkte | **6** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/full/qnap.txt) |
| **TrueNAS** | TrueNAS-/iXsystems-Endpunkte | **3** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/full/truenas.txt) |
| **Red Hat / OpenShift** | Red-Hat-/OpenShift-Endpunkte | **5** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/full/redhat-openshift.txt) |
| **HPE / Dell** | HPE-/Dell-Management-/Telemetry-Endpunkte | **5** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/nas-server/full/hpe-dell.txt) |

> In diesem Bereich ist der aktuelle Ausgangsdatenbestand klein. Deshalb können frühe Schutzstufen leer oder identisch sein. Das ist beabsichtigt und wird nicht mit erfundenen Domains aufgefüllt.

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

### Hersteller-/Ökosystem-Full-Listen

| Hersteller / Plattform | Beschreibung | Einträge | Full-Liste |
|---|---|---:|---|
| **Amazon / Alexa** | Amazon-/Alexa-Endpunkte | **13** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/full/amazon-alexa.txt) |
| **Samsung / SmartThings** | Samsung-/SmartThings-Endpunkte | **4** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/full/samsung-smartthings.txt) |
| **Xiaomi** | Xiaomi-/MIUI-nahe Smart-Home-Endpunkte | **9** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/full/xiaomi.txt) |
| **Huawei** | Huawei-/Cloud-Endpunkte | **37** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/full/huawei.txt) |
| **Sonos** | Sonos-Endpunkte | **2** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/full/sonos.txt) |
| **Gemeinsame / sonstige IoT-Dienste** | IoT-Endpunkte ohne sichere Einzelhersteller-Zuordnung | **20** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/platforms/iot-smart-home/full/shared-other.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="security"></a>
## 🛡️ Security

### Hauptlisten

| Profil | Schutz | Risiko | Einträge | Liste |
|---|---|:---:|---:|---|
| 🟩 **Light** | zurückhaltend | Minimal | **10.960** | [Light](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/light.txt) |
| 🟦 **Normal** | ausgewogen | Niedrig | **17.081** | [Normal](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/normal.txt) |
| 🟨 **Pro** | Datenschutz | Niedrig–Mittel | **594.410** | [Pro](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/pro.txt) |
| 🟧 **Pro++** | aggressiv | Mittel | **844.669** | [Pro++](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/pro-plus.txt) |
| 🟥 **Ultimate** | maximal | Hoch | **3.408.241** | [Ultimate](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/main/ultimate.txt) |

### Vollständige Security-Listen

| Schutzbereich | Beschreibung | Einträge | Full-Liste |
|---|---|---:|---|
| **Fake Shops** | potenzielle Fake-Shop-/Fraud-Domains | **10.960** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/fake-shops.txt) |
| **Cryptomining** | Mining-Infrastruktur | **6.121** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/cryptomining.txt) |
| **Phishing** | aktive und kuratierte Phishing-Domains | **577.332** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/phishing.txt) |
| **Scam / Fraud** | Betrugs-/Fraud-Domains | **265.246** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/scam.txt) |
| **Malware** | Malware-/Ransomware-/Badware-Domains | **2.656.377** | [Full](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/security/full/malware.txt) |

<p align="right"><a href="#blocklisten-navigation">⬆️ Blocklisten-Inhaltsverzeichnis</a></p>

---

<a id="lizenz"></a>
## 📜 Quellen & Lizenz

Das Repository steht unter **GNU GPL-3.0-only**. Details zur Herkunft stehen in [`THIRD_PARTY.md`](THIRD_PARTY.md) und in den `# Sources:`-Headern der einzelnen Listen.

Der statische BlackRabbitZ-Datenbestand enthält dokumentierte Anteile mehrerer Drittprojekte, darunter HaGeZi. Die neue Struktur übernimmt außerdem das sinnvolle Prinzip kumulativer Hauptstufen und separater Native-/Herstellerlisten, bleibt aber eine eigenständige BlackRabbitZ-Klassifizierung. Es gibt **keine automatische Fremdlisten-Synchronisation**.

<p align="right"><a href="#top">⬆️ Nach oben</a></p>

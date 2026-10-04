<p align="right">

🇩🇪 <strong>Deutsch</strong> · <a href="README_EN.md">🇬🇧 English</a>

</p>

<a id="top"></a>

<div align="center">

# 🐇 BlackRabbitZ DNS Blocklists

### Privacy • Geräte-Isolation • App-Blocking • Security • Family • Netzwerk-Kontrolle

[![Pi-hole](https://img.shields.io/badge/Pi--hole-kompatibel-96060C?logo=pihole&logoColor=white)](https://pi-hole.net/)
[![AdGuard Home](https://img.shields.io/badge/AdGuard%20Home-kompatibel-67B279?logo=adguard&logoColor=white)](https://github.com/AdguardTeam/AdGuardHome)
[![Unbound](https://img.shields.io/badge/Unbound-kompatibel-5B6770)](https://nlnetlabs.nl/projects/unbound/about/)
![Format](https://img.shields.io/badge/Format-Plain%20Domains-2EA44F)
![Profiles](https://img.shields.io/badge/Profile-Light%20%7C%20Normal%20%7C%20Pro%20%7C%20Pro%2B%2B%20%7C%20Ultimate-3178C6)
![Catalog](https://img.shields.io/badge/Katalog-100%20Kategorien-0088CC)

[![Validate](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/actions/workflows/validate.yml/badge.svg)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/actions/workflows/validate.yml)
[![License](https://img.shields.io/github/license/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists?label=Lizenz)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/blob/main/LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists?label=Letzter%20Commit)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/commits/main)
[![Issues](https://img.shields.io/github/issues/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/issues)
[![Repo Size](https://img.shields.io/github/repo-size/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists?label=Repo-Gr%C3%B6%C3%9Fe)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists)
[![Stars](https://img.shields.io/github/stars/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists?style=flat&label=Stars)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/stargazers)

**Modulare DNS-Blocklisten mit klar getrennten Schutzstufen für Privacy, Geräte, Apps, Security, Family und Netzwerk-Kontrolle.**

</div>

---
<!-- BRZ-TOC-START -->
# 📑 Inhaltsverzeichnis

- [🚀 Schnellstart – Werbung / Ads / Tracker / Telemetrie](#-schnellstart--werbung--ads--tracker--telemetrie)
- [💎 All-in Profile](#-all-in-profile)
- [📚 Hauptbereiche](#-hauptbereiche)
  - [👨‍👩‍👧 Family & Kinderschutz](#-family--kinderschutz)
  - [🧒 Kids Allow Only](#-kids-allow-only)
  - [📢 Werbung & Tracking](#-werbung--tracking)
  - [🧩 Software & Hardware Telemetrie](#-software--hardware-telemetrie)
  - [🤖 KI, Bots & Crawler](#-ki-bots--crawler)
  - [🛡️ Privatsphäre & Security](#️-privatsphäre--security)
  - [💻 Geräte, Systeme & Hersteller](#-geräte-systeme--hersteller)
  - [🎮 Gaming Privacy](#-gaming-privacy)
  - [☁️ Cloud, Server & Development](#️-cloud-server--development)
  - [🌐 Netzwerk & Spezialschutz](#-netzwerk--spezialschutz)
  - [🚫 Komplettblockierungen](#-komplettblockierungen)
    - [🧰 Software & Tools blockieren](#-software--tools-blockieren)
    - [🖥️ Systemblockierungen](#️-systemblockierungen)
- [🧠 Welche Liste brauche ich?](#-welche-liste-brauche-ich)
- [🐛 False Positive gefunden?](#-false-positive-gefunden)
- [❤️ Mitwirken](#️-mitwirken)
- [📜 Lizenz](#-lizenz)

---
<!-- BRZ-TOC-END -->

# 🚀 Schnellstart – Werbung / Ads / Tracker / Telemetrie

Du möchtest möglichst wenig selbst zusammenstellen? Dann wähle **genau ein Gesamtprofil**.

| Profil | Einträge | Schutz | Kompatibilität | Geeignet für | Liste |
| --- | :---: | --- | :---: | --- | --- |
| 🟩 **Light** | 234.013 | Blockiert Werbung und sehr eindeutig zuordenbare Tracker. Maximale Rücksicht auf Webseiten, Apps und Gerätefunktionen. | 🟢 Sehr hoch | Einsteiger / maximale Kompatibilität | [Liste öffnen](profiles/light.txt) |
| 🟦 **Normal** | 342.238 | Light + allgemeines Tracking, Analytics und erste Telemetrie-Endpunkte. | 🟢 Hoch | Normale Heimnetze | [Liste öffnen](profiles/normal.txt) |
| 🟨 **Pro ⭐** | 370.387 | Umfangreicher Schutz vor Ads, Trackern, Analytics, App-/Mobile-Tracking und Telemetrie bei möglichst normaler Nutzung. | 🟢 Hoch | **Für die meisten Nutzer** | [Liste öffnen](profiles/pro.txt) |
| 🟧 **Pro++** | 382.467 | Pro + aggressivere Privacy-, Telemetrie- und Geräte-Tracker. | 🟡 Mittel | Erfahrene Nutzer | [Liste öffnen](profiles/pro-plus.txt) |
| 🟥 **Ultimate** | 5.118.112 | Maximale allgemeine Ads-/Tracking-/Telemetry-Abdeckung. Höheres False-Positive-Risiko. | 🟠 Erhöht | Experten | [Liste öffnen](profiles/ultimate.txt) |

> ⭐ **Empfohlen:** `Pro` – hoher Datenschutz bei möglichst guter Kompatibilität.


<details>
<summary><strong>ℹ️ Was machen die Gesamtprofile – und was machen sie ausdrücklich nicht?</strong></summary>

| ✅ Die Gesamtprofile konzentrieren sich auf |  | 🚫 Sie sperren nicht automatisch |
|---|:---:|---|
| Werbung<br>Tracker<br>Analytics<br>Social Tracking<br>Mobile-/App-Tracking<br>Telemetrie<br>Diagnostics<br>Fingerprinting<br>bekannte Privacy-Endpunkte | **│**<br>**│**<br>**│**<br>**│**<br>**│**<br>**│**<br>**│**<br>**│**<br>**│**<br>**│** | Adult / NSFW<br>Glücksspiel<br>Social Media komplett<br>Streamingdienste komplett<br>Musikdienste komplett<br>Gaming-Plattformen komplett<br>Hersteller-Clouds komplett<br>Geräte-Updates<br>VPN / Tor / Proxy<br>ganze Apps oder Dienste |

> **Grundregel:** `Light → Normal → Pro → Pro++ → Ultimate` bedeutet mehr allgemeinen Schutz – **nicht automatisch mehr Zugriffssperren**.

</details>

---

<!-- ALL-IN-BANNER-START -->
# 💎 All-in Profile

<p align="center">
  <img src="assets/categories/09-all-in-profile.png" alt="All-in Profile" width="100%">
</p>

> **Maximalprofil:** bündelt Werbung, Tracking, Telemetrie, Family, Geräte, Security, Netzwerk und Komplettblockierungen in einer einzigen Liste.  
> ⚠️ **Sehr aggressiv:** Apps, Dienste, Updates, Cloud-Funktionen oder ganze Plattformen können dadurch absichtlich nicht mehr funktionieren.

| Profil | Einträge | Schutz | Geeignet für | Liste |
| --- | :---: | --- | --- | --- |
| 💎 **All-in** | 5.118.453 | Alle Schutz- und Blockierbereiche in einer Gesamtliste | Testsysteme, stark kontrollierte Netze, Experten | [Liste öffnen](profiles/all-in.txt) |

<!-- ALL-IN-BANNER-END -->

---

# 📚 Hauptbereiche

| Bereich | Zweck |
|---|---|
| 👨‍👩‍👧 [Family & Kinderschutz](#-family--kinderschutz) | Ungeeignete Inhalte gezielt filtern |
| 🧒 [Kids Allow Only](#-kids-allow-only) | Nur ausdrücklich erlaubte Seiten zulassen |
| 📢 [Werbung & Tracking](#-werbung--tracking) | Ads, Tracker, Analytics und Attribution |
| 🧩 [Software & Hardware Telemetrie](#-software--hardware-telemetrie) | Telemetrie von Software, Treibern und Hardware-Herstellern |
| 🤖 [KI, Bots & Crawler](#-ki-bots--crawler) | KI-Crawler, Scraper, Bots, Training und AI-Telemetrie |
| 🛡️ [Privatsphäre & Security](#️-privatsphäre--security) | Privacy-Schutz sowie Malware, Phishing und Threat Intelligence |
| 💻 [Geräte, Systeme & Hersteller](#-geräte-systeme--hersteller) | Geräte-, Hersteller-, ISP- und Ökosystem-Kommunikation steuern |
| 🎮 [Gaming Privacy](#-gaming-privacy) | Gaming-Telemetrie und Launcher-Tracking reduzieren |
| ☁️ [Cloud, Server & Development](#️-cloud-server--development) | Cloud-, Hosting-, CI/CD- und Entwicklerdienste |
| 🌐 [Netzwerk & Spezialschutz](#-netzwerk--spezialschutz) | DoH, VPN, Proxy, Tor, Spezial- und Regionallisten |
| 🚫 [Komplettblockierungen](#-komplettblockierungen) | Apps, Software, Tools und komplette Systeme gezielt sperren |

<br>

---

<br>

---

<br>


# 👨‍👩‍👧 Family & Kinderschutz

<!-- CATEGORY-BANNER:02-family-kinderschutz.png -->
<p align="center">
  <img src="assets/categories/02-family-kinderschutz.png" alt="Family & Kinderschutz" width="100%">
</p>
<!-- /CATEGORY-BANNER -->


## Fertige Family-Profile

| Profil | Einträge | Schutz | Geeignet für | Liste |
| --- | :---: | --- | --- | --- |
| 🟩 **Light** | 998.924 | Grundlegender Jugendschutz mit geringer Einschränkung | Jüngere Nutzer mit viel Freiraum | [Liste öffnen](family/main/light.txt) |
| 🟦 **Normal** | 1.419.159 | Adult + Gambling + SafeSearch-Basis | Familiennetzwerke | [Liste öffnen](family/main/normal.txt) |
| 🟨 **Pro ⭐** | 1.430.117 | Normal + Drugs + Violence + Weapons + Dating | **Empfohlen für Kindergeräte** | [Liste öffnen](family/main/pro.txt) |
| 🟧 **Pro++** | 1.769.650 | Pro + Social + Chats + Anti-Piracy + stärkerer Umgehungsschutz | Strengere Familiennetze | [Liste öffnen](family/main/pro-plus.txt) |
| 🟥 **Ultimate** | 2.347.190 | Maximale Family-Filterung ohne Allow-Only-Prinzip | Stark kontrollierte Geräte | [Liste öffnen](family/main/ultimate.txt) |

<details>
<summary><strong>📂 Einzelne Family-Listen anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste anzeigen |
| --- | :---: | --- | --- |
| 🔞 **Adult / NSFW** | 998.924 | Blockiert Pornografie, Adult-/NSFW-Seiten und zugehörige Dienste. | [Öffnen](lists/family/adult-nsfw.txt) |
| 🎰 **Gambling** | 420.536 | Blockiert Casinos, Sportwetten, Betting und Glücksspielplattformen. | [Öffnen](lists/family/gambling.txt) |
| 🎰 **Gambling Medium** | 420.536 | Kleinere Gambling-Variante mit geringerer Datenmenge. | [Öffnen](lists/family/gambling-medium.txt) |
| 🎰 **Gambling Mini** | 420.536 | Stark größenoptimierte Gambling-Variante für ressourcenarme Systeme. | [Öffnen](lists/family/gambling-mini.txt) |
| 💊 **Drugs** | 55 | Blockiert bekannte Drogenmärkte und einschlägige Plattformen. | [Öffnen](lists/family/drugs.txt) |
| 🩸 **Violence / Gore** | 53 | Blockiert Gore-, Shock- und extreme Gewaltinhalte. | [Öffnen](lists/family/violence-gore.txt) |
| 🔫 **Weapons** | 89 | Blockiert ausgewählte Waffenhandels- und problematische Waffenplattformen. | [Öffnen](lists/family/weapons.txt) |
| 💕 **Dating** | 40 | Blockiert Dating-Webseiten und Dating-Apps. | [Öffnen](lists/family/dating.txt) |
| 💬 **Social Networks** | 47 | Blockiert klassische soziale Netzwerke. | [Öffnen](lists/family/social-networks.txt) |
| 💭 **Chats & Communities** | 3 | Blockiert ausgewählte Chats, anonyme Communities und Community-Plattformen. | [Öffnen](lists/family/chats-communities.txt) |
| 🔍 **SafeSearch Unsupported** | 205 | Blockiert Suchdienste, die keinen verlässlichen SafeSearch-Modus anbieten. | [Öffnen](lists/family/safesearch-unsupported.txt) |
| 💀 **Anti-Piracy** | 101 | Blockiert Plattformen, die überwiegend zur unerlaubten Verbreitung urheberrechtlich geschützter Inhalte dienen. | [Öffnen](lists/family/anti-piracy.txt) |
| 🕳️ **Family Bypass Protection** | 306 | Blockiert typische DNS-/Proxy-/VPN-/Tor-Umgehungswege für Family-Gruppen. | [Öffnen](lists/family/bypass-protection.txt) |

</details>

---

<br>

---

<br>


# 🧒 Kids Allow Only

<!-- CATEGORY-BANNER:03-kids-allow-only.png -->
<p align="center">
  <img src="assets/categories/03-kids-allow-only.png" alt="Kids Allow Only" width="100%">
</p>
<!-- /CATEGORY-BANNER -->


**Komplett anderer Ansatz als Family:** Standardmäßig ist nichts erlaubt. Nur explizit freigegebene Domains funktionieren.

<details>
<summary><strong>🛠️ Pi-hole v6+: Kids Allow Only einrichten</strong></summary>

> **Prinzip:** Für die Kindergeräte wird eine eigene Pi-hole-Gruppe erstellt.  
> Diese Gruppe bekommt eine **Regex-Deny-Regel `.*`**, die zunächst alle Domains sperrt.  
> Anschließend wird **genau eine Kids-Allow-Only-Liste als abonnierte Allowlist** hinzugefügt.  
> Dadurch funktionieren nur die ausdrücklich erlaubten Domains.

### 1. Kindergerät eindeutig festlegen

Gib dem Kindergerät möglichst eine **feste IP-Adresse bzw. DHCP-Reservierung**, damit Pi-hole es dauerhaft derselben Gruppe zuordnen kann.

Beispiel:

`192.168.178.50` → Tablet des Kindes

### 2. Eigene Pi-hole-Gruppe erstellen

In Pi-hole:

**Group Management → Groups → Add Group**

Name zum Beispiel:

`Kids-Allow-Only`

### 3. Kindergerät der Gruppe zuweisen

Unter:

**Group Management → Clients**

das Kindergerät hinzufügen und ausschließlich der Gruppe **Kids-Allow-Only** zuweisen.

> **Empfehlung:** Die Zuordnung zur Gruppe `Default` für dieses Gerät entfernen, damit normale Netzwerkregeln nicht unerwartet mit dem Allow-Only-Profil kollidieren.

### 4. Passendes Kids-Profil auswählen

Wähle **genau eine** der fertigen Listen:

| Profil | Geeignet für |
|---|---|
| 🟩 **Basic** | sehr kleine, stark eingeschränkte Auswahl |
| 🟦 **School** | Schulgeräte und Lernplattformen |
| 🟨 **Learning ⭐** | Lernen + ausgewählte Kinder-/Medienangebote |
| 🟧 **Extended** | größere Auswahl inkl. ausgewählter Kommunikation |

Öffne die gewünschte Liste auf GitHub, klicke auf **Raw** und kopiere die Raw-URL.

### 5. Kids-Liste als abonnierte Allowlist eintragen

In **Pi-hole v6+** die kopierte Raw-URL als **Subscribed Allowlist / abonnierte Allowlist** hinzufügen.

Wichtig:

- Typ: **Allow**
- Gruppe: **nur `Kids-Allow-Only`**
- nicht der normalen `Default`-Gruppe zuweisen

Pi-hole v6 unterstützt abonnierte externe Allowlists direkt.

### 6. Alles andere sperren

Unter:

**Group Management → Domains**

eine neue **Regex-Denylist** anlegen:

```text
.*
```

Diese Regel ebenfalls **nur** der Gruppe `Kids-Allow-Only` zuweisen.

> ⚠️ **Niemals `.*` versehentlich der Gruppe `Default` zuweisen.**  
> Sonst blockierst du praktisch das gesamte Internet für alle Geräte, die diese Gruppe verwenden.

### 7. Listen aktualisieren

Anschließend die Listen/Gravity aktualisieren.

Über die Pi-hole-Oberfläche oder per Terminal:

```bash
pihole updateGravity
```

### 8. Funktion testen

Auf dem Kindergerät testen:

- eine Domain aus der Allowlist → **muss funktionieren**
- eine beliebige nicht freigegebene Domain → **muss blockiert werden**

Im **Query Log** kannst du genau sehen, welche Domains erlaubt oder blockiert wurden.

### 9. Wenn eine erlaubte Webseite nicht vollständig funktioniert

Viele Webseiten benötigen zusätzliche Domains für Bilder, Videos, Login, APIs oder CDNs.

Wenn eine eigentlich erlaubte Seite nicht richtig lädt:

1. Seite öffnen.
2. Pi-hole **Query Log** beobachten.
3. Die tatsächlich benötigten blockierten Domains prüfen.
4. Nur eindeutig notwendige Domains zusätzlich erlauben.
5. Diese Domains langfristig in die passende Kids-Liste bzw. Runtime-Liste aufnehmen.

> Keine kompletten Cloud-/CDN-Zonen pauschal erlauben. Sonst kann das Allow-Only-Prinzip sehr schnell ausgehebelt werden.

### 10. Umgehung verhindern

Kids Allow Only funktioniert nur zuverlässig, wenn das Gerät **Pi-hole tatsächlich als DNS-Server verwendet**.

Für stärker kontrollierte Kindergeräte zusätzlich sinnvoll:

- externes DNS am Router/Firewall blockieren
- DoH / DoT / Private DNS einschränken
- VPN-/Proxy-Umgehungen einschränken
- IPv4 **und** IPv6 berücksichtigen

DNS-Filtering allein ist kein vollständiger Ersatz für Firewall-, Geräte- oder Jugendschutzrichtlinien.

### Pi-hole v5

Das direkte Abonnieren externer **Allowlists** wurde erst mit **Pi-hole v6** eingeführt.  
Bei Pi-hole v5 müssten die erlaubten Domains einzeln bzw. per eigenem Importmechanismus als Allowlist eingetragen werden.

</details>

## Fertige Kids-Allow-Only-Profile

| Profil | Einträge | Schutz | Geeignet für | Liste |
| --- | :---: | --- | --- | --- |
| 🟩 **Basic** | 39 | Nur wichtige Lern-, Such- und Wissensdienste | Kleine Kinder | [Liste öffnen](lists/kids-allow-only/basic.txt) |
| 🟦 **School** | 39 | Basic + typische Schul- und Lernplattformen | Schulgeräte | [Liste öffnen](lists/kids-allow-only/school.txt) |
| 🟨 **Learning ⭐** | 26 | School + ausgewählte Mediatheken, Lernvideos und Kinderangebote | **Lern-Tablets / Familiengeräte** | [Liste öffnen](lists/kids-allow-only/learning.txt) |
| 🟧 **Extended** | 58 | Learning + ausgewählte Kommunikation und zusätzliche sichere Dienste | Ältere Kinder | [Liste öffnen](lists/kids-allow-only/extended.txt) |

<details>
<summary><strong>📂 Einzelne Allow-Only-Listen anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste anzeigen |
| --- | :---: | --- | --- |
| 📚 **Education** | 17 | Erlaubte Lern- und Bildungsplattformen. | [Öffnen](lists/kids-allow-only/education.txt) |
| 🏫 **School Platforms** | 17 | Erlaubte Schulportale, Lernmanagement- und Unterrichtsdienste. | [Öffnen](lists/kids-allow-only/school-platforms.txt) |
| 🔎 **Safe Search** | 39 | Erlaubte Suchmaschinen mit geeigneten Schutzoptionen. | [Öffnen](lists/kids-allow-only/safe-search.txt) |
| 📖 **Knowledge** | 39 | Erlaubte Wissens-, Lexikon- und Nachschlageangebote. | [Öffnen](lists/kids-allow-only/knowledge.txt) |
| 🎬 **Kids Media** | 16 | Ausgewählte Kinder-, Bildungs- und Mediathek-Angebote. | [Öffnen](lists/kids-allow-only/kids-media.txt) |
| 💬 **Approved Communication** | 39 | Gezielt erlaubte Kommunikationsdienste. | [Öffnen](lists/kids-allow-only/approved-communication.txt) |

</details>

---

<br>

---

<br>


# 📢 Werbung & Tracking

<!-- CATEGORY-BANNER:01-werbung-tracking.png -->
<p align="center">
  <img src="assets/categories/01-werbung-tracking.png" alt="Werbung & Tracking" width="100%">
</p>
<!-- /CATEGORY-BANNER -->


## Fertige Ads-&-Tracking-Profile

| Profil | Einträge | Schutz | Geeignet für | Liste |
| --- | :---: | --- | --- | --- |
| 🟩 **Light** | 31.392 | Eindeutige Werbung + sichere Tracker | Maximale Kompatibilität | [Liste öffnen](lists/privacy/main/light.txt) |
| 🟦 **Normal** | 55.932 | Light + allgemeines Tracking + Analytics | Normale Nutzung | [Liste öffnen](lists/privacy/main/normal.txt) |
| 🟨 **Pro ⭐** | 83.565 | Normal + Social + Mobile + App Tracking | **Die meisten Nutzer** | [Liste öffnen](lists/privacy/main/pro.txt) |
| 🟧 **Pro++** | 344.214 | Pro + Affiliate + Conversion + aggressive Tracker | Privacy-orientierte Nutzer | [Liste öffnen](lists/privacy/main/pro-plus.txt) |
| 🟥 **Ultimate** | 348.192 | Maximale Ads-/Tracking-Abdeckung | Experten | [Liste öffnen](lists/privacy/main/ultimate.txt) |

<details>
<summary><strong>📂 Einzelne Werbung-&-Tracking-Listen anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste anzeigen |
| --- | :---: | --- | --- |
| 📣 **Ads / Werbung** | 218.123 | Klassische Werbenetzwerke und Ad-Delivery. | [Öffnen](lists/privacy/full/ads.txt) |
| 🪟 **Pop-Up Ads** | 512 | Pop-up- und Pop-under-Werbung. | [Öffnen](lists/privacy/full/pop-up-ads.txt) |
| 🔗 **Affiliate Tracking** | 608 | Affiliate-, Referral- und Conversion-Tracking. | [Öffnen](lists/privacy/full/affiliate-tracking.txt) |
| ⚠️ **Aggressive Privacy** | 625 | Aggressivere Privacy-Endpunkte mit höherem Breakage-Risiko. | [Öffnen](lists/privacy/full/aggressive-privacy.txt) |
| 📊 **Analytics** | 34.728 | Web-, App- und Nutzungsanalyse. | [Öffnen](lists/privacy/full/analytics.txt) |
| 🤖 **Captcha / Antibot** | 378 | Ausgewählte Captcha-/Antibot-Infrastruktur. | [Öffnen](lists/privacy/full/captcha-antibot.txt) |
| 🌐 **CDN Tracking** | 19 | Tracking über CDN-/Edge-Infrastruktur. | [Öffnen](lists/privacy/full/cdn-tracking.txt) |
| 💬 **Chat Support** | 49 | Tracking in Chat-/Support-Systemen. | [Öffnen](lists/privacy/full/chat-support.txt) |
| 🍪 **Consent / CMP** | 41 | Consent- und CMP-Infrastruktur; bewusst aggressiv. | [Öffnen](lists/privacy/full/consent-cmp.txt) |
| 💥 **Crash Reporting** | 85 | Crash-, Fehler- und Ereignisberichte. | [Öffnen](lists/privacy/full/crash-reporting.txt) |
| 🗂️ **CRM** | 106 | CRM- und Lead-Tracking. | [Öffnen](lists/privacy/full/crm.txt) |
| 🛒 **E-Commerce Tracking** | 42 | Shop-, Conversion- und Commerce-Tracking. | [Öffnen](lists/privacy/full/ecommerce.txt) |
| 🔤 **External Fonts** | 3 | Externe Font-Endpunkte mit Privacy-Relevanz. | [Öffnen](lists/privacy/full/external-fonts.txt) |
| 🧬 **Fingerprinting** | 10 | Browser-/Device-Fingerprinting. | [Öffnen](lists/privacy/full/fingerprinting.txt) |
| 📢 **Marketing** | 2.004 | Marketing- und Kampagnenmessung. | [Öffnen](lists/privacy/full/marketing.txt) |
| 📱 **Mobile Tracking** | 208 | Mobile Attribution und SDK-Tracking. | [Öffnen](lists/privacy/full/mobile-tracking.txt) |
| 🧩 **Native Tracking** | 587 | Integrierte Tracker von OS, Apps und Geräten. | [Öffnen](lists/privacy/full/native-tracking.txt) |
| ✉️ **Newsletter Tracking** | 156 | Newsletter- und Mail-Tracking. | [Öffnen](lists/privacy/full/newsletter-tracking.txt) |
| 💳 **Payment Tracking** | 17 | Tracking rund um Zahlungsprozesse. | [Öffnen](lists/privacy/full/payment-tracking.txt) |
| 🔔 **Push Notifications** | 73 | Ausgewählte Push-/Notification-Endpunkte. | [Öffnen](lists/privacy/full/push-notifications.txt) |
| ⭐ **Recommendations** | 360 | Empfehlungs- und Personalisierungsdienste. | [Öffnen](lists/privacy/full/recommendations.txt) |
| 🔎 **Search Tracking** | 1 | Such- und Search-Tracking. | [Öffnen](lists/privacy/full/search-tracking.txt) |
| 📈 **SEO Tracking** | 115 | SEO-/Marketing-Messsysteme. | [Öffnen](lists/privacy/full/seo-tracking.txt) |
| 🎥 **Session Replay** | 195 | Session-Replay und Verhaltensaufzeichnung. | [Öffnen](lists/privacy/full/session-replay.txt) |
| 👥 **Social Tracking** | 29 | Tracking sozialer Netzwerke. | [Öffnen](lists/privacy/full/social-tracking.txt) |
| 📡 **Telemetry** | 27.984 | Allgemeine Telemetrie-Endpunkte. | [Öffnen](lists/privacy/full/telemetry.txt) |
| 👁️ **Trackers** | 106.915 | Große allgemeine Tracker-Liste. | [Öffnen](lists/privacy/full/trackers.txt) |
| 🟣 **Tracking Pixels** | 866 | Tracking-Pixel und Beacons. | [Öffnen](lists/privacy/full/tracking-pixels.txt) |
| 🔁 **Tracking Redirects** | 306 | Tracking-Weiterleitungen und Redirector-Infrastruktur. | [Öffnen](lists/privacy/full/tracking-redirects.txt) |

</details>

---

<br>

---

<br>



---

<br>

# 🧩 Software & Hardware Telemetrie

Gezielte Datenschutzlisten für **Software, Treiber, PC-Komponenten und Peripherie**. Die Privacy-Variante soll Telemetrie reduzieren, ohne die Kernfunktion absichtlich abzuschalten.

## Fertige Telemetrie-Profile

| Profil | Einträge | Schutz | Risiko | Liste |
| --- | :---: | --- | :---: | --- |
| 🟩 **Light** | 73 | sehr sichere Software-/Hardware-Telemetrie | Minimal | [Liste öffnen](lists/platforms/software-hardware-telemetry/main/light.txt) |
| 🟦 **Normal** | 73 | Light + zusätzliche Analytics | Niedrig | [Liste öffnen](lists/platforms/software-hardware-telemetry/main/normal.txt) |
| 🟨 **Pro ⭐** | 78 | umfangreicher Telemetrie-Schutz | Niedrig–Mittel | [Liste öffnen](lists/platforms/software-hardware-telemetry/main/pro.txt) |
| 🟧 **Pro++** | 78 | aggressivere Hersteller-Telemetrie | Mittel | [Liste öffnen](lists/platforms/software-hardware-telemetry/main/pro-plus.txt) |
| 🟥 **Ultimate** | 83 | maximaler Datenbestand dieses Bereichs | Hoch | [Liste öffnen](lists/platforms/software-hardware-telemetry/main/ultimate.txt) |

<details>
<summary><strong>📂 Software-/Hardware-Hersteller anzeigen</strong></summary>

| Name | Einträge | 🛡️ Privacy | ⚠️ Restrict | 🔄 Updates blockieren |
| --- | :---: | :---: | :---: | :---: |
| **Adobe** | 38 | **34 Einträge**<br>[Liste](lists/device-control/software-hardware/adobe/privacy.txt) | **38 Einträge**<br>[Liste](lists/device-control/software-hardware/adobe/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/software-hardware/adobe/updates.txt) |
| **AMD** | 2 | **1 Einträge**<br>[Liste](lists/device-control/software-hardware/amd/privacy.txt) | **2 Einträge**<br>[Liste](lists/device-control/software-hardware/amd/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/software-hardware/amd/updates.txt) |
| **Autodesk** | 7 | **7 Einträge**<br>[Liste](lists/device-control/software-hardware/autodesk/privacy.txt) | **7 Einträge**<br>[Liste](lists/device-control/software-hardware/autodesk/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/software-hardware/autodesk/updates.txt) |
| **Corsair** | 2 | **2 Einträge**<br>[Liste](lists/device-control/software-hardware/corsair/privacy.txt) | **2 Einträge**<br>[Liste](lists/device-control/software-hardware/corsair/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/software-hardware/corsair/updates.txt) |
| **Intel** | 3 | **3 Einträge**<br>[Liste](lists/device-control/software-hardware/intel/privacy.txt) | **3 Einträge**<br>[Liste](lists/device-control/software-hardware/intel/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/software-hardware/intel/updates.txt) |
| **Logitech** | 4 | **4 Einträge**<br>[Liste](lists/device-control/software-hardware/logitech/privacy.txt) | **4 Einträge**<br>[Liste](lists/device-control/software-hardware/logitech/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/software-hardware/logitech/updates.txt) |
| **Nvidia** | 9 | **9 Einträge**<br>[Liste](lists/device-control/software-hardware/nvidia/privacy.txt) | **9 Einträge**<br>[Liste](lists/device-control/software-hardware/nvidia/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/software-hardware/nvidia/updates.txt) |
| **Razer** | 3 | **3 Einträge**<br>[Liste](lists/device-control/software-hardware/razer/privacy.txt) | **3 Einträge**<br>[Liste](lists/device-control/software-hardware/razer/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/software-hardware/razer/updates.txt) |

</details>

---

<br>

# 🤖 KI, Bots & Crawler

Listen für **AI-/LLM-Crawler, Scraper, Training-Bots, SEO-Bots und unerwünschte automatisierte Zugriffe**.

> DNS-Blocking kann Crawler-Domains sperren, ersetzt aber keine WAF-, Webserver- oder `robots.txt`-Regeln.

## Fertige KI-/Bot-Profile

| Profil | Einträge | Schutz | Risiko | Liste |
| --- | :---: | --- | :---: | --- |
| 🟩 **Light** | 13 | sehr konservative Bot-/Crawler-Auswahl | Minimal | [Liste öffnen](lists/automation/main/light.txt) |
| 🟦 **Normal** | 28 | zusätzliche Crawler und Tracking-Endpunkte | Niedrig | [Liste öffnen](lists/automation/main/normal.txt) |
| 🟨 **Pro ⭐** | 33 | breiter KI-/Crawler-Schutz | Niedrig–Mittel | [Liste öffnen](lists/automation/main/pro.txt) |
| 🟧 **Pro++** | 50 | aggressivere Bot-/Scraper-Blockierung | Mittel | [Liste öffnen](lists/automation/main/pro-plus.txt) |
| 🟥 **Ultimate** | 301 | maximaler Datenbestand dieses Bereichs | Hoch | [Liste öffnen](lists/automation/main/ultimate.txt) |

<details>
<summary><strong>📂 Einzelne KI-, Bot- & Crawler-Listen anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste |
| --- | :---: | --- | --- |
| **Aggressive Crawlers** | 15 | aggressive bekannte Crawler-Operatoren | [Öffnen](lists/automation/full/aggressive-crawlers.txt) |
| **AI Crawlers** | 10 | Crawler von KI-/AI-Anbietern | [Öffnen](lists/automation/full/ai-crawlers.txt) |
| **AI Scrapers** | 3 | Scraping-Endpunkte mit KI-Bezug | [Öffnen](lists/automation/full/ai-scrapers.txt) |
| **AI Telemetry** | 36 | Telemetrie von KI-Diensten | [Öffnen](lists/automation/full/ai-telemetry.txt) |
| **AI Tracking** | 44 | Tracking durch KI-Dienste | [Öffnen](lists/automation/full/ai-tracking.txt) |
| **LLM Crawlers** | 188 | LLM-Crawler und verwandte Infrastruktur | [Öffnen](lists/automation/full/llm-crawlers.txt) |
| **Malicious Bots** | 1 | bekannte schädliche Bots | [Öffnen](lists/automation/full/malicious-bots.txt) |
| **SEO Bots** | 5 | SEO-Crawler und automatisierte Analyse | [Öffnen](lists/automation/full/seo-bots.txt) |
| **Training Bots** | 6 | Bots für Training/Datensammlung | [Öffnen](lists/automation/full/training-bots.txt) |
| **Web Crawlers** | 62 | allgemeine Webcrawler | [Öffnen](lists/automation/full/web-crawlers.txt) |

</details>


# 🛡️ Privatsphäre & Security

<!-- CATEGORY-BANNER:04-privatsphaere-security.png -->
<p align="center">
  <img src="assets/categories/04-privatsphaere-security.png" alt="Privatsphäre & Security" width="100%">
</p>
<!-- /CATEGORY-BANNER -->


## Fertige Privacy-&-Security-Profile

| Profil | Einträge | Schutz | Geeignet für | Liste |
| --- | :---: | --- | --- | --- |
| 🟩 **Light** | 10.960 | Sichere Privacy-/Security-Basis | Maximale Kompatibilität | [Liste öffnen](lists/security/main/light.txt) |
| 🟦 **Normal** | 17.081 | Telemetrie + Malware + Phishing | Normale Heimnetze | [Liste öffnen](lists/security/main/normal.txt) |
| 🟨 **Pro ⭐** | 594.410 | Umfassende Telemetrie + Malware + Phishing + Scam | **Empfohlen** | [Liste öffnen](lists/security/main/pro.txt) |
| 🟧 **Pro++** | 844.669 | Pro + aggressive Privacy- und Threat-Listen | Erfahrene Nutzer | [Liste öffnen](lists/security/main/pro-plus.txt) |
| 🟥 **Ultimate** | 3.408.596 | Maximale Privacy-/Security-Abdeckung | Experten | [Liste öffnen](lists/security/main/ultimate.txt) |

<details>
<summary><strong>🔐 Einzelne Privacy-Listen anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste anzeigen |
| --- | :---: | --- | --- |
| 📊 **General Telemetry** | 27.984 | Blockiert allgemeine Produkt-, App- und Herstellertelemetrie. | [Öffnen](lists/privacy-security/privacy/general-telemetry.txt) |
| 🩺 **Diagnostics** | 27.984 | Reduziert Diagnose-, Fehler- und Nutzungsdaten. | [Öffnen](lists/privacy-security/privacy/diagnostics.txt) |
| 💥 **Crash Reporting** | 85 | Blockiert ausgewählte automatische Crash-Reports. | [Öffnen](lists/privacy-security/privacy/crash-reporting.txt) |
| 🧬 **Fingerprinting** | 10 | Blockiert bekannte Infrastruktur zur Wiedererkennung und Profilbildung. | [Öffnen](lists/privacy-security/privacy/fingerprinting.txt) |
| 📈 **Usage Reporting** | 34.728 | Blockiert ausgewählte Nutzungsstatistiken und Usage Reports. | [Öffnen](lists/privacy-security/privacy/usage-reporting.txt) |
| ☁️ **Cloud Analytics** | 34.728 | Reduziert optionale Cloud-Analytics und Hersteller-Messdienste. | [Öffnen](lists/privacy-security/privacy/cloud-analytics.txt) |

</details>

<details>
<summary><strong>🛡️ Einzelne Security-Listen anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste anzeigen |
| --- | :---: | --- | --- |
| 🦠 **Malware** | 2.656.377 | Blockiert bekannte Malware-, Ransomware- und Schadsoftware-Infrastruktur. | [Öffnen](lists/privacy-security/security/malware.txt) |
| 🎣 **Phishing** | 577.332 | Blockiert bekannte Phishing- und Credential-Diebstahl-Domains. | [Öffnen](lists/privacy-security/security/phishing.txt) |
| 💰 **Scam & Internet Fraud** | 265.246 | Blockiert Betrugs-, Scam- und deceptive Domains. | [Öffnen](lists/privacy-security/security/scam-fraud.txt) |
| 🛒 **Fake Shops** | 10.960 | Blockiert bekannte Fake-Shops und betrügerische Store-Domains. | [Öffnen](lists/privacy-security/security/fake-shops.txt) |
| 🎭 **Fake Sites** | 265.318 | Blockiert Fake-Streaming-, Fake-Download-, Fake-Support- und sonstige Täuschungsseiten. | [Öffnen](lists/privacy-security/security/fake-sites.txt) |
| ⛏️ **Cryptomining** | 6.121 | Blockiert bekannte Browser-/Remote-Mining-Infrastruktur. | [Öffnen](lists/privacy-security/security/cryptomining.txt) |
| 🤖 **Botnets** | 53 | Blockiert bekannte Botnet-Infrastruktur. | [Öffnen](lists/privacy-security/security/botnets.txt) |
| 🎛️ **Command & Control** | 53 | Blockiert bekannte C2-Infrastruktur. | [Öffnen](lists/privacy-security/security/command-control.txt) |
| 🔐 **Threat Intelligence Full** | 3.408.596 | Große kombinierte Threat-Intelligence-Liste. | [Öffnen](lists/privacy-security/security/tif-full.txt) |
| 🔐 **Threat Intelligence Medium** | 844.669 | Mittlere TIF-Variante mit reduziertem Ressourcenbedarf. | [Öffnen](lists/privacy-security/security/tif-medium.txt) |
| 🔐 **Threat Intelligence Mini** | 594.410 | Kleine priorisierte TIF-Variante. | [Öffnen](lists/privacy-security/security/tif-mini.txt) |
| 🌐 **Threat Intelligence IPv4** | 0 | IPv4-Begleitliste für Firewall-/IP-basierte Threat-Intelligence-Filterung. | [Öffnen](lists/privacy-security/security/tif-ipv4.txt) |
| 🆕 **NRD 1–7 Tage** | 15.000 | Neu registrierte Domains der letzten 1–7 Tage; erhöhtes False-Positive-Risiko. | [Öffnen](lists/privacy-security/security/nrd-1-7d.txt) |
| 🆕 **NRD 8–14 Tage** | 0 | Neu registrierte Domains der Tage 8–14. | [Öffnen](lists/privacy-security/security/nrd-8-14d.txt) |
| 🆕 **NRD 15–21 Tage** | 0 | Neu registrierte Domains der Tage 15–21. | [Öffnen](lists/privacy-security/security/nrd-15-21d.txt) |
| 🆕 **NRD 22–28 Tage** | 0 | Neu registrierte Domains der Tage 22–28. | [Öffnen](lists/privacy-security/security/nrd-22-28d.txt) |
| 🆕 **NRD 29–35 Tage** | 0 | Neu registrierte Domains der Tage 29–35. | [Öffnen](lists/privacy-security/security/nrd-29-35d.txt) |
| 🧬 **DGA 7 Tage** | 0 | Algorithmisch erzeugte Domains aus aktuellen DGA-Daten. | [Öffnen](lists/privacy-security/security/dga-7d.txt) |
| 🧬 **DGA 14 Tage** | 0 | Größere DGA-Abdeckung über 14 Tage. | [Öffnen](lists/privacy-security/security/dga-14d.txt) |
| 🧬 **DGA 30 Tage** | 0 | Maximale DGA-Abdeckung über 30 Tage. | [Öffnen](lists/privacy-security/security/dga-30d.txt) |
| 🔏 **Dynamic DNS** | 74 | Blockiert bekannte Dynamic-DNS-Dienste mit erhöhtem Missbrauchspotenzial. | [Öffnen](lists/privacy-security/security/dynamic-dns.txt) |
| 💻 **Badware Hoster** | 24 | Blockiert besonders häufig für Schadsoftware missbrauchte Hosting-Infrastruktur. | [Öffnen](lists/privacy-security/security/badware-hoster.txt) |
| 🔮 **Most Abused TLDs** | 6.490 | Aggressive Liste häufig missbrauchter Top-Level-Domains. | [Öffnen](lists/privacy-security/security/abused-tlds.txt) |

</details>

---

<br>

---

<br>


# 💻 Geräte, Systeme & Hersteller

<!-- CATEGORY-BANNER:05-geraete-systeme-hersteller.png -->
<p align="center">
  <img src="assets/categories/05-geraete-systeme-hersteller.png" alt="Geräte, Systeme & Hersteller" width="100%">
</p>
<!-- /CATEGORY-BANNER -->


Hier steuerst du direkt, **wie stark einzelne Betriebssysteme, Geräte oder Hersteller eingeschränkt werden sollen**.

<details>
<summary><strong>ℹ️ Privacy, Restrict und Updates blockieren – Erklärung anzeigen</strong></summary>

| Modus | Erklärung |
|---|---|
| 🛡️ **Privacy** | Blockiert bekannte Tracker, Analytics und Telemetrie. Die normalen Kernfunktionen sollen möglichst erhalten bleiben. |
| ⚠️ **Restrict** | Enthält Privacy und blockiert zusätzlich optionale Hersteller-, Cloud-, Empfehlungs- und Komfortdienste. Einzelne Zusatzfunktionen können ausfallen. |
| 🔄 **Updates blockieren** | Blockiert gezielt die Update-, Firmware- oder Software-Update-Infrastruktur des jeweiligen Systems oder Herstellers. |

> **Du wählst pro Gerät/System nur die Wirkung, die du wirklich möchtest.**

</details>

## 📦 Geräte-Gesamtlisten

Du möchtest nicht jeden Hersteller einzeln auswählen? Dann kannst du komplette **Gerätegruppen** oder unten die **All-in-Liste** verwenden.

| Gerätegruppe | Einträge | 🛡️ Privacy | ⚠️ Restrict | 🔄 Updates blockieren |
| --- | :---: | :---: | :---: | :---: |
| 💻 **Computer / Laptop** | 307 | **257 Einträge**<br>[Liste](lists/device-control/groups/computer/privacy.txt) | **279 Einträge**<br>[Liste](lists/device-control/groups/computer/restrict.txt) | **28 Einträge**<br>[Liste](lists/device-control/groups/computer/updates.txt) |
| 📺 **TV / Streaming-Geräte** | 14.077 | **14.047 Einträge**<br>[Liste](lists/device-control/groups/tv-streaming/privacy.txt) | **14.061 Einträge**<br>[Liste](lists/device-control/groups/tv-streaming/restrict.txt) | **16 Einträge**<br>[Liste](lists/device-control/groups/tv-streaming/updates.txt) |
| 📱 **Handy / Tablet** | 13.811 | **13.773 Einträge**<br>[Liste](lists/device-control/groups/mobile-tablet/privacy.txt) | **13.782 Einträge**<br>[Liste](lists/device-control/groups/mobile-tablet/restrict.txt) | **29 Einträge**<br>[Liste](lists/device-control/groups/mobile-tablet/updates.txt) |
| 🏠 **Smart Home / IoT** | 446 | **417 Einträge**<br>[Liste](lists/device-control/groups/smart-home-iot/privacy.txt) | **434 Einträge**<br>[Liste](lists/device-control/groups/smart-home-iot/restrict.txt) | **12 Einträge**<br>[Liste](lists/device-control/groups/smart-home-iot/updates.txt) |
| 💾 **NAS / Server** | 17 | **14 Einträge**<br>[Liste](lists/device-control/groups/nas-server/privacy.txt) | **17 Einträge**<br>[Liste](lists/device-control/groups/nas-server/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/groups/nas-server/updates.txt) |
| 🌐 **Router / Netzwerkgeräte** | 70 | **57 Einträge**<br>[Liste](lists/device-control/groups/network/privacy.txt) | **67 Einträge**<br>[Liste](lists/device-control/groups/network/restrict.txt) | **3 Einträge**<br>[Liste](lists/device-control/groups/network/updates.txt) |
| 🎮 **Konsole / Gaming-Geräte** | 6 | **5 Einträge**<br>[Liste](lists/device-control/groups/gaming-devices/privacy.txt) | **6 Einträge**<br>[Liste](lists/device-control/groups/gaming-devices/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/groups/gaming-devices/updates.txt) |
| 🗣️ **Sprachassistenten** | 13.926 | **13.846 Einträge**<br>[Liste](lists/device-control/groups/voice-assistants/privacy.txt) | **13.882 Einträge**<br>[Liste](lists/device-control/groups/voice-assistants/restrict.txt) | **44 Einträge**<br>[Liste](lists/device-control/groups/voice-assistants/updates.txt) |
| 🧩 **All-in** | 14.633 | **14.523 Einträge**<br>**[Alle Privacy-Listen](lists/device-control/all-in/privacy.txt)** | **14.577 Einträge**<br>**[Alle Restrict-Listen](lists/device-control/all-in/restrict.txt)** | **56 Einträge**<br>**[Alle Update-Blocklisten](lists/device-control/all-in/updates.txt)** |

<details>
<summary><strong>📂 Einzelne Geräte-, System- & Herstellerlisten anzeigen</strong></summary>

| Name | Einträge | 🛡️ Privacy | ⚠️ Restrict | 🔄 Updates blockieren |
| --- | :---: | :---: | :---: | :---: |
| 🪟 **Windows** | 246 | **204 Einträge**<br>[Liste](lists/device-control/windows/privacy.txt) | **225 Einträge**<br>[Liste](lists/device-control/windows/restrict.txt) | **21 Einträge**<br>[Liste](lists/device-control/windows/updates.txt) |
| 🤖 **Android** | 13.453 | **13.440 Einträge**<br>[Liste](lists/device-control/android/privacy.txt) | **13.442 Einträge**<br>[Liste](lists/device-control/android/restrict.txt) | **11 Einträge**<br>[Liste](lists/device-control/android/updates.txt) |
| 📱 **Google / Pixel** | 13.453 | **13.440 Einträge**<br>[Liste](lists/device-control/google-pixel/privacy.txt) | **13.442 Einträge**<br>[Liste](lists/device-control/google-pixel/restrict.txt) | **11 Einträge**<br>[Liste](lists/device-control/google-pixel/updates.txt) |
| 📱 **Samsung Mobile** | 113 | **111 Einträge**<br>[Liste](lists/device-control/samsung-mobile/privacy.txt) | **112 Einträge**<br>[Liste](lists/device-control/samsung-mobile/restrict.txt) | **1 Einträge**<br>[Liste](lists/device-control/samsung-mobile/updates.txt) |
| 📱 **Huawei** | 17 | **16 Einträge**<br>[Liste](lists/device-control/huawei/privacy.txt) | **16 Einträge**<br>[Liste](lists/device-control/huawei/restrict.txt) | **1 Einträge**<br>[Liste](lists/device-control/huawei/updates.txt) |
| 📱 **Xiaomi** | 133 | **121 Einträge**<br>[Liste](lists/device-control/xiaomi/privacy.txt) | **126 Einträge**<br>[Liste](lists/device-control/xiaomi/restrict.txt) | **7 Einträge**<br>[Liste](lists/device-control/xiaomi/updates.txt) |
| 📱 **OPPO / Realme** | 40 | **39 Einträge**<br>[Liste](lists/device-control/oppo-realme/privacy.txt) | **39 Einträge**<br>[Liste](lists/device-control/oppo-realme/restrict.txt) | **1 Einträge**<br>[Liste](lists/device-control/oppo-realme/updates.txt) |
| 📱 **Vivo** | 5 | **4 Einträge**<br>[Liste](lists/device-control/vivo/privacy.txt) | **4 Einträge**<br>[Liste](lists/device-control/vivo/restrict.txt) | **1 Einträge**<br>[Liste](lists/device-control/vivo/updates.txt) |
| 🍎 **Apple / iOS / macOS** | 60 | **52 Einträge**<br>[Liste](lists/device-control/apple/privacy.txt) | **53 Einträge**<br>[Liste](lists/device-control/apple/restrict.txt) | **7 Einträge**<br>[Liste](lists/device-control/apple/updates.txt) |
| 🐧 **Linux** | 1 | **1 Einträge**<br>[Liste](lists/device-control/linux/privacy.txt) | **1 Einträge**<br>[Liste](lists/device-control/linux/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/linux/updates.txt) |
| 📺 **Samsung TV** | 115 | **113 Einträge**<br>[Liste](lists/device-control/smart-tv/samsung/privacy.txt) | **114 Einträge**<br>[Liste](lists/device-control/smart-tv/samsung/restrict.txt) | **1 Einträge**<br>[Liste](lists/device-control/smart-tv/samsung/updates.txt) |
| 📺 **LG webOS** | 332 | **332 Einträge**<br>[Liste](lists/device-control/smart-tv/lg/privacy.txt) | **332 Einträge**<br>[Liste](lists/device-control/smart-tv/lg/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/smart-tv/lg/updates.txt) |
| 📺 **Roku** | 5 | **5 Einträge**<br>[Liste](lists/device-control/smart-tv/roku/privacy.txt) | **5 Einträge**<br>[Liste](lists/device-control/smart-tv/roku/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/smart-tv/roku/updates.txt) |
| 🔥 **Fire TV** | 174 | **159 Einträge**<br>[Liste](lists/device-control/smart-tv/fire-tv/privacy.txt) | **170 Einträge**<br>[Liste](lists/device-control/smart-tv/fire-tv/restrict.txt) | **4 Einträge**<br>[Liste](lists/device-control/smart-tv/fire-tv/updates.txt) |
| 📦 **Amazon Geräte / Alexa** | 174 | **159 Einträge**<br>[Liste](lists/device-control/amazon/privacy.txt) | **170 Einträge**<br>[Liste](lists/device-control/amazon/restrict.txt) | **4 Einträge**<br>[Liste](lists/device-control/amazon/updates.txt) |
| 📺 **Android TV / Google TV** | 13.451 | **13.438 Einträge**<br>[Liste](lists/device-control/smart-tv/android-tv/privacy.txt) | **13.440 Einträge**<br>[Liste](lists/device-control/smart-tv/android-tv/restrict.txt) | **11 Einträge**<br>[Liste](lists/device-control/smart-tv/android-tv/updates.txt) |
| 🏠 **IoT / Smart Home** | 446 | **417 Einträge**<br>[Liste](lists/device-control/iot/privacy.txt) | **434 Einträge**<br>[Liste](lists/device-control/iot/restrict.txt) | **12 Einträge**<br>[Liste](lists/device-control/iot/updates.txt) |
| 💾 **NAS** | 17 | **14 Einträge**<br>[Liste](lists/device-control/nas/privacy.txt) | **17 Einträge**<br>[Liste](lists/device-control/nas/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/nas/updates.txt) |
| 🖥️ **Server** | 17 | **14 Einträge**<br>[Liste](lists/device-control/server/privacy.txt) | **17 Einträge**<br>[Liste](lists/device-control/server/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/server/updates.txt) |
| 🌐 **Router / Netzwerkgeräte** | 70 | **57 Einträge**<br>[Liste](lists/device-control/router/privacy.txt) | **67 Einträge**<br>[Liste](lists/device-control/router/restrict.txt) | **3 Einträge**<br>[Liste](lists/device-control/router/updates.txt) |
| 🎮 **Xbox** | 0 | **0 Einträge**<br>[Liste](lists/device-control/gaming/xbox/privacy.txt) | **0 Einträge**<br>[Liste](lists/device-control/gaming/xbox/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/gaming/xbox/updates.txt) |
| 🎮 **PlayStation** | 4 | **4 Einträge**<br>[Liste](lists/device-control/gaming/playstation/privacy.txt) | **4 Einträge**<br>[Liste](lists/device-control/gaming/playstation/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/gaming/playstation/updates.txt) |
| 🎮 **Nintendo** | 2 | **1 Einträge**<br>[Liste](lists/device-control/gaming/nintendo/privacy.txt) | **2 Einträge**<br>[Liste](lists/device-control/gaming/nintendo/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/gaming/nintendo/updates.txt) |
| 🗣️ **Sprachassistenten** | 13.926 | **13.846 Einträge**<br>[Liste](lists/device-control/voice-assistants/privacy.txt) | **13.882 Einträge**<br>[Liste](lists/device-control/voice-assistants/restrict.txt) | **44 Einträge**<br>[Liste](lists/device-control/voice-assistants/updates.txt) |

</details>

---

<br>

---

<br>




## 📚 Weitere Geräte-, Hersteller- & Providerbereiche

<details>
<summary><strong>📡 ISP / Provider anzeigen</strong></summary>

| Provider | Einträge | 🛡️ Privacy | ⚠️ Restrict | 🔄 Updates blockieren |
| --- | :---: | :---: | :---: | :---: |
| **1&1** | 2 | **2 Einträge**<br>[Liste](lists/device-control/providers/1und1/privacy.txt) | **2 Einträge**<br>[Liste](lists/device-control/providers/1und1/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/providers/1und1/updates.txt) |
| **Deutsche Glasfaser** | 6 | **6 Einträge**<br>[Liste](lists/device-control/providers/deutsche-glasfaser/privacy.txt) | **6 Einträge**<br>[Liste](lists/device-control/providers/deutsche-glasfaser/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/providers/deutsche-glasfaser/updates.txt) |
| **O2** | 4 | **3 Einträge**<br>[Liste](lists/device-control/providers/o2/privacy.txt) | **4 Einträge**<br>[Liste](lists/device-control/providers/o2/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/providers/o2/updates.txt) |
| **Telekom** | 6 | **6 Einträge**<br>[Liste](lists/device-control/providers/telekom/privacy.txt) | **6 Einträge**<br>[Liste](lists/device-control/providers/telekom/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/providers/telekom/updates.txt) |
| **Unitymedia** | 4 | **4 Einträge**<br>[Liste](lists/device-control/providers/unitymedia/privacy.txt) | **4 Einträge**<br>[Liste](lists/device-control/providers/unitymedia/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/providers/unitymedia/updates.txt) |
| **Vodafone** | 25 | **22 Einträge**<br>[Liste](lists/device-control/providers/vodafone/privacy.txt) | **22 Einträge**<br>[Liste](lists/device-control/providers/vodafone/restrict.txt) | **3 Einträge**<br>[Liste](lists/device-control/providers/vodafone/updates.txt) |

### Fertige Provider-Profile
| Profil | Einträge | Liste |
| --- | :---: | --- |
| **Light** | 5 | [Liste öffnen](lists/platforms/providers/main/light.txt) |
| **Normal** | 39 | [Liste öffnen](lists/platforms/providers/main/normal.txt) |
| **Pro** | 71 | [Liste öffnen](lists/platforms/providers/main/pro.txt) |
| **Pro++** | 166 | [Liste öffnen](lists/platforms/providers/main/pro-plus.txt) |
| **Ultimate** | 166 | [Liste öffnen](lists/platforms/providers/main/ultimate.txt) |

</details>

<details>
<summary><strong>🏢 Google, Microsoft, Apple & Amazon anzeigen</strong></summary>

| Ökosystem | Einträge | 🛡️ Privacy | ⚠️ Restrict | 🔄 Updates blockieren |
| --- | :---: | :---: | :---: | :---: |
| **Amazon** | 174 | **159 Einträge**<br>[Liste](lists/device-control/ecosystems/amazon/privacy.txt) | **170 Einträge**<br>[Liste](lists/device-control/ecosystems/amazon/restrict.txt) | **4 Einträge**<br>[Liste](lists/device-control/ecosystems/amazon/updates.txt) |
| **Apple** | 60 | **52 Einträge**<br>[Liste](lists/device-control/ecosystems/apple/privacy.txt) | **53 Einträge**<br>[Liste](lists/device-control/ecosystems/apple/restrict.txt) | **7 Einträge**<br>[Liste](lists/device-control/ecosystems/apple/updates.txt) |
| **Google** | 13.451 | **13.438 Einträge**<br>[Liste](lists/device-control/ecosystems/google/privacy.txt) | **13.440 Einträge**<br>[Liste](lists/device-control/ecosystems/google/restrict.txt) | **11 Einträge**<br>[Liste](lists/device-control/ecosystems/google/updates.txt) |
| **Microsoft** | 244 | **202 Einträge**<br>[Liste](lists/device-control/ecosystems/microsoft/privacy.txt) | **223 Einträge**<br>[Liste](lists/device-control/ecosystems/microsoft/restrict.txt) | **21 Einträge**<br>[Liste](lists/device-control/ecosystems/microsoft/updates.txt) |

</details>

<details>
<summary><strong>🏭 Herstellerlisten anzeigen</strong></summary>

| Hersteller | Einträge | 🛡️ Privacy | ⚠️ Restrict | 🔄 Updates blockieren |
| --- | :---: | :---: | :---: | :---: |
| Adobe | 38 | **34 Einträge**<br>[Liste](lists/device-control/manufacturers/adobe/privacy.txt) | **38 Einträge**<br>[Liste](lists/device-control/manufacturers/adobe/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/manufacturers/adobe/updates.txt) |
| Amazon | 174 | **159 Einträge**<br>[Liste](lists/device-control/manufacturers/amazon/privacy.txt) | **170 Einträge**<br>[Liste](lists/device-control/manufacturers/amazon/restrict.txt) | **4 Einträge**<br>[Liste](lists/device-control/manufacturers/amazon/updates.txt) |
| AMD | 2 | **1 Einträge**<br>[Liste](lists/device-control/manufacturers/amd/privacy.txt) | **2 Einträge**<br>[Liste](lists/device-control/manufacturers/amd/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/manufacturers/amd/updates.txt) |
| Apple | 59 | **51 Einträge**<br>[Liste](lists/device-control/manufacturers/apple/privacy.txt) | **52 Einträge**<br>[Liste](lists/device-control/manufacturers/apple/restrict.txt) | **7 Einträge**<br>[Liste](lists/device-control/manufacturers/apple/updates.txt) |
| Autodesk | 7 | **7 Einträge**<br>[Liste](lists/device-control/manufacturers/autodesk/privacy.txt) | **7 Einträge**<br>[Liste](lists/device-control/manufacturers/autodesk/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/manufacturers/autodesk/updates.txt) |
| EA | 39 | **37 Einträge**<br>[Liste](lists/device-control/manufacturers/ea/privacy.txt) | **39 Einträge**<br>[Liste](lists/device-control/manufacturers/ea/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/manufacturers/ea/updates.txt) |
| Epic | 5 | **5 Einträge**<br>[Liste](lists/device-control/manufacturers/epic/privacy.txt) | **5 Einträge**<br>[Liste](lists/device-control/manufacturers/epic/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/manufacturers/epic/updates.txt) |
| Google | 13.451 | **13.438 Einträge**<br>[Liste](lists/device-control/manufacturers/google/privacy.txt) | **13.440 Einträge**<br>[Liste](lists/device-control/manufacturers/google/restrict.txt) | **11 Einträge**<br>[Liste](lists/device-control/manufacturers/google/updates.txt) |
| Huawei | 12 | **12 Einträge**<br>[Liste](lists/device-control/manufacturers/huawei/privacy.txt) | **12 Einträge**<br>[Liste](lists/device-control/manufacturers/huawei/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/manufacturers/huawei/updates.txt) |
| LG | 329 | **329 Einträge**<br>[Liste](lists/device-control/manufacturers/lg/privacy.txt) | **329 Einträge**<br>[Liste](lists/device-control/manufacturers/lg/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/manufacturers/lg/updates.txt) |
| Logitech | 4 | **4 Einträge**<br>[Liste](lists/device-control/manufacturers/logitech/privacy.txt) | **4 Einträge**<br>[Liste](lists/device-control/manufacturers/logitech/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/manufacturers/logitech/updates.txt) |
| Meta | 15 | **12 Einträge**<br>[Liste](lists/device-control/manufacturers/meta/privacy.txt) | **13 Einträge**<br>[Liste](lists/device-control/manufacturers/meta/restrict.txt) | **2 Einträge**<br>[Liste](lists/device-control/manufacturers/meta/updates.txt) |
| Microsoft | 238 | **196 Einträge**<br>[Liste](lists/device-control/manufacturers/microsoft/privacy.txt) | **217 Einträge**<br>[Liste](lists/device-control/manufacturers/microsoft/restrict.txt) | **21 Einträge**<br>[Liste](lists/device-control/manufacturers/microsoft/updates.txt) |
| Nintendo | 4 | **3 Einträge**<br>[Liste](lists/device-control/manufacturers/nintendo/privacy.txt) | **4 Einträge**<br>[Liste](lists/device-control/manufacturers/nintendo/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/manufacturers/nintendo/updates.txt) |
| Nvidia | 8 | **8 Einträge**<br>[Liste](lists/device-control/manufacturers/nvidia/privacy.txt) | **8 Einträge**<br>[Liste](lists/device-control/manufacturers/nvidia/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/manufacturers/nvidia/updates.txt) |
| Philips | 63 | **63 Einträge**<br>[Liste](lists/device-control/manufacturers/philips/privacy.txt) | **63 Einträge**<br>[Liste](lists/device-control/manufacturers/philips/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/manufacturers/philips/updates.txt) |
| Razer | 3 | **3 Einträge**<br>[Liste](lists/device-control/manufacturers/razer/privacy.txt) | **3 Einträge**<br>[Liste](lists/device-control/manufacturers/razer/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/manufacturers/razer/updates.txt) |
| Samsung | 113 | **111 Einträge**<br>[Liste](lists/device-control/manufacturers/samsung/privacy.txt) | **112 Einträge**<br>[Liste](lists/device-control/manufacturers/samsung/restrict.txt) | **1 Einträge**<br>[Liste](lists/device-control/manufacturers/samsung/updates.txt) |
| Sony | 26 | **26 Einträge**<br>[Liste](lists/device-control/manufacturers/sony/privacy.txt) | **26 Einträge**<br>[Liste](lists/device-control/manufacturers/sony/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/manufacturers/sony/updates.txt) |
| Ubisoft | 6 | **6 Einträge**<br>[Liste](lists/device-control/manufacturers/ubisoft/privacy.txt) | **6 Einträge**<br>[Liste](lists/device-control/manufacturers/ubisoft/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/manufacturers/ubisoft/updates.txt) |
| Valve / Steam | 4 | **4 Einträge**<br>[Liste](lists/device-control/manufacturers/valve-steam/privacy.txt) | **4 Einträge**<br>[Liste](lists/device-control/manufacturers/valve-steam/restrict.txt) | **0 Einträge**<br>[Liste](lists/device-control/manufacturers/valve-steam/updates.txt) |
| Xiaomi | 133 | **121 Einträge**<br>[Liste](lists/device-control/manufacturers/xiaomi/privacy.txt) | **126 Einträge**<br>[Liste](lists/device-control/manufacturers/xiaomi/restrict.txt) | **7 Einträge**<br>[Liste](lists/device-control/manufacturers/xiaomi/updates.txt) |

</details>

<details>
<summary><strong>🚗 Automotive / Connected Cars anzeigen</strong></summary>

Fertige Profile:
| Profil | Einträge | Liste |
| --- | :---: | --- |
| **Light** | 42 | [Liste öffnen](lists/platforms/automotive/main/light.txt) |
| **Normal** | 102 | [Liste öffnen](lists/platforms/automotive/main/normal.txt) |
| **Pro** | 177 | [Liste öffnen](lists/platforms/automotive/main/pro.txt) |
| **Pro++** | 617 | [Liste öffnen](lists/platforms/automotive/main/pro-plus.txt) |
| **Ultimate** | 619 | [Liste öffnen](lists/platforms/automotive/main/ultimate.txt) |

Unterstützte Hersteller umfassen u. a. **BMW, Ford, Mercedes, Tesla und Volkswagen**.

</details>

<details>
<summary><strong>💾 NAS & Server anzeigen</strong></summary>

Unterstützt werden u. a. **Docker, HPE/Dell, Kubernetes, QNAP, Red Hat/OpenShift, Synology, TrueNAS und Unraid**.

[Zum Bereich](lists/device-control/nas-server/)

</details>

<details>
<summary><strong>🌐 Router & Netzwerkgeräte anzeigen</strong></summary>

Unterstützt werden u. a. **ASUS, AVM/FRITZ!Box, Cisco, Huawei, MikroTik, Netgear, TP-Link, Ubiquiti und Zyxel**.

[Zum Bereich](lists/device-control/network-devices/)

</details>

<details>
<summary><strong>🏠 IoT & Smart Home anzeigen</strong></summary>

Unterstützt werden u. a. **Amazon Alexa, Huawei, Samsung SmartThings, Sonos, Xiaomi und Shared/Other**.

[Zum Bereich](lists/device-control/iot-smart-home/)

</details>

<details>
<summary><strong>🎙️ Sprachassistenten anzeigen</strong></summary>

| Dienst | Einträge | 🛡️ Privacy | ⚠️ Restrict | 🔄 Updates blockieren |
| --- | :---: | :---: | :---: | :---: |
| Alexa | 174 | **159 Einträge**<br>[Liste](lists/device-control/voice-assistants/alexa/privacy.txt) | **170 Einträge**<br>[Liste](lists/device-control/voice-assistants/alexa/restrict.txt) | **4 Einträge**<br>[Liste](lists/device-control/voice-assistants/alexa/updates.txt) |
| Cortana | 236 | **194 Einträge**<br>[Liste](lists/device-control/voice-assistants/cortana/privacy.txt) | **215 Einträge**<br>[Liste](lists/device-control/voice-assistants/cortana/restrict.txt) | **21 Einträge**<br>[Liste](lists/device-control/voice-assistants/cortana/updates.txt) |
| Google Assistant | 13.452 | **13.438 Einträge**<br>[Liste](lists/device-control/voice-assistants/google-assistant/privacy.txt) | **13.441 Einträge**<br>[Liste](lists/device-control/voice-assistants/google-assistant/restrict.txt) | **11 Einträge**<br>[Liste](lists/device-control/voice-assistants/google-assistant/updates.txt) |
| Siri | 64 | **55 Einträge**<br>[Liste](lists/device-control/voice-assistants/siri/privacy.txt) | **56 Einträge**<br>[Liste](lists/device-control/voice-assistants/siri/restrict.txt) | **8 Einträge**<br>[Liste](lists/device-control/voice-assistants/siri/updates.txt) |

</details>


# 🎮 Gaming Privacy

<!-- CATEGORY-BANNER:06-gaming-privacy.png -->
<p align="center">
  <img src="assets/categories/06-gaming-privacy.png" alt="Gaming Privacy" width="100%">
</p>
<!-- /CATEGORY-BANNER -->


## Fertige Gaming-Profile

| Profil | Einträge | Schutz | Geeignet für | Liste |
| --- | :---: | --- | --- | --- |
| 🟩 **Light** | 2 | Nur sehr sichere Gaming-Telemetrie | Maximale Launcher-/Game-Kompatibilität | [Liste öffnen](lists/apps/gaming/main/light.txt) |
| 🟦 **Normal** | 30 | Launcher-Analytics + Crash-/Metrics-Endpunkte | Normale Gaming-PCs | [Liste öffnen](lists/apps/gaming/main/normal.txt) |
| 🟨 **Pro ⭐** | 42 | Breiter Gaming-Privacy-Schutz | **Empfohlen** | [Liste öffnen](lists/apps/gaming/main/pro.txt) |
| 🟧 **Pro++** | 46 | Aggressivere Launcher-/Game-Telemetrie | Erfahrene Nutzer | [Liste öffnen](lists/apps/gaming/main/pro-plus.txt) |
| 🟥 **Ultimate** | 50 | Maximale Gaming-Telemetrie-Abdeckung | Test-/Expertenumgebungen | [Liste öffnen](lists/apps/gaming/main/ultimate.txt) |

<details>
<summary><strong>📂 Einzelne Gaming-Listen anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste anzeigen |
| --- | :---: | --- | --- |
| 🎮 **Gaming Telemetry** | 28 | Empfohlene Game-, Launcher-, Analytics- und Crash-Reporting-Endpunkte mit geringem Risiko. | [Öffnen](lists/gaming/gaming-telemetry.txt) |
| ⚠️ **Gaming Telemetry – Aggressive** | 50 | Zusätzliche Endpunkte mit höherem Risiko für Launcher, Login oder Gameplay. | [Öffnen](lists/gaming/gaming-telemetry-aggressive.txt) |
| 🧩 **Gaming RegEx Rules** | 27 | Dynamische Pi-hole-RegEx-Regeln für zusätzliche Gaming-Telemetrie. | [Öffnen](lists/gaming/gaming-telemetry-regex.txt) |
| 🟦 **Steam Tracking** | 2 | Steam-/Valve-Tracking und Telemetrie reduzieren. | [Öffnen](lists/gaming/platforms/steam-privacy.txt) |
| 🟪 **Battle.net Tracking** | 3 | Blizzard-/Battle.net-Analytics und Telemetrie reduzieren. | [Öffnen](lists/gaming/platforms/battlenet-privacy.txt) |
| 🟨 **Rockstar Tracking** | 2 | Rockstar-Launcher-/Game-Telemetrie reduzieren. | [Öffnen](lists/gaming/platforms/rockstar-privacy.txt) |
| ⚫ **Epic Tracking** | 5 | Epic-Games-/Launcher-Telemetrie reduzieren. | [Öffnen](lists/gaming/platforms/epic-privacy.txt) |
| 🔴 **Riot Tracking** | 3 | Riot-Launcher-/Game-Telemetrie reduzieren. | [Öffnen](lists/gaming/platforms/riot-privacy.txt) |

</details>

---

<br>

---

<br>



---

<br>

# ☁️ Cloud, Server & Development

Privacy- und Block-All-Listen für **Cloud-Plattformen, Hosting, CI/CD und Entwicklerwerkzeuge**.

## Fertige Cloud-/Development-Profile

| Profil | Einträge | Schutz | Risiko | Liste |
| --- | :---: | --- | :---: | --- |
| 🟩 **Light** | 65 | konservativer Privacy-Schutz | Minimal | [Liste öffnen](lists/infrastructure/cloud-development/main/light.txt) |
| 🟦 **Normal** | 165 | zusätzliche Tracking-/Analytics-Endpunkte | Niedrig | [Liste öffnen](lists/infrastructure/cloud-development/main/normal.txt) |
| 🟨 **Pro ⭐** | 301 | umfangreicher Cloud-/Development-Privacy-Schutz | Niedrig–Mittel | [Liste öffnen](lists/infrastructure/cloud-development/main/pro.txt) |
| 🟧 **Pro++** | 1.486 | aggressive Cloud-/Developer-Telemetrie | Mittel | [Liste öffnen](lists/infrastructure/cloud-development/main/pro-plus.txt) |
| 🟥 **Ultimate** | 1.491 | maximaler Datenbestand dieses Bereichs | Hoch | [Liste öffnen](lists/infrastructure/cloud-development/main/ultimate.txt) |

<details>
<summary><strong>📂 Einzelne Cloud- & Development-Dienste anzeigen</strong></summary>

| Dienst | Einträge | 🛡️ Privacy | 🚫 Block All |
| --- | :---: | :---: | :---: |
| AWS | 440 | **125 Einträge**<br>[Liste](lists/service-blocking/cloud-development/aws/privacy.txt) | **440 Einträge**<br>[Liste](lists/service-blocking/cloud-development/aws/block-all.txt) |
| Azure | 186 | **16 Einträge**<br>[Liste](lists/service-blocking/cloud-development/azure/privacy.txt) | **186 Einträge**<br>[Liste](lists/service-blocking/cloud-development/azure/block-all.txt) |
| CI/CD | 2 | **0 Einträge**<br>[Liste](lists/service-blocking/cloud-development/cicd/privacy.txt) | **2 Einträge**<br>[Liste](lists/service-blocking/cloud-development/cicd/block-all.txt) |
| Cloud Storage | 12 | **4 Einträge**<br>[Liste](lists/service-blocking/cloud-development/cloud-storage/privacy.txt) | **12 Einträge**<br>[Liste](lists/service-blocking/cloud-development/cloud-storage/block-all.txt) |
| Cloudflare | 33 | **8 Einträge**<br>[Liste](lists/service-blocking/cloud-development/cloudflare/privacy.txt) | **33 Einträge**<br>[Liste](lists/service-blocking/cloud-development/cloudflare/block-all.txt) |
| GitHub | 18 | **3 Einträge**<br>[Liste](lists/service-blocking/cloud-development/github/privacy.txt) | **18 Einträge**<br>[Liste](lists/service-blocking/cloud-development/github/block-all.txt) |
| GitLab | 3 | **1 Einträge**<br>[Liste](lists/service-blocking/cloud-development/gitlab/privacy.txt) | **3 Einträge**<br>[Liste](lists/service-blocking/cloud-development/gitlab/block-all.txt) |
| Google Cloud | 49 | **2 Einträge**<br>[Liste](lists/service-blocking/cloud-development/google-cloud/privacy.txt) | **49 Einträge**<br>[Liste](lists/service-blocking/cloud-development/google-cloud/block-all.txt) |
| JetBrains | 1 | **1 Einträge**<br>[Liste](lists/service-blocking/cloud-development/jetbrains/privacy.txt) | **1 Einträge**<br>[Liste](lists/service-blocking/cloud-development/jetbrains/block-all.txt) |
| Oracle Cloud | 8 | **3 Einträge**<br>[Liste](lists/service-blocking/cloud-development/oracle-cloud/privacy.txt) | **8 Einträge**<br>[Liste](lists/service-blocking/cloud-development/oracle-cloud/block-all.txt) |
| Visual Studio | 2 | **1 Einträge**<br>[Liste](lists/service-blocking/cloud-development/visual-studio/privacy.txt) | **2 Einträge**<br>[Liste](lists/service-blocking/cloud-development/visual-studio/block-all.txt) |
| VS Code | 2 | **1 Einträge**<br>[Liste](lists/service-blocking/cloud-development/vs-code/privacy.txt) | **2 Einträge**<br>[Liste](lists/service-blocking/cloud-development/vs-code/block-all.txt) |

</details>


# 🌐 Netzwerk & Spezialschutz

<!-- CATEGORY-BANNER:07-netzwerk-spezialschutz.png -->
<p align="center">
  <img src="assets/categories/07-netzwerk-spezialschutz.png" alt="Netzwerk & Spezialschutz" width="100%">
</p>
<!-- /CATEGORY-BANNER -->


## Fertige Netzwerkprofile

| Profil | Einträge | Schutz | Geeignet für | Liste |
| --- | :---: | --- | --- | --- |
| 🟩 **Light** | 31 | Sichere DNS-/Bypass-Basis | Heimnetze | [Liste öffnen](lists/network/main/light.txt) |
| 🟦 **Normal** | 49 | Light + bekannte DoH-/Bypass-Endpunkte | Kontrollierte Heimnetze | [Liste öffnen](lists/network/main/normal.txt) |
| 🟨 **Pro ⭐** | 66 | DoH + VPN/Proxy + Rebind-/Redirect-Schutz | **Homelabs / Admins** | [Liste öffnen](lists/network/main/pro.txt) |
| 🟧 **Pro++** | 311 | Aggressivere Umgehungs- und Spezialfilter | Schulen / strengere Netze | [Liste öffnen](lists/network/main/pro-plus.txt) |
| 🟥 **Ultimate** | 947 | Maximale Netzwerk-Kontrolle | Experten / isolierte Netze | [Liste öffnen](lists/network/main/ultimate.txt) |

<details>
<summary><strong>📂 Einzelne Netzwerk-&-Speziallisten anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste anzeigen |
| --- | :---: | --- | --- |
| 📤 **DoH / VPN / Tor / Proxy Bypass** | 314 | Blockiert bekannte verschlüsselte DNS-, VPN-, Tor- und Proxy-Endpunkte zur Filterumgehung. | [Öffnen](lists/network/doh-vpn-tor-proxy-bypass.txt) |
| 🌐 **DoH Only** | 3 | Blockiert bekannte DNS-over-HTTPS-Endpunkte. | [Öffnen](lists/network/doh-only.txt) |
| 🌐 **DoH IPv4** | 3 | IPv4-Liste bekannter DoH-Resolver. | [Öffnen](lists/network/doh-ipv4.txt) |
| 🔎 **SafeSearch Unsupported** | 205 | Blockiert Suchmaschinen, die keinen verlässlichen SafeSearch-Modus unterstützen. | [Öffnen](lists/network/safesearch-unsupported.txt) |
| 📲 **URL Shortener** | 255 | Blockiert bekannte URL-Shortener und Redirect-Dienste. | [Öffnen](lists/network/url-shortener.txt) |
| 🛡️ **DNS Rebind Protection** | — | Dokumentation/Regeln zum Schutz gegen DNS-Rebinding. | [Öffnen](docs/DNS_REBIND_PROTECTION.md) |
| 🤖 **AI Crawler** | 10 | Blockiert ausgewählte KI-Crawler und Scraper. | [Öffnen](lists/network/ai-crawlers.txt) |
| 🕷️ **Scraper & Bots** | 66 | Blockiert ausgewählte aggressive Bots und Scraper. | [Öffnen](lists/network/scrapers-bots.txt) |
| 🔏 **Dynamic DNS** | 74 | Blockiert bekannte Dynamic-DNS-Dienste. | [Öffnen](lists/network/dynamic-dns.txt) |
| 🔮 **Suspicious TLDs** | 6.490 | Aggressive Regeln für ausgewählte missbrauchte Top-Level-Domains. | [Öffnen](lists/network/suspicious-tlds.txt) |
| 🔁 **Tracking Redirectors** | 306 | Blockiert bekannte Tracking- und Redirect-Infrastruktur. | [Öffnen](lists/network/tracking-redirectors.txt) |

</details>

<details>
<summary><strong>🧰 Speziallisten anzeigen</strong></summary>

| Spezialliste | Einträge | Zweck | Liste |
| --- | :---: | --- | --- |
| **Fake / Scam / Trap Sites** | 265.318 | Scam + Fake Shops + Fake Software gebündelt | [Öffnen](lists/special/fake-scam-trap-sites.txt) |
| **Threat Intelligence Mini** | 594.410 | kompakte Threat-Intelligence-Stufe | [Öffnen](lists/security/main/pro.txt) |
| **Threat Intelligence Medium** | 844.669 | mittlere Threat-Intelligence-Stufe | [Öffnen](lists/security/main/pro-plus.txt) |
| **Threat Intelligence Full** | 3.408.596 | kompletter Security-Ultimate-Datenbestand | [Öffnen](lists/security/main/ultimate.txt) |
| **Dynamic DNS** | 74 | bekannte DynDNS-Provider; aggressiv | [Öffnen](lists/network/full/dynamic-dns.txt) |
| **Badware Hoster** | 24 | häufig missbrauchte Hosting-/Site-Builder-Infrastruktur | [Öffnen](lists/security/full/badware-hosters.txt) |
| **Most Abused TLDs** | — | riskante TLDs/Suffixe | [Spezial-Doku](docs/SPECIAL_LISTS.md) |
| **DNS Rebind Protection** | — | Resolver-/dnsmasq-Policy | [Öffnen](policies/) |
| **DoH/VPN/Tor/Proxy Bypass** | 314 | kombinierte Umgehungsliste | [Öffnen](lists/network/full/dns-bypass.txt) |
| **Encrypted DNS Only** | — | DoH + DoT + Private DNS | [Öffnen](lists/network/) |
| **SafeSearch not supported** | 205 | Suchmaschinen ohne SafeSearch-Support | [Öffnen](lists/network/full/safesearch-not-supported.txt) |
| **URL Shortener** | 255 | bekannte Kurzlink-Dienste | [Öffnen](lists/network/full/url-shorteners.txt) |
| **Native Tracker** | 587 | integrierte Tracker von OS, Apps und Geräten | [Öffnen](lists/privacy/full/native-tracking.txt) |

</details>

<details>
<summary><strong>🌍 Regionale Listen anzeigen</strong></summary>

> Regionale Listen werden **nicht** einfach nach TLD gebaut, sondern aus dem vorhandenen Datenbestand kuratiert.

| Region | Einträge | Liste |
| --- | :---: | --- |
| 🇨🇳 **China** | 5.896 | [Öffnen](lists/regional/cn.txt) |
| 🇩🇪 **Deutschland** | 3.304 | [Öffnen](lists/regional/de.txt) |
| 🇪🇸 **Spanien** | 1.698 | [Öffnen](lists/regional/es.txt) |
| 🇪🇺 **EU** | 31.996 | [Öffnen](lists/regional/eu.txt) |
| 🇫🇷 **Frankreich** | 2.123 | [Öffnen](lists/regional/fr.txt) |
| 🇮🇹 **Italien** | 2.307 | [Öffnen](lists/regional/it.txt) |
| 🇯🇵 **Japan** | 625 | [Öffnen](lists/regional/jp.txt) |
| 🇰🇷 **Südkorea** | 479 | [Öffnen](lists/regional/kr.txt) |
| 🇷🇺 **Russland** | 15.374 | [Öffnen](lists/regional/ru.txt) |
| 🇬🇧 **UK** | 7.416 | [Öffnen](lists/regional/uk.txt) |
| 🇺🇸 **USA** | 6.302 | [Öffnen](lists/regional/us.txt) |

</details>


---

---

<br>


# 🚫 Komplettblockierungen

<!-- CATEGORY-BANNER:08-komplettblockierungen.png -->
<p align="center">
  <img src="assets/categories/08-komplettblockierungen.png" alt="Komplettblockierungen" width="100%">
</p>
<!-- /CATEGORY-BANNER -->


**Hier wird nicht optimiert oder Tracking reduziert – hier soll der gewählte Dienst absichtlich nicht mehr funktionieren.**

## Fertige Block-Pakete

| Paket | Einträge | Funktion | Liste |
| --- | :---: | --- | --- |
| 💬 **Social Media** | 175 | Blockiert unterstützte Social-Media-Plattformen vollständig. | [Liste öffnen](lists/block-all/packages/social-media.txt) |
| 🎵 **Music** | 134 | Blockiert unterstützte Musik-/Audio-Dienste vollständig. | [Liste öffnen](lists/block-all/packages/music.txt) |
| 📺 **Streaming** | 56 | Blockiert unterstützte Video-/Streamingdienste vollständig. | [Liste öffnen](lists/block-all/packages/streaming.txt) |
| 🎮 **Gaming** | 37 | Blockiert unterstützte Gaming-Plattformen vollständig. | [Liste öffnen](lists/block-all/packages/gaming.txt) |
| 💬 **Messaging** | 17 | Blockiert unterstützte Messenger und Chat-Dienste vollständig. | [Liste öffnen](lists/block-all/packages/messaging.txt) |
| 🤖 **AI** | 57 | Blockiert unterstützte KI-Dienste vollständig. | [Liste öffnen](lists/block-all/packages/ai.txt) |
| ☁️ **Cloud** | 754 | Blockiert ausgewählte Cloud-/Hosting-Dienste vollständig. | [Liste öffnen](lists/block-all/packages/cloud.txt) |

<details>
<summary><strong>📂 Einzelne Block-All-Listen anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste anzeigen |
| --- | :---: | --- | --- |
| 🎵 **Spotify** | 132 | Blockiert Spotify App, Webplayer, Login, APIs und Streaming-Endpunkte. | [Öffnen](lists/block-all/music/spotify.txt) |
| 🎵 **Deezer** | 2 | Blockiert Deezer vollständig. | [Öffnen](lists/block-all/music/deezer.txt) |
| 📺 **Netflix** | 25 | Blockiert Netflix App, Web und Streaming-Infrastruktur. | [Öffnen](lists/block-all/streaming/netflix.txt) |
| 📺 **Disney+** | 9 | Blockiert Disney+ vollständig. | [Öffnen](lists/block-all/streaming/disney-plus.txt) |
| 📺 **Prime Video** | 4 | Blockiert Prime Video vollständig. | [Öffnen](lists/block-all/streaming/prime-video.txt) |
| 🟣 **Twitch** | 18 | Blockiert Twitch Web, App und Streaming-Infrastruktur. | [Öffnen](lists/block-all/streaming/twitch.txt) |
| 📱 **TikTok** | 58 | Blockiert TikTok vollständig. | [Öffnen](lists/block-all/social/tiktok.txt) |
| 📸 **Instagram** | 10 | Blockiert Instagram vollständig. | [Öffnen](lists/block-all/social/instagram.txt) |
| 🔵 **Facebook** | 47 | Blockiert Facebook vollständig. | [Öffnen](lists/block-all/social/facebook.txt) |
| ✖️ **X / Twitter** | 25 | Blockiert X / Twitter vollständig. | [Öffnen](lists/block-all/social/x-twitter.txt) |
| 👻 **Snapchat** | 15 | Blockiert Snapchat vollständig. | [Öffnen](lists/block-all/social/snapchat.txt) |
| 🟠 **Reddit** | 26 | Blockiert Reddit vollständig. | [Öffnen](lists/block-all/social/reddit.txt) |
| 🎮 **Steam** | 7 | Blockiert Steam Store, Client und Netzwerkdienste. | [Öffnen](lists/block-all/gaming/steam.txt) |
| 🎮 **Epic Games** | 11 | Blockiert Epic Games Store und Launcher. | [Öffnen](lists/block-all/gaming/epic-games.txt) |
| 🎮 **Battle.net** | 8 | Blockiert Battle.net und Blizzard-Onlinedienste. | [Öffnen](lists/block-all/gaming/battlenet.txt) |
| 🎮 **Riot Games** | 6 | Blockiert Riot-Launcher und unterstützte Riot-Dienste. | [Öffnen](lists/block-all/gaming/riot-games.txt) |
| 🎮 **Rockstar** | 5 | Blockiert Rockstar Launcher und Online-Dienste. | [Öffnen](lists/block-all/gaming/rockstar.txt) |
| 💬 **Discord** | 12 | Blockiert Discord App, Web, API und Medien-Endpunkte. | [Öffnen](lists/block-all/messaging/discord.txt) |
| 💬 **Telegram** | 5 | Blockiert Telegram-Dienste. | [Öffnen](lists/block-all/messaging/telegram.txt) |

</details>

---




---

## 🧰 Software & Tools blockieren

Hier werden **Programme, Clients, Plattformen oder komplette Software-Kategorien vollständig gesperrt**.

> Diese Listen sind keine Privacy-Listen. Wenn eine Software hier blockiert wird, soll sie **bewusst nicht mehr online funktionieren**.

### Fertige Software-Blockpakete

| Paket | Einträge | Funktion | Liste |
| --- | :---: | --- | --- |
| ☁️ **Cloud Clients** | 21 | Blockiert typische Cloud-Sync-Clients und deren Online-Dienste. | [Liste öffnen](lists/block-all/software/cloud-clients.txt) |
| 💻 **Development Tools** | 35 | Blockiert unterstützte Entwicklungs- und Entwicklerplattformen. | [Liste öffnen](lists/block-all/software/development-tools.txt) |
| 🎮 **Game Launcher** | 37 | Blockiert unterstützte Spiele-Launcher vollständig. | [Liste öffnen](lists/block-all/software/game-launchers.txt) |
| 🤖 **AI Tools** | 57 | Blockiert unterstützte KI-Clients und AI-Dienste. | [Liste öffnen](lists/block-all/software/ai-tools.txt) |
| 📡 **Remote Access** | 5 | Blockiert Remote-Desktop-/Fernwartungssoftware und deren Infrastruktur. | [Liste öffnen](lists/block-all/software/remote-access.txt) |
| 💬 **Communication Tools** | 6 | Blockiert unterstützte Messenger-, Chat- und Collaboration-Software. | [Liste öffnen](lists/block-all/software/communication-tools.txt) |
| 📦 **Software Stores** | 7 | Blockiert unterstützte App-/Software-Stores und Paketquellen. | [Liste öffnen](lists/block-all/software/software-stores.txt) |
| 🔄 **Auto Updater** | 61 | Blockiert Update-Infrastruktur ausgewählter Software-Produkte. | [Liste öffnen](lists/block-all/software/auto-updaters.txt) |

<details>
<summary><strong>📂 Einzelne Software- & Tool-Blocklisten anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste anzeigen |
| --- | :---: | --- | --- |
| **OneDrive** | 15 | Blockiert OneDrive-Sync und zugehörige Onlinedienste. | [Öffnen](lists/block-all/software/onedrive.txt) |
| **Dropbox** | 15 | Blockiert Dropbox-Client und Cloudzugriff. | [Öffnen](lists/block-all/software/dropbox.txt) |
| **Google Drive** | 15 | Blockiert Google-Drive-Client und Cloudzugriff. | [Öffnen](lists/block-all/software/google-drive.txt) |
| **GitHub Desktop** | 21 | Blockiert GitHub-Desktop-Kommunikation. | [Öffnen](lists/block-all/software/github-desktop.txt) |
| **GitLab** | 5 | Blockiert GitLab-bezogene Client-/Service-Kommunikation. | [Öffnen](lists/block-all/software/gitlab.txt) |
| **VS Code Online Services** | 5 | Blockiert VS-Code-Onlinedienste, Marketplace und Telemetrie-Endpunkte vollständig. | [Öffnen](lists/block-all/software/vscode.txt) |
| **JetBrains** | 4 | Blockiert JetBrains-Onlinedienste und zugehörige Softwarekommunikation. | [Öffnen](lists/block-all/software/jetbrains.txt) |
| **TeamViewer** | 2 | Blockiert TeamViewer vollständig. | [Öffnen](lists/block-all/software/teamviewer.txt) |
| **AnyDesk** | 1 | Blockiert AnyDesk vollständig. | [Öffnen](lists/block-all/software/anydesk.txt) |
| **RustDesk** | 2 | Blockiert öffentliche RustDesk-Infrastruktur; selbst gehostete Server können separat erlaubt werden. | [Öffnen](lists/block-all/software/rustdesk.txt) |
| **Microsoft Teams** | 3 | Blockiert Teams vollständig. | [Öffnen](lists/block-all/software/microsoft-teams.txt) |
| **Slack** | 3 | Blockiert Slack vollständig. | [Öffnen](lists/block-all/software/slack.txt) |
| **Microsoft Store** | 3 | Blockiert den Microsoft Store und Store-Infrastruktur. | [Öffnen](lists/block-all/software/microsoft-store.txt) |
| **Snap Store** | 2 | Blockiert Snap-/Snapcraft-Infrastruktur. | [Öffnen](lists/block-all/software/snap-store.txt) |
| **Flatpak / Flathub** | 2 | Blockiert Flathub-/Flatpak-Onlinedienste. | [Öffnen](lists/block-all/software/flathub.txt) |

</details>

---

## 🖥️ Systemblockierungen

Systemblockierungen sind für Geräte gedacht, die **möglichst lokal betrieben werden sollen**.

Es gibt bewusst zwei Stufen:

| Modus | Wirkung |
|---|---|
| 🟠 **Local Mode** | Hersteller-, Cloud-, Telemetrie- und optionale Online-Dienste werden blockiert. **Updates bleiben erlaubt.** |
| 🔴 **Full Isolation** | Externe Kommunikation wird so weit wie über DNS möglich blockiert. **Updates werden ebenfalls blockiert.** |

> ⚠️ **Wichtig:** DNS-Blocklisten allein garantieren keine vollständige Netzisolation. Geräte können feste IP-Adressen, eigenes DoH/DoT, VPN-Tunnel oder andere Protokolle verwenden. Für echte Isolation zusätzlich Firewall-/VLAN-Regeln einsetzen.

### System-Blocklisten

| System / Gerät | Einträge | 🟠 Local Mode – Updates erlaubt | 🔴 Full Isolation – inkl. Updates |
| --- | :---: | :---: | :---: |
| 🪟 **Windows** | 793 | **225 Einträge**<br>[Liste](lists/system-blocking/windows/local-mode.txt) | **793 Einträge**<br>[Liste](lists/system-blocking/windows/full-isolation.txt) |
| 🍎 **macOS** | 340 | **53 Einträge**<br>[Liste](lists/system-blocking/macos/local-mode.txt) | **340 Einträge**<br>[Liste](lists/system-blocking/macos/full-isolation.txt) |
| 🤖 **Android** | 14.488 | **13.442 Einträge**<br>[Liste](lists/system-blocking/android/local-mode.txt) | **14.488 Einträge**<br>[Liste](lists/system-blocking/android/full-isolation.txt) |
| 🍏 **iOS / iPadOS** | 340 | **53 Einträge**<br>[Liste](lists/system-blocking/ios/local-mode.txt) | **340 Einträge**<br>[Liste](lists/system-blocking/ios/full-isolation.txt) |
| 🐧 **Linux** | 3 | **1 Einträge**<br>[Liste](lists/system-blocking/linux/local-mode.txt) | **3 Einträge**<br>[Liste](lists/system-blocking/linux/full-isolation.txt) |
| 📺 **Samsung TV** | 347 | **114 Einträge**<br>[Liste](lists/system-blocking/samsung-tv/local-mode.txt) | **347 Einträge**<br>[Liste](lists/system-blocking/samsung-tv/full-isolation.txt) |
| 📺 **LG webOS** | 620 | **332 Einträge**<br>[Liste](lists/system-blocking/lg-webos/local-mode.txt) | **620 Einträge**<br>[Liste](lists/system-blocking/lg-webos/full-isolation.txt) |
| 🔥 **Fire TV** | 776 | **170 Einträge**<br>[Liste](lists/system-blocking/fire-tv/local-mode.txt) | **776 Einträge**<br>[Liste](lists/system-blocking/fire-tv/full-isolation.txt) |
| 📺 **Android TV / Google TV** | 14.479 | **13.440 Einträge**<br>[Liste](lists/system-blocking/android-tv/local-mode.txt) | **14.479 Einträge**<br>[Liste](lists/system-blocking/android-tv/full-isolation.txt) |
| 💾 **Synology** | 3 | **2 Einträge**<br>[Liste](lists/system-blocking/synology/local-mode.txt) | **3 Einträge**<br>[Liste](lists/system-blocking/synology/full-isolation.txt) |
| 💾 **QNAP** | 6 | **6 Einträge**<br>[Liste](lists/system-blocking/qnap/local-mode.txt) | **6 Einträge**<br>[Liste](lists/system-blocking/qnap/full-isolation.txt) |
| 💾 **TrueNAS** | 3 | **1 Einträge**<br>[Liste](lists/system-blocking/truenas/local-mode.txt) | **3 Einträge**<br>[Liste](lists/system-blocking/truenas/full-isolation.txt) |
| 💾 **Unraid** | 2 | **0 Einträge**<br>[Liste](lists/system-blocking/unraid/local-mode.txt) | **2 Einträge**<br>[Liste](lists/system-blocking/unraid/full-isolation.txt) |
| 🌐 **Router / Netzwerkgeräte** | 441 | **67 Einträge**<br>[Liste](lists/system-blocking/network-devices/local-mode.txt) | **441 Einträge**<br>[Liste](lists/system-blocking/network-devices/full-isolation.txt) |
| 🏠 **IoT / Smart Home** | 1.757 | **434 Einträge**<br>[Liste](lists/system-blocking/iot/local-mode.txt) | **1.757 Einträge**<br>[Liste](lists/system-blocking/iot/full-isolation.txt) |
| 🗣️ **Sprachassistenten** | 16.383 | **13.882 Einträge**<br>[Liste](lists/system-blocking/voice-assistants/local-mode.txt) | **16.383 Einträge**<br>[Liste](lists/system-blocking/voice-assistants/full-isolation.txt) |
| 🎮 **Konsolen** | 31 | **6 Einträge**<br>[Liste](lists/system-blocking/consoles/local-mode.txt) | **31 Einträge**<br>[Liste](lists/system-blocking/consoles/full-isolation.txt) |

### System-Gesamtlisten

| Gesamtgruppe | Einträge | 🟠 Local Mode | 🔴 Full Isolation |
| --- | :---: | :---: | :---: |
| 💻 **Computer / Laptop** | 1.136 | **279 Einträge**<br>[Liste](lists/system-blocking/groups/computer/local-mode.txt) | **1.136 Einträge**<br>[Liste](lists/system-blocking/groups/computer/full-isolation.txt) |
| 📱 **Handy / Tablet** | 14.828 | **13.495 Einträge**<br>[Liste](lists/system-blocking/groups/mobile/local-mode.txt) | **14.828 Einträge**<br>[Liste](lists/system-blocking/groups/mobile/full-isolation.txt) |
| 📺 **TV / Streaming-Geräte** | 16.221 | **14.056 Einträge**<br>[Liste](lists/system-blocking/groups/tv-streaming/local-mode.txt) | **16.221 Einträge**<br>[Liste](lists/system-blocking/groups/tv-streaming/full-isolation.txt) |
| 💾 **NAS / Server** | 14 | **9 Einträge**<br>[Liste](lists/system-blocking/groups/nas-server/local-mode.txt) | **14 Einträge**<br>[Liste](lists/system-blocking/groups/nas-server/full-isolation.txt) |
| 🏠 **Smart Home / IoT** | 17.294 | **14.135 Einträge**<br>[Liste](lists/system-blocking/groups/iot/local-mode.txt) | **17.294 Einträge**<br>[Liste](lists/system-blocking/groups/iot/full-isolation.txt) |
| 🌐 **Netzwerkgeräte** | 441 | **67 Einträge**<br>[Liste](lists/system-blocking/groups/network/local-mode.txt) | **441 Einträge**<br>[Liste](lists/system-blocking/groups/network/full-isolation.txt) |
| 🧩 **All Systems** | 18.242 | **14.516 Einträge**<br>**[Liste](lists/system-blocking/all-in/local-mode.txt)** | **18.242 Einträge**<br>**[Liste](lists/system-blocking/all-in/full-isolation.txt)** |

<details>
<summary><strong>ℹ️ Wann nutze ich Privacy, Restrict, Local Mode oder Full Isolation?</strong></summary>

| Stufe | Ziel |
|---|---|
| 🛡️ **Privacy** | Tracking/Telemetrie reduzieren, normale Online-Funktion behalten |
| ⚠️ **Restrict** | zusätzliche Hersteller-/Cloud-Funktionen einschränken |
| 🟠 **Local Mode** | System weitgehend lokal betreiben, **Updates bleiben möglich** |
| 🔴 **Full Isolation** | externe Kommunikation maximal reduzieren, **inklusive Updates** |

</details>


# 🧠 Welche Liste brauche ich?

| Ziel | Empfehlung |
|---|---|
| Werbung, Tracker und Telemetrie blockieren | 🟨 **Gesamtprofil Pro** |
| Maximale Kompatibilität | 🟩 **Gesamtprofil Light** |
| Aggressiver allgemeiner Privacy-Schutz | 🟧 **Gesamtprofil Pro++** |
| Kinder schützen | 👨‍👩‍👧 **Family Pro** |
| Nur freigegebene Kinderseiten | 🧒 **Kids Allow Only – Learning** |
| Nur Ads & Tracking | 📢 **Ads & Tracking Pro** |
| Mehr Telemetrie-/Security-Schutz | 🛡️ **Privacy & Security Pro** |
| Smart-TV-Tracking reduzieren | 💻 **Gerät → Privacy** |
| Hersteller-Cloud einschränken | ⚠️ **Gerät → Restrict** |
| Gerät vom Hersteller trennen | 🔒 **Gerät → Isolate** |
| Firmware-/Systemupdates blockieren | 🔄 **Gerät → Updates** |
| Gaming-Telemetrie reduzieren | 🎮 **Gaming Pro** |
| Einzelnen Dienst komplett sperren | 🚫 **Block-All-Einzelliste** |
| Ganze Dienstgruppe sperren | 🚫 **Block-Paket** |
| Software oder Tools komplett sperren | 🧰 **Software & Tools blockieren** |
| System lokal halten, Updates aber erlauben | 🟠 **Systemblockierung → Local Mode** |
| System maximal isolieren inkl. Updates | 🔴 **Systemblockierung → Full Isolation** |
| DoH/VPN/Proxy/Tor einschränken | 🌐 **Netzwerk Pro** |
| Software-/Hardware-Telemetrie reduzieren | 🧩 **Software & Hardware Telemetrie Pro** |
| KI-Crawler/Scraper blockieren | 🤖 **KI, Bots & Crawler Pro** |
| ISP-/Provider-Tracking reduzieren | 📡 **Geräte → ISP / Provider → Privacy** |
| Herstellerübergreifend filtern | 🏭 **Herstellerlisten → Privacy/Restrict** |
| Cloud-/Developer-Telemetrie reduzieren | ☁️ **Cloud, Server & Development Pro** |
| Regionale Filter verwenden | 🌍 **Regionale Listen** |

---

<details>
<summary><strong>📊 Inclusion Matrix – Was steckt bereits in den Gesamtprofilen?</strong></summary>

| Bereich | Light | Normal | Pro | Pro++ | Ultimate |
|---|:---:|:---:|:---:|:---:|:---:|
| Werbung | ✅ | ✅ | ✅ | ✅ | ✅ |
| General Tracking | 🟡 | ✅ | ✅ | ✅ | ✅ |
| Analytics | ❌ | ✅ | ✅ | ✅ | ✅ |
| Social Tracking | ❌ | 🟡 | ✅ | ✅ | ✅ |
| Mobile / App Tracking | ❌ | ❌ | ✅ | ✅ | ✅ |
| Allgemeine Telemetrie | ❌ | 🟡 | ✅ | ✅ | ✅ |
| Geräte-/Native-Tracker | ❌ | ❌ | 🟡 | ✅ | ✅ |
| Fingerprinting | ❌ | ❌ | 🟡 | ✅ | ✅ |
| Malware / Phishing | ❌ | 🟡 | ✅ | ✅ | ✅ |
| Scam / Fake Shops | ❌ | ❌ | ✅ | ✅ | ✅ |
| Family / Adult | ❌ | ❌ | ❌ | ❌ | ❌ |
| Kids Allow Only | ❌ | ❌ | ❌ | ❌ | ❌ |
| Block All | ❌ | ❌ | ❌ | ❌ | ❌ |
| Geräte-Isolation | ❌ | ❌ | ❌ | ❌ | ❌ |
| Updates blockieren | ❌ | ❌ | ❌ | ❌ | ❌ |
| VPN / Tor / Proxy blockieren | ❌ | ❌ | ❌ | ❌ | ❌ |

**✅ enthalten · 🟡 teilweise enthalten · ❌ bewusst separat**

</details>

---

<details>
<summary><strong>🛠️ Technische Regeln & Qualitätsprinzipien</strong></summary>

- Privacy-/Ads-/Tracking-Listen sollen Kernfunktionen nicht absichtlich zerstören.
- Login-, Account-, Streaming-, Update- und Kern-API-Hosts gehören nicht in normale Privacy-Listen, wenn sie für die Funktion benötigt werden.
- `Restrict`, `Isolate`, `Updates` und `Block All` dürfen bewusst stärker eingreifen.
- Alle Listen werden normalisiert, dedupliziert und auf ungültige Einträge geprüft.
- Große Listen können zusätzlich als Full-/Medium-/Mini-Varianten veröffentlicht werden.
- DNS-Blocking kann First-Party-Tracking oder Werbung über dieselbe Domain wie den eigentlichen Inhalt nicht zuverlässig trennen.

</details>

---

# 🐛 False Positive gefunden?

Wenn eine normale Privacy-, Ads- oder Tracking-Liste eine wichtige Funktion blockiert:

[**False Positive melden**](../../issues)

Bitte angeben:

- betroffene Domain
- verwendete Liste / Profil
- App, Webseite oder Gerät
- ausgefallene Funktion
- optional Query-Log

---

# ❤️ Mitwirken

Pull Requests und Issues sind willkommen.

---

# 📜 Lizenz

Siehe [LICENSE](LICENSE).

---

<p align="center">

## 🐇 BlackRabbitZ DNS Blocklists

**Starker Schutz. Klare Wirkung. Volle Kontrolle.**

</p>

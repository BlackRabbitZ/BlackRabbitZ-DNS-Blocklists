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
| 🟩 **Light** | 15 | Blockiert Werbung und sehr eindeutig zuordenbare Tracker. Maximale Rücksicht auf Webseiten, Apps und Gerätefunktionen. | 🟢 Sehr hoch | Einsteiger / maximale Kompatibilität | [Liste öffnen](profiles/light.txt) |
| 🟦 **Normal** | 21 | Light + allgemeines Tracking, Analytics und erste Telemetrie-Endpunkte. | 🟢 Hoch | Normale Heimnetze | [Liste öffnen](profiles/normal.txt) |
| 🟨 **Pro ⭐** | 37 | Umfangreicher Schutz vor Ads, Trackern, Analytics, App-/Mobile-Tracking und Telemetrie bei möglichst normaler Nutzung. | 🟢 Hoch | **Für die meisten Nutzer** | [Liste öffnen](profiles/pro.txt) |
| 🟧 **Pro++** | 39 | Pro + aggressivere Privacy-, Telemetrie- und Geräte-Tracker. | 🟡 Mittel | Erfahrene Nutzer | [Liste öffnen](profiles/pro-plus.txt) |
| 🟥 **Ultimate** | 39 | Maximale allgemeine Ads-/Tracking-/Telemetry-Abdeckung. Höheres False-Positive-Risiko. | 🟠 Erhöht | Experten | [Liste öffnen](profiles/ultimate.txt) |

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
| 💎 **All-in** | 124 | Alle Schutz- und Blockierbereiche in einer Gesamtliste | Testsysteme, stark kontrollierte Netze, Experten | [Liste öffnen](profiles/all-in.txt) |

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
| 🟩 **Light** | 5 | Grundlegender Jugendschutz mit geringer Einschränkung | Jüngere Nutzer mit viel Freiraum | [Liste öffnen](family/main/light.txt) |
| 🟦 **Normal** | 10 | Adult + Gambling + SafeSearch-Basis | Familiennetzwerke | [Liste öffnen](family/main/normal.txt) |
| 🟨 **Pro ⭐** | 17 | Normal + Drugs + Violence + Weapons + Dating | **Empfohlen für Kindergeräte** | [Liste öffnen](family/main/pro.txt) |
| 🟧 **Pro++** | 17 | Pro + Social + Chats + Anti-Piracy + stärkerer Umgehungsschutz | Strengere Familiennetze | [Liste öffnen](family/main/pro-plus.txt) |
| 🟥 **Ultimate** | 19 | Maximale Family-Filterung ohne Allow-Only-Prinzip | Stark kontrollierte Geräte | [Liste öffnen](family/main/ultimate.txt) |

<details>
<summary><strong>📂 Einzelne Family-Listen anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste anzeigen |
| --- | :---: | --- | --- |
| 🔞 **Adult / NSFW** | 0 | Blockiert Pornografie, Adult-/NSFW-Seiten und zugehörige Dienste. | [Öffnen](lists/family/adult-nsfw.txt) |
| 🎰 **Gambling** | 5 | Blockiert Casinos, Sportwetten, Betting und Glücksspielplattformen. | [Öffnen](lists/family/gambling.txt) |
| 🎰 **Gambling Medium** | 5 | Kleinere Gambling-Variante mit geringerer Datenmenge. | [Öffnen](lists/family/gambling-medium.txt) |
| 🎰 **Gambling Mini** | 5 | Stark größenoptimierte Gambling-Variante für ressourcenarme Systeme. | [Öffnen](lists/family/gambling-mini.txt) |
| 💊 **Drugs** | 0 | Blockiert bekannte Drogenmärkte und einschlägige Plattformen. | [Öffnen](lists/family/drugs.txt) |
| 🩸 **Violence / Gore** | 0 | Blockiert Gore-, Shock- und extreme Gewaltinhalte. | [Öffnen](lists/family/violence-gore.txt) |
| 🔫 **Weapons** | 0 | Blockiert ausgewählte Waffenhandels- und problematische Waffenplattformen. | [Öffnen](lists/family/weapons.txt) |
| 💕 **Dating** | 5 | Blockiert Dating-Webseiten und Dating-Apps. | [Öffnen](lists/family/dating.txt) |
| 💬 **Social Networks** | 7 | Blockiert klassische soziale Netzwerke. | [Öffnen](lists/family/social-networks.txt) |
| 💭 **Chats & Communities** | 2 | Blockiert ausgewählte Chats, anonyme Communities und Community-Plattformen. | [Öffnen](lists/family/chats-communities.txt) |
| 🔍 **SafeSearch Unsupported** | 0 | Blockiert Suchdienste, die keinen verlässlichen SafeSearch-Modus anbieten. | [Öffnen](lists/family/safesearch-unsupported.txt) |
| 💀 **Anti-Piracy** | 0 | Blockiert Plattformen, die überwiegend zur unerlaubten Verbreitung urheberrechtlich geschützter Inhalte dienen. | [Öffnen](lists/family/anti-piracy.txt) |
| 🕳️ **Family Bypass Protection** | 0 | Blockiert typische DNS-/Proxy-/VPN-/Tor-Umgehungswege für Family-Gruppen. | [Öffnen](lists/family/bypass-protection.txt) |

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
| 🟩 **Basic** | 0 | Nur wichtige Lern-, Such- und Wissensdienste | Kleine Kinder | [Liste öffnen](lists/kids-allow-only/basic.txt) |
| 🟦 **School** | 0 | Basic + typische Schul- und Lernplattformen | Schulgeräte | [Liste öffnen](lists/kids-allow-only/school.txt) |
| 🟨 **Learning ⭐** | 0 | School + ausgewählte Mediatheken, Lernvideos und Kinderangebote | **Lern-Tablets / Familiengeräte** | [Liste öffnen](lists/kids-allow-only/learning.txt) |
| 🟧 **Extended** | 0 | Learning + ausgewählte Kommunikation und zusätzliche sichere Dienste | Ältere Kinder | [Liste öffnen](lists/kids-allow-only/extended.txt) |

<details>
<summary><strong>📂 Einzelne Allow-Only-Listen anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste anzeigen |
| --- | :---: | --- | --- |
| 📚 **Education** | 0 | Erlaubte Lern- und Bildungsplattformen. | [Öffnen](lists/kids-allow-only/education.txt) |
| 🏫 **School Platforms** | 0 | Erlaubte Schulportale, Lernmanagement- und Unterrichtsdienste. | [Öffnen](lists/kids-allow-only/school-platforms.txt) |
| 🔎 **Safe Search** | 0 | Erlaubte Suchmaschinen mit geeigneten Schutzoptionen. | [Öffnen](lists/kids-allow-only/safe-search.txt) |
| 📖 **Knowledge** | 0 | Erlaubte Wissens-, Lexikon- und Nachschlageangebote. | [Öffnen](lists/kids-allow-only/knowledge.txt) |
| 🎬 **Kids Media** | 0 | Ausgewählte Kinder-, Bildungs- und Mediathek-Angebote. | [Öffnen](lists/kids-allow-only/kids-media.txt) |
| 💬 **Approved Communication** | 0 | Gezielt erlaubte Kommunikationsdienste. | [Öffnen](lists/kids-allow-only/approved-communication.txt) |

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
| 🟩 **Light** | 15 | Eindeutige Werbung + sichere Tracker | Maximale Kompatibilität | [Liste öffnen](lists/privacy/main/light.txt) |
| 🟦 **Normal** | 21 | Light + allgemeines Tracking + Analytics | Normale Nutzung | [Liste öffnen](lists/privacy/main/normal.txt) |
| 🟨 **Pro ⭐** | 37 | Normal + Social + Mobile + App Tracking | **Die meisten Nutzer** | [Liste öffnen](lists/privacy/main/pro.txt) |
| 🟧 **Pro++** | 39 | Pro + Affiliate + Conversion + aggressive Tracker | Privacy-orientierte Nutzer | [Liste öffnen](lists/privacy/main/pro-plus.txt) |
| 🟥 **Ultimate** | 39 | Maximale Ads-/Tracking-Abdeckung | Experten | [Liste öffnen](lists/privacy/main/ultimate.txt) |

<details>
<summary><strong>📂 Einzelne Werbung-&-Tracking-Listen anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste anzeigen |
| --- | :---: | --- | --- |
| 📣 **Ads / Werbung** | 7 | Klassische Werbenetzwerke und Ad-Delivery. | [Öffnen](lists/privacy/full/ads.txt) |
| 🪟 **Pop-Up Ads** | 0 | Pop-up- und Pop-under-Werbung. | [Öffnen](lists/privacy/full/pop-up-ads.txt) |
| 🔗 **Affiliate Tracking** | 0 | Affiliate-, Referral- und Conversion-Tracking. | [Öffnen](lists/privacy/full/affiliate-tracking.txt) |
| ⚠️ **Aggressive Privacy** | 0 | Aggressivere Privacy-Endpunkte mit höherem Breakage-Risiko. | [Öffnen](lists/privacy/full/aggressive-privacy.txt) |
| 📊 **Analytics** | 8 | Web-, App- und Nutzungsanalyse. | [Öffnen](lists/privacy/full/analytics.txt) |
| 🤖 **Captcha / Antibot** | 0 | Ausgewählte Captcha-/Antibot-Infrastruktur. | [Öffnen](lists/privacy/full/captcha-antibot.txt) |
| 🌐 **CDN Tracking** | 0 | Tracking über CDN-/Edge-Infrastruktur. | [Öffnen](lists/privacy/full/cdn-tracking.txt) |
| 💬 **Chat Support** | 0 | Tracking in Chat-/Support-Systemen. | [Öffnen](lists/privacy/full/chat-support.txt) |
| 🍪 **Consent / CMP** | 0 | Consent- und CMP-Infrastruktur; bewusst aggressiv. | [Öffnen](lists/privacy/full/consent-cmp.txt) |
| 💥 **Crash Reporting** | 5 | Crash-, Fehler- und Ereignisberichte. | [Öffnen](lists/privacy/full/crash-reporting.txt) |
| 🗂️ **CRM** | 0 | CRM- und Lead-Tracking. | [Öffnen](lists/privacy/full/crm.txt) |
| 🛒 **E-Commerce Tracking** | 0 | Shop-, Conversion- und Commerce-Tracking. | [Öffnen](lists/privacy/full/ecommerce.txt) |
| 🔤 **External Fonts** | 0 | Externe Font-Endpunkte mit Privacy-Relevanz. | [Öffnen](lists/privacy/full/external-fonts.txt) |
| 🧬 **Fingerprinting** | 2 | Browser-/Device-Fingerprinting. | [Öffnen](lists/privacy/full/fingerprinting.txt) |
| 📢 **Marketing** | 0 | Marketing- und Kampagnenmessung. | [Öffnen](lists/privacy/full/marketing.txt) |
| 📱 **Mobile Tracking** | 5 | Mobile Attribution und SDK-Tracking. | [Öffnen](lists/privacy/full/mobile-tracking.txt) |
| 🧩 **Native Tracking** | 6 | Integrierte Tracker von OS, Apps und Geräten. | [Öffnen](lists/privacy/full/native-tracking.txt) |
| ✉️ **Newsletter Tracking** | 0 | Newsletter- und Mail-Tracking. | [Öffnen](lists/privacy/full/newsletter-tracking.txt) |
| 💳 **Payment Tracking** | 0 | Tracking rund um Zahlungsprozesse. | [Öffnen](lists/privacy/full/payment-tracking.txt) |
| 🔔 **Push Notifications** | 0 | Ausgewählte Push-/Notification-Endpunkte. | [Öffnen](lists/privacy/full/push-notifications.txt) |
| ⭐ **Recommendations** | 0 | Empfehlungs- und Personalisierungsdienste. | [Öffnen](lists/privacy/full/recommendations.txt) |
| 🔎 **Search Tracking** | 0 | Such- und Search-Tracking. | [Öffnen](lists/privacy/full/search-tracking.txt) |
| 📈 **SEO Tracking** | 0 | SEO-/Marketing-Messsysteme. | [Öffnen](lists/privacy/full/seo-tracking.txt) |
| 🎥 **Session Replay** | 0 | Session-Replay und Verhaltensaufzeichnung. | [Öffnen](lists/privacy/full/session-replay.txt) |
| 👥 **Social Tracking** | 4 | Tracking sozialer Netzwerke. | [Öffnen](lists/privacy/full/social-tracking.txt) |
| 📡 **Telemetry** | 6 | Allgemeine Telemetrie-Endpunkte. | [Öffnen](lists/privacy/full/telemetry.txt) |
| 👁️ **Trackers** | 8 | Große allgemeine Tracker-Liste. | [Öffnen](lists/privacy/full/trackers.txt) |
| 🟣 **Tracking Pixels** | 0 | Tracking-Pixel und Beacons. | [Öffnen](lists/privacy/full/tracking-pixels.txt) |
| 🔁 **Tracking Redirects** | 2 | Tracking-Weiterleitungen und Redirector-Infrastruktur. | [Öffnen](lists/privacy/full/tracking-redirects.txt) |

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
| 🟩 **Light** | 3 | sehr sichere Software-/Hardware-Telemetrie | Minimal | [Liste öffnen](lists/platforms/software-hardware-telemetry/main/light.txt) |
| 🟦 **Normal** | 4 | Light + zusätzliche Analytics | Niedrig | [Liste öffnen](lists/platforms/software-hardware-telemetry/main/normal.txt) |
| 🟨 **Pro ⭐** | 9 | umfangreicher Telemetrie-Schutz | Niedrig–Mittel | [Liste öffnen](lists/platforms/software-hardware-telemetry/main/pro.txt) |
| 🟧 **Pro++** | 10 | aggressivere Hersteller-Telemetrie | Mittel | [Liste öffnen](lists/platforms/software-hardware-telemetry/main/pro-plus.txt) |
| 🟥 **Ultimate** | 11 | maximaler Datenbestand dieses Bereichs | Hoch | [Liste öffnen](lists/platforms/software-hardware-telemetry/main/ultimate.txt) |

<details>
<summary><strong>📂 Software-/Hardware-Hersteller anzeigen</strong></summary>

| Name | Einträge | 🛡️ Privacy | ⚠️ Restrict | 🔄 Updates blockieren |
| --- | :---: | :---: | :---: | :---: |
| **Adobe** | 🛡️ Privacy: 2<br>⚠️ Restrict: 1<br>🔄 Updates blockieren: 2 | [Liste](lists/device-control/software-hardware/adobe/privacy.txt) | [Liste](lists/device-control/software-hardware/adobe/restrict.txt) | [Liste](lists/device-control/software-hardware/adobe/updates.txt) |
| **AMD** | 🛡️ Privacy: 1<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 1 | [Liste](lists/device-control/software-hardware/amd/privacy.txt) | [Liste](lists/device-control/software-hardware/amd/restrict.txt) | [Liste](lists/device-control/software-hardware/amd/updates.txt) |
| **Autodesk** | 🛡️ Privacy: 1<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 1 | [Liste](lists/device-control/software-hardware/autodesk/privacy.txt) | [Liste](lists/device-control/software-hardware/autodesk/restrict.txt) | [Liste](lists/device-control/software-hardware/autodesk/updates.txt) |
| **Corsair** | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/software-hardware/corsair/privacy.txt) | [Liste](lists/device-control/software-hardware/corsair/restrict.txt) | [Liste](lists/device-control/software-hardware/corsair/updates.txt) |
| **Intel** | 🛡️ Privacy: 1<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 1 | [Liste](lists/device-control/software-hardware/intel/privacy.txt) | [Liste](lists/device-control/software-hardware/intel/restrict.txt) | [Liste](lists/device-control/software-hardware/intel/updates.txt) |
| **Logitech** | 🛡️ Privacy: 1<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 1 | [Liste](lists/device-control/software-hardware/logitech/privacy.txt) | [Liste](lists/device-control/software-hardware/logitech/restrict.txt) | [Liste](lists/device-control/software-hardware/logitech/updates.txt) |
| **Nvidia** | 🛡️ Privacy: 2<br>⚠️ Restrict: 1<br>🔄 Updates blockieren: 2 | [Liste](lists/device-control/software-hardware/nvidia/privacy.txt) | [Liste](lists/device-control/software-hardware/nvidia/restrict.txt) | [Liste](lists/device-control/software-hardware/nvidia/updates.txt) |
| **Razer** | 🛡️ Privacy: 1<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 1 | [Liste](lists/device-control/software-hardware/razer/privacy.txt) | [Liste](lists/device-control/software-hardware/razer/restrict.txt) | [Liste](lists/device-control/software-hardware/razer/updates.txt) |

</details>

---

<br>

# 🤖 KI, Bots & Crawler

Listen für **AI-/LLM-Crawler, Scraper, Training-Bots, SEO-Bots und unerwünschte automatisierte Zugriffe**.

> DNS-Blocking kann Crawler-Domains sperren, ersetzt aber keine WAF-, Webserver- oder `robots.txt`-Regeln.

## Fertige KI-/Bot-Profile

| Profil | Einträge | Schutz | Risiko | Liste |
| --- | :---: | --- | :---: | --- |
| 🟩 **Light** | 0 | sehr konservative Bot-/Crawler-Auswahl | Minimal | [Liste öffnen](lists/automation/main/light.txt) |
| 🟦 **Normal** | 0 | zusätzliche Crawler und Tracking-Endpunkte | Niedrig | [Liste öffnen](lists/automation/main/normal.txt) |
| 🟨 **Pro ⭐** | 0 | breiter KI-/Crawler-Schutz | Niedrig–Mittel | [Liste öffnen](lists/automation/main/pro.txt) |
| 🟧 **Pro++** | 0 | aggressivere Bot-/Scraper-Blockierung | Mittel | [Liste öffnen](lists/automation/main/pro-plus.txt) |
| 🟥 **Ultimate** | 0 | maximaler Datenbestand dieses Bereichs | Hoch | [Liste öffnen](lists/automation/main/ultimate.txt) |

<details>
<summary><strong>📂 Einzelne KI-, Bot- & Crawler-Listen anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste |
| --- | :---: | --- | --- |
| **Aggressive Crawlers** | 0 | aggressive bekannte Crawler-Operatoren | [Öffnen](lists/automation/full/aggressive-crawlers.txt) |
| **AI Crawlers** | 0 | Crawler von KI-/AI-Anbietern | [Öffnen](lists/automation/full/ai-crawlers.txt) |
| **AI Scrapers** | 0 | Scraping-Endpunkte mit KI-Bezug | [Öffnen](lists/automation/full/ai-scrapers.txt) |
| **AI Telemetry** | 0 | Telemetrie von KI-Diensten | [Öffnen](lists/automation/full/ai-telemetry.txt) |
| **AI Tracking** | 0 | Tracking durch KI-Dienste | [Öffnen](lists/automation/full/ai-tracking.txt) |
| **LLM Crawlers** | 0 | LLM-Crawler und verwandte Infrastruktur | [Öffnen](lists/automation/full/llm-crawlers.txt) |
| **Malicious Bots** | 0 | bekannte schädliche Bots | [Öffnen](lists/automation/full/malicious-bots.txt) |
| **SEO Bots** | 0 | SEO-Crawler und automatisierte Analyse | [Öffnen](lists/automation/full/seo-bots.txt) |
| **Training Bots** | 0 | Bots für Training/Datensammlung | [Öffnen](lists/automation/full/training-bots.txt) |
| **Web Crawlers** | 0 | allgemeine Webcrawler | [Öffnen](lists/automation/full/web-crawlers.txt) |

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
| 🟩 **Light** | 0 | Sichere Privacy-/Security-Basis | Maximale Kompatibilität | [Liste öffnen](lists/security/main/light.txt) |
| 🟦 **Normal** | 0 | Telemetrie + Malware + Phishing | Normale Heimnetze | [Liste öffnen](lists/security/main/normal.txt) |
| 🟨 **Pro ⭐** | 0 | Umfassende Telemetrie + Malware + Phishing + Scam | **Empfohlen** | [Liste öffnen](lists/security/main/pro.txt) |
| 🟧 **Pro++** | 0 | Pro + aggressive Privacy- und Threat-Listen | Erfahrene Nutzer | [Liste öffnen](lists/security/main/pro-plus.txt) |
| 🟥 **Ultimate** | 0 | Maximale Privacy-/Security-Abdeckung | Experten | [Liste öffnen](lists/security/main/ultimate.txt) |

<details>
<summary><strong>🔐 Einzelne Privacy-Listen anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste anzeigen |
| --- | :---: | --- | --- |
| 📊 **General Telemetry** | 0 | Blockiert allgemeine Produkt-, App- und Herstellertelemetrie. | [Öffnen](lists/privacy-security/privacy/general-telemetry.txt) |
| 🩺 **Diagnostics** | 0 | Reduziert Diagnose-, Fehler- und Nutzungsdaten. | [Öffnen](lists/privacy-security/privacy/diagnostics.txt) |
| 💥 **Crash Reporting** | 0 | Blockiert ausgewählte automatische Crash-Reports. | [Öffnen](lists/privacy-security/privacy/crash-reporting.txt) |
| 🧬 **Fingerprinting** | 0 | Blockiert bekannte Infrastruktur zur Wiedererkennung und Profilbildung. | [Öffnen](lists/privacy-security/privacy/fingerprinting.txt) |
| 📈 **Usage Reporting** | 0 | Blockiert ausgewählte Nutzungsstatistiken und Usage Reports. | [Öffnen](lists/privacy-security/privacy/usage-reporting.txt) |
| ☁️ **Cloud Analytics** | 0 | Reduziert optionale Cloud-Analytics und Hersteller-Messdienste. | [Öffnen](lists/privacy-security/privacy/cloud-analytics.txt) |

</details>

<details>
<summary><strong>🛡️ Einzelne Security-Listen anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste anzeigen |
| --- | :---: | --- | --- |
| 🦠 **Malware** | 0 | Blockiert bekannte Malware-, Ransomware- und Schadsoftware-Infrastruktur. | [Öffnen](lists/privacy-security/security/malware.txt) |
| 🎣 **Phishing** | 0 | Blockiert bekannte Phishing- und Credential-Diebstahl-Domains. | [Öffnen](lists/privacy-security/security/phishing.txt) |
| 💰 **Scam & Internet Fraud** | 0 | Blockiert Betrugs-, Scam- und deceptive Domains. | [Öffnen](lists/privacy-security/security/scam-fraud.txt) |
| 🛒 **Fake Shops** | 0 | Blockiert bekannte Fake-Shops und betrügerische Store-Domains. | [Öffnen](lists/privacy-security/security/fake-shops.txt) |
| 🎭 **Fake Sites** | 0 | Blockiert Fake-Streaming-, Fake-Download-, Fake-Support- und sonstige Täuschungsseiten. | [Öffnen](lists/privacy-security/security/fake-sites.txt) |
| ⛏️ **Cryptomining** | 0 | Blockiert bekannte Browser-/Remote-Mining-Infrastruktur. | [Öffnen](lists/privacy-security/security/cryptomining.txt) |
| 🤖 **Botnets** | 0 | Blockiert bekannte Botnet-Infrastruktur. | [Öffnen](lists/privacy-security/security/botnets.txt) |
| 🎛️ **Command & Control** | 0 | Blockiert bekannte C2-Infrastruktur. | [Öffnen](lists/privacy-security/security/command-control.txt) |
| 🔐 **Threat Intelligence Full** | 0 | Große kombinierte Threat-Intelligence-Liste. | [Öffnen](lists/privacy-security/security/tif-full.txt) |
| 🔐 **Threat Intelligence Medium** | 0 | Mittlere TIF-Variante mit reduziertem Ressourcenbedarf. | [Öffnen](lists/privacy-security/security/tif-medium.txt) |
| 🔐 **Threat Intelligence Mini** | 0 | Kleine priorisierte TIF-Variante. | [Öffnen](lists/privacy-security/security/tif-mini.txt) |
| 🌐 **Threat Intelligence IPv4** | 0 | IPv4-Begleitliste für Firewall-/IP-basierte Threat-Intelligence-Filterung. | [Öffnen](lists/privacy-security/security/tif-ipv4.txt) |
| 🆕 **NRD 1–7 Tage** | 0 | Neu registrierte Domains der letzten 1–7 Tage; erhöhtes False-Positive-Risiko. | [Öffnen](lists/privacy-security/security/nrd-1-7d.txt) |
| 🆕 **NRD 8–14 Tage** | 0 | Neu registrierte Domains der Tage 8–14. | [Öffnen](lists/privacy-security/security/nrd-8-14d.txt) |
| 🆕 **NRD 15–21 Tage** | 0 | Neu registrierte Domains der Tage 15–21. | [Öffnen](lists/privacy-security/security/nrd-15-21d.txt) |
| 🆕 **NRD 22–28 Tage** | 0 | Neu registrierte Domains der Tage 22–28. | [Öffnen](lists/privacy-security/security/nrd-22-28d.txt) |
| 🆕 **NRD 29–35 Tage** | 0 | Neu registrierte Domains der Tage 29–35. | [Öffnen](lists/privacy-security/security/nrd-29-35d.txt) |
| 🧬 **DGA 7 Tage** | 0 | Algorithmisch erzeugte Domains aus aktuellen DGA-Daten. | [Öffnen](lists/privacy-security/security/dga-7d.txt) |
| 🧬 **DGA 14 Tage** | 0 | Größere DGA-Abdeckung über 14 Tage. | [Öffnen](lists/privacy-security/security/dga-14d.txt) |
| 🧬 **DGA 30 Tage** | 0 | Maximale DGA-Abdeckung über 30 Tage. | [Öffnen](lists/privacy-security/security/dga-30d.txt) |
| 🔏 **Dynamic DNS** | 0 | Blockiert bekannte Dynamic-DNS-Dienste mit erhöhtem Missbrauchspotenzial. | [Öffnen](lists/privacy-security/security/dynamic-dns.txt) |
| 💻 **Badware Hoster** | 0 | Blockiert besonders häufig für Schadsoftware missbrauchte Hosting-Infrastruktur. | [Öffnen](lists/privacy-security/security/badware-hoster.txt) |
| 🔮 **Most Abused TLDs** | 0 | Aggressive Liste häufig missbrauchter Top-Level-Domains. | [Öffnen](lists/privacy-security/security/abused-tlds.txt) |

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
| 💻 **Computer / Laptop** | 🛡️ Privacy: 10<br>⚠️ Restrict: 4<br>🔄 Updates blockieren: 9 | [Liste](lists/device-control/groups/computer/privacy.txt) | [Liste](lists/device-control/groups/computer/restrict.txt) | [Liste](lists/device-control/groups/computer/updates.txt) |
| 📺 **TV / Streaming-Geräte** | 🛡️ Privacy: 13<br>⚠️ Restrict: 4<br>🔄 Updates blockieren: 3 | [Liste](lists/device-control/groups/tv-streaming/privacy.txt) | [Liste](lists/device-control/groups/tv-streaming/restrict.txt) | [Liste](lists/device-control/groups/tv-streaming/updates.txt) |
| 📱 **Handy / Tablet** | 🛡️ Privacy: 23<br>⚠️ Restrict: 10<br>🔄 Updates blockieren: 17 | [Liste](lists/device-control/groups/mobile-tablet/privacy.txt) | [Liste](lists/device-control/groups/mobile-tablet/restrict.txt) | [Liste](lists/device-control/groups/mobile-tablet/updates.txt) |
| 🏠 **Smart Home / IoT** | 🛡️ Privacy: 10<br>⚠️ Restrict: 3<br>🔄 Updates blockieren: 2 | [Liste](lists/device-control/groups/smart-home-iot/privacy.txt) | [Liste](lists/device-control/groups/smart-home-iot/restrict.txt) | [Liste](lists/device-control/groups/smart-home-iot/updates.txt) |
| 💾 **NAS / Server** | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/groups/nas-server/privacy.txt) | [Liste](lists/device-control/groups/nas-server/restrict.txt) | [Liste](lists/device-control/groups/nas-server/updates.txt) |
| 🌐 **Router / Netzwerkgeräte** | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/groups/network/privacy.txt) | [Liste](lists/device-control/groups/network/restrict.txt) | [Liste](lists/device-control/groups/network/updates.txt) |
| 🎮 **Konsole / Gaming-Geräte** | 🛡️ Privacy: 4<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 4 | [Liste](lists/device-control/groups/gaming-devices/privacy.txt) | [Liste](lists/device-control/groups/gaming-devices/restrict.txt) | [Liste](lists/device-control/groups/gaming-devices/updates.txt) |
| 🗣️ **Sprachassistenten** | 🛡️ Privacy: 24<br>⚠️ Restrict: 9<br>🔄 Updates blockieren: 15 | [Liste](lists/device-control/groups/voice-assistants/privacy.txt) | [Liste](lists/device-control/groups/voice-assistants/restrict.txt) | [Liste](lists/device-control/groups/voice-assistants/updates.txt) |
| 🧩 **All-in** | 🛡️ Privacy: 46<br>⚠️ Restrict: 16<br>🔄 Updates blockieren: 29 | **[Alle Privacy-Listen](lists/device-control/all-in/privacy.txt)** | **[Alle Restrict-Listen](lists/device-control/all-in/restrict.txt)** | **[Alle Update-Blocklisten](lists/device-control/all-in/updates.txt)** |

<details>
<summary><strong>📂 Einzelne Geräte-, System- & Herstellerlisten anzeigen</strong></summary>

| Name | Einträge | 🛡️ Privacy | ⚠️ Restrict | 🔄 Updates blockieren |
| --- | :---: | :---: | :---: | :---: |
| 🪟 **Windows** | 🛡️ Privacy: 4<br>⚠️ Restrict: 2<br>🔄 Updates blockieren: 4 | [Liste](lists/device-control/windows/privacy.txt) | [Liste](lists/device-control/windows/restrict.txt) | [Liste](lists/device-control/windows/updates.txt) |
| 🤖 **Android** | 🛡️ Privacy: 2<br>⚠️ Restrict: 1<br>🔄 Updates blockieren: 2 | [Liste](lists/device-control/android/privacy.txt) | [Liste](lists/device-control/android/restrict.txt) | [Liste](lists/device-control/android/updates.txt) |
| 📱 **Google / Pixel** | 🛡️ Privacy: 4<br>⚠️ Restrict: 2<br>🔄 Updates blockieren: 3 | [Liste](lists/device-control/google-pixel/privacy.txt) | [Liste](lists/device-control/google-pixel/restrict.txt) | [Liste](lists/device-control/google-pixel/updates.txt) |
| 📱 **Samsung Mobile** | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/samsung-mobile/privacy.txt) | [Liste](lists/device-control/samsung-mobile/restrict.txt) | [Liste](lists/device-control/samsung-mobile/updates.txt) |
| 📱 **Huawei** | 🛡️ Privacy: 3<br>⚠️ Restrict: 1<br>🔄 Updates blockieren: 1 | [Liste](lists/device-control/huawei/privacy.txt) | [Liste](lists/device-control/huawei/restrict.txt) | [Liste](lists/device-control/huawei/updates.txt) |
| 📱 **Xiaomi** | 🛡️ Privacy: 4<br>⚠️ Restrict: 2<br>🔄 Updates blockieren: 2 | [Liste](lists/device-control/xiaomi/privacy.txt) | [Liste](lists/device-control/xiaomi/restrict.txt) | [Liste](lists/device-control/xiaomi/updates.txt) |
| 📱 **OPPO / Realme** | 🛡️ Privacy: 2<br>⚠️ Restrict: 1<br>🔄 Updates blockieren: 1 | [Liste](lists/device-control/oppo-realme/privacy.txt) | [Liste](lists/device-control/oppo-realme/restrict.txt) | [Liste](lists/device-control/oppo-realme/updates.txt) |
| 📱 **Vivo** | 🛡️ Privacy: 2<br>⚠️ Restrict: 1<br>🔄 Updates blockieren: 1 | [Liste](lists/device-control/vivo/privacy.txt) | [Liste](lists/device-control/vivo/restrict.txt) | [Liste](lists/device-control/vivo/updates.txt) |
| 🍎 **Apple / iOS / macOS** | 🛡️ Privacy: 4<br>⚠️ Restrict: 2<br>🔄 Updates blockieren: 5 | [Liste](lists/device-control/apple/privacy.txt) | [Liste](lists/device-control/apple/restrict.txt) | [Liste](lists/device-control/apple/updates.txt) |
| 🐧 **Linux** | 🛡️ Privacy: 2<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/linux/privacy.txt) | [Liste](lists/device-control/linux/restrict.txt) | [Liste](lists/device-control/linux/updates.txt) |
| 📺 **Samsung TV** | 🛡️ Privacy: 4<br>⚠️ Restrict: 1<br>🔄 Updates blockieren: 2 | [Liste](lists/device-control/smart-tv/samsung/privacy.txt) | [Liste](lists/device-control/smart-tv/samsung/restrict.txt) | [Liste](lists/device-control/smart-tv/samsung/updates.txt) |
| 📺 **LG webOS** | 🛡️ Privacy: 3<br>⚠️ Restrict: 1<br>🔄 Updates blockieren: 2 | [Liste](lists/device-control/smart-tv/lg/privacy.txt) | [Liste](lists/device-control/smart-tv/lg/restrict.txt) | [Liste](lists/device-control/smart-tv/lg/updates.txt) |
| 📺 **Roku** | 🛡️ Privacy: 3<br>⚠️ Restrict: 1<br>🔄 Updates blockieren: 1 | [Liste](lists/device-control/smart-tv/roku/privacy.txt) | [Liste](lists/device-control/smart-tv/roku/restrict.txt) | [Liste](lists/device-control/smart-tv/roku/updates.txt) |
| 🔥 **Fire TV** | 🛡️ Privacy: 10<br>⚠️ Restrict: 3<br>🔄 Updates blockieren: 2 | [Liste](lists/device-control/smart-tv/fire-tv/privacy.txt) | [Liste](lists/device-control/smart-tv/fire-tv/restrict.txt) | [Liste](lists/device-control/smart-tv/fire-tv/updates.txt) |
| 📦 **Amazon Geräte / Alexa** | 🛡️ Privacy: 10<br>⚠️ Restrict: 3<br>🔄 Updates blockieren: 2 | [Liste](lists/device-control/amazon/privacy.txt) | [Liste](lists/device-control/amazon/restrict.txt) | [Liste](lists/device-control/amazon/updates.txt) |
| 📺 **Android TV / Google TV** | 🛡️ Privacy: 4<br>⚠️ Restrict: 2<br>🔄 Updates blockieren: 3 | [Liste](lists/device-control/smart-tv/android-tv/privacy.txt) | [Liste](lists/device-control/smart-tv/android-tv/restrict.txt) | [Liste](lists/device-control/smart-tv/android-tv/updates.txt) |
| 🏠 **IoT / Smart Home** | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/iot/privacy.txt) | [Liste](lists/device-control/iot/restrict.txt) | [Liste](lists/device-control/iot/updates.txt) |
| 💾 **NAS** | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/nas/privacy.txt) | [Liste](lists/device-control/nas/restrict.txt) | [Liste](lists/device-control/nas/updates.txt) |
| 🖥️ **Server** | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/server/privacy.txt) | [Liste](lists/device-control/server/restrict.txt) | [Liste](lists/device-control/server/updates.txt) |
| 🌐 **Router / Netzwerkgeräte** | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/router/privacy.txt) | [Liste](lists/device-control/router/restrict.txt) | [Liste](lists/device-control/router/updates.txt) |
| 🎮 **Xbox** | 🛡️ Privacy: 2<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 1 | [Liste](lists/device-control/gaming/xbox/privacy.txt) | [Liste](lists/device-control/gaming/xbox/restrict.txt) | [Liste](lists/device-control/gaming/xbox/updates.txt) |
| 🎮 **PlayStation** | 🛡️ Privacy: 1<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 2 | [Liste](lists/device-control/gaming/playstation/privacy.txt) | [Liste](lists/device-control/gaming/playstation/restrict.txt) | [Liste](lists/device-control/gaming/playstation/updates.txt) |
| 🎮 **Nintendo** | 🛡️ Privacy: 1<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 1 | [Liste](lists/device-control/gaming/nintendo/privacy.txt) | [Liste](lists/device-control/gaming/nintendo/restrict.txt) | [Liste](lists/device-control/gaming/nintendo/updates.txt) |
| 🗣️ **Sprachassistenten** | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/voice-assistants/privacy.txt) | [Liste](lists/device-control/voice-assistants/restrict.txt) | [Liste](lists/device-control/voice-assistants/updates.txt) |

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
| **1&1** | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/providers/1und1/privacy.txt) | [Liste](lists/device-control/providers/1und1/restrict.txt) | [Liste](lists/device-control/providers/1und1/updates.txt) |
| **Deutsche Glasfaser** | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/providers/deutsche-glasfaser/privacy.txt) | [Liste](lists/device-control/providers/deutsche-glasfaser/restrict.txt) | [Liste](lists/device-control/providers/deutsche-glasfaser/updates.txt) |
| **O2** | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/providers/o2/privacy.txt) | [Liste](lists/device-control/providers/o2/restrict.txt) | [Liste](lists/device-control/providers/o2/updates.txt) |
| **Telekom** | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/providers/telekom/privacy.txt) | [Liste](lists/device-control/providers/telekom/restrict.txt) | [Liste](lists/device-control/providers/telekom/updates.txt) |
| **Unitymedia** | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/providers/unitymedia/privacy.txt) | [Liste](lists/device-control/providers/unitymedia/restrict.txt) | [Liste](lists/device-control/providers/unitymedia/updates.txt) |
| **Vodafone** | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/providers/vodafone/privacy.txt) | [Liste](lists/device-control/providers/vodafone/restrict.txt) | [Liste](lists/device-control/providers/vodafone/updates.txt) |

### Fertige Provider-Profile
| Profil | Einträge | Liste |
|---|:---:|---|
| **Light** | 0 | [Liste öffnen](lists/platforms/providers/main/light.txt) |
| **Normal** | 0 | [Liste öffnen](lists/platforms/providers/main/normal.txt) |
| **Pro** | 0 | [Liste öffnen](lists/platforms/providers/main/pro.txt) |
| **Pro++** | 0 | [Liste öffnen](lists/platforms/providers/main/pro-plus.txt) |
| **Ultimate** | 0 | [Liste öffnen](lists/platforms/providers/main/ultimate.txt) |

</details>

<details>
<summary><strong>🏢 Google, Microsoft, Apple & Amazon anzeigen</strong></summary>

| Ökosystem | Einträge | 🛡️ Privacy | ⚠️ Restrict | 🔄 Updates blockieren |
| --- | :---: | :---: | :---: | :---: |
| **Amazon** | 🛡️ Privacy: 10<br>⚠️ Restrict: 3<br>🔄 Updates blockieren: 2 | [Liste](lists/device-control/ecosystems/amazon/privacy.txt) | [Liste](lists/device-control/ecosystems/amazon/restrict.txt) | [Liste](lists/device-control/ecosystems/amazon/updates.txt) |
| **Apple** | 🛡️ Privacy: 4<br>⚠️ Restrict: 2<br>🔄 Updates blockieren: 5 | [Liste](lists/device-control/ecosystems/apple/privacy.txt) | [Liste](lists/device-control/ecosystems/apple/restrict.txt) | [Liste](lists/device-control/ecosystems/apple/updates.txt) |
| **Google** | 🛡️ Privacy: 4<br>⚠️ Restrict: 2<br>🔄 Updates blockieren: 3 | [Liste](lists/device-control/ecosystems/google/privacy.txt) | [Liste](lists/device-control/ecosystems/google/restrict.txt) | [Liste](lists/device-control/ecosystems/google/updates.txt) |
| **Microsoft** | 🛡️ Privacy: 6<br>⚠️ Restrict: 2<br>🔄 Updates blockieren: 5 | [Liste](lists/device-control/ecosystems/microsoft/privacy.txt) | [Liste](lists/device-control/ecosystems/microsoft/restrict.txt) | [Liste](lists/device-control/ecosystems/microsoft/updates.txt) |

</details>

<details>
<summary><strong>🏭 Herstellerlisten anzeigen</strong></summary>

| Hersteller | Einträge | 🛡️ Privacy | ⚠️ Restrict | 🔄 Updates blockieren |
| --- | :---: | :---: | :---: | :---: |
| Adobe | 🛡️ Privacy: 2<br>⚠️ Restrict: 1<br>🔄 Updates blockieren: 2 | [Liste](lists/device-control/manufacturers/adobe/privacy.txt) | [Liste](lists/device-control/manufacturers/adobe/restrict.txt) | [Liste](lists/device-control/manufacturers/adobe/updates.txt) |
| Amazon | 🛡️ Privacy: 10<br>⚠️ Restrict: 3<br>🔄 Updates blockieren: 2 | [Liste](lists/device-control/manufacturers/amazon/privacy.txt) | [Liste](lists/device-control/manufacturers/amazon/restrict.txt) | [Liste](lists/device-control/manufacturers/amazon/updates.txt) |
| AMD | 🛡️ Privacy: 1<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 1 | [Liste](lists/device-control/manufacturers/amd/privacy.txt) | [Liste](lists/device-control/manufacturers/amd/restrict.txt) | [Liste](lists/device-control/manufacturers/amd/updates.txt) |
| Apple | 🛡️ Privacy: 4<br>⚠️ Restrict: 2<br>🔄 Updates blockieren: 5 | [Liste](lists/device-control/manufacturers/apple/privacy.txt) | [Liste](lists/device-control/manufacturers/apple/restrict.txt) | [Liste](lists/device-control/manufacturers/apple/updates.txt) |
| Autodesk | 🛡️ Privacy: 1<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 1 | [Liste](lists/device-control/manufacturers/autodesk/privacy.txt) | [Liste](lists/device-control/manufacturers/autodesk/restrict.txt) | [Liste](lists/device-control/manufacturers/autodesk/updates.txt) |
| EA | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/manufacturers/ea/privacy.txt) | [Liste](lists/device-control/manufacturers/ea/restrict.txt) | [Liste](lists/device-control/manufacturers/ea/updates.txt) |
| Epic | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/manufacturers/epic/privacy.txt) | [Liste](lists/device-control/manufacturers/epic/restrict.txt) | [Liste](lists/device-control/manufacturers/epic/updates.txt) |
| Google | 🛡️ Privacy: 4<br>⚠️ Restrict: 2<br>🔄 Updates blockieren: 3 | [Liste](lists/device-control/manufacturers/google/privacy.txt) | [Liste](lists/device-control/manufacturers/google/restrict.txt) | [Liste](lists/device-control/manufacturers/google/updates.txt) |
| Huawei | 🛡️ Privacy: 3<br>⚠️ Restrict: 1<br>🔄 Updates blockieren: 1 | [Liste](lists/device-control/manufacturers/huawei/privacy.txt) | [Liste](lists/device-control/manufacturers/huawei/restrict.txt) | [Liste](lists/device-control/manufacturers/huawei/updates.txt) |
| LG | 🛡️ Privacy: 3<br>⚠️ Restrict: 1<br>🔄 Updates blockieren: 2 | [Liste](lists/device-control/manufacturers/lg/privacy.txt) | [Liste](lists/device-control/manufacturers/lg/restrict.txt) | [Liste](lists/device-control/manufacturers/lg/updates.txt) |
| Logitech | 🛡️ Privacy: 1<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 1 | [Liste](lists/device-control/manufacturers/logitech/privacy.txt) | [Liste](lists/device-control/manufacturers/logitech/restrict.txt) | [Liste](lists/device-control/manufacturers/logitech/updates.txt) |
| Meta | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/manufacturers/meta/privacy.txt) | [Liste](lists/device-control/manufacturers/meta/restrict.txt) | [Liste](lists/device-control/manufacturers/meta/updates.txt) |
| Microsoft | 🛡️ Privacy: 6<br>⚠️ Restrict: 2<br>🔄 Updates blockieren: 5 | [Liste](lists/device-control/manufacturers/microsoft/privacy.txt) | [Liste](lists/device-control/manufacturers/microsoft/restrict.txt) | [Liste](lists/device-control/manufacturers/microsoft/updates.txt) |
| Nintendo | 🛡️ Privacy: 1<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 1 | [Liste](lists/device-control/manufacturers/nintendo/privacy.txt) | [Liste](lists/device-control/manufacturers/nintendo/restrict.txt) | [Liste](lists/device-control/manufacturers/nintendo/updates.txt) |
| Nvidia | 🛡️ Privacy: 2<br>⚠️ Restrict: 1<br>🔄 Updates blockieren: 2 | [Liste](lists/device-control/manufacturers/nvidia/privacy.txt) | [Liste](lists/device-control/manufacturers/nvidia/restrict.txt) | [Liste](lists/device-control/manufacturers/nvidia/updates.txt) |
| Philips | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/manufacturers/philips/privacy.txt) | [Liste](lists/device-control/manufacturers/philips/restrict.txt) | [Liste](lists/device-control/manufacturers/philips/updates.txt) |
| Razer | 🛡️ Privacy: 1<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 1 | [Liste](lists/device-control/manufacturers/razer/privacy.txt) | [Liste](lists/device-control/manufacturers/razer/restrict.txt) | [Liste](lists/device-control/manufacturers/razer/updates.txt) |
| Samsung | 🛡️ Privacy: 4<br>⚠️ Restrict: 1<br>🔄 Updates blockieren: 2 | [Liste](lists/device-control/manufacturers/samsung/privacy.txt) | [Liste](lists/device-control/manufacturers/samsung/restrict.txt) | [Liste](lists/device-control/manufacturers/samsung/updates.txt) |
| Sony | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/manufacturers/sony/privacy.txt) | [Liste](lists/device-control/manufacturers/sony/restrict.txt) | [Liste](lists/device-control/manufacturers/sony/updates.txt) |
| Ubisoft | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/manufacturers/ubisoft/privacy.txt) | [Liste](lists/device-control/manufacturers/ubisoft/restrict.txt) | [Liste](lists/device-control/manufacturers/ubisoft/updates.txt) |
| Valve / Steam | 🛡️ Privacy: 0<br>⚠️ Restrict: 0<br>🔄 Updates blockieren: 0 | [Liste](lists/device-control/manufacturers/valve-steam/privacy.txt) | [Liste](lists/device-control/manufacturers/valve-steam/restrict.txt) | [Liste](lists/device-control/manufacturers/valve-steam/updates.txt) |
| Xiaomi | 🛡️ Privacy: 4<br>⚠️ Restrict: 2<br>🔄 Updates blockieren: 2 | [Liste](lists/device-control/manufacturers/xiaomi/privacy.txt) | [Liste](lists/device-control/manufacturers/xiaomi/restrict.txt) | [Liste](lists/device-control/manufacturers/xiaomi/updates.txt) |

</details>

<details>
<summary><strong>🚗 Automotive / Connected Cars anzeigen</strong></summary>

Fertige Profile:
| Profil | Einträge | Liste |
|---|:---:|---|
| **Light** | 0 | [Liste öffnen](lists/platforms/automotive/main/light.txt) |
| **Normal** | 0 | [Liste öffnen](lists/platforms/automotive/main/normal.txt) |
| **Pro** | 0 | [Liste öffnen](lists/platforms/automotive/main/pro.txt) |
| **Pro++** | 0 | [Liste öffnen](lists/platforms/automotive/main/pro-plus.txt) |
| **Ultimate** | 0 | [Liste öffnen](lists/platforms/automotive/main/ultimate.txt) |

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
| Alexa | 🛡️ Privacy: 10<br>⚠️ Restrict: 3<br>🔄 Updates blockieren: 2 | [Liste](lists/device-control/voice-assistants/alexa/privacy.txt) | [Liste](lists/device-control/voice-assistants/alexa/restrict.txt) | [Liste](lists/device-control/voice-assistants/alexa/updates.txt) |
| Cortana | 🛡️ Privacy: 6<br>⚠️ Restrict: 2<br>🔄 Updates blockieren: 5 | [Liste](lists/device-control/voice-assistants/cortana/privacy.txt) | [Liste](lists/device-control/voice-assistants/cortana/restrict.txt) | [Liste](lists/device-control/voice-assistants/cortana/updates.txt) |
| Google Assistant | 🛡️ Privacy: 4<br>⚠️ Restrict: 2<br>🔄 Updates blockieren: 3 | [Liste](lists/device-control/voice-assistants/google-assistant/privacy.txt) | [Liste](lists/device-control/voice-assistants/google-assistant/restrict.txt) | [Liste](lists/device-control/voice-assistants/google-assistant/updates.txt) |
| Siri | 🛡️ Privacy: 4<br>⚠️ Restrict: 2<br>🔄 Updates blockieren: 5 | [Liste](lists/device-control/voice-assistants/siri/privacy.txt) | [Liste](lists/device-control/voice-assistants/siri/restrict.txt) | [Liste](lists/device-control/voice-assistants/siri/updates.txt) |

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
| 🟩 **Light** | 0 | Nur sehr sichere Gaming-Telemetrie | Maximale Launcher-/Game-Kompatibilität | [Liste öffnen](lists/apps/gaming/main/light.txt) |
| 🟦 **Normal** | 0 | Launcher-Analytics + Crash-/Metrics-Endpunkte | Normale Gaming-PCs | [Liste öffnen](lists/apps/gaming/main/normal.txt) |
| 🟨 **Pro ⭐** | 0 | Breiter Gaming-Privacy-Schutz | **Empfohlen** | [Liste öffnen](lists/apps/gaming/main/pro.txt) |
| 🟧 **Pro++** | 0 | Aggressivere Launcher-/Game-Telemetrie | Erfahrene Nutzer | [Liste öffnen](lists/apps/gaming/main/pro-plus.txt) |
| 🟥 **Ultimate** | 0 | Maximale Gaming-Telemetrie-Abdeckung | Test-/Expertenumgebungen | [Liste öffnen](lists/apps/gaming/main/ultimate.txt) |

<details>
<summary><strong>📂 Einzelne Gaming-Listen anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste anzeigen |
| --- | :---: | --- | --- |
| 🎮 **Gaming Telemetry** | 0 | Empfohlene Game-, Launcher-, Analytics- und Crash-Reporting-Endpunkte mit geringem Risiko. | [Öffnen](lists/gaming/gaming-telemetry.txt) |
| ⚠️ **Gaming Telemetry – Aggressive** | 0 | Zusätzliche Endpunkte mit höherem Risiko für Launcher, Login oder Gameplay. | [Öffnen](lists/gaming/gaming-telemetry-aggressive.txt) |
| 🧩 **Gaming RegEx Rules** | 0 | Dynamische Pi-hole-RegEx-Regeln für zusätzliche Gaming-Telemetrie. | [Öffnen](lists/gaming/gaming-telemetry-regex.txt) |
| 🟦 **Steam Tracking** | 0 | Steam-/Valve-Tracking und Telemetrie reduzieren. | [Öffnen](lists/gaming/platforms/steam-privacy.txt) |
| 🟪 **Battle.net Tracking** | 0 | Blizzard-/Battle.net-Analytics und Telemetrie reduzieren. | [Öffnen](lists/gaming/platforms/battlenet-privacy.txt) |
| 🟨 **Rockstar Tracking** | 0 | Rockstar-Launcher-/Game-Telemetrie reduzieren. | [Öffnen](lists/gaming/platforms/rockstar-privacy.txt) |
| ⚫ **Epic Tracking** | 0 | Epic-Games-/Launcher-Telemetrie reduzieren. | [Öffnen](lists/gaming/platforms/epic-privacy.txt) |
| 🔴 **Riot Tracking** | 0 | Riot-Launcher-/Game-Telemetrie reduzieren. | [Öffnen](lists/gaming/platforms/riot-privacy.txt) |

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
| 🟩 **Light** | 0 | konservativer Privacy-Schutz | Minimal | [Liste öffnen](lists/infrastructure/cloud-development/main/light.txt) |
| 🟦 **Normal** | 0 | zusätzliche Tracking-/Analytics-Endpunkte | Niedrig | [Liste öffnen](lists/infrastructure/cloud-development/main/normal.txt) |
| 🟨 **Pro ⭐** | 0 | umfangreicher Cloud-/Development-Privacy-Schutz | Niedrig–Mittel | [Liste öffnen](lists/infrastructure/cloud-development/main/pro.txt) |
| 🟧 **Pro++** | 0 | aggressive Cloud-/Developer-Telemetrie | Mittel | [Liste öffnen](lists/infrastructure/cloud-development/main/pro-plus.txt) |
| 🟥 **Ultimate** | 0 | maximaler Datenbestand dieses Bereichs | Hoch | [Liste öffnen](lists/infrastructure/cloud-development/main/ultimate.txt) |

<details>
<summary><strong>📂 Einzelne Cloud- & Development-Dienste anzeigen</strong></summary>

| Dienst | Einträge | 🛡️ Privacy | 🚫 Block All |
| --- | :---: | :---: | :---: |
| AWS | 🛡️ Privacy: 0<br>🚫 Block All: 0 | [Liste](lists/service-blocking/cloud-development/aws/privacy.txt) | [Liste](lists/service-blocking/cloud-development/aws/block-all.txt) |
| Azure | 🛡️ Privacy: 0<br>🚫 Block All: 0 | [Liste](lists/service-blocking/cloud-development/azure/privacy.txt) | [Liste](lists/service-blocking/cloud-development/azure/block-all.txt) |
| CI/CD | 🛡️ Privacy: 0<br>🚫 Block All: 0 | [Liste](lists/service-blocking/cloud-development/cicd/privacy.txt) | [Liste](lists/service-blocking/cloud-development/cicd/block-all.txt) |
| Cloud Storage | 🛡️ Privacy: 0<br>🚫 Block All: 0 | [Liste](lists/service-blocking/cloud-development/cloud-storage/privacy.txt) | [Liste](lists/service-blocking/cloud-development/cloud-storage/block-all.txt) |
| Cloudflare | 🛡️ Privacy: 0<br>🚫 Block All: 0 | [Liste](lists/service-blocking/cloud-development/cloudflare/privacy.txt) | [Liste](lists/service-blocking/cloud-development/cloudflare/block-all.txt) |
| GitHub | 🛡️ Privacy: 0<br>🚫 Block All: 0 | [Liste](lists/service-blocking/cloud-development/github/privacy.txt) | [Liste](lists/service-blocking/cloud-development/github/block-all.txt) |
| GitLab | 🛡️ Privacy: 0<br>🚫 Block All: 0 | [Liste](lists/service-blocking/cloud-development/gitlab/privacy.txt) | [Liste](lists/service-blocking/cloud-development/gitlab/block-all.txt) |
| Google Cloud | 🛡️ Privacy: 0<br>🚫 Block All: 0 | [Liste](lists/service-blocking/cloud-development/google-cloud/privacy.txt) | [Liste](lists/service-blocking/cloud-development/google-cloud/block-all.txt) |
| JetBrains | 🛡️ Privacy: 0<br>🚫 Block All: 0 | [Liste](lists/service-blocking/cloud-development/jetbrains/privacy.txt) | [Liste](lists/service-blocking/cloud-development/jetbrains/block-all.txt) |
| Oracle Cloud | 🛡️ Privacy: 0<br>🚫 Block All: 0 | [Liste](lists/service-blocking/cloud-development/oracle-cloud/privacy.txt) | [Liste](lists/service-blocking/cloud-development/oracle-cloud/block-all.txt) |
| Visual Studio | 🛡️ Privacy: 0<br>🚫 Block All: 0 | [Liste](lists/service-blocking/cloud-development/visual-studio/privacy.txt) | [Liste](lists/service-blocking/cloud-development/visual-studio/block-all.txt) |
| VS Code | 🛡️ Privacy: 0<br>🚫 Block All: 0 | [Liste](lists/service-blocking/cloud-development/vs-code/privacy.txt) | [Liste](lists/service-blocking/cloud-development/vs-code/block-all.txt) |

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
| 🟩 **Light** | 4 | Sichere DNS-/Bypass-Basis | Heimnetze | [Liste öffnen](lists/network/main/light.txt) |
| 🟦 **Normal** | 4 | Light + bekannte DoH-/Bypass-Endpunkte | Kontrollierte Heimnetze | [Liste öffnen](lists/network/main/normal.txt) |
| 🟨 **Pro ⭐** | 9 | DoH + VPN/Proxy + Rebind-/Redirect-Schutz | **Homelabs / Admins** | [Liste öffnen](lists/network/main/pro.txt) |
| 🟧 **Pro++** | 9 | Aggressivere Umgehungs- und Spezialfilter | Schulen / strengere Netze | [Liste öffnen](lists/network/main/pro-plus.txt) |
| 🟥 **Ultimate** | 9 | Maximale Netzwerk-Kontrolle | Experten / isolierte Netze | [Liste öffnen](lists/network/main/ultimate.txt) |

<details>
<summary><strong>📂 Einzelne Netzwerk-&-Speziallisten anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste anzeigen |
| --- | :---: | --- | --- |
| 📤 **DoH / VPN / Tor / Proxy Bypass** | 0 | Blockiert bekannte verschlüsselte DNS-, VPN-, Tor- und Proxy-Endpunkte zur Filterumgehung. | [Öffnen](lists/network/doh-vpn-tor-proxy-bypass.txt) |
| 🌐 **DoH Only** | 4 | Blockiert bekannte DNS-over-HTTPS-Endpunkte. | [Öffnen](lists/network/doh-only.txt) |
| 🌐 **DoH IPv4** | 0 | IPv4-Liste bekannter DoH-Resolver. | [Öffnen](lists/network/doh-ipv4.txt) |
| 🔎 **SafeSearch Unsupported** | 0 | Blockiert Suchmaschinen, die keinen verlässlichen SafeSearch-Modus unterstützen. | [Öffnen](lists/network/safesearch-unsupported.txt) |
| 📲 **URL Shortener** | 5 | Blockiert bekannte URL-Shortener und Redirect-Dienste. | [Öffnen](lists/network/url-shortener.txt) |
| 🛡️ **DNS Rebind Protection** | — | Dokumentation/Regeln zum Schutz gegen DNS-Rebinding. | [Öffnen](docs/DNS_REBIND_PROTECTION.md) |
| 🤖 **AI Crawler** | 0 | Blockiert ausgewählte KI-Crawler und Scraper. | [Öffnen](lists/network/ai-crawlers.txt) |
| 🕷️ **Scraper & Bots** | 0 | Blockiert ausgewählte aggressive Bots und Scraper. | [Öffnen](lists/network/scrapers-bots.txt) |
| 🔏 **Dynamic DNS** | 0 | Blockiert bekannte Dynamic-DNS-Dienste. | [Öffnen](lists/network/dynamic-dns.txt) |
| 🔮 **Suspicious TLDs** | 0 | Aggressive Regeln für ausgewählte missbrauchte Top-Level-Domains. | [Öffnen](lists/network/suspicious-tlds.txt) |
| 🔁 **Tracking Redirectors** | 0 | Blockiert bekannte Tracking- und Redirect-Infrastruktur. | [Öffnen](lists/network/tracking-redirectors.txt) |

</details>

<details>
<summary><strong>🧰 Speziallisten anzeigen</strong></summary>

| Spezialliste | Einträge | Zweck | Liste |
| --- | :---: | --- | --- |
| **Fake / Scam / Trap Sites** | 0 | Scam + Fake Shops + Fake Software gebündelt | [Öffnen](lists/special/fake-scam-trap-sites.txt) |
| **Threat Intelligence Mini** | 0 | kompakte Threat-Intelligence-Stufe | [Öffnen](lists/security/main/pro.txt) |
| **Threat Intelligence Medium** | 0 | mittlere Threat-Intelligence-Stufe | [Öffnen](lists/security/main/pro-plus.txt) |
| **Threat Intelligence Full** | 0 | kompletter Security-Ultimate-Datenbestand | [Öffnen](lists/security/main/ultimate.txt) |
| **Dynamic DNS** | 0 | bekannte DynDNS-Provider; aggressiv | [Öffnen](lists/network/full/dynamic-dns.txt) |
| **Badware Hoster** | 0 | häufig missbrauchte Hosting-/Site-Builder-Infrastruktur | [Öffnen](lists/security/full/badware-hosters.txt) |
| **Most Abused TLDs** | — | riskante TLDs/Suffixe | [Spezial-Doku](docs/SPECIAL_LISTS.md) |
| **DNS Rebind Protection** | — | Resolver-/dnsmasq-Policy | [Öffnen](policies/) |
| **DoH/VPN/Tor/Proxy Bypass** | 0 | kombinierte Umgehungsliste | [Öffnen](lists/network/full/dns-bypass.txt) |
| **Encrypted DNS Only** | — | DoH + DoT + Private DNS | [Öffnen](lists/network/) |
| **SafeSearch not supported** | 0 | Suchmaschinen ohne SafeSearch-Support | [Öffnen](lists/network/full/safesearch-not-supported.txt) |
| **URL Shortener** | 5 | bekannte Kurzlink-Dienste | [Öffnen](lists/network/full/url-shorteners.txt) |
| **Native Tracker** | 6 | integrierte Tracker von OS, Apps und Geräten | [Öffnen](lists/privacy/full/native-tracking.txt) |

</details>

<details>
<summary><strong>🌍 Regionale Listen anzeigen</strong></summary>

> Regionale Listen werden **nicht** einfach nach TLD gebaut, sondern aus dem vorhandenen Datenbestand kuratiert.

| Region | Einträge | Liste |
| --- | :---: | --- |
| 🇨🇳 **China** | 0 | [Öffnen](lists/regional/cn.txt) |
| 🇩🇪 **Deutschland** | 0 | [Öffnen](lists/regional/de.txt) |
| 🇪🇸 **Spanien** | 0 | [Öffnen](lists/regional/es.txt) |
| 🇪🇺 **EU** | 0 | [Öffnen](lists/regional/eu.txt) |
| 🇫🇷 **Frankreich** | 0 | [Öffnen](lists/regional/fr.txt) |
| 🇮🇹 **Italien** | 0 | [Öffnen](lists/regional/it.txt) |
| 🇯🇵 **Japan** | 0 | [Öffnen](lists/regional/jp.txt) |
| 🇰🇷 **Südkorea** | 0 | [Öffnen](lists/regional/kr.txt) |
| 🇷🇺 **Russland** | 0 | [Öffnen](lists/regional/ru.txt) |
| 🇬🇧 **UK** | 0 | [Öffnen](lists/regional/uk.txt) |
| 🇺🇸 **USA** | 0 | [Öffnen](lists/regional/us.txt) |

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
| 💬 **Social Media** | 22 | Blockiert unterstützte Social-Media-Plattformen vollständig. | [Liste öffnen](lists/block-all/packages/social-media.txt) |
| 🎵 **Music** | 9 | Blockiert unterstützte Musik-/Audio-Dienste vollständig. | [Liste öffnen](lists/block-all/packages/music.txt) |
| 📺 **Streaming** | 17 | Blockiert unterstützte Video-/Streamingdienste vollständig. | [Liste öffnen](lists/block-all/packages/streaming.txt) |
| 🎮 **Gaming** | 18 | Blockiert unterstützte Gaming-Plattformen vollständig. | [Liste öffnen](lists/block-all/packages/gaming.txt) |
| 💬 **Messaging** | 8 | Blockiert unterstützte Messenger und Chat-Dienste vollständig. | [Liste öffnen](lists/block-all/packages/messaging.txt) |
| 🤖 **AI** | 0 | Blockiert unterstützte KI-Dienste vollständig. | [Liste öffnen](lists/block-all/packages/ai.txt) |
| ☁️ **Cloud** | 0 | Blockiert ausgewählte Cloud-/Hosting-Dienste vollständig. | [Liste öffnen](lists/block-all/packages/cloud.txt) |

<details>
<summary><strong>📂 Einzelne Block-All-Listen anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste anzeigen |
| --- | :---: | --- | --- |
| 🎵 **Spotify** | 7 | Blockiert Spotify App, Webplayer, Login, APIs und Streaming-Endpunkte. | [Öffnen](lists/block-all/music/spotify.txt) |
| 🎵 **Deezer** | 2 | Blockiert Deezer vollständig. | [Öffnen](lists/block-all/music/deezer.txt) |
| 📺 **Netflix** | 6 | Blockiert Netflix App, Web und Streaming-Infrastruktur. | [Öffnen](lists/block-all/streaming/netflix.txt) |
| 📺 **Disney+** | 4 | Blockiert Disney+ vollständig. | [Öffnen](lists/block-all/streaming/disney-plus.txt) |
| 📺 **Prime Video** | 3 | Blockiert Prime Video vollständig. | [Öffnen](lists/block-all/streaming/prime-video.txt) |
| 🟣 **Twitch** | 4 | Blockiert Twitch Web, App und Streaming-Infrastruktur. | [Öffnen](lists/block-all/streaming/twitch.txt) |
| 📱 **TikTok** | 4 | Blockiert TikTok vollständig. | [Öffnen](lists/block-all/social/tiktok.txt) |
| 📸 **Instagram** | 2 | Blockiert Instagram vollständig. | [Öffnen](lists/block-all/social/instagram.txt) |
| 🔵 **Facebook** | 5 | Blockiert Facebook vollständig. | [Öffnen](lists/block-all/social/facebook.txt) |
| ✖️ **X / Twitter** | 4 | Blockiert X / Twitter vollständig. | [Öffnen](lists/block-all/social/x-twitter.txt) |
| 👻 **Snapchat** | 3 | Blockiert Snapchat vollständig. | [Öffnen](lists/block-all/social/snapchat.txt) |
| 🟠 **Reddit** | 4 | Blockiert Reddit vollständig. | [Öffnen](lists/block-all/social/reddit.txt) |
| 🎮 **Steam** | 5 | Blockiert Steam Store, Client und Netzwerkdienste. | [Öffnen](lists/block-all/gaming/steam.txt) |
| 🎮 **Epic Games** | 3 | Blockiert Epic Games Store und Launcher. | [Öffnen](lists/block-all/gaming/epic-games.txt) |
| 🎮 **Battle.net** | 4 | Blockiert Battle.net und Blizzard-Onlinedienste. | [Öffnen](lists/block-all/gaming/battlenet.txt) |
| 🎮 **Riot Games** | 4 | Blockiert Riot-Launcher und unterstützte Riot-Dienste. | [Öffnen](lists/block-all/gaming/riot-games.txt) |
| 🎮 **Rockstar** | 2 | Blockiert Rockstar Launcher und Online-Dienste. | [Öffnen](lists/block-all/gaming/rockstar.txt) |
| 💬 **Discord** | 4 | Blockiert Discord App, Web, API und Medien-Endpunkte. | [Öffnen](lists/block-all/messaging/discord.txt) |
| 💬 **Telegram** | 4 | Blockiert Telegram-Dienste. | [Öffnen](lists/block-all/messaging/telegram.txt) |

</details>

---




---

## 🧰 Software & Tools blockieren

Hier werden **Programme, Clients, Plattformen oder komplette Software-Kategorien vollständig gesperrt**.

> Diese Listen sind keine Privacy-Listen. Wenn eine Software hier blockiert wird, soll sie **bewusst nicht mehr online funktionieren**.

### Fertige Software-Blockpakete

| Paket | Einträge | Funktion | Liste |
| --- | :---: | --- | --- |
| ☁️ **Cloud Clients** | 9 | Blockiert typische Cloud-Sync-Clients und deren Online-Dienste. | [Liste öffnen](lists/block-all/software/cloud-clients.txt) |
| 💻 **Development Tools** | 11 | Blockiert unterstützte Entwicklungs- und Entwicklerplattformen. | [Liste öffnen](lists/block-all/software/development-tools.txt) |
| 🎮 **Game Launcher** | 18 | Blockiert unterstützte Spiele-Launcher vollständig. | [Liste öffnen](lists/block-all/software/game-launchers.txt) |
| 🤖 **AI Tools** | 0 | Blockiert unterstützte KI-Clients und AI-Dienste. | [Liste öffnen](lists/block-all/software/ai-tools.txt) |
| 📡 **Remote Access** | 5 | Blockiert Remote-Desktop-/Fernwartungssoftware und deren Infrastruktur. | [Liste öffnen](lists/block-all/software/remote-access.txt) |
| 💬 **Communication Tools** | 6 | Blockiert unterstützte Messenger-, Chat- und Collaboration-Software. | [Liste öffnen](lists/block-all/software/communication-tools.txt) |
| 📦 **Software Stores** | 7 | Blockiert unterstützte App-/Software-Stores und Paketquellen. | [Liste öffnen](lists/block-all/software/software-stores.txt) |
| 🔄 **Auto Updater** | 0 | Blockiert Update-Infrastruktur ausgewählter Software-Produkte. | [Liste öffnen](lists/block-all/software/auto-updaters.txt) |

<details>
<summary><strong>📂 Einzelne Software- & Tool-Blocklisten anzeigen</strong></summary>

| Name | Einträge | Funktion | Liste anzeigen |
| --- | :---: | --- | --- |
| **OneDrive** | 3 | Blockiert OneDrive-Sync und zugehörige Onlinedienste. | [Öffnen](lists/block-all/software/onedrive.txt) |
| **Dropbox** | 3 | Blockiert Dropbox-Client und Cloudzugriff. | [Öffnen](lists/block-all/software/dropbox.txt) |
| **Google Drive** | 3 | Blockiert Google-Drive-Client und Cloudzugriff. | [Öffnen](lists/block-all/software/google-drive.txt) |
| **GitHub Desktop** | 3 | Blockiert GitHub-Desktop-Kommunikation. | [Öffnen](lists/block-all/software/github-desktop.txt) |
| **GitLab** | 2 | Blockiert GitLab-bezogene Client-/Service-Kommunikation. | [Öffnen](lists/block-all/software/gitlab.txt) |
| **VS Code Online Services** | 3 | Blockiert VS-Code-Onlinedienste, Marketplace und Telemetrie-Endpunkte vollständig. | [Öffnen](lists/block-all/software/vscode.txt) |
| **JetBrains** | 3 | Blockiert JetBrains-Onlinedienste und zugehörige Softwarekommunikation. | [Öffnen](lists/block-all/software/jetbrains.txt) |
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
| 🪟 **Windows** | 🟠 Local Mode – Updates erlaubt: 6<br>🔴 Full Isolation – inkl. Updates: 10 | [Liste](lists/system-blocking/windows/local-mode.txt) | [Liste](lists/system-blocking/windows/full-isolation.txt) |
| 🍎 **macOS** | 🟠 Local Mode – Updates erlaubt: 6<br>🔴 Full Isolation – inkl. Updates: 11 | [Liste](lists/system-blocking/macos/local-mode.txt) | [Liste](lists/system-blocking/macos/full-isolation.txt) |
| 🤖 **Android** | 🟠 Local Mode – Updates erlaubt: 3<br>🔴 Full Isolation – inkl. Updates: 5 | [Liste](lists/system-blocking/android/local-mode.txt) | [Liste](lists/system-blocking/android/full-isolation.txt) |
| 🍏 **iOS / iPadOS** | 🟠 Local Mode – Updates erlaubt: 6<br>🔴 Full Isolation – inkl. Updates: 11 | [Liste](lists/system-blocking/ios/local-mode.txt) | [Liste](lists/system-blocking/ios/full-isolation.txt) |
| 🐧 **Linux** | 🟠 Local Mode – Updates erlaubt: 2<br>🔴 Full Isolation – inkl. Updates: 2 | [Liste](lists/system-blocking/linux/local-mode.txt) | [Liste](lists/system-blocking/linux/full-isolation.txt) |
| 📺 **Samsung TV** | 🟠 Local Mode – Updates erlaubt: 0<br>🔴 Full Isolation – inkl. Updates: 0 | [Liste](lists/system-blocking/samsung-tv/local-mode.txt) | [Liste](lists/system-blocking/samsung-tv/full-isolation.txt) |
| 📺 **LG webOS** | 🟠 Local Mode – Updates erlaubt: 0<br>🔴 Full Isolation – inkl. Updates: 0 | [Liste](lists/system-blocking/lg-webos/local-mode.txt) | [Liste](lists/system-blocking/lg-webos/full-isolation.txt) |
| 🔥 **Fire TV** | 🟠 Local Mode – Updates erlaubt: 13<br>🔴 Full Isolation – inkl. Updates: 15 | [Liste](lists/system-blocking/fire-tv/local-mode.txt) | [Liste](lists/system-blocking/fire-tv/full-isolation.txt) |
| 📺 **Android TV / Google TV** | 🟠 Local Mode – Updates erlaubt: 6<br>🔴 Full Isolation – inkl. Updates: 9 | [Liste](lists/system-blocking/android-tv/local-mode.txt) | [Liste](lists/system-blocking/android-tv/full-isolation.txt) |
| 💾 **Synology** | 🟠 Local Mode – Updates erlaubt: 0<br>🔴 Full Isolation – inkl. Updates: 0 | [Liste](lists/system-blocking/synology/local-mode.txt) | [Liste](lists/system-blocking/synology/full-isolation.txt) |
| 💾 **QNAP** | 🟠 Local Mode – Updates erlaubt: 0<br>🔴 Full Isolation – inkl. Updates: 0 | [Liste](lists/system-blocking/qnap/local-mode.txt) | [Liste](lists/system-blocking/qnap/full-isolation.txt) |
| 💾 **TrueNAS** | 🟠 Local Mode – Updates erlaubt: 0<br>🔴 Full Isolation – inkl. Updates: 0 | [Liste](lists/system-blocking/truenas/local-mode.txt) | [Liste](lists/system-blocking/truenas/full-isolation.txt) |
| 💾 **Unraid** | 🟠 Local Mode – Updates erlaubt: 0<br>🔴 Full Isolation – inkl. Updates: 0 | [Liste](lists/system-blocking/unraid/local-mode.txt) | [Liste](lists/system-blocking/unraid/full-isolation.txt) |
| 🌐 **Router / Netzwerkgeräte** | 🟠 Local Mode – Updates erlaubt: 0<br>🔴 Full Isolation – inkl. Updates: 0 | [Liste](lists/system-blocking/network-devices/local-mode.txt) | [Liste](lists/system-blocking/network-devices/full-isolation.txt) |
| 🏠 **IoT / Smart Home** | 🟠 Local Mode – Updates erlaubt: 0<br>🔴 Full Isolation – inkl. Updates: 0 | [Liste](lists/system-blocking/iot/local-mode.txt) | [Liste](lists/system-blocking/iot/full-isolation.txt) |
| 🗣️ **Sprachassistenten** | 🟠 Local Mode – Updates erlaubt: 13<br>🔴 Full Isolation – inkl. Updates: 15 | [Liste](lists/system-blocking/voice-assistants/local-mode.txt) | [Liste](lists/system-blocking/voice-assistants/full-isolation.txt) |
| 🎮 **Konsolen** | 🟠 Local Mode – Updates erlaubt: 4<br>🔴 Full Isolation – inkl. Updates: 8 | [Liste](lists/system-blocking/consoles/local-mode.txt) | [Liste](lists/system-blocking/consoles/full-isolation.txt) |

### System-Gesamtlisten

| Gesamtgruppe | Einträge | 🟠 Local Mode | 🔴 Full Isolation |
| --- | :---: | :---: | :---: |
| 💻 **Computer / Laptop** | 🟠 Local Mode: 14<br>🔴 Full Isolation: 23 | [Liste](lists/system-blocking/groups/computer/local-mode.txt) | [Liste](lists/system-blocking/groups/computer/full-isolation.txt) |
| 📱 **Handy / Tablet** | 🟠 Local Mode: 9<br>🔴 Full Isolation: 16 | [Liste](lists/system-blocking/groups/mobile/local-mode.txt) | [Liste](lists/system-blocking/groups/mobile/full-isolation.txt) |
| 📺 **TV / Streaming-Geräte** | 🟠 Local Mode: 19<br>🔴 Full Isolation: 24 | [Liste](lists/system-blocking/groups/tv-streaming/local-mode.txt) | [Liste](lists/system-blocking/groups/tv-streaming/full-isolation.txt) |
| 💾 **NAS / Server** | 🟠 Local Mode: 0<br>🔴 Full Isolation: 0 | [Liste](lists/system-blocking/groups/nas-server/local-mode.txt) | [Liste](lists/system-blocking/groups/nas-server/full-isolation.txt) |
| 🏠 **Smart Home / IoT** | 🟠 Local Mode: 13<br>🔴 Full Isolation: 15 | [Liste](lists/system-blocking/groups/iot/local-mode.txt) | [Liste](lists/system-blocking/groups/iot/full-isolation.txt) |
| 🌐 **Netzwerkgeräte** | 🟠 Local Mode: 0<br>🔴 Full Isolation: 0 | [Liste](lists/system-blocking/groups/network/local-mode.txt) | [Liste](lists/system-blocking/groups/network/full-isolation.txt) |
| 🧩 **All Systems** | 🟠 Local Mode: 33<br>🔴 Full Isolation: 49 | **[Liste](lists/system-blocking/all-in/local-mode.txt)** | **[Liste](lists/system-blocking/all-in/full-isolation.txt)** |

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

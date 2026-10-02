# Drittquellen & Herkunft

Dieses Repository steht unter **GPL-3.0-only**. Die Listen basieren auf dem statischen BlackRabbitZ-Datenbestand und dessen dokumentierten Quellen.

## HaGeZi DNS Blocklists
- Projekt: `hagezi/dns-blocklists`
- Lizenz: GPL-3.0
- Im BlackRabbitZ-Snapshot dokumentierte HaGeZi-Anteile umfassen u. a. Native Tracking, LG webOS und Gambling.
- HaGeZi dient zusätzlich als Strukturreferenz für kumulative Hauptstufen und getrennte Native-/Hersteller-/Speziallisten.
- **Keine automatische Live-Synchronisation.**

Weitere Quellen je nach Ursprungsliste: Block List Project, AnudeepND, NextDNS Native Tracking Protection, Perflyst, URLhaus und Phishing.Database.

## Zusaetzliche Speziallisten

### HaGeZi DNS Blocklists
- Lizenz: GPL-3.0.
- In dieser Version werden kleine, klar abgegrenzte Snapshots fuer `SafeSearch not supported` und `Most Abused TLDs` mit Attribution mitgeliefert.
- `config/special-upstreams.json` enthaelt ausserdem optionale Live-Upstreams, die nur durch den manuellen Updater abgerufen werden.

### MISP Warning Lists
- Projekt: `MISP/misp-warninglists`
- Lizenz: CC0 1.0 Universal.
- Verwendet fuer den mitgelieferten Snapshot der bekannten URL-Shortener.

### Block List Project
- Lizenz: MIT (laut jeweiligem Listen-Header).
- Optionale manuelle Upstreams fuer Piracy, Ransomware und Redirect/Malicious Redirects sind im Speziallisten-Updater hinterlegt.

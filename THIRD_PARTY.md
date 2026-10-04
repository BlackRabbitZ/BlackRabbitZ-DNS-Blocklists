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

## Effect-List-Erweiterung 2026-10-03

- NextDNS `services` und `native-tracking-domains` dienten als öffentlich dokumentierte Referenz für die Trennung zwischen Service-Blocking und Native-/Device-Tracking.
- Microsoft Learn wurde für Cortana-/Live-Tile- und Windows-Update-Endpunkte herangezogen.
- AssoEchap `stalkerware-indicators` wurde für eine konservative statische Auswahl bekannter Stalkerware-/C2-Domains verwendet.
- NAV `cplt` diente als Referenz für typische Exfiltrationsdienste (Webhooks, Paste-/File-Sharing, Tunneling).
- HaGeZi-Dokumentation wurde als Referenz für Privacy-Tiers, Native Tracker und Bypass-/NRD-Semantik verwendet.
- Block List Project wurde als Referenz für Pi-hole-kompatible Kategorien und Listenpflege verwendet.
- Es wurde **keine neue automatische Fremdlisten-Synchronisation** eingebaut; die neuen Listen sind statische Snapshots bzw. aus dem vorhandenen BRZ-Bestand abgeleitet.

## Rebuilt README project (2026-10-04)

The rebuilt project uses the current BlackRabbitZ repository snapshot as the primary dataset. That snapshot already contains and documents GPL-3.0-compatible HaGeZi-derived Native Tracking, Family, Threat Intelligence, DNS/Bypass and other standalone data. New convenience/group/system lists are derived from these existing source files without removing the original attribution.


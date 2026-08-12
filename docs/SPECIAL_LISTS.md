# Erweiterte Schutz- & Speziallisten

**🌐 Sprache / Language:** 🇩🇪 **Deutsch** · [🇬🇧 English](SPECIAL_LISTS_EN.md)

BlackRabbitZ bildet die HaGeZi-Themen **7 bis 24** aus dem archivierten Repository-Stand vom **2. August 2026** ab. Die eigentlichen Blocklisten aus den Punkten 7–22 werden – soweit sie als statische Listen vorlagen – aus archivierten Rohdaten erzeugt. Die Punkte 23 und 24 sind Dokumentationsbereiche und erscheinen deshalb als **Empfehlungen** und **Online-DNS-Dienste** in der README.

Archivierte Ausgangsseite:

```text
https://web.archive.org/web/20260802022304/https://github.com/hagezi/dns-blocklists
```

## Wichtiger Archiv-Hinweis

Diese Dateien sind **keine aktuellen HaGeZi-Feeds**. Sie sind eingefrorene bzw. dem August-2026-Stand möglichst nahe Wayback-Snapshots. BlackRabbitZ:

- bewahrt Herkunft und GPL-Attribution in `THIRD_PARTY.md`,
- normalisiert Domain- und IPv4-Listen,
- entfernt exakte Treffer aus `config/allowlist.txt` aus Domainlisten,
- dedupliziert und sortiert normale Domain-/IP-Varianten,
- teilt große Ausgaben auf maximal **50 MiB pro Datei**,
- hält die Speziallisten getrennt von den täglich aktualisierten BlackRabbitZ-Upstreams.

## Enthaltene Bereiche

| Punkt | BlackRabbitZ-Bereich | Varianten / Umsetzung | Risiko |
|---:|---|---|---|
| 7 | Fake & Internet-Betrug | Voll | Mittel |
| 8 | Pop-Up-Werbung | Voll | Mittel |
| 9 | Threat Intelligence Feeds | Full, Medium, Mini, IPv4 | Mittel–Hoch |
| 10 | NRD / DGA | fünf NRD-Zeitfenster + DGA 7/14/30 Tage | Sehr hoch |
| 11 | DNS-Bypass-Schutz | Full, DoH-only, DoH-IPv4 | Hoch |
| 12 | SafeSearch nicht unterstützt | Domainliste | Hoch |
| 13 | Dynamisches DNS | Domainliste | Hoch |
| 14 | Badware-Hoster | Domainliste | Sehr hoch |
| 15 | URL-Shortener | Domainliste | Sehr hoch |
| 16 | Häufig missbrauchte TLDs | archiviertes Adblock-Format | Sehr hoch |
| 17 | DNS-Rebind-Schutz | Pi-hole-/dnsmasq-Dokumentation | Konfiguration |
| 18 | Anti-Piracy | Domainliste | Hoch |
| 19 | Glücksspiel | Full, Medium, Mini | Hoch |
| 20 | Soziale Netzwerke | Domainliste | Sehr hoch |
| 21 | NSFW | Domainliste | Hoch |
| 22 | Native Tracker | Amazon, Apple, Huawei, Microsoft, Samsung, TikTok, LG webOS, Roku, Vivo, OPPO/Realme, Xiaomi | Mittel–Hoch |
| 23 | Empfehlungen | README-Dokumentation | — |
| 24 | Online-DNS-Dienste | README-Dokumentation | — |

## Warum NRD/DGA nicht automatisch täglich gebaut wird

Die archivierten NRD-Daten sind extrem groß. Im HaGeZi-Snapshot lagen die fünf NRD-Wochenfenster jeweils bei mehreren Millionen Domains; zusätzlich gab es DGA-/Entropy-Varianten. Diese Daten können den Repository-Umfang und den Speicherbedarf eines DNS-Blockers massiv erhöhen.

Deshalb werden die archivierten Speziallisten **nicht** im normalen täglichen Upstream-Refresh heruntergeladen. Für sie gibt es einen eigenen GitHub-Action-Workflow:

```text
Actions → Update archived special lists → Run workflow
```

Wenn wirklich alle Punkt-7-bis-22-Varianten erzeugt werden sollen, muss **„Große NRD/DGA-Listen mitbauen“** aktiviert bleiben.

## Verzeichnisse

```text
lists/special/   # Domain-/Adblock-Speziallisten und 50-MiB-Parts
lists/ips/       # IPv4-Speziallisten
metadata/special-lists.json
```

Die README liest `metadata/special-lists.json` und erzeugt daraus automatisch Eintragszahlen, View-/Raw-Links und Part-Tabellen.

## Format-Hinweise

### Domainlisten

Normale Speziallisten werden als eine Domain pro Zeile veröffentlicht und können wie andere BlackRabbitZ-Listen eingebunden werden.

### IPv4-Listen

Die TIF- und DoH-IPv4-Varianten sind **keine normalen Pi-hole-Adlists**. Sie sind für Firewalls bzw. DNS-Produkte gedacht, die IP-/Netzlisten ausdrücklich unterstützen.

### Häufig missbrauchte TLDs

Die archivierte TLD-Variante wird im ursprünglichen **Adblock-Regelformat** erhalten. Sie wird nicht blind in eine reine Domainliste umgewandelt, weil TLD-Wildcards und Ausnahmen sonst semantisch verändert würden.

### DNS-Rebind-Schutz

HaGeZis damalige Rebind-Liste war auf AdGuard/AdGuard Home ausgerichtet. Pi-hole besitzt über FTL/dnsmasq eigene Rebind-Mechanismen. Für BlackRabbitZ ist Punkt 17 deshalb bewusst eine Konfigurationsdokumentation statt einer ungeeigneten statischen Adlist:

[`DNS_REBIND_PROTECTION.md`](DNS_REBIND_PROTECTION.md)

## Wartung

Die archivierten Rohquellen ändern sich nicht planmäßig. Ein erneuter Build ist sinnvoll, wenn:

- die BlackRabbitZ-Allowlist geändert wurde,
- das Split-Limit oder der Normalisierer geändert wurde,
- eine fehlende Wayback-Ressource durch einen besseren archivierten Snapshot ersetzt wird,
- erzeugte Dateien neu aufgebaut werden sollen.

Neue **aktuelle** Drittquellen sollten weiterhin über den normalen BlackRabbitZ-Upstream-Prozess bewertet werden und nicht stillschweigend als „HaGeZi aktuell“ bezeichnet werden.

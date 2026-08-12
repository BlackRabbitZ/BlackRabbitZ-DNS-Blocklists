# Erweiterte Schutz- & Funktionslisten

**🌐 Sprache / Language:** 🇩🇪 **Deutsch** · [🇬🇧 English](SPECIAL_LISTS_EN.md)

BlackRabbitZ integriert zusätzliche HaGeZi-Funktionslisten **nach Funktion** in die bestehenden BlackRabbitZ-Bereiche. Überlappende Daten werden nicht als parallele Doppel-Listen veröffentlicht. Nur Funktionen, für die BlackRabbitZ noch keine passende Liste besitzt, bleiben als eigene optionale Liste bzw. kompakte Variantengruppe sichtbar.

## Upstream-Verhalten

Die Update-Konfiguration verwendet **keine Wayback-/Archiv-Adresse als Datenquelle**. Sie versucht die ursprünglichen Live-/CDN-/Raw-Quellen des HaGeZi-Projekts direkt abzurufen.

Ist eine Quelle vorübergehend nicht erreichbar:

- wird sie nach begrenzten Wiederholungsversuchen für diesen Lauf übersprungen,
- bereits vorhandenes BlackRabbitZ-Material bleibt erhalten,
- der restliche Listen-Build läuft weiter,
- Security, Family und Ultimate können trotzdem neu gebaut und in **maximal 50 MiB große Parts** geteilt werden,
- ein späterer Workflow-Lauf versucht die ausgefallene Quelle erneut.

Originalprojekt:

```text
https://github.com/hagezi/dns-blocklists
```

## Enthaltene Bereiche

| Punkt | BlackRabbitZ-Bereich | Varianten / Umsetzung | Risiko |
|---:|---|---|---|
| 7 | Scam & Internet-Betrug | in bestehende `scam.txt` integriert | Mittel |
| 8 | Werbung | in bestehende `ads.txt` integriert | Mittel |
| 9 | Threat Intelligence Feeds | Full, Medium, Mini, IPv4 | Mittel–Hoch |
| 10 | NRD / DGA | fünf NRD-Zeitfenster + DGA 7/14/30 Tage | Sehr hoch |
| 11 | DNS-Bypass-Schutz | Full, DoH-only, DoH-IPv4 | Hoch |
| 12 | SafeSearch nicht unterstützt | Domainliste | Hoch |
| 13 | Dynamisches DNS | Domainliste | Hoch |
| 14 | Badware-Hoster | Domainliste | Sehr hoch |
| 15 | URL-Shortener | Domainliste | Sehr hoch |
| 16 | Häufig missbrauchte TLDs | Adblock-Format | Sehr hoch |
| 17 | DNS-Rebind-Schutz | Pi-hole-/dnsmasq-Dokumentation | Konfiguration |
| 18 | Anti-Piracy | Domainliste | Hoch |
| 19 | Glücksspiel | Full in `gambling.txt`; Medium/Mini optional | Hoch |
| 20 | Soziale Netzwerke | Domainliste | Sehr hoch |
| 21 | Erwachsene Inhalte / NSFW | in bestehende `adult.txt` integriert | Hoch |
| 22 | Native Tracker | in Apple-/Windows-/Android-/Smart-TV-/IoT-/Mobile-Tracking-Listen integriert | Mittel–Hoch |
| 23 | Empfehlungen | README-Dokumentation | — |
| 24 | Online-DNS-Dienste | README-Dokumentation | — |

## Verzeichnisse

```text
lists/categories/   # bestehende Kategorien + funktional neue optionale Listen/Parts
lists/ips/          # optionale IPv4-Varianten
metadata/special-lists.json
```

Die README liest `metadata/special-lists.json` und erzeugt daraus automatisch Eintragszahlen, Anzeigen-/Raw-Links und Part-Tabellen.

## Wartung

Die Quell-URLs werden zentral in `config/special-lists.json` gepflegt. Temporäre Upstream-Ausfälle sind **nicht fatal** und stoppen den normalen BlackRabbitZ-Build nicht.

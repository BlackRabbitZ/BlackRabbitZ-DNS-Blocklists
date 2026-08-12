# Drittanbieter-Material

**🌐 Sprache / Language:** 🇩🇪 **Deutsch** · [🇬🇧 English](THIRD_PARTY_EN.md)

Dieses Repository enthält neben BlackRabbitZ-eigenen Einträgen zusammengeführte und deduplizierte Domain-Indikatoren aus Blocklisten- und Threat-Intelligence-Projekten Dritter.

Maßgeblich bleiben die jeweiligen Upstream-Projekte. Deren Daten können sich häufiger ändern als die hier commiteten Snapshots. Copyright, Datenbankrechte, Marken und Lizenzbedingungen verbleiben bei den jeweiligen Upstream-Rechteinhabern.

## Importierte / abgeleitete Quellen

- **The Block List Project** — Daten zu Werbung, Tracking, Malware, Ransomware, Phishing, Scam, Fraud, Pornografie, Glücksspiel und Smart-TV. Das Upstream-Repository weist aktuell die Unlicense als Projektlizenz aus; auch erzeugte Listen-Header des heruntergeladenen Snapshots enthalten Upstream-Lizenzmetadaten. Bei Weiterverbreitung müssen die Upstream-Hinweise erhalten bleiben.
  - https://github.com/blocklistproject/Lists
- **Phishing.Database** — aktive Phishing-Domains. Upstream unter MIT-Lizenz.
  - https://github.com/Phishing-Database/Phishing.Database
- **AnudeepND blacklist** — Quellen für Werbung/Tracking und CoinMiner. Upstream unter MIT-Lizenz.
  - https://github.com/anudeepND/blacklist
- **NextDNS native-tracking-domains / click-tracking-domains** — natives Plattform-/Geräte-Tracking sowie Affiliate-/Klick-Tracking-Domains. Das Native-Tracking-Repository ist upstreamseitig MIT-lizenziert.
  - https://github.com/nextdns/native-tracking-domains
  - https://github.com/nextdns/click-tracking-domains
- **Perflyst PiHoleBlocklist** — Android-, Smart-TV- und Amazon-Fire-TV-Tracking-/Telemetriequellen. Upstream unter MIT-Lizenz.
  - https://github.com/Perflyst/PiHoleBlocklist
- **HaGeZi DNS Blocklists** — zusätzliche archivierte Quellen für Werbung, Betrugs-/Security-Schutz, DNS-Bypass, Familienfilter und geräte-/dienstespezifisches Native Tracking. Überlappende Daten werden funktional in vorhandene BlackRabbitZ-Kategorien integriert; Upstream-GPL-/Lizenzhinweise und Namensnennung bleiben erhalten.
  - https://github.com/hagezi/dns-blocklists
- **StevenBlack/hosts** — reine Pornografie-Erweiterung für die Adult-Kategorie. Upstream unter MIT-Lizenz.
  - https://github.com/StevenBlack/hosts
- **NoCoin** — Domains für Browser-Kryptomining. Upstream unter MIT-Lizenz.
  - https://github.com/hoshsadiq/adblock-nocoin-list
- **DurableNapkin Scam Blocklist** — Scam-Indikatoren; Upstream unter MIT-Lizenz.
  - https://github.com/durablenapkin/scamblocklist
- **URLhaus (abuse.ch / Spamhaus)** — aktive Hosts zur Malware-Verteilung.
  - https://urlhaus.abuse.ch/
  - https://urlhaus.abuse.ch/downloads/hostfile/
- **BaFin** — kuratierte öffentliche Verbraucherwarnungen, die aus der bisherigen Scam-Liste übernommen werden.
  - https://www.bafin.de/DE/verbraucherinnen-verbraucher/news-warnungen/news-warnungen_node.html
- **Verbraucherzentrale / Fakeshop-Finder** — kuratierte öffentliche Fake-Shop-Warnungen, die aus der bisherigen Fake-Shops-Liste übernommen werden.
  - https://www.verbraucherzentrale.de/fakeshopfinder-71560
- **Herstellerdokumentation** (Canonical/Debian, Synology/TrueNAS/QNAP, Red Hat, Dell, HPE) — kleine Telemetrie-Endpunkt-Sammlungen für Linux-, NAS- und Server-Kategorien.


## Archivierte Upstream-Daten für erweiterte Funktionslisten

BlackRabbitZ kann zusätzlich die im Wayback-Snapshot vom **2. August 2026** dokumentierten HaGeZi-Listen importieren und **nach Funktion in die bestehenden BlackRabbitZ-Bereiche einsortieren**. Die ursprünglichen Listen wurden unter GPL-3.0 veröffentlicht. Zur reproduzierbaren Übernahme dieses dokumentierten Stands nutzt BlackRabbitZ **archivierte Raw-Captures** und kennzeichnet sie klar als Drittquelle. Dadurch hängen die daraus erzeugten Listen nicht davon ab, ob sich das Live-Repository später ändert oder zeitweise nicht erreichbar ist.

- Archivierte Repository-Seite: `https://web.archive.org/web/20260802022304/https://github.com/hagezi/dns-blocklists`
- Originalprojekt: `https://github.com/hagezi/dns-blocklists`
- Build-Konfiguration: `config/special-lists.json`
- Funktional einsortierte Domainlisten: `lists/categories/`
- Erzeugte IPv4-Listen: `lists/ips/`
- Maschinenlesbare Herkunft/Prüfsummen: `metadata/special-lists.json`

Die Konfiguration verweist auf die jeweiligen archivierten Raw-Captures. Bei einzelnen Dateien führt der Link des 2.-August-Snapshots zur nächst verfügbaren Wayback-Capture derselben Datei. BlackRabbitZ normalisiert Domain-/IP-Varianten und teilt große Ausgaben auf; Adblock-spezifische Syntax wird nur dort unverändert erhalten, wo sie für die Funktion der Liste notwendig ist (z. B. TLD-Regeln).

## Abgeleitete Teilmengen

Einige Kategorien werden über kategoriespezifische Filter aus breiteren Upstream-Datensätzen abgeleitet:

- `telemetry.txt` — Telemetrie-/Analyse-/Metrik-/Diagnose-Teilmenge aus Tracking-Daten.
- `social-trackers.txt` — Tracking-Teilmenge sozialer Plattformen.
- `mobile-tracking.txt` — Teilmenge mobiler Analyse-/Attribution-SDKs plus Android-Tracking-Daten.
- `affiliate-tracking.txt` — Affiliate-/Klick-/Referral-Teilmenge plus NextDNS-Klick-Tracking-Daten.
- `consent-cmp.txt` — Consent-Management-/CMP-Teilmenge.
- `fake-shops.txt` — nach Einzelhandel/Shops aussehende Teilmenge aus Scam-/Fraud-Intelligence plus kuratierte Fake-Shop-Warnungen.

Abgeleitete Kategorien sind bewusst aggressiv. Die Aufnahme einer Domain in eine abgeleitete Kategorie ist eine Blocking-Klassifizierung und keine rechtliche Feststellung über den Domaininhaber.

## Weiterverbreitung

BlackRabbitZ-eigenes Material bleibt unter `GPL-3.0-only`. Drittanbieter-Material unterliegt weiterhin den jeweils geltenden Upstream-Lizenzen und Hinweisen. Bei der Weiterverbreitung wesentlicher Teile eines Upstream-Datensatzes müssen die dort erforderlichen Copyright-, Genehmigungs- und Namensnennungshinweise erhalten bleiben; die verlinkte Upstream-Lizenz ist die maßgebliche Fassung.

### Änderungsvermerk HaGeZi-abgeleiteter Daten

Stand **12. August 2026**: Von HaGeZi übernommenes Material wird von BlackRabbitZ normalisiert, dedupliziert, bei Bedarf mit der globalen Allowlist gefiltert und funktional neu kategorisiert. Überlappende Quellen werden in bestehende BlackRabbitZ-Listen integriert; nur eigenständige Funktionen bleiben als separate optionale Ausgabe erhalten. Große eigenständige Ausgaben werden in bis zu 50-MiB-Parts geteilt. Die Herkunft bleibt in den Datei-Headern bzw. in dieser Drittanbieter-Dokumentation erhalten.

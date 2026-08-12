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
- **HaGeZi DNS Blocklists** — Quellen für Apple Native Tracking, LG webOS und Glücksspiel. Upstream-GPL-/Lizenzhinweise und Namensnennung müssen erhalten bleiben.
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

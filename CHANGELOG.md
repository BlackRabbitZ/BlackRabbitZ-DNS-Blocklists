# Änderungsverlauf

**🌐 Sprache / Language:** 🇩🇪 **Deutsch** · [🇬🇧 English](CHANGELOG_EN.md)

## 3.1.0 - 2026-08-12

- Deutsche README als Standard eingeführt und eine separate englische `README_EN.md` ergänzt.
- Sprachumschalter am Anfang beider README-Dateien ergänzt.
- Inhaltsverzeichnis mit stabilen Abschnittsankern hinzugefügt.
- **Optionale Schutzmodule** und **Große Profil-Teile** direkt unter dem **Schutzvergleich** einsortiert.
- `scripts/update-readme.py` auf zweisprachige README-Synchronisierung erweitert.
- `config/readme-i18n.json` als zentrale Sprachkonfiguration für automatisch erzeugte README-Bereiche ergänzt.
- Deutsche und englische Versionen der wichtigsten Wartungsdokumentation ergänzt.
- GitHub-Issue-Formulare zweisprachig beschriftet.

## 3.0.0 - 2026-08-12

- Die nur für Ultimate vorhandene Split-Logik wurde durch einen generischen, von `config/profiles.json` gesteuerten Profil-Publisher ersetzt.
- Deterministische 5-MiB-`*-part-NN.txt`-Ausgaben für Security, Family und Ultimate ergänzt.
- Ultimate-Parts von `ultimate-N.txt` auf nullgefüllte `ultimate-part-NN.txt`-Dateinamen umgestellt.
- Die zuvor einzelnen Security- und Family-Dateien in größenbegrenzte Parts aufgeteilt.
- Affiliate Tracking aus Balanced entfernt und in Strict/Ultimate belassen, um vermeidbare Referral-/Link-Fehlfunktionen im empfohlenen Profil zu reduzieren.
- Consent/CMP aus Ultimate entfernt und als explizite optionale Kategorie belassen, weil DNS-basiertes CMP-Blocking ein erhöhtes Website-Fehlfunktionsrisiko besitzt.
- Security und Family in der README als optionale Schutzmodule statt als fortlaufende Datenschutzstufen positioniert.
- `metadata/build.json` mit maschinenlesbaren Profil-/Kategorie-Zahlen, Part-Informationen, Größen und SHA-256-Hashes ergänzt.
- Erzeugung von `metadata/SHA256SUMS` hinzugefügt.
- Validierung der erzeugten Profile auf globale Sortierung, Duplikate, Part-Größenlimits und Metadatenkonsistenz ergänzt.
- `.gitattributes`-Regeln für generierte kombinierte Profile und Metadaten hinzugefügt.
- Strukturierte GitHub-Issue-Formulare für False Positives, Domain-Vorschläge und neue Upstream-Quellen ergänzt.
- Dokumentation zu Beiträgen und automatischen Updates erweitert.

### Migrationshinweis

Der erste v3-Neuaufbau entfernt die bisherigen erzeugten URLs `lists/combined/security.txt`, `lists/combined/family.txt` und `lists/combined/ultimate-N.txt`. Bestehende Abonnements müssen durch **alle** neuen `*-part-NN.txt`-Raw-URLs ersetzt werden, die in der README angezeigt werden.

## 2.1.1 - 2026-08-12

- Die einzelne große `lists/combined/ultimate.txt` wurde durch automatisch erzeugte `ultimate-N.txt`-Parts ersetzt.
- `scripts/split-ultimate.py` mit einem Ziel-Limit von 40 MiB pro Ultimate-Part ergänzt.
- Automatische README-Erzeugung für Ultimate-Part-Anzahl, Größen sowie View-/Raw-Links ergänzt.
- Der Blocklist-Workflow wurde erweitert, sodass Änderungen an Split-Generator-Skripten einen Neuaufbau auslösen.
- Alte/verwaiste Ultimate-Part-Dateien werden vor jeder Neuerzeugung automatisch entfernt.

## 2.1.0 - 2026-08-12

- Täglichen Upstream-Refresh per GitHub Actions hinzugefügt.
- `scripts/update-upstreams.py` für additive automatische Domain-Importe ergänzt.
- `scripts/upstream-sources.json` mit quellenbezogenen Upstreams und Sicherheitsgrenzen hinzugefügt.
- Download-Wiederholungen, Mindestgrößenprüfung, Domain-Normalisierung, Deduplizierung und Growth Guards ergänzt.
- `config/allowlist.txt` für kritische Ausschlüsse bei automatischen Imports hinzugefügt.
- `docs/AUTOMATIC_UPDATES.md` mit Wartungs- und Fail-Safe-Dokumentation ergänzt.
- Workflow-Concurrency vereinheitlicht und Bash-Ausführung unabhängig von ausführbaren Dateirechten gehalten.

## 2.0.2 - 2026-08-11

- Beschreibungen zur Family-Lists-Tabelle in der README ergänzt.
- Malware-, Phishing-, Scam- und Fake-Shops-Sicherheitskategorien mit kuratierten, extern verifizierten Indikatoren befüllt.
- Quellenhinweise zu Sicherheits-Kategoriedateien und `THIRD_PARTY.md` ergänzt.
- Security- und Ultimate-Profile neu gebaut und alle Eintragszahlen synchronisiert.

## 2.0.1 - 2026-08-11

- Die umfangreichere README-Darstellung im Stil von v1.3 wiederhergestellt.
- Zentriertes Projekt-Branding und stärkere visuelle Hierarchie ergänzt.
- Schutzvergleichsmatrix und gruppierte Kategorien wiederhergestellt.
- Alle statischen v2.0.0-Listen und Domainzahlen unverändert beibehalten.

## 2.0.0 - 2026-08-11

- Große Erweiterung der statisch kuratierten Datenschutz-/Werbe-/Telemetrielisten.
- 128 Werbe-Endpunkte ergänzt.
- 136 Tracking-/Analyse-Endpunkte ergänzt.
- Eigene Kategorien für Social-, Mobile-, Native-App-, Affiliate- und CMP-Tracking hinzugefügt.
- Windows-, Apple-, Android-, Smart-TV- und IoT-Telemetrie erweitert.
- Kombinierte Profile als direkte statische Dateien aktualisiert.
- Das Repository blieb script- und Python-frei.
- Security-Threat-Kategorien blieben bewusst konservativ und importierten keine Live-Feeds von Drittanbietern.

## 1.3.0 - 2026-08-11

- README und Darstellung der statischen Listen neu gestaltet.

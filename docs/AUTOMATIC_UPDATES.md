# Automatische Updates – sichere Upstream-Architektur

Dieses Repository verwendet ab dieser korrigierten Version **keinen rein additiven Import mehr**.

## Warum wurde die alte Logik ersetzt?

Der frühere Updater schrieb neue Domains direkt in `lists/categories/*.txt` und verwendete anschließend die Vereinigungsmenge aus vorhandenem Inhalt und neuen Treffern. Dadurch blieben einmal falsch einsortierte oder später aus einer Fremdquelle entfernte Domains dauerhaft in der Kategorie.

Zusätzlich konnten breite Keyword-Regeln wie `firebase`, `events.`, `stats.` oder `collector.` funktionale Endpunkte erwischen.

## Neue Datenstruktur

```text
sources/manual/            manuell gepflegte BlackRabbitZ-Basis
sources/upstream/<cat>/    letzter erfolgreicher Snapshot je einzelner Fremdquelle
review/quarantine/         zurückgestellte Kandidaten mit Begründung
lists/categories/          generierte Kategorie-Listen
lists/combined/            generierte Profile
```

### Manuelle Einträge

Manuell gepflegte Domains gehören nach `sources/manual/<kategorie>.txt`.

`lists/categories/*.txt` sind generierte Ausgaben und sollen nicht mehr als primäre Datenquelle editiert werden.

### Upstream-Cache pro Quelle

Jede konfigurierte Fremdquelle erhält eine eigene Cache-Datei. Bei einem erfolgreichen Abruf wird **nur dieser Source-Cache vollständig ersetzt**.

Das bedeutet:

- neue Domain in der Quelle → kann hinzugefügt werden;
- Domain aus der Quelle entfernt → verschwindet beim nächsten erfolgreichen Refresh wieder aus diesem Cache;
- Quelle nicht erreichbar → letzter guter Cache bleibt erhalten;
- ungewöhnlich großer Zuwachs oder Einbruch → Guard stoppt den automatischen Vorschlag.

## Schutz vor Fehlklassifizierungen

Privacy- und Device-Listen werden vor dem Import gegen zwei Schutzebenen geprüft:

1. `config/allowlist.txt`
2. `config/critical-services.txt`

Zusätzlich werden verdächtige funktionale Kandidaten über `config/functional-guard-tokens.txt` erkannt. Dazu zählen z. B. Update-, Firmware-, Login-, Auth-, Push- und Zertifikatsendpunkte.

Solche Kandidaten werden **nicht automatisch blockiert**, sondern nach `review/quarantine/<kategorie>.tsv` geschrieben.

Diese funktionale Heuristik wird bewusst **nicht** pauschal auf Malware-/Phishing-/Scam-Listen angewendet, weil echte Schad-Domains Wörter wie `login`, `auth` oder `update` enthalten können.

## Modulare Kategorien

`scripts/build-categories.py` hält breite Listen bewusst weniger restriktiv:

- `trackers.txt` enthält keine Domains, die bereits in spezialisierten Telemetrie-, Device-, Mobile-, Social-, Affiliate- oder CMP-Listen liegen;
- `telemetry.txt` enthält keine Domains, die bereits in Device-/Mobile-/Smart-TV-Telemetrie liegen.

Dadurch kann z. B. `Balanced` allgemeines Tracking blockieren, ohne automatisch alle Betriebssystem-/Geräte-Telemetrie mitzunehmen.

## Workflows

### `daily-upstream-update.yml`

Der tägliche Workflow:

1. prüft die Konfiguration;
2. lädt Fremdquellen;
3. ersetzt erfolgreiche Source-Caches;
4. behält bei Fehlern den letzten guten Cache;
5. schreibt unsichere Kandidaten in die Quarantäne;
6. baut Kategorien und kombinierte Profile neu;
7. validiert das Repository;
8. erstellt bzw. aktualisiert einen **Pull Request**.

Er pusht automatische Fremdquellen-Änderungen nicht mehr direkt auf `main`.

### `update-lists.yml`

Dieser Workflow ist nur noch ein Validator. Er schreibt nichts in das Repository und besitzt lediglich Leserechte.

Er prüft, ob die committed generierten Listen exakt zu `sources/`, Konfiguration und Build-Skripten passen.

## Lokaler Build

```bash
python3 scripts/build-categories.py
bash scripts/update-lists.sh
python3 scripts/validate-repository.py
```

## Einmalige Bereinigung

Die mitgelieferte Version wurde bereits mit folgendem Befehl bereinigt:

```bash
python3 scripts/reclassify-existing.py --apply
```

Das Skript entfernt geschützte funktionale Endpunkte aus Privacy-/Device-Kategorien und trennt breite Tracker-/Telemetry-Listen von den vorhandenen Speziallisten.

Ein Bericht liegt unter:

```text
metadata/cleanup-report.json
```

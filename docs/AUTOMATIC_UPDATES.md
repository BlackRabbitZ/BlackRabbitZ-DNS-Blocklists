# Automatische Upstream-Updates

**🌐 Sprache / Language:** 🇩🇪 **Deutsch** · [🇬🇧 English](AUTOMATIC_UPDATES_EN.md)

BlackRabbitZ aktualisiert ausgewählte Kategorielisten und erzeugt die veröffentlichten Profile automatisch mit GitHub Actions neu.

## Workflows

- `.github/workflows/daily-upstream-update.yml` läuft täglich um **03:17 UTC** und kann zusätzlich manuell gestartet werden.
- `.github/workflows/update-lists.yml` hält kombinierte Profile, gesplittete Teile, Metadaten, Prüfsummen und beide README-Dateien nach Kategorie-, Profilkonfigurations- oder Build-Skript-Änderungen synchron.

## Ablauf des täglichen Updates

1. `scripts/update-upstreams.py` liest `scripts/upstream-sources.json`.
2. Upstream-Feeds werden per HTTPS mit Wiederholungen, Timeouts und maximaler Downloadgröße geladen.
3. Hosts-, Plain-Domain-, URL-, AdGuard/ABP- und Wildcard-Einträge werden auf eine Domain pro Zeile normalisiert.
4. Ungültige Werte, IP-Adressen, Duplikate und Domains aus `config/allowlist.txt` werden ignoriert.
5. Neue Domains werden **additiv** in bestehende Kategoriedateien übernommen. Vorhandene Einträge werden vom automatischen Importer nie still gelöscht.
6. Mindestgrößen pro Quelle verwerfen verdächtig leere Downloads.
7. Wachstumsschutz pro Kategorie blockiert unplausibel große Zuwächse innerhalb eines Laufs.
8. `scripts/update-lists.sh` liest `config/profiles.json`, führt die benötigten Kategorien zusammen und sortiert/dedupliziert jedes kombinierte Profil.
9. `scripts/publish-profile.py` veröffentlicht Light/Balanced/Strict als Einzeldateien und große konfigurierte Profile als deterministische, größenbegrenzte Teile.
10. `scripts/generate-metadata.py` erstellt `metadata/build.json` und `metadata/SHA256SUMS`.
11. `scripts/update-readme.py` synchronisiert **README.md (Deutsch)** und **README_EN.md (Englisch)** einschließlich Profiltabellen, Part-Links, Vergleichsdaten und Kategorie-Zahlen.
12. `scripts/validate-generated.py` prüft Sortierung, Eindeutigkeit, Part-Größen und Metadatenkonsistenz der erzeugten Profile.
13. Wenn sich das Repository geändert hat und alle Prüfungen erfolgreich waren, committet GitHub Actions das Ergebnis nach `main`.

## Profilkonfiguration

`config/profiles.json` ist die zentrale Quelle für:

- die Kategorien jedes kombinierten Profils;
- die Einordnung als Haupt-Datenschutzprofil oder optionales Modul;
- die Veröffentlichung als nummerierte Teile;
- die maximale Größe erzeugter Parts;
- technische Anzeige-Metadaten und Breakage-Indikatoren;
- die Schutzvergleichsmatrix.

`config/readme-i18n.json` enthält die sprachabhängigen Texte für die automatisch erzeugten Bereiche der deutschen und englischen README.

### Aktuelle Profilpolitik

- **Light**: nur Werbung.
- **Balanced**: Werbung + allgemeine Tracker + Social Tracker. Affiliate-/Referral-Blocking ist bewusst ausgeschlossen, um vermeidbare Fehlfunktionen zu reduzieren.
- **Strict**: ergänzt Affiliate Tracking, allgemeine Telemetrie, Plattform-/Geräte-Telemetrie und natives/App-Tracking.
- **Security**: Sicherheits-Add-on mit Malware, Phishing, Scam, Fake Shops und Cryptomining.
- **Family**: Familien-Add-on mit Werbung/Tracking sowie Adult- und Gambling-Filterung.
- **Ultimate**: aggressiver All-in-one-Schutz. Consent/CMP bleibt bewusst separat, weil DNS-basiertes CMP-Blocking Website-Consent-Abläufe und Seitenfunktionen beeinträchtigen kann.

## Aufteilung großer Profile

Profile mit `"split": true` werden immer als nummerierte Teile veröffentlicht. Dadurch ändern sich URLs nicht ständig, wenn eine Liste zeitweise wächst oder schrumpft.

Aktuell gesplittete Profile:

- `security-part-01.txt`, `security-part-02.txt`, ...
- `family-part-01.txt`, `family-part-02.txt`, ...
- `ultimate-part-01.txt`, `ultimate-part-02.txt`, ...

Jeder erzeugte Part zielt auf maximal **50 MiB** (`52428800` Bytes einschließlich Header). Die Nummerierung ist mit führender Null versehen, damit die Dateireihenfolge auch bei mehr als neun Teilen stabil bleibt.

Für vollständige Abdeckung müssen DNS-Blocker **alle in der README angezeigten Teile** des jeweiligen Profils abonnieren.

### Migration vom alten Schema

Das v3-Schema ersetzt:

- `lists/combined/security.txt`
- `lists/combined/family.txt`
- `lists/combined/ultimate-1.txt`, `ultimate-2.txt`, ...

mit größenbegrenzten `*-part-NN.txt`-Dateien. Bestehende Pi-hole-Abonnements mit alten URLs müssen nach dem ersten v3-Neuaufbau durch alle neuen Raw-URLs aus der README ersetzt werden.

## Generierte Metadaten und Prüfsummen

`metadata/build.json` enthält maschinenlesbare Informationen zu jeder Kategorie und jedem kombinierten Profil, darunter:

- Eintragszahl;
- Dateinamen;
- Anzahl der Parts;
- Dateigröße;
- SHA-256-Hash;
- enthaltene Kategorien.

`metadata/SHA256SUMS` enthält eine standardisierte Prüfsummenliste für alle Kategorie- und kombinierten Profil-Dateien.

Beide Dateien sind deterministisch: Ein Neuaufbau unveränderter Eingaben soll keinen reinen Zeitstempel-Diff erzeugen.

## Aus Upstreams aktualisierte Kategorien

Die Quellenmatrix deckt derzeit Ads, Trackers, abgeleitete Telemetrie-Kategorien, Windows-/Apple-/Android-Telemetrie, Native Tracking, Smart TV, IoT, Cryptomining, Malware, Phishing, Scam, Fake Shops, Adult und Gambling ab.

`gaming-telemetry.txt`, `gaming-telemetry-aggressive.txt`, `linux-telemetry.txt`, `nas-telemetry.txt` und `server-telemetry.txt` können manuell kuratiert bleiben, wenn keine einzelne vertrauenswürdige allgemeine Upstream-Quelle diese spezialisierten Endpunkte sauber abbildet.

## Sicherheitsverhalten

Die Import-/Build-Pipeline ist auf sicheres Fehlschlagen ausgelegt:

- Ist eine Upstream-Quelle nicht erreichbar, bleibt die zuletzt commitete Kategorie erhalten.
- Fallen alle Quellen einer Kategorie aus, bleibt diese Kategorie unverändert.
- Liefert ein Feed plötzlich deutlich weniger Einträge als das konfigurierte Minimum, wird er verworfen.
- Überschreiten neue Imports das konfigurierte Wachstumslimit eines Laufs, beendet sich der Workflow vor jedem Commit.
- Fehlende Kategoriedateien, die von einem Profil referenziert werden, führen zum Build-Abbruch.
- Gesplittete Teile oberhalb des konfigurierten Größenlimits führen zu einem Validierungsfehler.
- Duplikate oder falsche Sortierung über erzeugte Profilteile hinweg führen zu einem Validierungsfehler.
- Abweichende Eintragszahlen in den Metadaten führen zu einem Validierungsfehler.
- Reguläre Git-Dateien oberhalb des GitHub-Hard-Limits von 100 MiB führen vor dem Commit zum Build-Abbruch.

## Upstream hinzufügen oder entfernen

Bearbeite:

```text
scripts/upstream-sources.json
```

Jede Quelle besitzt einen Namen, eine HTTPS-URL und `min_entries`. Optional kann `include_keywords` verwendet werden, um aus einem breiteren Feed eine engere Kategorie abzuleiten.

Nach einer Konfigurationsänderung:

```bash
python3 scripts/update-upstreams.py --check-config
python3 scripts/update-upstreams.py --dry-run
bash scripts/update-lists.sh
```

## Profil ändern

Bearbeite:

```text
config/profiles.json
```

Sprachabhängige README-Texte befinden sich in:

```text
config/readme-i18n.json
```

Bearbeite Dateien unter `lists/combined/`, `metadata/build.json` oder `metadata/SHA256SUMS` nicht manuell; sie werden erzeugt.

Danach:

```bash
bash scripts/update-lists.sh
```

## Allowlist gegen False Positives

Kritische Domains werden hier eingetragen:

```text
config/allowlist.txt
```

Eine allowgelistete Domain und ihre Subdomains werden von **neuen automatischen Imports** ausgeschlossen. Bereits vorhandene Kategorie-Einträge werden nicht still gelöscht.

## GitHub-Repository-Einstellung

Die Workflows benötigen Schreibrechte, um erzeugte Änderungen zu pushen. In GitHub müssen die Actions-Workflow-Berechtigungen Schreibzugriff auf Repository-Inhalte erlauben. Branch-Protection-Regeln müssen dem Workflow/Bot ebenfalls erlauben, `main` zu aktualisieren.

## Android-Guard beim ersten Import

`android-telemetry` erlaubt bewusst ein größeres Wachstum beim ersten Lauf als der globale Standard, weil konfigurierte Huawei-/Xiaomi-/Oppo-Realme-/Vivo-Native-Tracking-Quellen auf einmal mehr als 1.000 gültige Domains hinzufügen können. Die Kategorie bleibt trotzdem durch ihren konfigurierten Growth Guard geschützt.

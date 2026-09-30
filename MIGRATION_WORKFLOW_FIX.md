# Migration auf den korrigierten Workflow

## Empfohlener Ablauf

1. Vorhandenes Repository sichern.
2. Die Dateien dieser korrigierten Version in einen Test-Branch übernehmen.
3. `python3 scripts/validate-repository.py` ausführen.
4. `python3 scripts/build-categories.py` ausführen.
5. `bash scripts/update-lists.sh` ausführen.
6. Änderungen an `lists/categories/` und `lists/combined/` prüfen.
7. Erst danach den Branch nach `main` mergen.

## Wichtige Änderung

Ab dieser Version werden manuelle Domains unter `sources/manual/` gepflegt.

Nicht mehr direkt pflegen:

```text
lists/categories/*.txt
```

Stattdessen:

```text
sources/manual/*.txt
```

Die Kategorie-Dateien werden aus der manuellen Basis und den getrennten Upstream-Caches erzeugt.

## Erster automatischer Lauf

Beim ersten Lauf sind `sources/upstream/`-Caches leer. Der Workflow lädt die konfigurierten Quellen und erstellt je Quelle einen eigenen Snapshot. Die bereits bereinigte manuelle Basis bleibt erhalten. Doppelte Domains werden beim Build automatisch dedupliziert.

## Sicherheit

Automatische Upstream-Änderungen landen in einem Pull Request und nicht mehr direkt in `main`.

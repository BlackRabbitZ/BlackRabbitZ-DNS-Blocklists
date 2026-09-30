# BlackRabbitZ DNS Blocklists – Pipeline Hotfix v2.0.4

Dieser Hotfix behebt genau den Fehler aus dem GitHub-Actions-Log:

`AssertionError: update-upstreams.py must not build public categories before classification`

## Was wird geändert?

Nur `scripts/update-upstreams.py`:

Der veraltete direkte Aufruf von `build-categories.py` am Ende des Upstream-Downloaders wird entfernt.

Danach ist die Pipeline:

1. `update-upstreams.py` → lädt Fremdlisten nur in `sources/upstream/`
2. `classify-upstreams.py` → sortiert Domains in `sources/classified/`
3. `validate-classifier.py`
4. `build-categories.py` → erzeugt deine vorhandenen öffentlichen Listen aus `manual + classified`

Deine vorhandenen Listen und manuellen Domains werden durch diesen Hotfix nicht ersetzt oder gelöscht.

## Windows

ZIP in den Root des Repositories entpacken und dort ausführen:

```powershell
powershell -ExecutionPolicy Bypass -File .\APPLY_FIX.ps1
```

## Linux/macOS

```bash
python3 APPLY_FIX.py
```

Das Script erstellt vor einer Änderung automatisch:
`scripts/update-upstreams.py.bak`

Danach zeigt es den Pipeline-Vertragstest an.

# BlackRabbitZ – Workflow-Konsolidierung auf 10 Workflows

## Zielstruktur

1. `Daily upstream refresh` – täglicher Import + neue NXDOMAINs abweisen
2. `DNS maintenance` – DNS-Health + mehrfach bestätigte tote Domains bereinigen
3. `Issue & PR automation` – Issue-Triage + PR-Zusammenfassung
4. `Quality & statistics` – Statistiken + Qualitätsbericht
5. `CI & Security` – Security Scan + Permissions Audit + Reproducible Build
6. `Update blocklists` – zentraler Build mit Allowlist-Defense-in-Depth
7. `Update extended lists` – manueller Heavy-/Archiv-Build
8. `Upstream monitoring` – Erreichbarkeit + Größen-/Anomalieprüfung
9. `Validate repository` – v3-Validator + neuer Domain-DNS-Check bei PRs
10. `Weekly release` – wöchentliche Releases bei Änderungen

`Actions cleanup` wird bewusst entfernt. Die GitHub-Retention-Einstellungen reichen für den aktuellen Projektumfang.

## Installation

1. Inhalt dieses Pakets in das Root deines bestehenden Repositories kopieren und vorhandene Dateien überschreiben.
2. Im Repository-Root ausführen: `bash ./install-consolidated-workflows.sh`
3. `git status` kontrollieren. Es müssen die alten Workflow-Dateien als gelöscht und die neuen/angepassten Dateien als geändert erscheinen.
4. Committen und auf `main` pushen.

## Wichtig zum alten Validator-Run

Ein GitHub-Button **Re-run jobs** startet denselben alten Commit erneut. Starte nach der Migration einen **neuen** manuellen Lauf von `Validate repository`, damit die v3-Datei verwendet wird.

## Allowlist

Das Paket enthält zusätzlich die bereits vorbereitete Defense-in-Depth-Version von `scripts/update-lists.sh` und `scripts/apply-allowlist.py`. Dadurch wird die Allowlist beim Kategorie-Build und unmittelbar vor Veröffentlichung der Combined-Profile erneut angewendet.

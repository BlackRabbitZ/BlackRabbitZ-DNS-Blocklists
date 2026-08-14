# Workflow-Übersicht

| Nr. | Workflow | Aufgabe |
|---:|---|---|
| 1 | `validate.yml` | Prüft JSON, Python-/Shell-Syntax, Domainformat, Sortierung, Duplikate, Allowlist-Kollisionen, Header und erzeugte Profile. |
| 2 | `dns-health-check.yml` | Prüft wöchentlich eine rotierende Stichprobe bestehender Domains und führt NXDOMAIN-Kandidaten weiter. |
| 3 | `new-domain-check.yml` | Prüft neu hinzukommende PR-Domains über zwei Resolver; bestätigtes NXDOMAIN lässt den PR-Check fehlschlagen. Zusätzlich in den Daily-Upstream-Workflow integriert. |
| 4 | `issue-triage.yml` | Legt Triage-Labels an und kommentiert/schließt Issues automatisch anhand dieser Labels. |
| 5 | `release.yml` | Erstellt wöchentlich nur bei neuen Commits einen datumsbasierten GitHub-Release samt SHA256SUMS. |
| 6 | `quality-report.yml` | Erstellt `QUALITY.md` und `metadata/quality.json` mit Qualitätskennzahlen. |
| 7 | `security-scan.yml` | Prüft Python-Kompilierung, ShellCheck, definierte Hochrisiko-Muster und Workflow-Berechtigungen. |
| 8 | `cleanup.yml` | Löscht monatlich alte abgeschlossene Workflow-Runs älter als 30 Tage und behält mindestens 15 pro Workflow. Manuelle Läufe sind standardmäßig Dry-run. |
| 9 | `list-statistics.yml` | Erzeugt stabile Statistiken für Kategorie- und kombinierte Listen. |
| 10 | `reproducible-build.yml` | Baut dieselben Quellen zweimal unabhängig und vergleicht die veröffentlichten kombinierten Listen bytegenau. |
| 11 | `upstream-health.yml` | Prüft täglich Erreichbarkeit, HTTP-Status und Größeninformationen der konfigurierten Upstream-Quellen. |
| 12 | `upstream-change-alert.yml` | Vergleicht Upstream-Größen mit einer gesunden Baseline und schlägt bei starken Einbrüchen, extremem Wachstum oder Nichterreichbarkeit fehl. |
| 13 | `pr-summary.yml` | Erstellt/aktualisiert automatisch eine PR-Zusammenfassung, ohne untrusted PR-Code auszuführen. |
| 14 | `dead-domain-cleanup.yml` | Entfernt erst mehrfach bestätigte tote Domains nach einer zusätzlichen finalen DNS-Gegenprüfung und baut anschließend Profile/Metadaten neu. |
| 15 | `permissions-audit.yml` | Prüft alle Workflows auf explizite minimale Berechtigungen, `write-all` und gefährliche `pull_request_target`/Checkout-Kombinationen. |

## Zusätzlich geändert

- `.github/workflows/daily-upstream-update.yml` – enthält jetzt den DNS-Check für neue Upstream-Domains.

## Unterstützende Skripte

Alle neuen Hilfsprogramme liegen unter `scripts/automation/` und verwenden für DNS-Abfragen das auf GitHub-Hosted-Ubuntu vorhandene `dig`.

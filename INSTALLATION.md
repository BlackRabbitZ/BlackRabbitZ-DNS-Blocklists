# BlackRabbitZ DNS Blocklists – Automation Pack

Dieses Paket ist als **Overlay für das bestehende Repository** `BlackRabbitZ/BlackRabbitZ-DNS-Blocklists` gebaut.

## Installation

1. Repository lokal klonen oder als ZIP von GitHub laden.
2. Inhalt dieses Pakets in das **Root-Verzeichnis** des Repositorys kopieren.
3. Beim Kopieren `.github/workflows/daily-upstream-update.yml` ersetzen.
4. Die bestehenden Workflows `update-lists.yml` und `update-special-lists.yml` **nicht löschen**.
5. Änderungen committen und pushen.

## Empfohlene erste manuelle Läufe

1. `Workflow permissions audit`
2. `Validate repository`
3. `Issue triage` einmal manuell starten, damit die benötigten Labels angelegt werden.
4. `Upstream change alert` einmal starten, damit `metadata/upstream-baseline.json` erzeugt wird.
5. `DNS health check` einmal starten.
6. `Dead domain cleanup` beim ersten Test mit `dry_run = true` ausführen.

## Wichtige Sicherheitsregeln

- Neue Domains werden nur dann als nicht existent eingestuft, wenn **Cloudflare (1.1.1.1) und Google (8.8.8.8) beide NXDOMAIN** liefern.
- `SERVFAIL`, `TIMEOUT`, `REFUSED` und andere unklare DNS-Zustände führen nicht zum automatischen Löschen.
- Bereits vorhandene Domains müssen mindestens **drei getrennte DNS-Health-Checks** als NXDOMAIN überstehen und werden vor dem Entfernen nochmals final geprüft.
- Der tägliche Upstream-Import stoppt absichtlich, wenn mehr als 25.000 neue Domains in einem Lauf DNS-geprüft werden müssten. So werden öffentliche Resolver nicht mit unkontrollierten Massenabfragen belastet.

## Neu erzeugte Metadaten

Die Workflows können folgende Dateien erzeugen:

- `metadata/dns-health.json`
- `metadata/dns-health-state.json`
- `metadata/quality.json`
- `metadata/statistics.json`
- `metadata/upstream-baseline.json`
- `QUALITY.md`
- `STATISTICS.md`

## Bestehender Daily-Workflow

`daily-upstream-update.yml` wurde erweitert. Nach `update-upstreams.py` läuft jetzt die neue DNS-Prüfung für ausschließlich neu hinzugefügte Domains. Bestätigte NXDOMAINs werden noch vor dem Profil-Build wieder aus der betroffenen Kategorie entfernt.

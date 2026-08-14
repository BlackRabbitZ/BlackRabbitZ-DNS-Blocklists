# BlackRabbitZ Allowlist Defense-in-Depth

## Ersetzen/Hinzufügen

Kopiere diese Dateien in das Root deines bestehenden Repositories:

- `scripts/apply-allowlist.py` **neu**
- `scripts/update-lists.sh` **ersetzen**
- `.github/workflows/update-lists.yml` **ersetzen**

## Danach

Committe die drei Dateien auf `main`.

`Update blocklists` wird automatisch ausgelöst, weil der Workflow auf diese Pfade reagiert.
Alternativ: **Actions → Update blocklists → Run workflow**.

Beim Lauf passiert automatisch:

1. Die Allowlist wird auf **alle Kategorie-Domainlisten** angewendet.
2. Aktuelle Konflikte wie `collector.github.com` und `collector-cdn.github.com`
   werden aus den betroffenen Kategorien entfernt.
3. Die `# Entries:`-Header werden danach neu berechnet.
4. Combined-Profile werden neu gebaut.
5. Direkt vor jeder Veröffentlichung wird die Allowlist **noch einmal** auf das
   temporäre Combined-Profil angewendet.
6. Metadaten, Prüfsummen und READMEs werden wie bisher regeneriert.

Die vorhandene Import-Sperre in `update-upstreams.py` bleibt die erste Schutzschicht.

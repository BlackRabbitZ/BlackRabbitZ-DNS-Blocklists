# BlackRabbitZ Validator v3 – Korrektur

Ersetze nur:

`scripts/automation/validate_repository.py`

Dein bestehendes `.github/workflows/validate.yml` kann unverändert bleiben.

## Korrigiert

- Erkennt Adblock-/AdGuard-Dateien automatisch (`[Adblock Plus]`, `! Syntax: AdBlock`, `||host^`).
- `||actor^`, `||co.com^` usw. werden nicht mehr fälschlich als normale Domains validiert.
- TLD-Regeln mit nur einem Label sind im Adblock-Modus zulässig.
- `[Adblock Plus]` und `!`-Metadaten werden nicht als Domainfehler gewertet.
- `# Entries:` wird exakt nach der bestehenden `count_entries()`-Semantik des Repositories geprüft:
  eindeutige, nicht-leere Zeilen, die nicht mit `#` beginnen.
- Die Prüfung bricht nach 50 gemeldeten Fehlerdetails NICHT mehr ab. Dadurch entstehen keine falschen
  Header-Fehler durch einen vorzeitigen Abbruch.
- Duplikate werden weiterhin vollständig gezählt.
- Allowlist-Kollisionen bleiben echte Fehler/Hinweise und werden nicht unterdrückt.

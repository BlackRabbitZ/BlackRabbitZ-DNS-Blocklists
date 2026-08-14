# Installation

Ersetze in deinem Repository genau diese beiden Dateien:

- `.github/workflows/validate.yml`
- `scripts/automation/validate_repository.py`

Danach unter **Actions → Validate repository → Run workflow** den Scope **all** auswählen.

Der Validator prüft:
- `lists/categories/`: Domain-Syntax, Duplikate (auch unsortierte), Sortierung, Allowlist, Entries-Header
- `lists/combined/`: Domain-Syntax, Duplikate, Sortierung, Allowlist, Entries-Header
- `lists/ips/`: IPv4/IPv6-Syntax, Duplikate, Sortierung, Entries-Header
- `lists/regex/`: RegEx/PCRE-Syntax, Duplikate, Entries-Header
- JSON-Konfiguration und bestehende generierte Profil-Metadaten

Wichtig: Überschneidungen zwischen unterschiedlichen Kategorie-Dateien werden nicht als Fehler behandelt,
weil eine Domain fachlich in mehreren Kategorien vorkommen kann. Duplikate innerhalb einer Datei werden
hingegen sicher erkannt.

# Kids Allow-Only

1. Pi-hole-Gruppe `Kids-AllowOnly` anlegen.
2. `kids-de.txt` als abonnierte Allowlist nur dieser Gruppe zuweisen.
3. Regex-Denylist `.*` nur dieser Gruppe zuweisen.
4. Listen aktualisieren und testen.
5. Fehlende, eindeutig notwendige Hosts im Query Log prüfen und in `kids-runtime-de.txt` dokumentieren.

`.*` niemals versehentlich auf die Default-Gruppe anwenden.

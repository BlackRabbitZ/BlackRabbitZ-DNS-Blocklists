# Migration auf v3.3.2

Diese Version ordnet die erweiterten Listen **nach Funktion** in die bestehenden BlackRabbitZ-Bereiche ein. Die README trennt sie nicht mehr nach ihrer Herkunft.

Beim ersten Workflow-Lauf nach dem Upgrade passiert automatisch:

1. Alte source-präfixierte Dateien unter `lists/special/hagezi-*.txt` und `lists/ips/hagezi-*.txt` werden entfernt.
2. Die erweiterten Listen werden unter neutralen BlackRabbitZ-Funktionsnamen in `lists/categories/` bzw. `lists/ips/` neu erzeugt.
3. Große Security-, Family-, Ultimate-, NRD-/DGA- und andere erweiterte Listen werden mit maximal **50 MiB pro Part** veröffentlicht.
4. `README.md` und `README_EN.md` erhalten die aktuellen Eintragszahlen, Raw-Links und gegebenenfalls Part-Tabellen.
5. Die HaGeZi-Herkunft bleibt in den generierten Datei-Headern sowie in `THIRD_PARTY.md`/`ATTRIBUTION.md` dokumentiert.

## Wichtig

Nach dem Push den Workflow **Update blocklists** vollständig durchlaufen lassen und anschließend in GitHub Desktop **Fetch origin** ausführen, bevor weitere lokale Änderungen vorgenommen werden.

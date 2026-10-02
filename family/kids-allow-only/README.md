# Kids Allow-Only

Dieses Modell ist **keine normale Blockliste**. Fuer eine eigene Pi-hole-Gruppe wird standardmaessig alles blockiert (`.*`) und anschliessend werden nur bewusst freigegebene Domains erlaubt.

1. Eigene Pi-hole-Gruppe fuer Kindergeraete anlegen.
2. `block-all.regex` nur dieser Gruppe zuweisen.
3. Domains aus `approved-sites.txt` als Allowlist fuer diese Gruppe eintragen.
4. Benötigte CDN-/Login-Domains pro Seite testen und gezielt ergaenzen.

> Nicht ungeprueft auf das gesamte Heimnetz anwenden.

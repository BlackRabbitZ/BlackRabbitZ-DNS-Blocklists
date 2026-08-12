# Migration auf v3.3.3

Diese Version behebt zwei Punkte der vorherigen Integration:

1. **Profil-Parts werden wirklich mit bis zu 50 MiB neu gebaut.** Vor dem Build werden alte 5-MiB-Parts von Security, Family und Ultimate gelöscht. Die Validierung erkennt anschließend verbliebene Legacy-Parts.
2. **Überlappende Spezialquellen erzeugen keine parallelen Listen mehr.** Stattdessen werden sie nach Funktion in vorhandene BlackRabbitZ-Kategorien integriert und dedupliziert.

## Automatische Zuordnung

| Zusatzquelle | Ziel in BlackRabbitZ |
|---|---|
| Fake / Internet-Betrug | `scam.txt` |
| Pop-Up-Werbung | `ads.txt` |
| Gambling Full | `gambling.txt` |
| NSFW | `adult.txt` |
| Apple Native Tracker | `apple-telemetry.txt` |
| Microsoft/Windows/Office Native Tracker | `windows-telemetry.txt` |
| Huawei, Samsung, Vivo, OPPO/Realme, Xiaomi | `android-telemetry.txt` |
| TikTok Native Tracker | `mobile-tracking.txt` |
| LG webOS, Roku | `smart-tv.txt` |
| Amazon | `iot.txt` |

Threat Intelligence, NRD/DGA, DNS-Bypass, Dynamic DNS, Badware-Hoster, URL-Kürzer, TLD-Regeln, SafeSearch, Anti-Piracy und Social-Network-Blocking bleiben als eigene optionale Funktionen erhalten, weil dafür keine gleichwertige bestehende BlackRabbitZ-Kategorie existiert.

## Erster Lauf

Nach dem Commit startet **Update blocklists** automatisch. Der Workflow:

1. migriert bereits erzeugte parallele Dateien in die passenden Zielkategorien oder lädt die archivierte Quelle, falls nur ein Platzhalter existiert,
2. entfernt die alten parallelen Ausgaben erst nach erfolgreicher Integration,
3. löscht alte 5-MiB-Profilparts,
4. baut Security, Family und Ultimate mit maximal 50 MiB pro Part neu,
5. erzeugt Metadaten, Checksums sowie deutsche und englische README neu.

Nach dem Bot-Commit in GitHub Desktop einmal **Fetch origin** ausführen, bevor du lokal weiterarbeitest.

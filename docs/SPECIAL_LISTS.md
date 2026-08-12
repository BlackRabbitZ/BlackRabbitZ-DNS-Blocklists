# Erweiterte Schutz- & Funktionslisten

**🌐 Sprache / Language:** 🇩🇪 **Deutsch** · [🇬🇧 English](SPECIAL_LISTS_EN.md)

BlackRabbitZ erweitert seine bestehenden Kategorien mit ausgewählten HaGeZi-DNS-Blocklisten. Die Daten werden **nach Funktion zusammengeführt**: Existiert bereits eine passende BlackRabbitZ-Liste, werden die zusätzlichen Domains dort integriert, normalisiert, dedupliziert und durch die zentrale Allowlist gefiltert. Nur wirklich neue Funktionen bleiben als eigene optionale Liste bzw. Variantengruppe erhalten.

## Primäre Quelle

Für die DNS-Blocklisten wird der von HaGeZi bereitgestellte GitLab-Mirror verwendet:

```text
https://gitlab.com/hagezi/mirror/-/tree/main/dns-blocklists
```

Die eigentlichen Downloads erfolgen über die Raw-Dateien unter:

```text
https://gitlab.com/hagezi/mirror/-/raw/main/dns-blocklists/
```

Originalprojekt / Lizenzreferenz:

```text
https://github.com/hagezi/dns-blocklists
```

## Verhalten bei Ausfällen

Ist der GitLab-Mirror vorübergehend nicht erreichbar:

- wird die betroffene Quelle nach begrenzten Wiederholungsversuchen für diesen Lauf übersprungen,
- bereits vorhandenes BlackRabbitZ-Material bleibt erhalten,
- der restliche Build läuft weiter,
- Security, Family und Ultimate werden weiterhin erzeugt,
- große Profile werden mit **maximal 50 MiB pro Part** geteilt,
- ein späterer Workflow-Lauf versucht die Quelle erneut.

## Funktionale Zusammenführung

| HaGeZi-Funktion | BlackRabbitZ-Ziel |
|---|---|
| Fake / Internet-Betrug | bestehende `scam.txt` |
| Pop-Up Ads | bestehende `ads.txt` |
| Gambling Full | bestehende `gambling.txt` |
| NSFW | bestehende `adult.txt` |
| Native Apple | bestehende `apple-telemetry.txt` |
| Native Windows / Office | bestehende `windows-telemetry.txt` |
| Native Huawei / Samsung / Vivo / OPPO / Realme / Xiaomi | bestehende `android-telemetry.txt` |
| Native TikTok | bestehende `mobile-tracking.txt` |
| Native LG webOS / Roku | bestehende `smart-tv.txt` |
| Native Amazon | bestehende `iot.txt` |

Eigenständig bleiben nur Funktionen, für die BlackRabbitZ keine passende bestehende Kategorie besitzt, z. B. Threat Intelligence, Dynamic DNS, Badware-Hoster, DNS-Bypass, SafeSearch, Anti-Piracy, Social-Network-Blocking oder URL-Shortener.

## NRD / DGA

NRD/DGA gehört bei HaGeZi zu einem **separaten `nrd`-Repository** und liegt nicht im von dir angegebenen `dns-blocklists`-Pfad des GitLab-Mirrors. Diese Quellen bleiben deshalb separat konfiguriert. Fällt auch diese Quelle aus, greift derselbe Skip-/Fallback-Mechanismus.

## Wartung

Alle Quell-URLs liegen zentral in `config/special-lists.json`. Die erzeugten Listen und Metadaten werden anschließend wie bisher vom BlackRabbitZ-Build verarbeitet.

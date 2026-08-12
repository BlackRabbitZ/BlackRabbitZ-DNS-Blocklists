# Mitwirken

**🌐 Sprache / Language:** 🇩🇪 **Deutsch** · [🇬🇧 English](CONTRIBUTING_EN.md)

Beiträge sind willkommen, wenn sie die Qualität, Abdeckung, Dokumentation oder Build-Sicherheit der Listen verbessern.

## Domain-Vorschläge

Nutze das Issue-Template **Domain request** und gib Folgendes an:

- die exakte Domain;
- die vorgeschlagene Kategorie;
- eine klare technische Begründung;
- nach Möglichkeit unabhängige Nachweise.

Kopiere keine vollständig gepflegten Drittanbieter-Blocklisten massenhaft in dieses Repository. Neue Upstream-Feeds sollten separat vorgeschlagen werden, damit Wartungsqualität, Format sowie Lizenz-/Nutzungsbedingungen geprüft werden können.

## Fehlblockierungen / False Positives

Nutze das Issue-Template **False positive** und nenne die betroffene Domain, die BlackRabbitZ-Liste bzw. das Profil, Anwendung/Gerät, die genaue Fehlfunktion und Reproduktionsschritte.

False-Positive-Meldungen haben Vorrang vor bloßem Listenwachstum. Ziel des Projekts ist eine nützliche Filterung, nicht die größtmögliche Anzahl an Domains.

## Upstream-Quellen

Nutze das Issue-Template **Upstream source**. Ein vorgeschlagener Feed sollte Folgendes bieten:

- eine stabile HTTPS-URL;
- klar erkennbare Pflege/Verantwortung;
- geeignete Lizenz- bzw. Nutzungsbedingungen;
- ein Format, das validiert und normalisiert werden kann;
- eine eindeutige Zuordnung zu einer vorhandenen BlackRabbitZ-Kategorie.

## Generierte Dateien

Bearbeite folgende Dateien nicht manuell:

- `lists/combined/*`
- `metadata/build.json`
- `metadata/SHA256SUMS`

Kombinierte Profile und Metadaten werden aus den Kategoriedateien sowie `config/profiles.json` durch `scripts/update-lists.sh` erzeugt.

## Lokale Validierung

Führe vor einem Pull Request mit Build-/Konfigurationsänderungen Folgendes aus:

```bash
python3 scripts/update-upstreams.py --check-config
python3 -m json.tool config/profiles.json >/dev/null
python3 -m json.tool config/readme-i18n.json >/dev/null
bash scripts/update-lists.sh
git diff --check
```

Generierte Änderungen sollten gemeinsam mit der Quell-/Konfigurationsänderung committed werden, durch die sie entstanden sind.

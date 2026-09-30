# Was wurde verbessert?

- Kein Tier-Modell: bestehende BRZ-Kategorien bleiben unverändert.
- Fremdquelle ist nur noch **Evidenz**, nicht automatisch das endgültige Ziel.
- Hersteller-/Plattformhinweise für Microsoft/Windows, Apple, Android-Hersteller, Smart-TV, IoT, NAS und Gaming.
- Funktionshinweise für Telemetrie, Social Tracking, Mobile SDK Tracking, Affiliate, CMP und Ads.
- Critical/functional Endpoints werden vor der Privacy-Klassifikation abgefangen.
- Confidence + Margin verhindern unsichere automatische Zuordnung.
- Eine Privacy-Domain bekommt nur eine kanonische Kategorie.
- Security/Family bleiben unabhängig und dürfen sich fachlich überschneiden.
- Re-Klassifizierung ist deterministisch: bessere Regeln verschieben Domains beim nächsten Build automatisch.
- Vollständige Nachvollziehbarkeit über `metadata/domain-classification.csv`.
- Quarantäne über `review/classifier-quarantine.tsv`.
- Manueller Altbestand wird separat auditiert und nicht still verändert.


## v2.0.1 Hotfix
- `classifier-validation.yml` ruft nun den vorhandenen kanonischen Builder `scripts/build-categories.py` auf.
- `scripts/build-categories-classified.py` wurde als Kompatibilitäts-Wrapper ergänzt.
- Workflow-/Script-Verweise wurden gegengeprüft.

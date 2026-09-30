# BlackRabbitZ Domain Classifier Fix v2.0

Dieser Fix erweitert das bestehende `BlackRabbitZ-DNS-Blocklists`-Repository **ohne Tier-System**. Die vorhandenen öffentlichen Kategorien und Raw-URLs bleiben bestehen.

## Was sich ändert

1. `sources/upstream/` bleibt der unveränderte Last-Good-Cache der Fremdquellen.
2. `scripts/classify-upstreams.py` bewertet jede Privacy-/Device-Domain einzeln.
3. Privacy-Domains erhalten genau **eine kanonische Kategorie**.
4. Security-/Family-Kategorien behalten ihre eigene Semantik und werden nicht zwangsweise dedupliziert.
5. Unsichere oder funktionale/critical Kandidaten landen in `review/classifier-quarantine.tsv`.
6. `metadata/domain-classification.csv` dokumentiert Entscheidung, Confidence und Ursprung.
7. `sources/classified/` ist die neue Build-Zwischenstufe.
8. `build-categories-classified.py` erzeugt die bisherigen `lists/categories/*.txt` aus `sources/manual/ + sources/classified/`.

## Einbau

ZIP in den Root des Repositories entpacken. Danach lokal:

```bash
python3 tests/test_classifier.py
python3 scripts/classify-upstreams.py
python3 scripts/validate-classifier.py
python3 scripts/build-categories-classified.py
python3 scripts/validate-repository.py
python3 scripts/audit-manual-classification.py
```

**Wichtig:** `audit-manual-classification.py` verändert deine manuellen Listen nicht. Es erzeugt nur einen Review-Bericht.

## Daily Workflow

Im bestehenden `daily-upstream-update.yml` müssen nach `update-upstreams.py` diese Schritte vor dem Build ergänzt werden:

```yaml
- name: Classify upstream domains
  run: python3 ./scripts/classify-upstreams.py

- name: Validate classifier output
  run: python3 ./scripts/validate-classifier.py
```

Und beim Kategorien-Build statt `build-categories.py`:

```bash
python3 ./scripts/build-categories-classified.py
```

Der zusätzliche `classifier-validation.yml` prüft den Classifier außerdem bei Push/PR.

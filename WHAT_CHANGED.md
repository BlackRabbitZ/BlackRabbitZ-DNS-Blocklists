# BlackRabbitZ DNS Blocklists – Classifier Pipeline Fix v2.0.3

Ziel: Fremdlisten werden **nicht** direkt in öffentliche Kategorien übernommen.

Fester Ablauf:

1. `scripts/update-upstreams.py` lädt/aktualisiert nur `sources/upstream/` (Raw-/Last-Good-Caches).
2. `scripts/classify-upstreams.py` bewertet die Domains und schreibt `sources/classified/<deine-kategorie>/...`.
3. `scripts/validate-classifier.py` prüft die Klassifizierung.
4. `scripts/build-categories.py` baut `lists/categories/*.txt` ausschließlich aus `sources/manual/` + `sources/classified/`.
5. Profile/Metadaten werden danach aktualisiert.

## Behobener Pipeline-Fehler

Der bisherige `update-upstreams.py` startete am Ende selbst `build-categories.py`. Damit wurde vor dem Classifier gebaut. Dieser Aufruf wird durch `scripts/patch-classified-pipeline.py` entfernt.

## Schutz gegen Regression

`tests/test_pipeline_contract.py` bricht CI ab, wenn:
- der Updater wieder öffentliche Listen baut,
- der Builder wieder direkt aus `sources/upstream/` liest,
- die Workflow-Reihenfolge nicht `Updater -> Classifier -> Validate -> Builder` ist.

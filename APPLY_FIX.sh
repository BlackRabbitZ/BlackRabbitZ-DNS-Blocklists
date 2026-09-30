#!/usr/bin/env bash
set -euo pipefail
for p in scripts/upstream-sources.json scripts/update-upstreams.py sources/manual sources/upstream lists/categories; do [[ -e "$p" ]] || { echo "Nicht im Repository-Root oder Pfad fehlt: $p" >&2; exit 2; }; done
python3 ./scripts/patch-classified-pipeline.py
python3 ./tests/test_pipeline_contract.py
python3 ./tests/test_classifier.py
python3 ./scripts/classify-upstreams.py
python3 ./scripts/validate-classifier.py
python3 ./scripts/build-categories.py
python3 ./scripts/validate-repository.py
echo 'Pipeline korrigiert: Fremdlisten -> raw cache -> classifier -> vorhandene Kategorien.'
echo 'Danach git status und git diff prüfen.'

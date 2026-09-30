#!/usr/bin/env bash
set -euo pipefail
for p in scripts/upstream-sources.json sources/manual sources/upstream lists/categories; do [[ -e "$p" ]] || { echo "Nicht im Repository-Root oder Pfad fehlt: $p" >&2; exit 2; }; done
python3 ./tests/test_classifier.py
python3 ./scripts/classify-upstreams.py
python3 ./scripts/validate-classifier.py
python3 ./scripts/build-categories.py
python3 ./scripts/validate-repository.py
echo 'Classifier eingebaut und Listen lokal neu gebaut.'
echo 'Optional: python3 ./scripts/audit-manual-classification.py'
echo 'Danach unbedingt git status und git diff prüfen.'

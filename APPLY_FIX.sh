#!/usr/bin/env bash
set -euo pipefail

test -d .git || { echo "Bitte im ROOT deines Git-Repositories ausführen."; exit 1; }
test -f scripts/update-upstreams.py
test -f tests/test_pipeline_contract.py

needle='subprocess.run([sys.executable, str(ROOT / "scripts" / "build-categories.py")], check=True)'

if grep -Fq "$needle" scripts/update-upstreams.py; then
  git apply --check ./FIX.patch
  git apply ./FIX.patch
fi

if grep -Fq "$needle" scripts/update-upstreams.py; then
  echo "VERIFIKATION FEHLGESCHLAGEN"
  exit 1
fi

python3 tests/test_pipeline_contract.py

echo
echo "FIX OK - Pipeline contract OK"
echo
echo "Jetzt committen und pushen:"
echo "git add scripts/update-upstreams.py"
echo 'git commit -m "Fix upstream classifier pipeline order"'
echo "git push"

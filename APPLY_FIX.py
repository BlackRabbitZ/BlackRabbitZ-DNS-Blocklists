#!/usr/bin/env python3
from pathlib import Path
import re
import shutil
import subprocess
import sys

root = Path.cwd()
target = root / "scripts" / "update-upstreams.py"
test = root / "tests" / "test_pipeline_contract.py"

if not target.exists():
    raise SystemExit("Nicht im Repository-Root ausgeführt: scripts/update-upstreams.py wurde nicht gefunden.")

text = target.read_text(encoding="utf-8")
original = text

pattern = re.compile(
    r'(?ms)^\s*if not args\.dry_run:\s*\n'
    r'\s*subprocess\.run\(\[sys\.executable,\s*str\(ROOT / "scripts" / "build-categories\.py"\)\],\s*check=True\)\s*\n'
)
text = pattern.sub("", text)

if text == original:
    if "subprocess.run" in text and "build-categories.py" in text:
        raise SystemExit("Alter Builder-Aufruf gefunden, aber Muster passt nicht. Datei wurde NICHT verändert.")
    print("Der vorzeitige Builder-Aufruf ist bereits entfernt.")
else:
    shutil.copy2(target, target.with_suffix(target.suffix + ".bak"))
    target.write_text(text, encoding="utf-8", newline="\n")
    print("Fix angewendet: vorzeitiger build-categories.py-Aufruf entfernt.")
    print("Backup: scripts/update-upstreams.py.bak")

text = target.read_text(encoding="utf-8")
if "subprocess." not in text:
    text = re.sub(r"(?m)^import subprocess\n", "", text)
    target.write_text(text, encoding="utf-8", newline="\n")

check = target.read_text(encoding="utf-8")
if "subprocess.run" in check and "build-categories.py" in check:
    raise SystemExit("Fix fehlgeschlagen: update-upstreams.py ruft build-categories.py weiterhin direkt auf.")

print("\nErwartete Pipeline:")
print("  update-upstreams.py -> classify-upstreams.py -> validate-classifier.py -> build-categories.py")

if test.exists():
    print("\nFühre Pipeline-Vertragstest aus...")
    subprocess.run([sys.executable, str(test)], check=True)

print("\nHOTFIX OK.")
print("Jetzt prüfen:")
print("  git diff -- scripts/update-upstreams.py")
print("  git status")

#!/usr/bin/env python3
from pathlib import Path
import shutil
import subprocess
import sys

target = Path("scripts/update-upstreams.py")
if not target.exists():
    raise SystemExit("Falscher Ordner: scripts/update-upstreams.py wurde nicht gefunden.")

text = target.read_text(encoding="utf-8")
old = """    if not args.dry_run:
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build-categories.py")], check=True)

"""

if old in text:
    shutil.copy2(target, target.with_suffix(target.suffix + ".bak"))
    text = text.replace(old, "")
    if "subprocess." not in text:
        text = text.replace("import subprocess\n", "")
    target.write_text(text, encoding="utf-8", newline="\n")
    print("update-upstreams.py wurde korrigiert.")
    print("Backup: scripts/update-upstreams.py.bak")
elif "subprocess.run" not in text or "build-categories.py" not in text:
    print("Der vorzeitige Builder-Aufruf ist bereits entfernt.")
else:
    raise SystemExit("Bekannter Aufruf gefunden, aber nicht im erwarteten Format. Nichts gespeichert.")

verify = target.read_text(encoding="utf-8")
if "subprocess.run" in verify and "build-categories.py" in verify:
    raise SystemExit("VERIFIKATION FEHLGESCHLAGEN: Builder-Aufruf weiterhin vorhanden.")

subprocess.run([sys.executable, "tests/test_pipeline_contract.py"], check=True)
print("OK: Pipeline-Contract bestanden.")

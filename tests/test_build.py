import subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_validate():
    subprocess.run([sys.executable,str(ROOT/"scripts/validate.py")],check=True)
def test_build():
    subprocess.run([sys.executable,str(ROOT/"scripts/build.py")],check=True)
    assert (ROOT/"dist/balanced.txt").exists()
def test_no_third_party_blocklist_imports_in_data():
    # Source datasets must be maintained locally and must not contain imported URLs.
    text="\n".join(p.read_text(encoding="utf-8",errors="ignore") for p in (ROOT/"data").rglob("*.txt"))
    assert "raw.githubusercontent.com/" not in text.lower()
    assert "http://" not in text.lower()
    assert "https://" not in text.lower()

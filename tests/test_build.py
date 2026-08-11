import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def test_validate():
    subprocess.run([sys.executable,str(ROOT/"scripts/validate.py")],check=True)

def test_build():
    subprocess.run([sys.executable,str(ROOT/"scripts/build.py")],check=True)
    cfg=json.loads((ROOT/"config.json").read_text(encoding="utf-8"))
    for profile in cfg["profiles"]:
        assert (ROOT/f"dist/{profile}.txt").exists()
        assert (ROOT/f"dist/{profile}-hosts.txt").exists()

def test_readme_links_cover_profiles():
    cfg=json.loads((ROOT/"config.json").read_text(encoding="utf-8"))
    readme=(ROOT/"README.md").read_text(encoding="utf-8")
    for profile in cfg["profiles"]:
        assert f"/dist/{profile}.txt" in readme

def test_no_hagezi_imports():
    forbidden=("raw.githubusercontent.com/hagezi","github.com/hagezi/dns-blocklists/raw")
    for p in ROOT.rglob("*"):
        if not p.is_file() or ".git" in p.parts:
            continue
        try:
            text=p.read_text(encoding="utf-8",errors="strict").lower()
        except (UnicodeDecodeError,OSError):
            continue
        for token in forbidden:
            assert token not in text

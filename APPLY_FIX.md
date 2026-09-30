# Anwenden

ZIP in den Root des aktuellen Repositories entpacken und die enthaltenen Dateien übernehmen.

Danach im Repository-Root:

Windows PowerShell:
```powershell
.\APPLY_FIX.ps1
```

Linux/macOS:
```bash
./APPLY_FIX.sh
```

Der Patch verändert `scripts/update-upstreams.py` gezielt in der aktuell vorhandenen Repo-Version, statt eine ältere komplette Datei darüberzukopieren.

$ErrorActionPreference = "Stop"

if (-not (Test-Path ".git")) {
    throw "Bitte im ROOT des Git-Repositories ausführen."
}
if (-not (Test-Path "scripts\update-upstreams.py")) {
    throw "scripts\update-upstreams.py fehlt."
}
if (-not (Test-Path "tests\test_pipeline_contract.py")) {
    throw "tests\test_pipeline_contract.py fehlt."
}

Write-Host "1/3 Patch gegen den aktuellen Repo-Stand prüfen..." -ForegroundColor Cyan
git apply --check ".\FIX.patch"
if ($LASTEXITCODE -ne 0) {
    throw "Der Patch passt nicht exakt. Es wurde NICHTS verändert."
}

Write-Host "2/3 Patch anwenden..." -ForegroundColor Cyan
git apply ".\FIX.patch"
if ($LASTEXITCODE -ne 0) {
    throw "git apply ist fehlgeschlagen."
}

$content = Get-Content "scripts\update-upstreams.py" -Raw -Encoding UTF8
if (($content -match 'subprocess\.run') -and ($content -match 'build-categories\.py')) {
    throw "Verifikation fehlgeschlagen: vorzeitiger Builder-Aufruf ist noch vorhanden."
}

Write-Host "3/3 Exakten Pipeline-Contract ausführen..." -ForegroundColor Cyan
python tests/test_pipeline_contract.py
if ($LASTEXITCODE -ne 0) {
    throw "Pipeline-Contract ist weiterhin fehlgeschlagen."
}

Write-Host ""
Write-Host "OK: Pipeline contract OK" -ForegroundColor Green
Write-Host ""
Write-Host "Jetzt committen und pushen:"
Write-Host "  git add scripts/update-upstreams.py"
Write-Host '  git commit -m "Fix upstream classifier pipeline"'
Write-Host "  git push"

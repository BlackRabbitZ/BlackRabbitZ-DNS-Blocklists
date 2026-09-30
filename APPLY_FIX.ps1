$ErrorActionPreference = "Stop"

if (-not (Test-Path ".git")) {
    throw "Bitte im ROOT deines Git-Repositories ausführen."
}

$target = "scripts\update-upstreams.py"
$test = "tests\test_pipeline_contract.py"

if (-not (Test-Path $target)) { throw "$target fehlt." }
if (-not (Test-Path $test)) { throw "$test fehlt." }

Write-Host "1/4 Prüfe aktuellen Fehlerblock..." -ForegroundColor Cyan
$before = Get-Content $target -Raw -Encoding UTF8
$needle = 'subprocess.run([sys.executable, str(ROOT / "scripts" / "build-categories.py")], check=True)'

if (-not $before.Contains($needle)) {
    Write-Host "Der fehlerhafte Aufruf ist bereits nicht mehr vorhanden." -ForegroundColor Yellow
} else {
    Write-Host "2/4 Prüfe Patch gegen deinen Repo-Stand..." -ForegroundColor Cyan
    git apply --check ".\FIX.patch"
    if ($LASTEXITCODE -ne 0) {
        throw "Patch passt nicht exakt. Es wurde NICHTS verändert."
    }

    Write-Host "3/4 Wende Patch an..." -ForegroundColor Cyan
    git apply ".\FIX.patch"
    if ($LASTEXITCODE -ne 0) {
        throw "Patch konnte nicht angewendet werden."
    }
}

$after = Get-Content $target -Raw -Encoding UTF8
if ($after.Contains($needle)) {
    throw "VERIFIKATION FEHLGESCHLAGEN: der vorzeitige Builder-Aufruf ist noch vorhanden."
}

Write-Host "4/4 Starte exakt den Pipeline-Test aus GitHub Actions..." -ForegroundColor Cyan
python tests/test_pipeline_contract.py
if ($LASTEXITCODE -ne 0) {
    throw "Pipeline-Test ist weiterhin fehlgeschlagen."
}

Write-Host ""
Write-Host "=========================================" -ForegroundColor Green
Write-Host "  FIX OK - Pipeline contract OK" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Green
Write-Host ""
Write-Host "WICHTIG: Jetzt MUSS die geänderte Datei zu GitHub gepusht werden:"
Write-Host ""
Write-Host "git add scripts/update-upstreams.py"
Write-Host 'git commit -m "Fix upstream classifier pipeline order"'
Write-Host "git push"
Write-Host ""
Write-Host "Danach erst GitHub Actions erneut starten."

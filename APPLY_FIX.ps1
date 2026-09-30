$ErrorActionPreference = "Stop"

$repo = (Get-Location).Path
$target = Join-Path $repo "scripts\update-upstreams.py"
$test = Join-Path $repo "tests\test_pipeline_contract.py"

if (-not (Test-Path $target)) {
    throw "Nicht im Repository-Root ausgeführt: scripts\update-upstreams.py wurde nicht gefunden."
}

$content = Get-Content -LiteralPath $target -Raw -Encoding UTF8
$original = $content

# Entferne den veralteten, vorzeitigen Public-List-Build.
$pattern = '(?ms)^\s*if not args\.dry_run:\s*\r?\n\s*subprocess\.run\(\[sys\.executable,\s*str\(ROOT / "scripts" / "build-categories\.py"\)\],\s*check=True\)\s*\r?\n'
$content = [regex]::Replace($content, $pattern, '')

if ($content -eq $original) {
    if ($content -match 'subprocess\.run' -and $content -match 'build-categories\.py') {
        throw "Der alte Builder-Aufruf wurde gefunden, aber das erwartete Muster passt nicht. Datei wurde NICHT verändert."
    } else {
        Write-Host "Der vorzeitige Builder-Aufruf ist bereits entfernt." -ForegroundColor Yellow
    }
} else {
    Copy-Item -LiteralPath $target -Destination "$target.bak" -Force
    Set-Content -LiteralPath $target -Value $content -Encoding UTF8 -NoNewline
    Write-Host "Fix angewendet: vorzeitiger build-categories.py-Aufruf entfernt." -ForegroundColor Green
    Write-Host "Backup: scripts\update-upstreams.py.bak"
}

# Optional: unbenutzten subprocess-Import entfernen, wenn kein subprocess mehr genutzt wird.
$content2 = Get-Content -LiteralPath $target -Raw -Encoding UTF8
if ($content2 -notmatch 'subprocess\.') {
    $content2 = [regex]::Replace($content2, '(?m)^import subprocess\r?\n', '')
    Set-Content -LiteralPath $target -Value $content2 -Encoding UTF8 -NoNewline
}

# Harte Kontrolle.
$check = Get-Content -LiteralPath $target -Raw -Encoding UTF8
if ($check -match 'subprocess\.run' -and $check -match 'build-categories\.py') {
    throw "Fix fehlgeschlagen: update-upstreams.py ruft build-categories.py weiterhin direkt auf."
}

Write-Host ""
Write-Host "Erwartete Pipeline:" -ForegroundColor Cyan
Write-Host "  update-upstreams.py -> classify-upstreams.py -> validate-classifier.py -> build-categories.py"
Write-Host ""

if (Test-Path $test) {
    Write-Host "Führe Pipeline-Vertragstest aus..." -ForegroundColor Cyan
    python tests/test_pipeline_contract.py
    if ($LASTEXITCODE -ne 0) {
        throw "Pipeline-Vertragstest ist fehlgeschlagen."
    }
}

Write-Host ""
Write-Host "HOTFIX OK." -ForegroundColor Green
Write-Host "Jetzt prüfen:"
Write-Host "  git diff -- scripts/update-upstreams.py"
Write-Host "  git status"

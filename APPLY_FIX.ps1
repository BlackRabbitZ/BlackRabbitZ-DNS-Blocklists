$ErrorActionPreference = "Stop"

$target = Join-Path (Get-Location) "scripts\update-upstreams.py"

if (-not (Test-Path -LiteralPath $target)) {
    throw "Falscher Ordner: scripts\update-upstreams.py wurde nicht gefunden. Fuehre diese Datei im ROOT des Repositories aus."
}

$content = Get-Content -LiteralPath $target -Raw -Encoding UTF8

$oldBlockCRLF = "    if not args.dry_run:`r`n        subprocess.run([sys.executable, str(ROOT / `"scripts`" / `"build-categories.py`")], check=True)`r`n`r`n"
$oldBlockLF   = "    if not args.dry_run:`n        subprocess.run([sys.executable, str(ROOT / `"scripts`" / `"build-categories.py`")], check=True)`n`n"

$found = $false

if ($content.Contains($oldBlockCRLF)) {
    $content = $content.Replace($oldBlockCRLF, "")
    $found = $true
}
elseif ($content.Contains($oldBlockLF)) {
    $content = $content.Replace($oldBlockLF, "")
    $found = $true
}
else {
    $line = '        subprocess.run([sys.executable, str(ROOT / "scripts" / "build-categories.py")], check=True)'
    if ($content.Contains($line)) {
        $content = $content.Replace("    if not args.dry_run:`r`n$line`r`n", "")
        $content = $content.Replace("    if not args.dry_run:`n$line`n", "")
        $found = $true
    }
}

if (-not $found) {
    if (($content -notmatch 'build-categories\.py') -or ($content -notmatch 'subprocess\.run')) {
        Write-Host "Der vorzeitige Builder-Aufruf ist bereits entfernt." -ForegroundColor Yellow
    }
    else {
        throw "Der bekannte Builder-Aufruf wurde gefunden, konnte aber nicht sicher automatisch entfernt werden. Es wurde NICHTS gespeichert."
    }
}
else {
    Copy-Item -LiteralPath $target -Destination "$target.bak" -Force

    $tmp = $content -replace '(?m)^import subprocess\r?\n', ''
    Set-Content -LiteralPath $target -Value $tmp -Encoding UTF8 -NoNewline
    Write-Host "update-upstreams.py wurde korrigiert." -ForegroundColor Green
    Write-Host "Backup: scripts\update-upstreams.py.bak"
}

$verify = Get-Content -LiteralPath $target -Raw -Encoding UTF8
if (($verify -match 'subprocess\.run') -and ($verify -match 'build-categories\.py')) {
    throw "VERIFIKATION FEHLGESCHLAGEN: Der vorzeitige Builder-Aufruf ist weiterhin vorhanden."
}

Write-Host ""
Write-Host "Pruefe Pipeline-Contract..." -ForegroundColor Cyan
python tests/test_pipeline_contract.py
if ($LASTEXITCODE -ne 0) {
    throw "Pipeline-Contract ist weiterhin fehlgeschlagen."
}

Write-Host ""
Write-Host "OK: Pipeline-Contract bestanden." -ForegroundColor Green
Write-Host "Jetzt committen/pushen:"
Write-Host "  git add scripts/update-upstreams.py"
Write-Host "  git commit -m `"Fix classified upstream pipeline`""
Write-Host "  git push"

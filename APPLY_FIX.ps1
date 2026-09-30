$ErrorActionPreference = 'Stop'
Write-Host 'BlackRabbitZ Classifier Fix v2.0' -ForegroundColor Cyan
$required = @('scripts/upstream-sources.json','sources/manual','sources/upstream','lists/categories')
foreach ($p in $required) { if (-not (Test-Path $p)) { throw "Nicht im Repository-Root oder Pfad fehlt: $p" } }
python .\tests\test_classifier.py
python .\scripts\classify-upstreams.py
python .\scripts\validate-classifier.py
python .\scripts\build-categories.py
python .\scripts\validate-repository.py
Write-Host 'Classifier eingebaut und Listen lokal neu gebaut.' -ForegroundColor Green
Write-Host 'Optional: python .\scripts\audit-manual-classification.py'
Write-Host 'Danach unbedingt git status und git diff prüfen.'

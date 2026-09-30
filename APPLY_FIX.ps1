$ErrorActionPreference = 'Stop'
Write-Host 'BlackRabbitZ Classifier Pipeline Fix v2.0.3' -ForegroundColor Cyan
$required = @('scripts/upstream-sources.json','scripts/update-upstreams.py','sources/manual','sources/upstream','lists/categories')
foreach ($p in $required) { if (-not (Test-Path $p)) { throw "Nicht im Repository-Root oder Pfad fehlt: $p" } }
python .\scripts\patch-classified-pipeline.py
python .\tests\test_pipeline_contract.py
python .\tests\test_classifier.py
python .\scripts\classify-upstreams.py
python .\scripts\validate-classifier.py
python .\scripts\build-categories.py
python .\scripts\validate-repository.py
Write-Host 'Pipeline korrigiert: Fremdlisten -> raw cache -> classifier -> vorhandene Kategorien.' -ForegroundColor Green
Write-Host 'Danach git status und git diff prüfen.'

#!/usr/bin/env bash
set -euo pipefail

# Dieses Skript wird im Root des BlackRabbitZ-DNS-Blocklists-Repositories ausgeführt.
required=(
  ".github/workflows/dns-maintenance.yml"
  ".github/workflows/issue-pr-automation.yml"
  ".github/workflows/quality-statistics.yml"
  ".github/workflows/ci-security.yml"
  ".github/workflows/upstream-monitoring.yml"
  ".github/workflows/validate.yml"
  ".github/workflows/update-lists.yml"
  "scripts/automation/validate_repository.py"
  "scripts/apply-allowlist.py"
  "scripts/update-lists.sh"
)

for file in "${required[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "FEHLER: Neue Datei fehlt: $file" >&2
    exit 1
  fi
done

old=(
  cleanup.yml
  dead-domain-cleanup.yml
  dns-health-check.yml
  issue-triage.yml
  list-statistics.yml
  new-domain-check.yml
  pr-summary.yml
  quality-report.yml
  reproducible-build.yml
  security-scan.yml
  upstream-change-alert.yml
  upstream-health.yml
  permissions-audit.yml
)

for file in "${old[@]}"; do
  rm -f ".github/workflows/$file"
done

python3 -m compileall -q scripts
find scripts -type f -name '*.sh' -print0 | xargs -0 -r -n1 bash -n

echo "Migration abgeschlossen. Erwartete Workflow-Anzahl:"
find .github/workflows -maxdepth 1 -type f \( -name '*.yml' -o -name '*.yaml' \) -printf '%f\n' | sort

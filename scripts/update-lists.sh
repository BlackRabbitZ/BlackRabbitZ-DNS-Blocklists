#!/usr/bin/env bash
set -euo pipefail

# v3.3.2 migration cleanup: extended lists are now functionally integrated under lists/categories.
rm -f lists/special/hagezi-*.txt 2>/dev/null || true
rm -f lists/ips/hagezi-*.txt 2>/dev/null || true

# Deterministic and substantially faster sorting for multi-million-entry lists.
export LC_ALL=C

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

# v3.3.3: force a clean republish of every split profile. This is intentional:
# repositories that still contain legacy 5-MiB parts must not keep reusing those
# files after the configured limit changed to 50 MiB. publish-profile.py will
# recreate the exact required set immediately below.
rm -f lists/combined/security-part-*.txt \
      lists/combined/family-part-*.txt \
      lists/combined/ultimate-part-*.txt \
      lists/combined/ultimate-[0-9]*.txt 2>/dev/null || true
rm -f metadata/build.json metadata/SHA256SUMS 2>/dev/null || true

REPO_URL="https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists"
PROFILE_CONFIG="config/profiles.json"

count_entries() {
  local file="$1"
  { grep -Ev '^[[:space:]]*(#|$)' "$file" || true; } \
    | sed 's/\r$//' \
    | sort -u \
    | wc -l \
    | tr -d '[:space:]'
}

update_entries_header() {
  local file="$1"
  local count="$2"
  local tmp
  tmp="$(mktemp)"
  awk -v count="$count" '
    /^# Entries:/ {
      print "# Entries: " count
      next
    }
    { print }
  ' "$file" > "$tmp"
  mv "$tmp" "$file"
}

write_category_header_if_missing() {
  local file="$1"
  local category="$2"
  local count="$3"

  if grep -q '^# BlackRabbitZ DNS Blocklists$' "$file"; then
    return 0
  fi

  local tmp
  tmp="$(mktemp)"
  {
    echo "# BlackRabbitZ DNS Blocklists"
    echo "# Category: $category"
    echo "# Author: BlackRabbitZ"
    echo "# Repository: $REPO_URL"
    echo "# License: GPL-3.0-only for project-original material; third-party notices: THIRD_PARTY.md"
    echo "# Entries: $count"
    echo "#"
    { grep -Ev '^[[:space:]]*(#|$)' "$file" || true; }
  } > "$tmp"
  mv "$tmp" "$file"
}

if [[ ! -f "$PROFILE_CONFIG" ]]; then
  echo "Missing profile configuration: $PROFILE_CONFIG" >&2
  exit 1
fi

# Keep category-file entry headers synchronized with actual unique non-comment entries.
for file in lists/categories/*.txt; do
  category="$(basename "$file" .txt)"
  count="$(count_entries "$file")"
  write_category_header_if_missing "$file" "$category" "$count"
  update_entries_header "$file" "$count"
done

build_profile() {
  local profile="$1"
  local split="$2"
  local max_bytes="$3"
  local categories_csv="$4"
  local tmp_domains
  tmp_domains="$(mktemp)"
  : > "$tmp_domains"

  local categories=()
  IFS=',' read -r -a categories <<< "$categories_csv"

  for category in "${categories[@]}"; do
    local src="lists/categories/${category}.txt"
    if [[ ! -f "$src" ]]; then
      echo "Missing category file required by profile '$profile': $src" >&2
      rm -f "$tmp_domains"
      exit 1
    fi
    { grep -Ev '^[[:space:]]*(#|$)' "$src" || true; } | sed 's/\r$//' >> "$tmp_domains"
  done

  sort -u "$tmp_domains" -o "$tmp_domains"

  local includes
  includes="$(IFS=', '; echo "${categories[*]}")"

  local args=(
    "$tmp_domains"
    --profile "$profile"
    --output-dir lists/combined
    --max-bytes "$max_bytes"
    --repo-url "$REPO_URL"
    --includes "$includes"
  )
  if [[ "$split" == "true" ]]; then
    args+=(--split)
  fi

  python3 ./scripts/publish-profile.py "${args[@]}"
  rm -f "$tmp_domains"
}

# config/profiles.json is the single source of truth for profile composition,
# display metadata and which large profiles are published as numbered parts.
while IFS=$'\t' read -r profile split max_bytes categories_csv; do
  build_profile "$profile" "$split" "$max_bytes" "$categories_csv"
done < <(
  python3 - "$PROFILE_CONFIG" <<'PY'
import json
import sys
from pathlib import Path

config = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
max_bytes = int(config["split_max_bytes"])
for name, profile in config["profiles"].items():
    print("\t".join([
        name,
        "true" if profile.get("split") else "false",
        str(max_bytes),
        ",".join(profile["categories"]),
    ]))
PY
)

check_github_file_sizes() {
  local warn_bytes=$((50 * 1024 * 1024))
  local max_bytes=$((100 * 1024 * 1024))
  local failed=0

  for file in lists/categories/*.txt lists/combined/*.txt; do
    local size
    size="$(wc -c < "$file" | tr -d '[:space:]')"
    if (( size > max_bytes )); then
      echo "ERROR: $file is larger than GitHub's 100 MiB regular-file limit ($size bytes)." >&2
      failed=1
    elif (( size > warn_bytes )); then
      echo "WARNING: $file is larger than 50 MiB ($size bytes); GitHub will warn about this large file." >&2
    fi
  done

  if (( failed != 0 )); then
    exit 1
  fi
}

check_github_file_sizes
python3 ./scripts/generate-metadata.py
python3 ./scripts/update-readme.py
python3 ./scripts/validate-generated.py

echo "Blocklists, combined profiles, split parts, metadata, checksums and German/English READMEs are synchronized."

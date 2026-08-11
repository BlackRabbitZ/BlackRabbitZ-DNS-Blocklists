#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

REPO_URL="https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists"

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
    BEGIN { updated = 0 }
    /^# Entries:/ {
      print "# Entries: " count
      updated = 1
      next
    }
    { print }
    END {
      if (!updated) {
        # Existing project category files have a standard header. New files
        # should use that header as well; this branch intentionally does not
        # inject metadata into an arbitrary file layout.
      }
    }
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
    echo "# License: GPL-3.0-only; see LICENSE, NOTICE and ATTRIBUTION.md"
    echo "# Entries: $count"
    echo "#"
    { grep -Ev '^[[:space:]]*(#|$)' "$file" || true; }
  } > "$tmp"
  mv "$tmp" "$file"
}

# Keep all category-file entry headers synchronized with the actual unique
# non-comment entries. Category content itself is never regenerated here.
for file in lists/categories/*.txt; do
  category="$(basename "$file" .txt)"
  count="$(count_entries "$file")"
  write_category_header_if_missing "$file" "$category" "$count"
  update_entries_header "$file" "$count"
done

build_combined() {
  local profile="$1"
  shift
  local categories=("$@")
  local out="lists/combined/${profile}.txt"
  local tmp_domains
  tmp_domains="$(mktemp)"

  : > "$tmp_domains"
  for category in "${categories[@]}"; do
    local src="lists/categories/${category}.txt"
    if [[ ! -f "$src" ]]; then
      echo "Missing category file: $src" >&2
      rm -f "$tmp_domains"
      exit 1
    fi
    { grep -Ev '^[[:space:]]*(#|$)' "$src" || true; } | sed 's/\r$//' >> "$tmp_domains"
  done

  sort -u "$tmp_domains" -o "$tmp_domains"
  local count
  count="$(wc -l < "$tmp_domains" | tr -d '[:space:]')"
  local includes
  includes="$(printf '%s, ' "${categories[@]}")"
  includes="${includes%, }"

  {
    echo "# BlackRabbitZ DNS Blocklists"
    echo "# Category: combined/$profile"
    echo "# Author: BlackRabbitZ"
    echo "# Repository: $REPO_URL"
    echo "# License: GPL-3.0-only; see LICENSE, NOTICE and ATTRIBUTION.md"
    echo "# Entries: $count"
    echo "#"
    echo "# Includes: $includes"
    echo "#"
    cat "$tmp_domains"
  } > "$out"

  rm -f "$tmp_domains"
}

# Profile definitions. These arrays are the single source of truth for which
# category lists feed each published combined profile.
build_combined light \
  ads

build_combined balanced \
  ads trackers social-trackers affiliate-tracking

build_combined strict \
  ads trackers social-trackers affiliate-tracking \
  telemetry windows-telemetry apple-telemetry android-telemetry \
  linux-telemetry nas-telemetry server-telemetry \
  mobile-tracking native-tracking smart-tv iot

build_combined security \
  malware phishing scam fake-shops cryptomining

build_combined family \
  ads trackers social-trackers adult gambling

build_combined ultimate \
  ads trackers telemetry windows-telemetry apple-telemetry android-telemetry \
  linux-telemetry nas-telemetry server-telemetry \
  smart-tv iot mobile-tracking social-trackers native-tracking \
  phishing malware scam cryptomining fake-shops adult gambling \
  consent-cmp affiliate-tracking

update_readme_count() {
  local path="$1"
  local value="$2"
  local tmp
  tmp="$(mktemp)"

  local column=3
  if [[ "$path" == lists/combined/* ]]; then
    column=4
  fi

  awk -v target="[View]($path)" -v value="$value" -v column="$column" '
    index($0, target) && $0 ~ /^\|/ {
      n = split($0, field, "|")
      if (n >= column) {
        field[column] = " " value " "
        line = field[1]
        for (i = 2; i <= n; i++) {
          line = line "|" field[i]
        }
        print line
        next
      }
    }
    { print }
  ' README.md > "$tmp"

  mv "$tmp" README.md
}

# Update every README table row that links to a category or combined list.
for file in lists/categories/*.txt; do
  count="$(count_entries "$file")"
  update_readme_count "$file" "$count"
done

for file in lists/combined/*.txt; do
  count="$(count_entries "$file")"
  update_readme_count "$file" "**$count**"
done

echo "Blocklists, combined profiles and README entry counts are synchronized."

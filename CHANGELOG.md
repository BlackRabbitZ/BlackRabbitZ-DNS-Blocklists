# Changelog

## 2.1.1 - 2026-08-12

- Replaced the single large `lists/combined/ultimate.txt` with automatically generated `ultimate-N.txt` parts.
- Added `scripts/split-ultimate.py` with a 40 MiB target ceiling per Ultimate part.
- Added automatic README generation for Ultimate part counts, sizes, View links and Raw links.
- Updated the blocklist workflow so changes to the split-generator scripts trigger a rebuild.
- Old/stale Ultimate part files are removed automatically before every regeneration.

## 2.1.0 - 2026-08-12

- Added a daily upstream-refresh GitHub Actions workflow.
- Added `scripts/update-upstreams.py` for additive automatic domain imports.
- Added `scripts/upstream-sources.json` with per-category upstream sources and safety thresholds.
- Added download retries, source minimum-size validation, domain normalization, deduplication and growth guards.
- Added `config/allowlist.txt` for critical automatic-import exclusions.
- Added `docs/AUTOMATIC_UPDATES.md` with maintenance and fail-safe documentation.
- Unified workflow concurrency and kept Bash invocation independent of executable file permissions.

## 2.0.2 - 2026-08-11

- Added descriptions to the Family Lists table in the README.
- Populated Malware, Phishing, Scam and Fake Shops security categories with curated, externally verified indicators.
- Added source notes to security category files and THIRD_PARTY.md.
- Rebuilt Security and Ultimate combined profiles and synchronized all entry counts.

## 2.0.1 - 2026-08-11

- Restored the richer v1.3-style README presentation.
- Added centered project branding and stronger visual hierarchy.
- Restored protection comparison matrix and grouped category sections.
- Kept all v2.0.0 static lists and domain counts unchanged.

## 2.0.0 - 2026-08-11

- Major expansion of static curated privacy/ad/telemetry lists.
- Added 128 advertising endpoints.
- Added 136 tracking/analytics endpoints.
- Added dedicated social, mobile, native-app, affiliate and CMP categories.
- Expanded Windows, Apple, Android, Smart-TV and IoT telemetry categories.
- Combined profiles refreshed as direct static files.
- Repository remains script-free and Python-free.
- Security threat categories remain intentionally conservative rather than importing third-party live feeds.

## 1.3.0 - 2026-08-11

- Redesigned README and static list presentation.

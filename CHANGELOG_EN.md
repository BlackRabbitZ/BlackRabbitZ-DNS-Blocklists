# Changelog

**🌐 Language / Sprache:** [🇩🇪 Deutsch](CHANGELOG.md) · 🇬🇧 **English**

## 3.3.0 — 2026-08-12

- Increased the split limit for large profiles and special lists from 5 MiB to **50 MiB per part**, significantly reducing the number of Security, Family, Ultimate and large add-on files.
- Integrated HaGeZi topics **7–22** as optional reproducible special lists in the appropriate README categories; topics **23–24** are included as recommendations and online-DNS guidance.
- Added a new **DNS, Web & Bypass Protection** category for DoH/VPN/TOR/Proxy bypass, URL shorteners and DNS rebind protection.
- Added a short explanation of why DNS blocklists are useful before the table of contents.
- Expanded the table of contents with a short description for every entry.
- Updated README automation to maintain categorized special-list blocks.

## 3.2.0 - 2026-08-12

- Integrated HaGeZi topics **7–22** from the archived repository state as optional BlackRabbitZ special lists.
- Added dedicated archive builder `scripts/update-special-lists.py` with normalization, allowlist handling, deduplication, sanity thresholds and automatic 5 MiB splitting.
- Added TIF Full/Medium/Mini, NRD/DGA windows, DNS bypass, SafeSearch, DynDNS, badware hosters, URL shorteners, TLD rules, anti-piracy, gambling variants, social-network blocking, NSFW and native-tracker variants.
- Implemented topic **17 DNS Rebind Protection** as Pi-hole resolver/dnsmasq guidance because the archived HaGeZi list was AdGuard-specific.
- Added HaGeZi topics **23 Recommendations** and **24 Online DNS Services** as BlackRabbitZ documentation sections; neither is a blocklist.
- Expanded the table of contents and added a short description after every link.
- Special-list metadata, Raw/part links and German/English README sections are synchronized automatically.
- Expanded archive source and license/attribution documentation.

## 3.1.0 - 2026-08-12

- Added German `README.md` as the default and a separate English `README_EN.md`.
- Added a language switch at the top of both README files.
- Added a table of contents with stable section anchors.
- Moved **Optional Protection Modules** and **Large Profile Parts** directly under **Protection Comparison**.
- Extended `scripts/update-readme.py` to synchronize both language versions.
- Added `config/readme-i18n.json` as the central language configuration for generated README blocks.
- Added German and English versions of the main maintenance documentation.
- Made the GitHub issue forms bilingual.

## 3.0.0 - 2026-08-12

- Replaced Ultimate-only split logic with a generic profile publisher driven by `config/profiles.json`.
- Added deterministic 5 MiB `*-part-NN.txt` output for Security, Family and Ultimate.
- Renamed Ultimate parts from `ultimate-N.txt` to zero-padded `ultimate-part-NN.txt`.
- Split the previously single-file Security and Family profiles into size-bounded parts.
- Removed Affiliate Tracking from Balanced and kept it in Strict/Ultimate to reduce avoidable referral/link breakage for the recommended profile.
- Removed Consent/CMP from Ultimate and kept it as an explicit optional category because DNS-level CMP blocking has elevated website-breakage risk.
- Repositioned Security and Family as optional protection modules rather than sequential privacy tiers in the README.
- Added `metadata/build.json` with machine-readable profile/category counts, part information, sizes and SHA-256 hashes.
- Added `metadata/SHA256SUMS` generation.
- Added generated-profile validation for global sort order, duplicates, part-size limits and metadata consistency.
- Added `.gitattributes` rules for generated combined profiles and metadata.
- Added structured GitHub issue forms for false positives, domain requests and upstream-source proposals.
- Expanded contributing and automatic-update documentation.

### Migration note

The first v3 rebuild removes the previous generated URLs `lists/combined/security.txt`, `lists/combined/family.txt` and `lists/combined/ultimate-N.txt`. Replace existing subscriptions with **all** new `*-part-NN.txt` Raw URLs shown in the README.

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

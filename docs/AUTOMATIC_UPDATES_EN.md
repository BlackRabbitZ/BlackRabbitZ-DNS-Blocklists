# Automatic upstream updates

**🌐 Language / Sprache:** [🇩🇪 Deutsch](AUTOMATIC_UPDATES.md) · 🇬🇧 **English**

BlackRabbitZ updates selected category lists and regenerates published profiles with GitHub Actions.

## Workflows

- `.github/workflows/daily-upstream-update.yml` runs every day at **03:17 UTC** and can also be started manually.
- `.github/workflows/update-lists.yml` keeps combined profiles, split parts, metadata, checksums and both README language versions synchronized after category, profile-config or build-script changes.

## Daily update flow

1. `scripts/update-upstreams.py` reads `scripts/upstream-sources.json`.
2. Upstream feeds are downloaded over HTTPS with retries, timeouts and a maximum download size.
3. Hosts, plain-domain, URL, AdGuard/ABP and wildcard-style entries are normalized to one-domain-per-line format.
4. Invalid values, IP addresses, duplicates and domains covered by `config/allowlist.txt` are ignored.
5. New domains are merged **additively** into the existing category files. Existing entries are never silently deleted by the automatic importer.
6. Per-source minimum sizes reject suspiciously empty downloads.
7. Per-category growth guards reject implausibly large one-run additions.
8. `scripts/update-lists.sh` reads `config/profiles.json`, merges the required categories and sorts/deduplicates every combined profile.
9. `scripts/publish-profile.py` publishes Light/Balanced/Strict as single files and large configured profiles as deterministic size-bounded parts.
10. `scripts/generate-metadata.py` creates `metadata/build.json` and `metadata/SHA256SUMS`.
11. `scripts/update-readme.py` synchronizes both **README.md (German)** and **README_EN.md (English)**, including profile tables, part links, comparison data and category counts.
12. `scripts/validate-generated.py` verifies generated profile ordering, uniqueness, part-size limits and metadata consistency.
13. If the generated repository changed and all checks passed, GitHub Actions commits the result to `main`.

## Profile configuration

`config/profiles.json` is the single source of truth for:

- which categories belong to each combined profile;
- whether a profile is shown as a main privacy tier or optional module;
- whether a profile is always published as numbered parts;
- the maximum generated part size;
- technical display metadata and breakage indicators;
- the protection-comparison matrix.

`config/readme-i18n.json` contains language-specific strings for the generated German and English README blocks.

This removes profile composition from shell-code branches and prevents README/configuration drift.

### Current profile policy

- **Light**: Ads only.
- **Balanced**: Ads + general trackers + social trackers. Affiliate/referral blocking is deliberately excluded to reduce avoidable breakage.
- **Strict**: Adds affiliate tracking, telemetry, platform/device telemetry and native/app tracking.
- **Security**: Security-focused add-on with malware, phishing, scam, fake-shop and cryptomining categories.
- **Family**: Family add-on with advertising/tracking plus adult and gambling filtering.
- **Ultimate**: Aggressive all-in-one protection. Consent/CMP is deliberately kept separate because DNS-level CMP blocking can break website consent flows and page functionality.

## Large-profile splitting

Profiles marked with `"split": true` are always published as numbered parts. This avoids URL layouts changing back and forth when a list temporarily grows or shrinks.

Current split profiles:

- `security-part-01.txt`, `security-part-02.txt`, ...
- `family-part-01.txt`, `family-part-02.txt`, ...
- `ultimate-part-01.txt`, `ultimate-part-02.txt`, ...

Each generated part targets a maximum of **5 MiB** (`5242880` bytes including its header). Part numbering is zero-padded so file ordering remains stable when a profile grows beyond nine parts.

For complete coverage, DNS blockers must subscribe to **all parts** shown in the README for that profile.

### Migration from the old layout

The v3 layout replaces these previous generated outputs:

- `lists/combined/security.txt`
- `lists/combined/family.txt`
- `lists/combined/ultimate-1.txt`, `ultimate-2.txt`, ...

with size-bounded `*-part-NN.txt` files. Existing Pi-hole subscriptions using the old URLs must be replaced with all new Raw URLs listed in the README after the first v3 rebuild.

## Generated metadata and checksums

`metadata/build.json` provides machine-readable information for every category and combined profile, including:

- entry counts;
- file names;
- part count;
- byte size;
- SHA-256 hash;
- included categories.

`metadata/SHA256SUMS` contains a standard checksum list for all category and combined profile files.

Both files are deterministic: rebuilding unchanged input should not create a timestamp-only diff.

## Categories updated from upstreams

The source matrix currently covers Ads, Trackers, Telemetry-derived subsets, Windows/Apple/Android native telemetry, Native Tracking, Smart TV, IoT, Cryptomining, Malware, Phishing, Scam, Fake Shops, Adult and Gambling.

`gaming-telemetry.txt`, `gaming-telemetry-aggressive.txt`, `linux-telemetry.txt`, `nas-telemetry.txt` and `server-telemetry.txt` can remain manually curated when no single trustworthy general-purpose upstream cleanly represents those specialized endpoints.

## Safety behavior

The importer/build pipeline is designed to fail safely:

- If one upstream is unavailable, the last committed category remains intact.
- If every source for a category fails, that category is left unchanged.
- If a feed suddenly returns far fewer entries than its configured minimum, it is rejected.
- If newly imported data exceeds the configured one-run growth limit, the workflow exits before committing anything.
- Missing category files referenced by a profile cause the build to fail.
- Split parts larger than the configured part limit cause validation to fail.
- Duplicate or out-of-order domains across generated profile parts cause validation to fail.
- Metadata entry-count mismatches cause validation to fail.
- Any regular Git file over GitHub's 100 MiB hard limit causes the build to fail before commit.

## Adding or removing an upstream

Edit:

```text
scripts/upstream-sources.json
```

Each source has a name, HTTPS URL and `min_entries`. A source can optionally use `include_keywords` to derive a narrow category from a broader feed.

After changing the configuration, run:

```bash
python3 scripts/update-upstreams.py --check-config
python3 scripts/update-upstreams.py --dry-run
bash scripts/update-lists.sh
```

## Changing a profile

Edit:

```text
config/profiles.json
```

Language-specific README strings are configured in `config/readme-i18n.json`.

Do not manually edit files under `lists/combined/`, `metadata/build.json` or `metadata/SHA256SUMS`; they are generated outputs.

Run:

```bash
bash scripts/update-lists.sh
```

## False-positive safety allowlist

Add critical domains to:

```text
config/allowlist.txt
```

An allowlisted domain and its subdomains are excluded from **new automatic imports**. Existing category entries are not silently removed.

## GitHub repository setting

The workflows need permission to push their generated changes. In GitHub, ensure the repository's Actions workflow permissions allow write access to repository contents. Branch protection rules must also permit the workflow/bot to update `main`, or the automatic commit will fail.

## Android first-import guard

`android-telemetry` intentionally permits a larger first-run growth than the global default because configured Huawei/Xiaomi/Oppo-Realme/Vivo native-tracking sources can add more than 1,000 valid domains at once. The category remains protected by its configured growth guard.

# Automatic upstream updates

BlackRabbitZ can update selected category lists automatically with GitHub Actions.

## Workflows

- `.github/workflows/daily-upstream-update.yml` runs every day at **03:17 UTC** and can also be started manually.
- `.github/workflows/update-lists.yml` keeps combined profiles and README counts synchronized after manual category edits.

## Daily update flow

1. `scripts/update-upstreams.py` reads `scripts/upstream-sources.json`.
2. Upstream feeds are downloaded over HTTPS with retries, timeouts and a maximum download size.
3. Hosts, plain-domain, URL, AdGuard/ABP and wildcard-style entries are normalized to one-domain-per-line format.
4. Invalid values, IP addresses, duplicates and domains covered by `config/allowlist.txt` are ignored.
5. New domains are merged **additively** into the existing category files. Existing entries are never deleted by the automatic importer.
6. Per-source minimum sizes reject suspiciously empty downloads.
7. Per-category growth guards reject implausibly large one-run additions.
8. `scripts/update-lists.sh` rebuilds all combined profiles, updates entry counts and enforces GitHub file-size limits.
9. If the generated repository changed and all checks passed, GitHub Actions commits the result to `main`.

## Categories updated from upstreams

The source matrix currently covers Ads, Trackers, Telemetry-derived subsets, Windows/Apple/Android native telemetry, Native Tracking, Smart TV, IoT, Cryptomining, Malware, Phishing, Scam, Fake Shops, Adult and Gambling.

`linux-telemetry.txt`, `nas-telemetry.txt` and `server-telemetry.txt` remain manually curated because there is no single trustworthy upstream feed that cleanly represents those vendor-specific telemetry endpoints.

## Safety behavior

The importer is designed to fail safely:

- If one upstream is unavailable, the last committed list remains intact.
- If every source for a category fails, that category is left unchanged.
- If a feed suddenly returns far fewer entries than its configured minimum, it is rejected.
- If newly imported data exceeds the configured one-run growth limit, the workflow exits before committing anything.
- If a generated list exceeds GitHub's regular-file size limit, `update-lists.sh` fails before the automatic commit.

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

## False-positive safety allowlist

Add critical domains to:

```text
config/allowlist.txt
```

An allowlisted domain and its subdomains are excluded from **new automatic imports**. Existing category entries are not silently removed.

## GitHub repository setting

The workflows need permission to push their generated changes. In GitHub, ensure the repository's Actions workflow permissions allow write access to repository contents. Branch protection rules must also permit the workflow/bot to update `main`, or the automatic commit will fail.

## Split Ultimate profile

The `Ultimate` profile is generated as multiple size-bounded files instead of one very large `ultimate.txt`.

- `scripts/update-lists.sh` merges and deduplicates the Ultimate categories.
- `scripts/split-ultimate.py` writes `lists/combined/ultimate-1.txt`, `ultimate-2.txt`, and additional numbered parts as needed.
- Each part targets a maximum size of **40 MiB**.
- Old numbered parts are removed automatically before regeneration.
- `scripts/update-ultimate-readme.py` updates the aggregate Ultimate entry count and rebuilds the README table of Part/View/Raw links.
- For complete Ultimate coverage, DNS blockers must subscribe to **all** numbered Ultimate Raw URLs shown in the README.

This avoids a single Ultimate file approaching GitHub's normal per-file hard limit while keeping the split deterministic and fully automatic.

## Android first-import guard

`android-telemetry` intentionally permits a larger first-run growth than the global default because the configured HaGeZi Huawei/Xiaomi/Oppo-Realme/Vivo native-tracking sources can add more than 1,000 valid domains at once. The category is capped at 5,000 new domains per run and still remains protected by the growth guard.

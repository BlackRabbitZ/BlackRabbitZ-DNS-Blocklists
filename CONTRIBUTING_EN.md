# Contributing

**🌐 Language / Sprache:** [🇩🇪 Deutsch](CONTRIBUTING.md) · 🇬🇧 **English**

Contributions are welcome when they improve list quality, coverage, documentation or build safety.

## Domain submissions

Use the **Domain request** issue template and provide:

- the exact domain;
- the proposed category;
- a clear technical rationale;
- independent evidence where possible.

Do not bulk-copy third-party maintained blocklists into this repository. New upstream feeds should be proposed separately so their maintenance quality, format and license/reuse terms can be reviewed.

## False positives

Use the **False positive** issue template and include the affected domain, BlackRabbitZ list/profile, application/device, exact breakage and reproduction steps.

False-positive reports are prioritized over raw list-size growth. The project goal is useful filtering, not the largest possible number of domains.

## Upstream sources

Use the **Upstream source** issue template. A proposed feed should have:

- a stable HTTPS URL;
- clear maintenance ownership;
- suitable reuse/license terms;
- a format that can be validated and normalized;
- a clear mapping to an existing BlackRabbitZ category.

## Generated files

Do not manually edit:

- `lists/combined/*`
- `metadata/build.json`
- `metadata/SHA256SUMS`

Combined profiles and metadata are generated from category files and `config/profiles.json` by `scripts/update-lists.sh`.

## Local validation

Before opening a pull request for build/configuration changes, run:

```bash
python3 scripts/update-upstreams.py --check-config
python3 -m json.tool config/profiles.json >/dev/null
bash scripts/update-lists.sh
git diff --check
```

Generated changes should be committed together with the source/configuration change that caused them.

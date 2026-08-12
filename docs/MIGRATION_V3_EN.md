# Migration to v3 split profiles

**🌐 Language / Sprache:** [🇩🇪 Deutsch](MIGRATION_V3.md) · 🇬🇧 **English**

BlackRabbitZ v3 generalizes large-list splitting and changes the published URLs for Security, Family and Ultimate.

## Repository maintainer

1. Replace/add the files from the v3 upgrade package.
2. Commit and push them to `main`.
3. The `Update blocklists` workflow rebuilds all combined profiles automatically.
4. The workflow removes old generated Security/Family/Ultimate outputs, creates the new `*-part-NN.txt` files, generates metadata/checksums and updates both README language versions with exact Raw URLs.
5. Verify that the workflow completes successfully before announcing the new URLs.

No category domain files need to be manually edited for the migration.

## Pi-hole / DNS-filter users

Old subscriptions using any of these paths must be replaced:

```text
lists/combined/security.txt
lists/combined/family.txt
lists/combined/ultimate-1.txt
lists/combined/ultimate-2.txt
...
```

After the v3 rebuild, open the repository README and add **every Raw part** shown for the desired split profile:

```text
security-part-01.txt
security-part-02.txt
...

family-part-01.txt
family-part-02.txt
...

ultimate-part-01.txt
ultimate-part-02.txt
...
```

Remove the obsolete old URLs after the new parts have been added, then update Gravity.

## Behavioral changes

- Balanced no longer includes Affiliate Tracking. Affiliate/referral blocking starts with Strict.
- Consent/CMP is no longer included in Ultimate. The standalone Consent/CMP category remains available for users who intentionally accept its higher website-breakage risk.
- Security and Family are documented as optional protection modules rather than sequential privacy tiers.

# 🐇 BlackRabbitZ DNS Blocklists

[![Validate](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/actions/workflows/validate.yml/badge.svg)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/actions/workflows/validate.yml)
![License](https://img.shields.io/badge/license-GPL--3.0--only-blue)
![Pi-hole](https://img.shields.io/badge/Pi--hole-compatible-green)
![Lists](https://img.shields.io/badge/profiles-7-informational)

Independent, transparent and extensible DNS blocklists maintained by **BlackRabbitZ** for Pi-hole and other DNS filtering systems.

## 🚀 Blocklists

**Recommended for most users: `Balanced`**

| Profile | Level | What it targets | Pi-hole domain list | Hosts |
|---|---:|---|---|---|
| Mini | 🟢 Very low | Core advertising | **[Open / Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/mini.txt)** | [Hosts](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/mini-hosts.txt) |
| Light | 🟩 Low | Ads + common trackers | **[Open / Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/light.txt)** | [Hosts](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/light-hosts.txt) |
| **Balanced** | 🟦 Recommended | Ads + tracking + selected telemetry | **[Open / Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/balanced.txt)** | [Hosts](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/balanced-hosts.txt) |
| Strict | 🟧 High | Privacy + platform/device telemetry | **[Open / Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/strict.txt)** | [Hosts](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/strict-hosts.txt) |
| Security | 🛡️ Security | Phishing, malware, scam, cryptomining, etc. | **[Open / Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/security.txt)** | [Hosts](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/security-hosts.txt) |
| Family | 👨‍👩‍👧 Family | Balanced + adult + gambling categories | **[Open / Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/family.txt)** | [Hosts](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/family-hosts.txt) |
| Ultimate | 🟥 Maximum | All enabled privacy/security categories | **[Open / Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/ultimate.txt)** | [Hosts](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/ultimate-hosts.txt) |

> Empty or small specialist categories in early releases are intentional. Domains are added only after independent verification rather than bulk-copying another maintainer's list.

### Copy-ready Pi-hole URLs

**Balanced**
```text
https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/balanced.txt
```

**Strict**
```text
https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/strict.txt
```

**Security**
```text
https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/security.txt
```

**Ultimate**
```text
https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/ultimate.txt
```

## 🧩 Categories

The repository is intentionally category-driven. Profiles are combinations of categories.

```text
data/categories/
├── ads.txt
├── trackers.txt
├── telemetry.txt
├── social-trackers.txt
├── native-tracking.txt
├── phishing.txt
├── malware.txt
├── scam.txt
├── fake-shops.txt
├── cryptomining.txt
├── dynamic-dns.txt
├── newly-registered.txt
├── url-shorteners.txt
├── smart-tv.txt
├── mobile-tracking.txt
├── windows-telemetry.txt
├── apple-telemetry.txt
├── android-telemetry.txt
├── iot-telemetry.txt
├── adult.txt
└── gambling.txt
```

This structure is designed to grow. Adding another category does **not** require rewriting the generator.

## ➕ Add a completely new category

Example: later you want `gaming-telemetry`.

1. Create:
```text
data/categories/gaming-telemetry.txt
```

2. Put independently verified domains in it:
```text
telemetry.example-game.invalid
metrics.example-game.invalid
```

3. Add `"gaming-telemetry"` to whichever profiles should include it in `config.json`.

4. Run:
```bash
python scripts/validate.py
python scripts/build.py
```

Done.

## ➕ Add a completely new blocklist profile

You can also create a new finished list without touching Python.

Add this to `config.json`:

```json
"gaming": {
  "label": "Gaming",
  "emoji": "🎮",
  "description": "Gaming telemetry and advertising.",
  "categories": [
    "ads",
    "gaming-telemetry"
  ]
}
```

Then run:

```bash
python scripts/build.py
```

The builder automatically creates:

```text
dist/gaming.txt
dist/gaming-hosts.txt
```

That is the core design goal: **categories and profiles are data, not hard-coded Python logic.**

## 🕳️ Global allowlist

False positives go into:

```text
data/allowlist/global.txt
```

The allowlist is subtracted from every generated profile.

## 🧪 Validation

```bash
python scripts/validate.py
python scripts/build.py
```

GitHub Actions performs the same validation on pushes and pull requests.

## 🛡️ Curation policy

A domain should only be added with independent evidence such as:

- direct DNS/network observation,
- reproducible application/browser behavior,
- vendor documentation,
- an independently verified community report,
- defensible security analysis.

**Do not copy domains in bulk from another blocklist merely because they appear there.**

See:
- [Methodology](docs/METHODOLOGY.md)
- [Licensing & provenance](docs/LICENSING_AND_PROVENANCE.md)
- [Third-party material](THIRD_PARTY.md)

## 📥 Pi-hole

In Pi-hole, add one of the `dist/*.txt` raw URLs as an Adlist and update Gravity.

For most users:

```text
https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/balanced.txt
```

## 🤝 Contributions / False positives

Use the GitHub issue templates for:
- domain submissions,
- false positives.

New entries should contain enough evidence to be independently reproduced or verified.

## ⚖️ License

Repository code, original documentation and the original curated dataset are published under **GPL-3.0-only**.

Copyright (C) 2026 **BlackRabbitZ**.

See:
- `LICENSE`
- `NOTICE`
- `ATTRIBUTION.md`
- `THIRD_PARTY.md`

Original repository:

```text
https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists
```

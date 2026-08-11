# BlackRabbitZ DNS Blocklists

[![Validate](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/actions/workflows/validate.yml/badge.svg)](https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/actions/workflows/validate.yml)
![License](https://img.shields.io/badge/license-GPL--3.0--only-blue)
![Pi-hole](https://img.shields.io/badge/Pi--hole-compatible-green)

Independent, transparent DNS blocklists for Pi-hole and other DNS sinkholes.

> This is an original project by **BlackRabbitZ**. It is not a fork, mirror, copy, or transformed version of HaGeZi or another third-party DNS blocklist.

## Lists

| Tier | Purpose | Raw URL |
|---|---|---|
| Light | Conservative advertising blocking | `.../dist/light.txt` |
| Balanced | Ads + common tracking | `.../dist/balanced.txt` |
| Strict | Balanced + non-essential telemetry | `.../dist/strict.txt` |
| Threat | Independently verified malicious domains | `.../dist/threat.txt` |
| Ultimate | Strict + Threat | `.../dist/ultimate.txt` |

After the repository is public, the Pi-hole URL for Balanced is:

```text
https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/dist/balanced.txt
```

Hosts-format variants are also generated as `*-hosts.txt`.

## Pi-hole

Pi-hole → **Lists / Adlists** → add the raw URL → update Gravity.

CLI example:

```bash
pihole -g
```

## Philosophy

- no third-party blocklist imports by default
- independent evidence for additions
- conservative handling of false positives
- deterministic generated lists
- explicit allowlist
- reviewable Git history
- source categories separated from generated outputs

See [Methodology](docs/METHODOLOGY.md) and [Licensing & Provenance](docs/LICENSING_AND_PROVENANCE.md).

## Build

```bash
python scripts/validate.py
python scripts/build.py
```

## Contributing

Use the Domain Submission or False Positive issue templates. Evidence is required for new entries.

## License

GPL-3.0-only. Copyright (C) 2026 BlackRabbitZ.

See `LICENSE`, `NOTICE`, `ATTRIBUTION.md`, and `THIRD_PARTY.md`.

**Important:** A license policy can reduce risk but cannot guarantee that no third party will ever make a complaint. This repository intentionally avoids importing other maintained blocklists to minimize that risk.

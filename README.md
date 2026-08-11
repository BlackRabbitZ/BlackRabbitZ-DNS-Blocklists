# 🐇 BlackRabbitZ DNS Blocklists

![License](https://img.shields.io/badge/license-GPL--3.0--only-blue)
![Pi-hole](https://img.shields.io/badge/Pi--hole-compatible-green)

Independent DNS blocklists maintained by **BlackRabbitZ** for Pi-hole and other DNS filtering systems.

There are **no scripts and no local installation required**. Choose a list, open the Raw link, copy its URL and add that URL to Pi-hole.

## 🚀 Combined blocklists

| List | Purpose | Raw list |
|---|---|---|
| **Light** | Conservative ad blocking | [Open Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/light.txt) |
| **Balanced** | Ads + common tracking; recommended default | [Open Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/balanced.txt) |
| **Strict** | Ads + tracking + telemetry | [Open Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/strict.txt) |
| **Security** | Malware / phishing / scam entries | [Open Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/security.txt) |
| **Family** | Privacy base + optional family categories | [Open Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/family.txt) |
| **Ultimate** | Maximum combined privacy/security profile | [Open Raw](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/ultimate.txt) |

### Recommended Pi-hole URL

```text
https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/combined/balanced.txt
```

## 🧩 Individual category lists

Use these when you want to build your own selection in Pi-hole instead of using a combined list.

| Category | Raw list |
|---|---|
| Advertising | [ads.txt](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/ads.txt) |
| Trackers | [trackers.txt](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/trackers.txt) |
| General telemetry | [telemetry.txt](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/telemetry.txt) |
| Windows telemetry | [windows-telemetry.txt](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/windows-telemetry.txt) |
| Apple telemetry | [apple-telemetry.txt](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/apple-telemetry.txt) |
| Android telemetry | [android-telemetry.txt](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/android-telemetry.txt) |
| Smart TV | [smart-tv.txt](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/smart-tv.txt) |
| IoT devices | [iot.txt](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/iot.txt) |
| Mobile tracking | [mobile-tracking.txt](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/mobile-tracking.txt) |
| Social trackers | [social-trackers.txt](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/social-trackers.txt) |
| Phishing | [phishing.txt](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/phishing.txt) |
| Malware | [malware.txt](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/malware.txt) |
| Scam / fraud | [scam.txt](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/scam.txt) |
| Cryptomining | [cryptomining.txt](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/cryptomining.txt) |
| Fake shops | [fake-shops.txt](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/fake-shops.txt) |
| Adult | [adult.txt](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/adult.txt) |
| Gambling | [gambling.txt](https://raw.githubusercontent.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists/main/lists/categories/gambling.txt) |

## 📥 Add a list to Pi-hole

1. Open the list you want above.
2. Copy the Raw URL from the browser.
3. Open Pi-hole.
4. Add the URL under your ad/block list management.
5. Update Gravity.

No Python, container or installer from this repository is required.

## ➕ Extending the repository

The structure is intentionally simple:

```text
lists/
├── combined/
│   ├── light.txt
│   ├── balanced.txt
│   ├── strict.txt
│   ├── security.txt
│   ├── family.txt
│   └── ultimate.txt
└── categories/
    ├── ads.txt
    ├── trackers.txt
    ├── telemetry.txt
    ├── windows-telemetry.txt
    ├── apple-telemetry.txt
    ├── android-telemetry.txt
    ├── smart-tv.txt
    ├── iot.txt
    ├── mobile-tracking.txt
    ├── social-trackers.txt
    ├── phishing.txt
    ├── malware.txt
    ├── scam.txt
    ├── cryptomining.txt
    ├── fake-shops.txt
    ├── adult.txt
    └── gambling.txt
```

To add a new individual list later, simply create another `.txt` file under `lists/categories/` and add its Raw link to this README.

To extend a combined list, edit the corresponding file under `lists/combined/` directly.

## ⚖️ License

Repository documentation and the original curated list collection are published under **GPL-3.0-only** with the attribution notices in `NOTICE` and `ATTRIBUTION.md`.

Copyright (C) 2026 **BlackRabbitZ**.

Original repository:

```text
https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists
```

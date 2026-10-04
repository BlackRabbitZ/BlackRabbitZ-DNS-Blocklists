# Katalog der 100 Listenarten

Die 100 Kategorien aus dem BRZ Pi-hole DNS-Listen & Kinderschutz-Handbuch (30.09.2026) sind hier auf konkrete Repo-Pfade gemappt. `vorbereitet` bedeutet: Struktur vorhanden, aber kein belastbarer Domainbestand im statischen Snapshot.

| # | Kategorie | Kanonischer Pfad | Einträge | Methode |
|---:|---|---|---:|---|
| 1 | Werbung / Ads | `lists/privacy/full/ads.txt` | 234.003 | `source` |
| 2 | Tracking | `lists/privacy/full/trackers.txt` | 113.606 | `source` |
| 3 | Analytics | `lists/privacy/full/analytics.txt` | 35.879 | `derived-keyword` |
| 4 | Telemetrie | `lists/privacy/full/telemetry.txt` | 29.163 | `source` |
| 5 | Betriebssysteme | `lists/platforms/operating-systems/main/ultimate.txt` | 308 | `generated-tier` |
| 6 | Smartphones / Mobile | `lists/platforms/mobile/main/ultimate.txt` | 1.004 | `generated-tier` |
| 7 | Smart-TV | `lists/platforms/smart-tv/main/ultimate.txt` | 646 | `generated-tier` |
| 8 | Streaming | `lists/platforms/streaming/main/ultimate.txt` | 282 | `generated-tier` |
| 9 | Gaming | `lists/apps/gaming/main/ultimate.txt` | 373 | `generated-tier` |
| 10 | Social Media | `lists/apps/social-media/main/ultimate.txt` | 21.588 | `generated-tier` |
| 11 | Google | `lists/ecosystems/full/google.txt` | 13.584 | `derived-keyword` |
| 12 | Microsoft | `lists/ecosystems/full/microsoft.txt` | 769 | `derived-keyword` |
| 13 | Apple | `lists/ecosystems/full/apple.txt` | 333 | `derived-keyword` |
| 14 | Amazon | `lists/ecosystems/full/amazon.txt` | 775 | `derived-keyword` |
| 15 | Cloud-Dienste | `lists/infrastructure/cloud-development/main/ultimate.txt` | 1.491 | `generated-tier` |
| 16 | IoT | `lists/platforms/iot-smart-home/main/ultimate.txt` | 85 | `source` |
| 17 | Sprachassistenten | `lists/platforms/voice-assistants/main/ultimate.txt` | 109 | `generated-tier` |
| 18 | Autos / Connected Cars | `lists/platforms/automotive/main/ultimate.txt` | 665 | `generated-tier` |
| 19 | NAS / Server | `lists/platforms/nas-server/main/ultimate.txt` | 63 | `generated-tier` |
| 20 | Router / Netzwerkgeräte | `lists/platforms/network-devices/main/ultimate.txt` | 383 | `generated-tier` |
| 21 | ISP / Provider | `lists/platforms/providers/main/ultimate.txt` | 171 | `generated-tier` |
| 22 | Malware | `lists/security/full/malware.txt` | 2.656.377 | `source` |
| 23 | Phishing | `lists/security/full/phishing.txt` | 577.332 | `source` |
| 24 | Scam / Betrug | `lists/security/full/scam.txt` | 265.246 | `source` |
| 25 | Spam | `lists/security/full/spam.txt` | 0 | `prepared` |
| 26 | Ransomware | `lists/security/full/ransomware.txt` | 0 | `prepared` |
| 27 | Exploit / Angriffsinfrastruktur | `lists/security/full/exploits.txt` | 0 | `prepared` |
| 28 | Cryptomining | `lists/security/full/cryptomining.txt` | 6.121 | `source` |
| 29 | DNS / Netzwerkangriffe | `lists/network/full/dns-attacks.txt` | 0 | `derived-keyword` |
| 30 | Proxy / VPN / Tor | `lists/network/main/ultimate.txt` | 309 | `generated-tier` |
| 31 | Tracking Redirects | `lists/privacy/full/tracking-redirects.txt` | 377 | `derived-keyword` |
| 32 | URL Shortener | `lists/network/full/url-shorteners.txt` | 255 | `source-misp-cc0` |
| 33 | Push Notifications | `lists/privacy/full/push-notifications.txt` | 74 | `derived-keyword` |
| 34 | Cookies / Consent | `lists/privacy/full/consent-cmp.txt` | 44 | `source` |
| 35 | Fingerprinting | `lists/privacy/full/fingerprinting.txt` | 14 | `derived-keyword` |
| 36 | Session Replay | `lists/privacy/full/session-replay.txt` | 212 | `derived-keyword` |
| 37 | Error-/Crash-Reporting | `lists/privacy/full/crash-reporting.txt` | 91 | `derived-keyword` |
| 38 | Developer Telemetry | `lists/infrastructure/cloud-development/main/ultimate.txt` | 1.491 | `generated-tier` |
| 39 | Software Telemetrie | `lists/platforms/software-hardware-telemetry/main/ultimate.txt` | 77 | `generated-tier` |
| 40 | Hardware-/Treiber-Telemetrie | `lists/platforms/software-hardware-telemetry/main/ultimate.txt` | 77 | `generated-tier` |
| 41 | E-Commerce | `lists/privacy/full/ecommerce.txt` | 44 | `derived-keyword` |
| 42 | Payment | `lists/privacy/full/payment-tracking.txt` | 0 | `derived-keyword` |
| 43 | Newsletter | `lists/privacy/full/newsletter-tracking.txt` | 166 | `derived-keyword` |
| 44 | Tracking Pixel | `lists/privacy/full/tracking-pixels.txt` | 927 | `derived-keyword` |
| 45 | CDN Tracking | `lists/privacy/full/cdn-tracking.txt` | 20 | `derived-keyword` |
| 46 | Marketing | `lists/privacy/full/marketing.txt` | 2.060 | `derived-keyword` |
| 47 | CRM | `lists/privacy/full/crm.txt` | 121 | `derived-keyword` |
| 48 | Chat / Support | `lists/privacy/full/chat-support.txt` | 64 | `derived-keyword` |
| 49 | Captcha / Anti-Bot | `lists/privacy/full/captcha-antibot.txt` | 379 | `derived-keyword` |
| 50 | Content-Empfehlungen | `lists/privacy/full/recommendations.txt` | 362 | `derived-keyword` |
| 51 | Adult / Porn | `family/content/adult.txt` | 998.924 | `source` |
| 52 | Dating | `family/content/dating.txt` | 0 | `prepared` |
| 53 | Gambling | `family/content/gambling.txt` | 420.536 | `source` |
| 54 | Drugs | `family/content/drugs.txt` | 0 | `prepared` |
| 55 | Weapons | `family/content/weapons.txt` | 0 | `prepared` |
| 56 | Violence / Gore | `family/content/violence-gore.txt` | 0 | `prepared` |
| 57 | Family Protection | `family/main/ultimate.txt` | 2.346.905 | `source` |
| 58 | Dating / Sexual Content | `family/content/sexual-content.txt` | 0 | `prepared` |
| 59 | Piracy | `family/content/piracy.txt` | 0 | `prepared` |
| 60 | Torrent | `family/content/torrents.txt` | 0 | `prepared` |
| 61 | Fake Software | `lists/security/full/fake-software.txt` | 0 | `prepared` |
| 62 | Potentially Unwanted Programs | `lists/security/full/pup-pua.txt` | 0 | `prepared` |
| 63 | Browser Extensions | `lists/security/full/malicious-extensions.txt` | 0 | `prepared` |
| 64 | Fake News / Misinformation | `family/content/misinformation.txt` | 0 | `prepared` |
| 65 | AI / KI | `lists/automation/main/ultimate.txt` | 300 | `generated-tier` |
| 66 | Crawler / Bots | `lists/automation/main/ultimate.txt` | 300 | `generated-tier` |
| 67 | Search Engines | `lists/privacy/full/search-tracking.txt` | 1 | `derived-keyword` |
| 68 | SEO | `lists/privacy/full/seo-tracking.txt` | 0 | `derived-keyword` |
| 69 | Fonts / externe Ressourcen | `lists/privacy/full/external-fonts.txt` | 3 | `derived-keyword` |
| 70 | DoH / DoT / DNS-Umgehung | `lists/network/main/ultimate.txt` | 309 | `generated-tier` |
| 71 | Bypass-Dienste | `lists/network/main/ultimate.txt` | 309 | `generated-tier` |
| 72 | Dynamic DNS | `lists/network/full/dynamic-dns.txt` | 74 | `curated-provider-roots` |
| 73 | Newly Registered Domains | `lists/security/full/newly-registered-domains.txt` | 0 | `prepared` |
| 74 | Suspicious TLDs | `policies/adblock/most-abused-tlds.adblock` | 130 | `source-hagezi-gpl3-adblock` |
| 75 | Disposable Email | `lists/security/full/disposable-email.txt` | 0 | `prepared` |
| 76 | Parked Domains | `lists/security/full/parked-domains.txt` | 0 | `prepared` |
| 77 | Expired Domains | `lists/security/full/expired-domains.txt` | 0 | `prepared` |
| 78 | Typosquatting | `lists/security/full/typosquatting.txt` | 0 | `prepared` |
| 79 | Brand Impersonation | `lists/security/full/brand-impersonation.txt` | 0 | `prepared` |
| 80 | Cybersecurity / Threat Intelligence | `lists/security/main/ultimate.txt` | 3.408.241 | `source` |
| 81 | Abuse | `lists/security/full/abuse.txt` | 0 | `prepared` |
| 82 | DDoS | `lists/security/full/ddos.txt` | 0 | `prepared` |
| 83 | Scanning | `lists/security/full/scanners.txt` | 0 | `prepared` |
| 84 | Cryptocurrency | `lists/security/full/cryptocurrency.txt` | 0 | `prepared` |
| 85 | NFT | `lists/security/full/nft.txt` | 0 | `prepared` |
| 86 | Malvertising | `lists/security/full/malvertising.txt` | 0 | `prepared` |
| 87 | Redirect Malware | `lists/security/full/malicious-redirects.txt` | 0 | `prepared` |
| 88 | Command & Control | `lists/security/full/command-control.txt` | 0 | `prepared` |
| 89 | Data Exfiltration | `lists/security/full/data-exfiltration.txt` | 0 | `prepared` |
| 90 | Cloud Storage | `lists/infrastructure/cloud-development/full/cloud-storage.txt` | 563 | `derived-keyword` |
| 91 | Remote Access | `lists/security/full/remote-access.txt` | 0 | `prepared` |
| 92 | Surveillance | `lists/security/full/surveillance.txt` | 0 | `prepared` |
| 93 | DNS Security | `lists/security/full/dns-security.txt` | 0 | `prepared` |
| 94 | Privacy | `lists/privacy/main/ultimate.txt` | 371.530 | `generated-tier` |
| 95 | Aggressive Privacy | `lists/privacy/full/aggressive-privacy.txt` | 652 | `generated-bundle` |
| 96 | Safe / Balanced | `profiles/normal.txt` | 342.216 | `source` |
| 97 | Strict | `profiles/pro-plus.txt` | 383.624 | `source` |
| 98 | Allowlist | `allowlists/false-positives.txt` | 0 | `manual` |
| 99 | Regionale Listen | `lists/regional/de.txt` | 0 | `prepared` |
| 100 | Herstellerlisten | `lists/manufacturers/microsoft.txt` | 754 | `derived-keyword` |

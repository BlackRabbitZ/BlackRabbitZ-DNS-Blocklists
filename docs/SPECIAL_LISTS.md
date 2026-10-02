# Speziallisten

Diese Repo enthaelt neben den Light/Normal/Pro/Pro++/Ultimate-Profilen eigenstaendige Speziallisten.

- **BRZ-native/abgeleitete Listen** sind direkt im Repository enthalten.
- **Live-Upstreams** koennen optional mit `scripts/update-special-lists.py` manuell aktualisiert werden.
- Es existiert **kein automatischer Fremdlisten-Workflow**.

## Risikoklassen

Listen wie Dynamic DNS, Most Abused TLDs, SafeSearch-not-supported, VPN/Proxy-Bypass und Badware-Hoster koennen legitime Dienste blockieren. Sie sollten zunaechst einer Testgruppe zugeordnet werden.

## Formate

Die normalen `.txt`-Dateien sind Plain-Domain-Listen. `policies/adblock/most-abused-tlds.adblock` ist absichtlich eine Adblock-Suffixliste, weil ganze TLDs nicht korrekt als normale Domainliste modelliert werden koennen. IP-Speziallisten werden vom manuellen Updater separat erzeugt und gehoeren nicht in normale Domain-Profile.

# DNS-Rebind-Schutz mit Pi-hole

**🌐 Sprache / Language:** 🇩🇪 **Deutsch** · [🇬🇧 English](DNS_REBIND_PROTECTION_EN.md)

HaGeZis archivierter Punkt 17 verwendete eine spezielle Rebind-Liste für AdGuard/AdGuard Home. Für BlackRabbitZ wird diese Liste **nicht als normale Pi-hole-Adlist kopiert**, weil Pi-hole/FTL auf dnsmasq-Funktionen für DNS-Rebind-Schutz zurückgreifen kann.

Pi-hole dokumentiert, dass A- und AAAA-Antworten bei aktiviertem `stop-dns-rebind` gegen mögliche Rebind-Angriffe geprüft werden. Benötigte lokale Ausnahmen können mit `rebind-domain-ok=/domain/` zugelassen werden.

Offizielle Pi-hole-Dokumentation:

```text
https://docs.pi-hole.net/ftldns/dnsmasq_warn/
```

## dnsmasq-Direktiven

Die relevanten Direktiven lauten:

```text
stop-dns-rebind
rebind-domain-ok=/fritz.box/
```

Die zweite Zeile ist **nur ein Beispiel** für eine lokale Domain, die absichtlich auf private Adressen auflösen darf. Verwende ausschließlich Ausnahmen, die du in deinem eigenen Netzwerk tatsächlich benötigst.

> Der genaue Weg, benutzerdefinierte dnsmasq-/FTL-Optionen einzubinden, hängt von deiner Pi-hole-Version und Installationsart ab. Prüfe deshalb die aktuelle Pi-hole-Dokumentation deiner Installation, bevor du Konfigurationsdateien änderst.

## Warum das keine Blockliste ist

DNS-Rebinding wird anhand der **DNS-Antwort/IP-Adresse** erkannt. Eine statische Liste bekannter Domains kann dieses Problem nicht vollständig und zuverlässig abbilden. Resolver-seitiger Rebind-Schutz ist für Pi-hole deshalb die passendere Umsetzung.

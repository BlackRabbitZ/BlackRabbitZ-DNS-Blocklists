# DNS Rebind Protection with Pi-hole

**🌐 Language / Sprache:** [🇩🇪 Deutsch](DNS_REBIND_PROTECTION.md) · 🇬🇧 **English**

HaGeZi's archived point 17 used a dedicated rebind list for AdGuard/AdGuard Home. BlackRabbitZ does **not copy it as a normal Pi-hole Adlist**, because Pi-hole/FTL can use dnsmasq's DNS rebind protection functionality.

Pi-hole documents that A and AAAA responses are checked for possible rebind attacks when `stop-dns-rebind` is enabled. Required local exceptions can be allowed with `rebind-domain-ok=/domain/`.

Official Pi-hole documentation:

```text
https://docs.pi-hole.net/ftldns/dnsmasq_warn/
```

## dnsmasq directives

Relevant directives are:

```text
stop-dns-rebind
rebind-domain-ok=/fritz.box/
```

The second line is **only an example** of a local domain that is intentionally allowed to resolve to private addresses. Add only exceptions that your own network actually requires.

> The exact method for supplying custom dnsmasq/FTL options depends on your Pi-hole version and installation method. Check the current Pi-hole documentation for your installation before changing configuration files.

## Why this is not a blocklist

DNS rebinding is detected from the **DNS answer/IP address**. A static list of known domains cannot model this problem completely or reliably. Resolver-side rebind protection is therefore the more appropriate Pi-hole implementation.

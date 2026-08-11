# Methodology

This project is intentionally **not a mirror, fork or transformation of HaGeZi or another blocklist**.

## Inclusion rules

A domain may be added when there is independent evidence that the hostname primarily serves:
- advertising,
- cross-site/user tracking or measurement,
- non-essential product telemetry,
- confirmed malicious infrastructure.

Evidence should come from direct observation, vendor documentation, packet/DNS logs, reproducible test cases, or a community report that can be independently verified.

## Exclusion rules

Do not add:
- domains copied from third-party blocklists merely because they appear there,
- domains without independently verifiable rationale,
- essential authentication/CDN/update endpoints unless there is a narrowly scoped reason,
- entire parent domains when a specific hostname is sufficient.

## False positives

Functional breakage wins over list size. A domain is removed or allowlisted when blocking causes material breakage and the privacy/security benefit does not justify it.

## Threat data

Threat domains are deliberately empty in v1.0.0. Threat intelligence expires quickly and needs stricter provenance, freshness and evidence handling than ordinary ad/tracker curation.

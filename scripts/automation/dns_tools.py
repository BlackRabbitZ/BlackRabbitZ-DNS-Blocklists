#!/usr/bin/env python3
from __future__ import annotations

import concurrent.futures
import re
import shutil
import subprocess
from dataclasses import dataclass

DEFAULT_RESOLVERS = ("1.1.1.1", "8.8.8.8")
STATUS_RE = re.compile(r"status:\s*([A-Z]+)")


@dataclass(frozen=True)
class DNSResult:
    domain: str
    classification: str
    statuses: tuple[str, ...]


def query_status(domain: str, resolver: str, timeout: int = 2) -> str:
    if not shutil.which("dig"):
        raise RuntimeError("'dig' wurde nicht gefunden. Auf GitHub ubuntu-latest ist dnsutils vorinstalliert.")
    command = [
        "dig",
        f"@{resolver}",
        domain,
        "A",
        f"+time={timeout}",
        "+tries=1",
        "+noall",
        "+comments",
    ]
    try:
        proc = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=max(3, timeout + 2),
            check=False,
        )
    except subprocess.TimeoutExpired:
        return "TIMEOUT"
    output = f"{proc.stdout}\n{proc.stderr}"
    match = STATUS_RE.search(output)
    if match:
        return match.group(1).upper()
    if proc.returncode != 0:
        return "ERROR"
    return "UNKNOWN"


def classify_domain(
    domain: str,
    resolvers: tuple[str, ...] = DEFAULT_RESOLVERS,
    timeout: int = 2,
) -> DNSResult:
    statuses: list[str] = []
    for resolver in resolvers:
        status = query_status(domain, resolver, timeout=timeout)
        statuses.append(status)
        # NOERROR means the DNS name exists even if the requested A RRset is empty.
        if status == "NOERROR":
            return DNSResult(domain, "exists", tuple(statuses))
    if statuses and all(status == "NXDOMAIN" for status in statuses):
        return DNSResult(domain, "nxdomain", tuple(statuses))
    return DNSResult(domain, "temporary", tuple(statuses))


def check_domains(
    domains: list[str] | set[str],
    *,
    resolvers: tuple[str, ...] = DEFAULT_RESOLVERS,
    timeout: int = 2,
    workers: int = 32,
) -> list[DNSResult]:
    ordered = sorted(set(domains))
    if not ordered:
        return []
    results: list[DNSResult] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        futures = {
            pool.submit(classify_domain, domain, resolvers, timeout): domain
            for domain in ordered
        }
        for future in concurrent.futures.as_completed(futures):
            domain = futures[future]
            try:
                results.append(future.result())
            except Exception as exc:
                results.append(DNSResult(domain, "temporary", (f"EXCEPTION:{type(exc).__name__}",)))
    return sorted(results, key=lambda item: item.domain)

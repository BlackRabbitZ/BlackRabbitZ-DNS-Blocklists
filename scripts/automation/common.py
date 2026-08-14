#!/usr/bin/env python3
from __future__ import annotations

import ipaddress
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATEGORY_DIR = ROOT / "lists" / "categories"
ALLOWLIST_PATH = ROOT / "config" / "allowlist.txt"

DOMAIN_RE = re.compile(
    r"^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?\.)+"
    r"[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?$",
    re.IGNORECASE,
)
SKIP_NAMES = {
    "localhost",
    "localhost.localdomain",
    "broadcasthost",
    "ip6-localhost",
    "ip6-loopback",
}


def normalize_domain(value: str) -> str | None:
    value = value.strip().lower().rstrip(".")
    if value.startswith("*."):
        value = value[2:]
    value = value.lstrip(".")
    value = value.split("^", 1)[0].split("$", 1)[0].strip()
    if not value or value in SKIP_NAMES:
        return None
    try:
        ipaddress.ip_address(value)
        return None
    except ValueError:
        pass
    try:
        value = value.encode("idna").decode("ascii")
    except (UnicodeError, ValueError):
        return None
    return value if DOMAIN_RE.fullmatch(value) else None


def payload_lines(path: Path):
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        for raw in handle:
            text = raw.strip()
            if text and not text.startswith(("#", "!")):
                yield text


def load_allowlist(path: Path = ALLOWLIST_PATH) -> set[str]:
    if not path.exists():
        return set()
    result: set[str] = set()
    for raw in payload_lines(path):
        domain = normalize_domain(raw)
        if domain:
            result.add(domain)
    return result


def is_allowlisted(domain: str, allowlist: set[str]) -> bool:
    return any(domain == item or domain.endswith("." + item) for item in allowlist)


def category_files() -> list[Path]:
    return sorted(CATEGORY_DIR.glob("*.txt"))


def remove_domains_from_file(path: Path, domains: set[str]) -> int:
    if not domains or not path.exists():
        return 0
    removed = 0
    output: list[str] = []
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        for raw in handle:
            text = raw.strip()
            normalized = None if not text or text.startswith(("#", "!")) else normalize_domain(text)
            if normalized in domains:
                removed += 1
                continue
            output.append(raw.rstrip("\n\r"))
    path.write_text("\n".join(output) + "\n", encoding="utf-8", newline="\n")
    return removed

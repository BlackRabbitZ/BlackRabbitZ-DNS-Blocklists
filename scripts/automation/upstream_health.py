#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import urllib.error
import urllib.request
from pathlib import Path

from common import ROOT

CONFIG = ROOT / "scripts" / "upstream-sources.json"


def load_sources() -> list[dict]:
    data = json.loads(CONFIG.read_text(encoding="utf-8"))
    found: dict[str, dict] = {}
    for category, settings in data.get("categories", {}).items():
        for source in settings.get("sources", []):
            url = source.get("url")
            if not url:
                continue
            item = found.setdefault(url, {"url": url, "names": [], "categories": []})
            item["names"].append(str(source.get("name", url)))
            item["categories"].append(category)
    return sorted(found.values(), key=lambda item: item["url"])


def probe(source: dict, timeout: int, sample_bytes: int) -> dict:
    request = urllib.request.Request(
        source["url"],
        headers={
            "User-Agent": "BlackRabbitZ-DNS-Blocklists-Health/1.0",
            "Accept": "text/plain,*/*;q=0.8",
            "Accept-Encoding": "identity",
            "Range": f"bytes=0-{sample_bytes - 1}",
        },
    )
    result = {
        "url": source["url"],
        "names": sorted(set(source["names"])),
        "categories": sorted(set(source["categories"])),
        "status": "error",
        "http_status": None,
        "content_length": None,
        "sample_sha256": None,
        "error": None,
    }
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read(sample_bytes)
            result["http_status"] = int(getattr(response, "status", 200) or 200)
            length = response.headers.get("Content-Length")
            content_range = response.headers.get("Content-Range")
            total = None
            if content_range and "/" in content_range:
                tail = content_range.rsplit("/", 1)[1]
                if tail.isdigit():
                    total = int(tail)
            if total is None and length and length.isdigit() and result["http_status"] == 200:
                total = int(length)
            result["content_length"] = total
            result["sample_sha256"] = hashlib.sha256(body).hexdigest()
            result["status"] = "ok" if 200 <= result["http_status"] < 400 and body else "error"
    except urllib.error.HTTPError as exc:
        result["http_status"] = exc.code
        result["error"] = f"HTTP {exc.code}"
    except Exception as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--sample-bytes", type=int, default=65536)
    parser.add_argument("--fail-on-error", action="store_true")
    args = parser.parse_args()

    sources = load_sources()
    results: list[dict] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = [pool.submit(probe, source, args.timeout, args.sample_bytes) for source in sources]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    results.sort(key=lambda item: item["url"])
    ok = sum(item["status"] == "ok" for item in results)
    failed = len(results) - ok
    payload = {"schema_version": 1, "sources": results, "summary": {"total": len(results), "ok": ok, "failed": failed}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload["summary"], indent=2))
    for item in results:
        if item["status"] != "ok":
            print(f"WARN {item['url']}: {item['error'] or item['http_status']}")
    return 1 if args.fail_on_error and failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

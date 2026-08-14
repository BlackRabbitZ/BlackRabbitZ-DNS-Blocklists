#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def by_url(payload: dict) -> dict[str, dict]:
    return {item["url"]: item for item in payload.get("sources", [])}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--current", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--max-drop", type=float, default=0.70, help="Alarm bei Größenabfall unter diesen Anteil, Standard 70 %")
    parser.add_argument("--max-growth", type=float, default=3.0, help="Alarm bei Wachstum über diesen Faktor")
    args = parser.parse_args()

    current = json.loads(args.current.read_text(encoding="utf-8"))
    if not args.baseline.exists():
        report = {"schema_version": 1, "bootstrap": True, "alerts": [], "message": "Noch keine Baseline vorhanden."}
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print("Keine Baseline vorhanden; erster Lauf dient als Bootstrap.")
        return 0

    baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
    old = by_url(baseline)
    now = by_url(current)
    alerts: list[dict] = []
    for url, item in now.items():
        previous = old.get(url)
        if item.get("status") != "ok":
            alerts.append({"url": url, "type": "unreachable", "detail": item.get("error") or item.get("http_status")})
            continue
        if not previous or previous.get("status") != "ok":
            continue
        old_size = previous.get("content_length")
        new_size = item.get("content_length")
        if isinstance(old_size, int) and old_size > 0 and isinstance(new_size, int):
            ratio = new_size / old_size
            if ratio < args.max_drop:
                alerts.append({"url": url, "type": "size_drop", "old": old_size, "new": new_size, "ratio": round(ratio, 4)})
            elif ratio > args.max_growth:
                alerts.append({"url": url, "type": "size_growth", "old": old_size, "new": new_size, "ratio": round(ratio, 4)})
    for url in sorted(set(old) - set(now)):
        alerts.append({"url": url, "type": "source_removed_from_probe"})

    report = {"schema_version": 1, "bootstrap": False, "alerts": alerts, "alert_count": len(alerts)}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if alerts:
        for alert in alerts:
            print(f"ALARM: {json.dumps(alert, ensure_ascii=False)}")
        return 2
    print("Keine ungewöhnlichen Upstream-Änderungen erkannt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

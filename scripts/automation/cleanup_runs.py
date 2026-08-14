#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timedelta, timezone

API = "https://api.github.com"


def request(path: str, token: str, method: str = "GET") -> dict | None:
    req = urllib.request.Request(
        API + path,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "BlackRabbitZ-Actions-Cleanup/1.0",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        if response.status == 204:
            return None
        return json.loads(response.read().decode("utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=30)
    parser.add_argument("--keep", type=int, default=15)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    repo = os.environ.get("GITHUB_REPOSITORY")
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    current = int(os.environ.get("GITHUB_RUN_ID", "0") or 0)
    if not repo or not token:
        raise SystemExit("GITHUB_REPOSITORY/GITHUB_TOKEN fehlen")

    runs: list[dict] = []
    page = 1
    while True:
        payload = request(f"/repos/{repo}/actions/runs?per_page=100&page={page}", token) or {}
        chunk = payload.get("workflow_runs", [])
        runs.extend(chunk)
        if len(chunk) < 100:
            break
        page += 1
        if page > 20:
            break

    grouped: dict[int, list[dict]] = defaultdict(list)
    for run in runs:
        grouped[int(run["workflow_id"])].append(run)
    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
    delete: list[dict] = []
    for workflow_runs in grouped.values():
        ordered = sorted(workflow_runs, key=lambda r: r["created_at"], reverse=True)
        protected = {int(run["id"]) for run in ordered[: args.keep]}
        for run in ordered[args.keep :]:
            created = datetime.fromisoformat(run["created_at"].replace("Z", "+00:00"))
            if created < cutoff and int(run["id"]) not in protected and int(run["id"]) != current and run.get("status") == "completed":
                delete.append(run)

    print(f"Gefundene alte Runs zum Löschen: {len(delete)}")
    for run in delete:
        print(f"  {run['id']} | {run.get('name')} | {run.get('created_at')}")
        if not args.dry_run:
            request(f"/repos/{repo}/actions/runs/{run['id']}", token, method="DELETE")
    print("Dry-run: nichts gelöscht." if args.dry_run else f"Gelöscht: {len(delete)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

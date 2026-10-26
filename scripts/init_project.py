#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


DIRECTORIES = ("00-config", "01-sources", "02-raw", "03-normalized", "04-evidence", "05-drafts", "06-deliverables", "07-audit")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a resumable academic/case writing project scaffold.")
    parser.add_argument("destination", type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument("--genre", choices=("academic-paper", "literature-review", "teaching-case", "mixed"), default="academic-paper")
    parser.add_argument("--timezone", default="Asia/Shanghai")
    args = parser.parse_args()

    root = args.destination.resolve()
    if root.exists() and any(root.iterdir()):
        raise SystemExit(f"destination is not empty: {root}")
    root.mkdir(parents=True, exist_ok=True)
    for name in DIRECTORIES:
        (root / name).mkdir()

    now = datetime.now(ZoneInfo(args.timezone))
    state = {
        "schema_version": 1,
        "project": {"title": args.title, "genre": args.genre, "timezone": args.timezone},
        "created_at": now.isoformat(),
        "status": "initialized",
        "counts": {"sources": 0, "records": 0, "candidate_evidence": 0, "verified_evidence": 0, "blocked": 0},
        "gates": {},
        "exceptions": [],
    }
    (root / "00-config" / "project-state.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

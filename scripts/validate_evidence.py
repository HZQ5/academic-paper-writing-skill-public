#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED = ("evidence_id", "source_id", "claim", "locator", "quote", "status", "source_genre", "focal_status")
ALLOWED_STATUS = {"candidate", "verified", "rejected", "blocked"}
ALLOWED_FOCAL = {"focal", "secondary", "not-applicable", "unclear"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate workbench evidence JSONL.")
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    errors: list[str] = []
    seen: set[str] = set()
    count = 0
    for line_no, raw in enumerate(args.input.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        count += 1
        try:
            item = json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_no}: invalid JSON: {exc}")
            continue
        missing = [key for key in REQUIRED if item.get(key) in (None, "")]
        if missing:
            errors.append(f"line {line_no}: missing {', '.join(missing)}")
        eid = str(item.get("evidence_id", ""))
        if eid in seen:
            errors.append(f"line {line_no}: duplicate evidence_id {eid}")
        seen.add(eid)
        if item.get("status") not in ALLOWED_STATUS:
            errors.append(f"line {line_no}: invalid status {item.get('status')!r}")
        if item.get("focal_status") not in ALLOWED_FOCAL:
            errors.append(f"line {line_no}: invalid focal_status {item.get('focal_status')!r}")
        if item.get("status") == "verified" and len(str(item.get("quote", "")).strip()) < 5:
            errors.append(f"line {line_no}: verified quote is too short")
    report = {"records": count, "errors": errors, "valid": not errors}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())

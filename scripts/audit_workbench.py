#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


DATE_PREFIX = re.compile(r"^\d{8}-.+")
REQUIRED_DIRS = ("00-config", "01-sources", "02-raw", "03-normalized", "04-evidence", "05-drafts", "06-deliverables", "07-audit")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a workbench project scaffold and required gates.")
    parser.add_argument("project", type=Path)
    parser.add_argument("--require-gate", action="append", default=[])
    args = parser.parse_args()
    root = args.project.resolve()
    failures: list[str] = []
    warnings: list[str] = []
    missing_dirs = [name for name in REQUIRED_DIRS if not (root / name).is_dir()]
    if missing_dirs:
        failures.append("missing directories: " + ", ".join(missing_dirs))
    state_path = root / "00-config" / "project-state.json"
    state = {}
    if not state_path.exists():
        failures.append("missing 00-config/project-state.json")
    else:
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            failures.append(f"invalid project state: {exc}")
    gates = state.get("gates", {}) if isinstance(state, dict) else {}
    for gate in args.require_gate:
        if gates.get(gate) is not True:
            failures.append(f"required gate not passed: {gate}")
    deliverables = root / "06-deliverables"
    if deliverables.is_dir():
        for path in sorted(p for p in deliverables.iterdir() if p.is_file() and not p.name.startswith(".")):
            if not DATE_PREFIX.match(path.name):
                failures.append(f"deliverable lacks YYYYMMDD- prefix: {path.name}")
    for path in root.rglob("*"):
        if path.is_file() and path.stat().st_size > 25_000_000:
            warnings.append(f"large file requires redistribution/privacy review: {path.relative_to(root)}")
    report = {"project": str(root), "failures": failures, "warnings": warnings, "passed": not failures}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())

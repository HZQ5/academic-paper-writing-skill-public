#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


PATTERNS = {
    "private-key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "github-token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "openai-key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "personal-path": re.compile(r"/(?:Users|home)/[^/\s]+/"),
}
TEXT_SUFFIXES = {".md", ".txt", ".py", ".json", ".yaml", ".yml", ".toml", ".csv", ".tsv", ".sh"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan distributable text for common secrets and personal absolute paths.")
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    findings = []
    for path in sorted(args.root.resolve().rglob("*")):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_no, line in enumerate(text.splitlines(), 1):
            # Regex definitions in this scanner necessarily contain their own
            # signatures; scanning them would make a clean repository fail.
            if path.name == Path(__file__).name and "re.compile" in line:
                continue
            for kind, pattern in PATTERNS.items():
                if pattern.search(line):
                    findings.append({"file": str(path.relative_to(args.root.resolve())), "line": line_no, "kind": kind})
    print(json.dumps({"findings": findings, "passed": not findings}, ensure_ascii=False, indent=2))
    return 0 if not findings else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import difflib
import json
import re
import sys
import unicodedata
from pathlib import Path


REFERENCE_DIR = Path(__file__).resolve().parents[1] / "references" / "journal-data"
FILES = {
    "swufe_2025_journal_tiers.csv": ("SWUFE 2025", "journal_title", "tier", "discipline"),
    "abs_ajg_2024_3plus.csv": ("ABS AJG 2024", "journal_title", "ajg_2024", "field"),
    "ft50_2026_status.csv": ("FT50 2026", "journal_title", "ft50_2026", "change_status"),
    "utd24_current.csv": ("UTD24 verified 2026-07-25", "journal_title", None, None),
    "utd24_ft50_legacy_image_snapshot.csv": ("LEGACY UTD/FT image snapshot", "journal_title", "ft50_snapshot", "utd24_snapshot"),
}


def normalize(value: str) -> str:
    text = unicodedata.normalize("NFKC", value).casefold().replace("&", " and ")
    text = re.sub(r"\b(?:the|and)\b", " ", text)
    return re.sub(r"\s+", " ", re.sub(r"[^\w\u3400-\u9fff]+", " ", text)).strip()


def load() -> list[dict[str, str]]:
    records = []
    for filename, (system, title_field, tier_field, detail_field) in FILES.items():
        with (REFERENCE_DIR / filename).open(encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                title = row[title_field]
                tier = "YES" if tier_field is None else row.get(tier_field, "")
                detail = "" if detail_field is None else row.get(detail_field, "")
                records.append({"system": system, "journal": title, "tier": tier, "detail": detail, "_key": normalize(title)})
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description="Look up audited journal-list snapshots.")
    parser.add_argument("journals", nargs="+")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    records = load()
    keys = {row["_key"]: row["journal"] for row in records}
    results = []
    for query in args.journals:
        key = normalize(query)
        matches = [{k: v for k, v in row.items() if not k.startswith("_")} for row in records if row["_key"] == key]
        suggestions = [] if matches else [keys[k] for k in difflib.get_close_matches(key, keys, n=5, cutoff=0.7)]
        results.append({"query": query, "matches": matches, "suggestions": suggestions})
    if args.json:
        json.dump(results, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    else:
        for result in results:
            print(f"## {result['query']}")
            if result["matches"]:
                for match in result["matches"]:
                    print(f"- {match['system']}: {match['tier']} {match['detail']}".rstrip())
            else:
                print("- No exact match in bundled snapshots.")
                if result["suggestions"]:
                    print("- Suggestions: " + "; ".join(result["suggestions"]))
        print("\nCurrent/latest claims require verification against the official list owner.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

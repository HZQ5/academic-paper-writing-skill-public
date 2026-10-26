#!/usr/bin/env python3
"""Install the bundled Skill without network access or overwriting files."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import tempfile

NAME = "academic-paper-writing"
PAYLOAD = ("SKILL.md", "agents", "references", "scripts", "assets")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", choices=("codex", "claude", "cursor", "generic"), default="generic")
    parser.add_argument("--dest", type=Path, help="Skills parent directory; the skill name is appended")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    home = Path.home()
    roots = {
        "codex": Path(os.environ.get("CODEX_HOME", str(home / ".codex"))) / "skills",
        "claude": home / ".claude" / "skills",
        "cursor": home / ".cursor" / "skills",
        "generic": home / ".agents" / "skills",
    }
    parent = (args.dest if args.dest is not None else roots[args.target]).expanduser().resolve()
    destination = parent / NAME
    source = Path(__file__).resolve().parent
    if destination.exists() or destination.is_symlink():
        parser.error(f"Destination already exists; nothing was changed: {destination}")
    for entry in PAYLOAD:
        path = source / entry
        if not path.exists():
            parser.error(f"Missing required payload: {entry}")
        if path.is_symlink() or (path.is_dir() and any(p.is_symlink() for p in path.rglob("*"))):
            parser.error(f"Refusing symbolic links in payload: {entry}")
    print(f"Destination: {destination}")
    if args.dry_run:
        print("Dry run: no files created.")
        return 0
    parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".academic-skill-", dir=parent) as tmp:
        staged = Path(tmp) / NAME
        staged.mkdir()
        for entry in PAYLOAD:
            src = source / entry
            if src.is_dir():
                shutil.copytree(src, staged / entry, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"))
            else:
                shutil.copy2(src, staged / entry)
        destination.mkdir()
        try:
            for child in staged.iterdir():
                shutil.move(str(child), str(destination / child.name))
        except BaseException:
            shutil.rmtree(destination)
            raise
    print("Installed as an optional supplement; installation is not consent to use it.")
    print("Existing skills and other conversations must remain unaffected.")
    print("Recommendation: open a separate chat and test with a copy or example first.")
    print("You may adapt, remove or iterate these rules; they are not universal academic standards.")
    print("Autonomous invocation requires explicit user consent in the current task.")
    print("Refresh the host's Skill list or open a new session to discover the Skill.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

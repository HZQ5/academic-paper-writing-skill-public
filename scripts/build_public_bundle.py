#!/usr/bin/env python3
"""Rebuild or check the repository's portable Markdown and SHA-256 manifest."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {".git", "__pycache__", ".venv", ".pytest_cache"}
EXCLUDED_NAMES = {"MANIFEST.json", ".DS_Store", ".env"}
HEADER = """# 学术论文写作：单文件便携规则

**第一原则：仅作补充。安装或读取不等于启用；AI 自主调用前须先询问用户。不改写已有 Skill，不干扰其他对话。建议独立聊天测试。在自己的 Fork 或本地副本中自由迭代，不回写作者正式版，不把它作为统一标准。**

完整约束见下方 SKILL.md 首节；仅在用户明确同意的当前任务范围内应用。本文包含全部 Markdown 参考，章节与语言规范均已内置，不需要额外子 Skill。相对路径指向完整版文件，单文件使用时可按“文件”标题查找相应内容。期刊 CSV 与脚本需要完整包，不得假装已查询或运行。
"""


def portable_text(root: Path) -> str:
    paths = [root / "SKILL.md", *sorted((root / "references").rglob("*.md"))]
    return HEADER + "".join(
        f"\n\n---\n\n## 文件：{p.relative_to(root).as_posix()}\n\n"
        + p.read_text(encoding="utf-8").rstrip() + "\n"
        for p in paths
    )


def release_paths(root: Path) -> list[Path]:
    result = []
    for p in sorted(root.rglob("*")):
        rel = p.relative_to(root)
        if set(rel.parts) & EXCLUDED_PARTS or p.name in EXCLUDED_NAMES or p.suffix == ".pyc":
            continue
        if p.is_symlink():
            raise ValueError(f"Refusing symbolic link in release: {rel}")
        if p.is_file():
            result.append(p)
    return result


def manifest_text(root: Path) -> str:
    files = []
    for p in release_paths(root):
        data = p.read_bytes()
        files.append({"path": p.relative_to(root).as_posix(), "bytes": len(data),
                      "sha256": hashlib.sha256(data).hexdigest()})
    return json.dumps({
        "skill": "academic-paper-writing", "file_count": len(files), "files": files,
        "source_commit": "95568a02902de76adbee1630aac2439716ca96bd",
        "manifest_excludes": ["MANIFEST.json", ".git/", "__pycache__/", ".venv/",
                              ".pytest_cache/", ".DS_Store", ".env", "*.pyc"],
        "edition": "consent-first-self-contained-writing",
    }, ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report drift without writing")
    args = parser.parse_args()
    if not (ROOT / "install.py").is_file() or not (ROOT / "README.md").is_file():
        parser.error("Run this maintainer script in a full repository copy, not an installed Skill.")
    for name, build in (("PORTABLE.md", portable_text), ("MANIFEST.json", manifest_text)):
        expected = build(ROOT)
        path = ROOT / name
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                print(f"OUT OF DATE: {name}")
                return 1
        else:
            path.write_text(expected, encoding="utf-8")
    print("Portable rules and manifest verified." if args.check else "Portable rules and manifest rebuilt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

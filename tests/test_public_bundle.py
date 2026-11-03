"""Packaging checks; these are not a substitute for testing an AI's writing."""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("bundle", ROOT / "scripts/build_public_bundle.py")
BUNDLE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUNDLE)


def file_hashes(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob("*") if p.is_file() and "__pycache__" not in p.parts}


class PublicBundleTests(unittest.TestCase):
    def test_portable_contains_every_reference_verbatim(self):
        self.assertEqual((ROOT / "PORTABLE.md").read_text(), BUNDLE.portable_text(ROOT))
        portable = (ROOT / "PORTABLE.md").read_text()
        for p in (ROOT / "references").rglob("*.md"):
            self.assertIn(p.read_text().rstrip(), portable, str(p))

    def test_manifest_matches_exact_release_files(self):
        self.assertEqual(json.loads((ROOT / "MANIFEST.json").read_text()),
                         json.loads(BUNDLE.manifest_text(ROOT)))

    def test_entrypoint_routes_to_local_modules(self):
        entry = (ROOT / "SKILL.md").read_text()
        paths = re.findall(r"`(references/[^`]+\.md)`", entry)
        self.assertTrue(paths)
        for rel in paths:
            self.assertTrue((ROOT / rel).is_file(), rel)
        for rel in ("04-academic-writing.md", "11-language-calibration.md", "12-writing-examples.md"):
            self.assertIn("references/" + rel, paths)
        self.assertNotIn("use the independent `academic-language-calibration`", entry)

    def test_relative_markdown_links_resolve(self):
        for p in [ROOT / "README.md", *(ROOT / "references").rglob("*.md")]:
            for link in re.findall(r"\]\(([^)\s]+)\)", p.read_text()):
                if "://" in link or link.startswith("#"):
                    continue
                target = (p.parent / link.split("#")[0]).resolve()
                self.assertTrue(target.is_relative_to(ROOT), f"Outside package: {link}")
                self.assertTrue(target.exists(), f"Broken link in {p}: {link}")

    def test_isolated_install_and_repeat_refusal(self):
        with tempfile.TemporaryDirectory(prefix="public-skill-test-") as folder:
            parent = Path(folder)
            sentinel = parent / "other-skill" / "SKILL.md"
            sentinel.parent.mkdir()
            sentinel.write_text("Existing user skill: do not modify")
            cmd = [sys.executable, str(ROOT / "install.py"), "--dest", str(parent)]
            self.assertEqual(subprocess.run(cmd + ["--dry-run"], capture_output=True).returncode, 0)
            self.assertFalse((parent / "academic-paper-writing").exists())
            result = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            installed = parent / "academic-paper-writing"
            for rel in ("SKILL.md", "references/04-academic-writing.md",
                        "references/11-language-calibration.md", "references/12-writing-examples.md"):
                self.assertEqual((ROOT / rel).read_bytes(), (installed / rel).read_bytes())
            before = file_hashes(parent)
            again = subprocess.run(cmd, capture_output=True, text=True)
            self.assertNotEqual(again.returncode, 0)
            self.assertIn("Destination already exists", again.stderr)
            self.assertEqual(before, file_hashes(parent))
            self.assertEqual(sentinel.read_text(), "Existing user skill: do not modify")

    def test_generated_check_rejects_mutated_copy(self):
        with tempfile.TemporaryDirectory(prefix="public-skill-drift-") as folder:
            root = Path(folder)
            (root / "references").mkdir()
            (root / "SKILL.md").write_text("original entry")
            (root / "references/test.md").write_text("original reference")
            expected = BUNDLE.portable_text(root)
            (root / "references/test.md").write_text("changed reference")
            self.assertNotEqual(expected, BUNDLE.portable_text(root))
            before = BUNDLE.manifest_text(root)
            (root / "references/test.md").write_text("another changed reference")
            self.assertNotEqual(before, BUNDLE.manifest_text(root))


if __name__ == "__main__":
    unittest.main()

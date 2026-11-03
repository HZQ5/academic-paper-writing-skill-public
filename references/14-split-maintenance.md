# Public edition maintenance

Derived from `HZQ5/academic-paper-writing-skill`, source commit `95568a02902de76adbee1630aac2439716ca96bd`, retrieved 2026-10-26. The original is private and is not a runtime dependency. Public repository: `HZQ5/academic-paper-writing-skill-public`. Skill name: `academic-paper-writing`.

Preserved: paper argument/revision rules, evidence boundaries, historical writing references, dated journal-list snapshots and five Python helpers. Historical preferences are optional, not universal academic requirements. Their references to earlier topic materials are provenance notes, not runtime dependencies.

Adapted: removed private four-repository synchronization from runtime requirements; added portable use, public installation documentation, a local installer and a single-file fallback. The 2026-11-03 revision embeds generic chapter guidance, bilingual language calibration and constructed examples. Ordinary writing no longer routes to a separate language Skill. Zotero and document tools are optional for text work but required for claims about actual app operations or dynamic citation fields.

Maintain this edition independently. Validate instructions and relative references, run affected scripts, scan for secrets/personal paths, and update `MANIFEST.json`. Keep private manuscripts, participant data, credentials, review originals, model weights and local databases out of the repository. Never synchronize another repository or overwrite an installed Skill without authorization.

From the repository root, run `python3 scripts/build_public_bundle.py` to rebuild `PORTABLE.md` and the SHA-256 manifest, then run the same command with `--check` and `python3 -m unittest discover -s tests -v`. The manifest excludes itself and development/cache metadata. Tests verify packaging and installation boundaries, not model behaviour, research validity or acceptance by a journal.

No blanket open-source license is inferred from the source. Journal-list snapshots retain their source owners' rights and are historical lookup aids; check issuing bodies for current information and reuse conditions.

The author's public `main` is frozen by repository branch rules. Others may iterate their own Fork/local copy for installation, use and personal needs; never push, merge or synchronize changes into the author's current version or remove its protections. The author must separately authorize and unlock any future official update. This permission does not expand rights to third-party journal data.

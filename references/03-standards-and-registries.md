# Standards and registries

## File naming

Name each newly created user-facing deliverable `YYYYMMDD-meaningful-name.ext` using the exact event/source date when supplied, otherwise the creation date in the user's timezone. Do not rename required platform files such as `SKILL.md`, `README.md`, `package.json`, or `Dockerfile`.

## Journal registries

Keep each list/version in a separate field. Never invent a universal grade.

Recommended fields:

- journal canonical name and aliases;
- UTD24 status and verification date;
- FT50 status and effective version;
- ABS/AJG edition and grade;
- institution-specific list and edition (for example SWUFE 2025);
- Chinese lists: CSSCI/CSSCI source collection, AMI, Peking University Core, CSCD where relevant;
- discipline and match note;
- official source URL.

Interpret “not listed” only as absence from that registry. Verify requests for the current/latest UTD24, FT50, AJG, CSSCI, AMI, PKU Core, or institutional list against the official owner because lists change. Preserve historical snapshots as `legacy`, not `current`.

Useful official starting points:

- UTD24: <https://jsom.utdallas.edu/the-utd-top-100-business-school-research-rankings/list-of-journals>
- FT50: <https://www.ft.com/ft50-journals>
- AJG: Chartered Association of Business Schools journal guide site
- Chinese registries: use the issuing institution's official notice/database or a user-supplied authoritative file.

The bundled `scripts/lookup_journal_rank.py` queries the audited SWUFE 2025, ABS/AJG 2024 (3/4/4* subset), FT50 2026, UTD24, and explicitly labeled legacy snapshot tables. These tables support reproducible historical/local lookup; current claims still require official verification.

## Citation and quotation

1. Follow the target journal, school, or template rule when supplied.
2. Otherwise agree on author–date or numbered style before drafting.
3. Preserve DOI, source record key, page, and exact quote outside the prose for audit.
4. Distinguish focal evidence from a secondary citation.
5. Do not invent authors, years, pages, DOIs, references, or access dates.
6. Ensure every in-text citation has a reference entry and every reference entry is cited unless the target style permits a bibliography.

## Academic typography

Treat a supplied template as the source of truth. When no template is supplied, use a conservative editable baseline and label it as a default, not an institutional rule:

- Chinese body: 宋体/SimSun or the institution's required CJK font, usually 10.5–12 pt.
- English body: Times New Roman or target-journal font, usually 10.5–12 pt.
- Headings: use true Word heading styles with restrained size hierarchy.
- Tables: consistent units, notes, source line, decimal precision, and no clipped cells.
- Figures: readable at final page width with editable captions and source notes.
- Pages: stable margins, widow/orphan control, page numbers, and automatic TOC where needed.

Never claim a default matches a school or journal without a verified guideline. Render final DOCX/PDF and inspect visually.

## Source labeling

For case/news material, attach `fact`, `inference`, `assumption`, `forecast`, or `recommendation`. For academic sources, attach genre, identification strength, focal/secondary status, and validation status.

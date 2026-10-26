# Quality, privacy, and release

## Structural QA

- Validate `SKILL.md` frontmatter and every relative reference.
- Run included scripts on sample inputs.
- Ensure intermediate state can resume.
- Check every in-text citation/reference pair and every exhibit/table source.
- Run the workbench audit and inspect all warnings.

## DOCX/PDF/Spreadsheet QA

- Use real heading styles, consistent fonts, automatic TOC/page numbers when needed.
- Inspect tables, figures, captions, source notes, page breaks, clipped text, blank pages, and CJK fallback fonts.
- Render every final DOCX/PDF and inspect page images or contact sheets.
- Verify spreadsheet formulas, types, filters, frozen headers, units, data validation, source sheets, and totals.

## Privacy and security audit

Search for credentials, tokens, cookies, API keys, emails, participant identifiers, unpublished source text, absolute home/Desktop paths, and local database files. Replace personal paths with parameters and examples. Do not commit raw corpora unless redistribution is authorized.

## Skill publication

For an explicitly requested Skill release, validate one canonical copy, build a SHA-256 manifest, and verify remote files and requested visibility. This Skill does not authorize publishing a user's manuscript, dataset or review, changing repository visibility, or updating private backup repositories. Research projects remain private unless their owner requests otherwise. Preserve third-party rights; licensing and visibility are separate decisions.

## Final report

For a Skill release, report source, validation, script checks, privacy findings, manifest, remote commit and actual visibility. For ordinary writing, report the requested output, evidence limitations and unavailable capabilities without imposing a release workflow.

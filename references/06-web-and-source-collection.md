# Web and source collection

## Source hierarchy

1. User-supplied files and authorized local/reference managers.
2. Official publisher, regulator, company, institution, journal, or database pages.
3. Structured APIs, feeds, sitemaps, and exports.
4. Authenticated browser collection within the user's access.
5. General web discovery for locating primary sources.

## Collection contract

Define start URLs or records, include/exclude scope, date boundary, fields, full-text requirement, maximum pages/records, authentication, rate restraint, and output schema before a batch.

## Resumable crawl

1. Prefer API/export/`llms.txt`/`sitemap.xml` for URL discovery.
2. Canonicalize URLs and enforce origin/path/glob scope.
3. Use breadth-first collection with visited, queue, failures, depth, and checkpoint state.
4. Save one record per page/item immediately.
5. Separate HTML/metadata from extracted main text and downloaded files.
6. Test 1–2 records before a full batch.
7. Use polite pacing; do not bypass CAPTCHAs, paywalls, robots rules, or access controls.
8. Report success, failures, missing fields, duplicates, and coverage.

## Catalog and news extraction

Preserve list-page position, detail URL, stable ID, title, author/organization, date, category, abstract/body, attachments, source label, retrieved time, and extraction method. Match records by stable ID first, canonical URL second, normalized title only as fallback.

## Research use

Web material can document chronology, organizational statements, policies, markets, and public phenomena. It does not automatically support causal or scholarly consensus claims. Archive locators and quote snippets; honor copyright limits when sharing.

## PDF and binary files

Record link provenance before download. Verify identity after download. Treat supplementary files, book reviews, appendices, and alternate versions separately from the focal document.

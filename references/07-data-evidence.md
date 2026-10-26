# Data, cleaning, coding, and evidence

## Layered data model

Maintain separate layers:

```text
raw → parsed → normalized → matched/deduplicated → coded candidate → verified evidence → synthesis/output
```

Never overwrite raw values. Store transformations, tool/version, timestamp, and reason.

## Stable identity and matching

Prefer DOI, Zotero key, official record ID, canonical URL, ISBN, or content hash. Normalize Unicode, whitespace, punctuation, case, and known aliases for comparison while preserving originals. Use fuzzy title matching only to create review candidates. Audit identical file hashes attached to different parent records.

## Literature evidence

At minimum record title, authors, year, venue, DOI/key, document genre, method/data, X/Y or propositions where applicable, theory, mechanism, boundary, finding, identification strength, PDF identity, page, quote, focal/secondary status, and validation status.

Do not force X/Y into conceptual, qualitative, policy, book, or computational records. Use `not applicable`, `unclear`, or `needs review`.

## Qualitative/case coding

Use a stable source/item ID and locator. Record first-order evidence, descriptive code, second-order theme, aggregate dimension, temporal phase, mechanism role, counterevidence, confidence, memo, and follow-up question. Keep chronology and negative cases visible. A coding table is an analytical aid, not proof by itself.

## Data cleaning gates

- schema and type validation;
- missingness and unexpected nulls;
- duplicate and collision report;
- range/category/unit checks;
- date/timezone normalization;
- join cardinality and unmatched keys;
- reproducible transformation log;
- sample/manual spot check;
- aggregate reconciliation with source counts.

## Evidence acceptance

Accept direct writing evidence only when the source identity is verified, the page/locator exists, the exact quote is found or visually verified, focal/secondary status is known, and the proposed claim preserves genre and boundary. Keep candidate and accepted evidence separate.

---
id: pattern-parser-selection-contract
type: pattern
title: Parser Selection and Ingestion Contract
status: reviewed
privacy: public
confidence: 0.88
created_at: 2026-08-12T18:42:00+02:00
updated_at: 2026-08-12T18:42:00+02:00
review_at: 2026-11-12
source_ids:
  - source-document-parsing-evidence-2026
relations:
  - predicate: derived_from
    target: source-document-parsing-evidence-2026
---

# Parser Selection and Ingestion Contract

## Selection rule

Choose parsers by document-slice and downstream task. Keep native text parsing
as the latency/cost control, then add layout OCR or a VLM parser only for slices
where paired replay shows a material outcome gain.

## Typed output contract

Each parsed element carries document/version/page identity, element type,
reading order, hierarchy path, bounding box when available, raw text, normalized
text, parser/model/config identity and confidence/failure flags. Tables, formulas
and figures remain typed objects rather than flattened prose.

## Evaluation

- field and character fidelity where deterministic labels exist;
- reading-order and hierarchy accuracy;
- table cell/record fidelity and cross-page continuity;
- formula, caption, footnote and figure retention;
- downstream evidence Recall@k and citation-anchor validity;
- latency, cost, failure rate and manual-review load by slice.

## Rollout

Shadow-index the candidate parser, dual-read a stable query set, and retain the
old parse/index until promotion. Kill on missing pages, ACL/provenance loss,
silent truncation or a hard downstream regression.

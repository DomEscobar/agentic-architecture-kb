---
id: pattern-chunking-technique-catalog
type: pattern
title: Chunking Technique Catalog and Routing Matrix
status: reviewed
privacy: public
confidence: 0.9
created_at: 2026-08-12T20:51:00+02:00
updated_at: 2026-08-12T20:51:00+02:00
review_at: 2026-10-12
source_ids:
  - source-chunking-landscape-2026-08
relations:
  - predicate: derived_from
    target: source-chunking-landscape-2026-08
  - predicate: depends_on
    target: pattern-chunking-baseline-ablation
---

# Chunking Technique Catalog and Routing Matrix

## Controls

- Fixed token windows provide a reproducible size baseline.
- Recursive splitting provides a cheap boundary-aware baseline.
- Sliding overlap tests whether boundary recall justifies duplicate index cost.

## Natural and document structure

- Sentence windows suit local claims whose neighbors disambiguate them.
- Paragraph or section-aware chunks preserve author structure with a size cap.
- Markdown title-chain chunks retain hierarchical location in technical content.
- Table-aware chunks preserve headers, rows and key-value relationships.
- AST chunks preserve functions, classes and sibling code nodes.
- Conversation chunks preserve complete turns, speakers and bounded episodes.

## Generated or contextual units

- Semantic splitting detects embedding-distance topic boundaries but is not a
  universal improvement over cheaper controls.
- Proposition chunking indexes atomic self-contained claims for fine fact lookup.
- Contextual prefixes add document-specific explanatory text before indexing.
- Late chunking embeds long context before pooling into chunk embeddings.

## Multi-granular retrieval

- Parent-child retrieval searches small units and returns their larger parent.
- Neighbor expansion retrieves a hit and bounded adjacent source units.
- Hierarchical summary trees support questions spanning multiple abstraction levels.
- Adaptive or mixture selection chooses granularity per document or query class.
- Tree navigation avoids a flat chunk index but still creates hierarchical nodes;
  “no chunking” must not be interpreted as no segmentation or summarization.

## Routing defaults

Start with fixed and structure-aware candidates. Use proposition units for atomic
fact questions, parent-child for fine matching plus broad answer context, AST for
code, table-aware for relational rows, turn-aware for conversations, and hierarchy
for synthesis across long documents. Promote prefixes, semantic, late, adaptive or
LLM-generated structures only when paired evaluation pays for their added cost and
failure surface.

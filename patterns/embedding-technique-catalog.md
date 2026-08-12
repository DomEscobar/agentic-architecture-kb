---
id: pattern-embedding-technique-catalog
type: pattern
title: Embedding Technique Catalog and Migration Routing
status: reviewed
privacy: public
confidence: 0.92
created_at: 2026-08-12T22:09:00+02:00
updated_at: 2026-08-12T22:09:00+02:00
review_at: 2026-10-12
source_ids:
  - source-embedding-landscape-2026-08
relations:
  - predicate: derived_from
    target: source-embedding-landscape-2026-08
  - predicate: depends_on
    target: pattern-embedding-selection-migration
---

# Embedding Technique Catalog and Migration Routing

## Baselines and modes

- A general dense encoder is the semantic control; multilingual dense is required when query and corpus languages differ.
- Learned sparse retrieval preserves inspectable term dimensions and lexical expansion, but needs compatible sparse infrastructure.
- Dense-sparse hybrid retrieval protects both paraphrase and exact-identifier slices; fusion weights are evaluation parameters.
- Multi-vector late interaction preserves token-level evidence at higher index and scoring cost.

## Specialization

- Domain adaptation is justified only after a zero-shot model fails stable domain slices and trustworthy positives or carefully audited pseudo-labels exist.
- Long-input encoders prevent silent truncation but do not prove that embedding an entire document is better than structure-aware units.
- Matryoshka-compatible truncation reduces index bytes only for models explicitly trained or adapted for nested dimensions.
- Quantized indexes are a memory/latency candidate only after full-precision replay; preserve a rescoring path when ranking drift matters.
- Asymmetric encoders require a pinned query/passage instruction, tokenizer, pooling and normalization contract across every client.

## Migration contract

Every index manifest records model and tokenizer revisions, instructions, normalization, dimension, truncation, chunk manifest and source hashes. Re-embedding uses an immutable challenger index. Promotion requires coverage checks, paired replay, shadow or dual-read, latency/cost gates and alias rollback rehearsal.

## Default route

Start with BM25, incumbent dense and one strong multilingual dense challenger under fixed chunking. Add hybrid for identifier-heavy corpora, multi-vector for fine-grained matching, long-input only for measured truncation failures, and adaptation only after cheaper failures are localized.

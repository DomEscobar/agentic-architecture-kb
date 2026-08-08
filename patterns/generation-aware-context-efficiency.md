---
id: pattern-generation-aware-context-efficiency
type: pattern
title: Generation-aware Context Efficiency
status: reviewed
privacy: internal
confidence: 0.82
created_at: 2026-08-08T18:35:00+02:00
updated_at: 2026-08-08T18:35:00+02:00
review_at: 2026-10-08
source_ids:
  - source-rag-developments-2026-batch-2
relations:
  - predicate: derived_from
    target: source-rag-developments-2026-batch-2
---

# Generation-aware Context Efficiency

## Distinct optimization surfaces

- **Index compression:** reduce stored retrieval representations, as
  MarginMerge does for visual patch vectors.
- **Candidate utility:** select documents or document sets for downstream answer
  value, as in InfoGain-RAG and CORAG.
- **Context compression:** shorten or encode the evidence shown to the model.
- **Inference optimization:** reduce prefill/decoding work and KV-cache pressure,
  as in REFRAG.

These mechanisms are complementary but not interchangeable. Every optimization
must state which surface and metric it changes.

## Evaluation contract

Measure retrieval nDCG/Recall, evidence coverage, final grounded accuracy,
unsupported claims, stored bytes, index/query latency, time to first token,
throughput and total cost. Compare at equal evidence and answer-quality targets.

For learned utility scorers, test generator swaps and calibration drift. For
visual compression, retain hard slices with small text, tables, diagrams and
cross-page references. For runtime-specific decoding, require hardware-local
benchmarks and a fallback to the standard model serving path.

## Maturity rule

Do not make a days-old preprint or a custom decoding kernel the default path.
Run it as an optional projection or canary until independent or internal replay
confirms quality retention and operating benefit.


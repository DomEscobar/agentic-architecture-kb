---
id: pattern-memory-read-routing
type: pattern
title: Type-Aware Memory Read and Retrieval
status: reviewed
privacy: internal
confidence: 0.9
created_at: 2026-08-09T16:10:00+02:00
updated_at: 2026-08-09T16:10:00+02:00
review_at: 2026-10-09
source_ids: [source-agent-memory-foundations-2026, source-agent-memory-evaluation-security-2026]
relations:
  - predicate: derived_from
    target: source-agent-memory-foundations-2026
  - predicate: evaluated_by
    target: source-agent-memory-evaluation-security-2026
---

# Type-Aware Memory Read and Retrieval

## Read contract

1. Classify intent and required memory types.
2. Apply tenant, user, project, privacy, status and validity filters before
   lexical or semantic retrieval.
3. Load run state by exact identity; retrieve episodes by time plus lexical/
   semantic similarity; retrieve facts by hybrid search; use graph traversal
   only for relational questions; select procedures by verified preconditions.
4. Fuse/rerank candidates without discarding provenance or trust metadata.
5. Surface active contradictions and superseded values when relevant.
6. Load a bounded evidence packet, then log what was used and the outcome.

Evaluate retrieval separately from reading and action. Report Recall@k,
Precision@k, MRR/nDCG, abstention, distractor robustness, latency and cost.
Cross-tenant retrieval is a zero-tolerance gate.


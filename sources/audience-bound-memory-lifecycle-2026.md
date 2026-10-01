---
id: source-audience-bound-memory-lifecycle-2026
type: source
title: Audience-Bound Persistent Memory Lifecycle Evidence 2026
status: reviewed
privacy: public
confidence: 0.76
created_at: 2026-10-01T11:27:00+02:00
updated_at: 2026-10-01T11:27:00+02:00
review_at: 2026-11-30
auditability: public
source_ids: []
relations:
  - predicate: supports
    target: pattern-agent-memory-evaluation-blueprint
---

# Audience-Bound Persistent Memory Lifecycle Evidence — 2026

Primary: [Audience-Bound Persistent Memory, arXiv:2609.36373v1](https://arxiv.org/html/2609.36373v1), inspected 2026-10-01. Author-reported preprint with a stated formal argument and an ancillary research artifact; no independent reproduction performed.

## Mechanism and observed result

An item inherits the audience of the conversation where it was recorded. Derived items partition, intersect audiences, or are suppressed; a grant is exact and object-specific, not a unioned or inheritable wildcard. Before *each physical model attempt*, including retry/fallback, the assembled context admits a current item only if every resolved viewer is inside an authorized audience. Unresolved identity fails closed. The paper proves conditional context-exclusion and exhaustive-retrieval policy completeness **assuming** correct transport identity, provenance, and complete mediation; it does not prove that a deployed resolver or all context paths satisfy those assumptions.

The authors report a prospectively frozen synthetic comparison over 10,000 multi-party histories and 200,000 assembled contexts: no inadmissible items in the two separately persisted reference implementations, against forbidden inclusion in 82% of unscoped contexts. Entitled recall matched policy-equivalent baselines; an additional superiority comparison with unscoped retrieval reported +0.30 Recall@5. Wrong-principal substitutions were too rare to establish the prespecified joint decision. These are the paper's §5–6 numbers, not production leakage rates.

## Limits and KB use

The ancillary artifact is described as containing oracle, two stores, conformance tests and analysis; large per-history outputs and the native-runtime source slice are withheld until a final version. This audit did not run the artifact. The guarantee excludes forged transport identities, misresolved principals, same-audience contextual-integrity violations, action authorization, physical erasure and injection. This extends the existing tenant/owner and pre-injection gates in `pattern-agent-memory-evaluation-blueprint`, not a claim that a new policy oracle is production-proven.

Test group-to-DM reuse, ambiguous viewer identities, derivation from mixed audiences, exact grant/revocation, and retries across model attempts. Compare entitled recall and forbidden *context inclusion*, not only output leakage; fail any unauthorized attempt regardless of aggregate quality.

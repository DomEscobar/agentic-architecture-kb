---
id: pattern-rag-security-and-retrieval-governance
type: pattern
title: RAG Security and Retrieval Governance
status: reviewed
privacy: public
confidence: 0.91
created_at: 2026-08-13T14:10:00+02:00
updated_at: 2026-08-13T14:10:00+02:00
review_at: 2026-10-13
source_ids: [source-agentic-security-landscape-2026-08]
relations:
  - predicate: derived_from
    target: source-agentic-security-landscape-2026-08
  - predicate: applies_to
    target: synthesis-rag-pipeline-taxonomy
---

# RAG Security and Retrieval Governance

## Security pipeline

```text
source admission -> quarantine -> parse in sandbox -> classify + ACL + lineage
       -> immutable version/hash -> embed/index -> authorization-first retrieval
       -> injection and anomaly signals -> independent-source corroboration
       -> bounded untrusted context -> cited answer -> output policy -> audit
```

Authorization must run before or inside candidate generation. Post-retrieval
filtering can already disclose forbidden content to caches, logs, rerankers or
the model. Tenant, user, document, field, purpose, jurisdiction, time and
version scopes must travel with every candidate and parent or neighbor
expansion. Missing or stale ACL metadata fails closed.

## Ingestion and index controls

- Admit only authenticated connectors and attributed sources. Quarantine new,
  changed, user-uploaded and externally synchronized content until policy and
  malware or hidden-content checks complete.
- Parse untrusted files without host credentials or unrestricted network and
  filesystem access. Preserve the original blob, parser version, extracted
  structure, hashes and transformations.
- Separate trust domains and tenants physically or with independently tested
  logical controls. Encrypt source objects, indexes, caches and transport.
- Monitor index membership, source hashes, ACL drift, unusual embedding
  distributions, targeted query dominance and deletion propagation.
- Treat embeddings as sensitive derived data. Test extraction and inversion
  risk; do not assume vectors anonymize their source.

## Retrieval and context controls

- Propagate user and agent identity into retrieval. Apply deny-by-default ACL,
  privacy, retention and version predicates before scoring.
- Label retrieved content as untrusted evidence, delimit it from instructions
  and cap chunks, tokens, source concentration and recursion.
- Use multi-source verification only across independently governed provenance
  domains. Require source diversity or abstain for consequential claims; two
  chunks derived from one compromised source count as one source.
- Use injection classifiers, LLM verification prompts and anomaly detectors as
  defense signals. They can quarantine or escalate but cannot grant access or
  authorize tools.
- Bind citations to exact retrieved source versions and validate that claims
  are supported. If retrieval, ACL, integrity or citation validation fails,
  abstain or return a scoped error rather than silently fall back to model-only
  generation.

## Required evaluations

- poisoned documents, hidden text, conflicting sources and targeted retriever
  manipulation;
- cross-tenant, revoked-access, stale-cache, parent-expansion and metadata-
  missing leakage;
- embedding inversion and index-exfiltration probes appropriate to the data;
- indirect prompt injection that attempts tool use, memory writes or source
  suppression;
- source-diversity spoofing and correlated upstream compromise;
- deletion through source, chunks, embeddings, indexes, caches and traces;
- citation entailment, unsupported synthesis, PII and secret output leakage;
- fail-closed behavior for unavailable policy, integrity and verification
  services.

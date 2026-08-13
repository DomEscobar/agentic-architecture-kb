---
id: pattern-agentic-rag-security-architecture
type: pattern
title: Agentic RAG Security Architecture
status: reviewed
privacy: public
confidence: 0.9
created_at: 2026-08-13T14:10:00+02:00
updated_at: 2026-08-13T14:10:00+02:00
review_at: 2026-10-13
source_ids: [source-agentic-security-landscape-2026-08]
relations:
  - predicate: derived_from
    target: source-agentic-security-landscape-2026-08
  - predicate: depends_on
    target: pattern-agentic-runtime-security-boundary
  - predicate: depends_on
    target: pattern-rag-security-and-retrieval-governance
---

# Agentic RAG Security Architecture

## Combined threat boundary

Agentic RAG compounds risks because retrieved content can influence planning,
tool calls and durable memory. A poisoned document can become an instruction;
delegated authority can drift across retrieval and agent hops; a malicious
summary can persist after the original session; and retries can amplify one
compromised decision into cascading effects.

```text
identity + intent
      |
      v
bounded controller ---- budgets / kill switch / trace
      |
      v
authorization-first retrieval <---- governed corpus + provenance
      |
      v
untrusted evidence gate ---- injection / integrity / diversity signals
      |
      v
planner proposes action ---- no authority is inherited from evidence
      |
      v
policy gateway ---- approval if high risk ---- isolated tool executor
      |
      +---- effect receipt
      +---- quarantined memory candidate, never direct canonical write
```

## Decision rule

Break the combination of sensitive data, untrusted input and external action at
multiple independent boundaries. If all three are present, require strict
runtime isolation, current identity propagation, authorization-first retrieval,
deterministic tool policy, and human approval for high-impact effects. If the
system is read-only over a public curated corpus, a smaller bounded controller
can omit credentials, code execution and approval while retaining corpus
integrity, citation, injection and budget gates.

## Practical release checklist

1. Inventory and risk-classify agents, corpora, tools, identities and effects.
2. Threat-model every data and authority transition, including cache, memory,
   reranker, verifier and observability sinks.
3. Implement least privilege, short-lived delegation, source admission,
   authorization-first retrieval, isolated execution and deterministic policy.
4. Add multi-source verification where independent sources exist; otherwise
   make abstention and human escalation explicit.
5. Run OWASP-aligned adversarial traces plus corpus-specific poisoning,
   cross-tenant, MCP, sandbox, recovery and cascading-failure tests.
6. Canary with read-only or shadow execution, monitor policy decisions and
   anomalous retrieval, and rehearse kill, revoke, quarantine and rollback.

No deployment is promoted from checklist completion alone. The release record
must identify the tested versions, threat model, protected cases, deterministic
oracle results, residual probabilistic detection rates and unresolved risks.

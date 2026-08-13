---
id: source-agentic-security-landscape-2026-08
type: source
title: Agentic Runtime and RAG Security Evidence Audit August 2026
status: reviewed
privacy: public
confidence: 0.9
created_at: 2026-08-13T14:10:00+02:00
updated_at: 2026-08-13T14:10:00+02:00
review_at: 2026-10-13
source_ids: []
relations: []
---

# Agentic Runtime and RAG Security Evidence Audit — August 2026

This audit covers the security boundary created when probabilistic model output
can influence retrieval, memory, tools, code execution, other agents and
external side effects. It distinguishes taxonomies and implementation guidance
from controls with independently measured effectiveness.

## Primary sources

- [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/)
- [OWASP LLM01 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/),
  [LLM06 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/),
  [LLM08 Vector and Embedding Weaknesses](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/)
  and [RAG Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html)
- [Microsoft zero-trust guidance for autonomous agents](https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-agentic-systems)
  and [least privilege for agent identities](https://learn.microsoft.com/en-us/security/zero-trust/sfi/least-privilege-for-ai-agents)
- [AWS security principles for agentic AI](https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/)
  and [Agentic AI Lens security principles](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/security-design-principles.html)
- [NIST CAISI analysis of agent-security RFI responses](https://www.nist.gov/publications/summary-analysis-responses-request-information-regarding-security-considerations-ai)
- [PoisonedRAG, USENIX Security 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/zou)
- [Kubernetes SIGs Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox)
  and [Azure Container Apps dynamic sessions](https://learn.microsoft.com/en-us/azure/container-apps/sessions)
- [Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit)
- [A2AS paper](https://arxiv.org/abs/2510.13825) and
  [IBM runtime-security article](https://www.ibm.com/think/insights/agentic-ai-runtime-security)
- [Databricks DASF v3 conference description](https://www.databricks.com/dataaisummit/session/move-fast-stay-secure-enterprise-ai-agent-security-practice)

## Confirmed security model

OWASP's agentic taxonomy names goal hijacking, tool misuse, identity and
privilege abuse, agentic supply-chain vulnerabilities and unexpected code
execution among its top risks. The LLM taxonomy separately covers prompt
injection, excessive agency and vector or embedding weaknesses. These lists are
threat taxonomies, not proof that one product or prompt mitigates the risks.

The strongest repeated architecture principle across OWASP, AWS and Microsoft
is to keep authorization and safety enforcement outside model reasoning.
Retrieved text, tool output, memory, peer-agent messages and generated code are
untrusted inputs. Every action must be checked against current user delegation,
agent identity, resource scope, arguments, risk, budget and effect state by a
deterministic policy boundary.

PoisonedRAG demonstrates that a small number of crafted corpus entries can
steer selected answers in a large retrieval corpus. Its reported attack rates
are benchmark-specific; they establish a practical attack surface, not a
universal production compromise rate. The defensive implication is broader:
source approval, lineage, quarantine, index integrity, authorization-before-
retrieval, cross-source corroboration and fail-closed behavior must be tested as
one pipeline.

## Tool and framework corrections

The Microsoft repository found during this audit is
`microsoft/agent-governance-toolkit`, not `microsoft/agent-rag-governance`. It
implements a policy-interception and audit layer and includes RAG-related
controls, but it is a public-preview implementation candidate, not a security
standard or automatic trust boundary. Pin a release and test policy bypass,
adapter coverage, identity propagation, fail-closed behavior and upgrade
rollback before adoption.

A2AS defines behavior certificates, authenticated prompts, security boundaries,
in-context defenses and codified policies. Its paper and vendor descriptions
make it E2 design evidence. A signed declaration describes intended authority;
it does not prove runtime conformance unless an external monitor enforces and
audits it.

Kubernetes Agent Sandbox and Azure Container Apps sessions provide concrete
isolation substrates. Their existence does not make arbitrary configuration
safe: egress, host mounts, secrets, kernel boundary, resource quotas, image
provenance, lifecycle cleanup and tenant mapping remain deployment tests.

## Evidence boundaries and unresolved claims

Databricks publicly describes DASF v3 and its focus on the combination of
sensitive data, untrusted inputs and external actions. The exact claim of
"35 new agentic risks plus six controls" was not confirmed in an accessible
primary artifact during this review, so it is not promoted into the knowledge
base. DASF remains E2 vendor framework guidance until the versioned artifact and
control inventory can be audited directly.

No reviewed source establishes perfect prompt-injection detection, universally
safe verification prompting or a universally trusted agent framework. Multiple
retrieval sources improve resilience only when they have independent trust
provenance; duplicating the same poisoned upstream through two indexes is not
corroboration. Model-based scanners and verifier prompts are signals, never the
sole authorization or action-safety control.

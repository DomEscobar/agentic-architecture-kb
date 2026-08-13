---
id: source-agentic-security-verification-2026-08
type: source
title: Agentic Security Cross-verification Audit August 2026
status: reviewed
privacy: public
confidence: 0.91
created_at: 2026-08-13T16:55:00+02:00
updated_at: 2026-08-13T16:55:00+02:00
review_at: 2026-10-13
source_ids: []
relations: []
---

# Agentic Security Cross-verification Audit — August 2026

This second-pass audit cross-checks security claims against peer-reviewed
benchmarks, official protocol specifications, reviewed advisories, current
repository state and community failure reports. Community posts are used only
to discover cases that can be reproduced or verified elsewhere.

## Benchmarks and attack evidence

- [AgentDojo, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html)
  provides a dynamic tool-use environment with benign utility tasks and prompt-
  injection security cases.
- [InjecAgent, Findings of ACL 2024](https://aclanthology.org/2024.findings-acl.624/)
  covers indirect prompt injection, harmful actions and data exfiltration across
  tool-integrated agents.
- [AgentDyn](https://arxiv.org/abs/2602.03117) and
  [Indirect Prompt Injections: Are Firewalls All You Need?](https://arxiv.org/abs/2510.05244)
  are recent preprints showing that static benchmark saturation can hide weak
  attacks, flawed oracles and over-defense. They support adaptive attacks and
  utility controls, but remain E2 until peer review or independent replication.
- [AgentSecBench](https://arxiv.org/abs/2605.26269) formalizes instruction,
  retrieval-confidentiality and capability-integrity games. Its key distinction
  between model-visible annotations and enforcing projections is useful E2
  methodology rather than a universal security proof.

The convergent result is not a reliable universal attack percentage. It is that
tool-using agents need paired utility/security evaluation, adaptive attacks,
deterministic external-state oracles and explicit authority boundaries. A
defense that reaches zero attacks on one frozen benchmark is not established as
secure against changed tools, models, tasks or adaptive attackers.

## Protocol and extension evidence

The [MCP authorization specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)
requires resource or audience binding for protected HTTP servers and forbids
token passthrough. The current
[MCP security guidance](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices)
also covers per-client consent, session hijacking, one-click local server
installation and least privilege. MCP provides interoperability; it does not
make tool descriptions, local commands, project configuration or server output
trusted.

Reviewed advisories establish concrete cross-layer failures:

- [GHSA-8q5r-mmjf-575q](https://github.com/advisories/GHSA-8q5r-mmjf-575q):
  attacker-controlled project MCP configuration in a pull request could execute
  on a privileged automation runner before version 1.0.74.
- [GHSA-7r34-79r5-rcc9](https://github.com/advisories/GHSA-7r34-79r5-rcc9):
  unauthenticated SSRF in an MCP server could reach internal services and inject
  attacker-controlled responses into agent context before version 0.17.0.
- [GHSA-3q26-f695-pp76](https://github.com/advisories/GHSA-3q26-f695-pp76):
  indirect instructions in Git history could reach command-injection-prone MCP
  tools.
- [GHSA-9mqq-jqxf-grvw](https://github.com/advisories/GHSA-9mqq-jqxf-grvw):
  path traversal through an MCP tool could become persistent code execution.
- [GHSA-c67j-w6g6-q2cm](https://github.com/advisories/GHSA-c67j-w6g6-q2cm):
  model-controlled serialized fields could reach a deserialization path and
  extract secrets in affected LangChain versions.

These incidents do not imply that MCP or one framework is inherently unsafe.
They show why configuration, transport, tool schema, serialization, network and
runtime execution must be evaluated as one authority chain.

## Security tooling and repository verification

Repository metadata and latest releases were checked on 2026-08-13. All listed
projects were active and non-archived at that time.

- [AgentDojo](https://github.com/ethz-spylab/agentdojo): benchmark environment;
  latest observed release `v0.1.35`. No root `SECURITY.md` was found at the
  expected path.
- [Microsoft PyRIT](https://github.com/microsoft/PyRIT): flexible red-team
  orchestration; latest observed release `v1.0.1`; security policy present.
- [NVIDIA garak](https://github.com/NVIDIA/garak): model vulnerability scanner;
  latest observed release `v0.16.0`; security policy present.
- [promptfoo](https://github.com/promptfoo/promptfoo): eval and red-team runner;
  latest observed release `0.122.0`; its security policy explicitly states that
  configurations and referenced code are trusted and not sandboxed.
- [Cisco Skill Scanner](https://github.com/cisco-ai-defense/skill-scanner) and
  [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector): best-effort
  static and optional model-assisted extension scanners. Passing scans are not
  proof of benign behavior.
- [Kubernetes SIGs Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox)
  and [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox): sandbox
  control planes with current releases and security policies. The configured
  runtime, mounts, egress, secrets and tenancy determine the actual boundary.
- [Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit):
  policy and audit implementation candidate; latest observed release `v4.1.0`;
  version-specific application tests remain required.

Tool claims are E2 maintainer evidence. Activity, releases and a security policy
are health signals, not comparative effectiveness. The
[PyRIT v0.12.1 security release](https://github.com/microsoft/PyRIT/releases/tag/v0.12.1)
is an especially important counterexample: a remotely loaded poisoned dataset
could reach unsafe template rendering. Security evaluation tooling must itself
run with isolated credentials, filesystem and egress.

## Community and forum signals

Recent Reddit and GitHub discussions surfaced weak regex-only injection filters,
multi-turn attacks, agent-team trust gaps and proxy defenses reporting perfect
scores on selected benchmarks. These are useful hypothesis generators, but the
reports use small or self-selected datasets and sometimes promote the author's
own product. No performance number from a forum post is promoted here. Their
reproducible lesson is converted into tests: preserve benign controls, include
multi-turn and adaptive variants, record seeds and versions, and verify claimed
blocks against authoritative tool state.

## Durable conclusions

1. Test security and benign utility together; otherwise refusal is mistaken for
   protection.
2. Add adaptive attacks and changed tool schemas after tuning; frozen public
   suites are development sets, not final holdouts.
3. Enforce authority by projection, policy, isolation and validation, not by
   prompt annotations or scanner verdicts alone.
4. Treat skills, MCP configuration, eval fixtures, reports and red-team tools as
   executable supply-chain inputs.
5. Keep the exact component version, configuration, model, attack corpus,
   oracle and residual failures in every security release record.

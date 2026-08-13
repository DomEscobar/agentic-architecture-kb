---
id: pattern-agentic-runtime-security-boundary
type: pattern
title: Agentic Runtime Security Boundary
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
    target: pattern-runtime-safety-baseline
---

# Agentic Runtime Security Boundary

## Control-plane invariant

The model proposes; deterministic infrastructure authorizes and executes. A
prompt, model guardrail, verifier agent or behavior certificate may inform a
decision but cannot be the only enforcement point for data access, code
execution, privilege changes or irreversible effects.

```text
user + agent identity + delegated scope
                  |
untrusted input -> planner -> proposed action
                              |
                              v
                 deterministic policy gateway
                   | deny | approve | allow
                   v                  v
             audit + alert      isolated executor
                                      |
                           effect ledger + receipt
```

## Required layers

1. Inventory every agent, owner, model, tool, MCP server, data source, memory
   store and downstream effect. Version the inventory and expire unused agents.
2. Assign a unique agent identity and preserve the invoking user's delegation
   chain. Mint short-lived, task-scoped credentials after policy evaluation.
3. Allowlist tool operations and validate canonical arguments. Recheck current
   authority immediately before execution and commit.
4. Run generated code and risky parsers in an isolated, disposable environment
   with bounded CPU, memory, processes, storage, time and network egress.
5. Require an approval interrupt for irreversible, financial, external,
   privilege-changing or ambiguous actions. Bind approval to the exact action.
6. Keep append-only decision and effect records with redacted inputs, policy
   version, identity, causal operation ID and authoritative result.
7. Enforce step, token, cost, fan-out, delegation and wall-time limits outside
   the model. Provide a tested kill switch and credential revocation path.

## Trust and adoption gate

An open-source governance or sandbox project is a component candidate, not a
trusted system. Evaluate a pinned release for adapter completeness, default
policy, bypass paths, credential handling, isolation boundary, telemetry,
security response, migration and rollback. Compare it against a minimal custom
policy gateway on the same adversarial traces.

## Minimum security evaluations

- direct and indirect goal hijacking through users, documents, tool output,
  memory and peer-agent messages;
- unauthorized tool, parameter, resource and tenant access;
- stale delegation, approval replay and privilege escalation after resume;
- sandbox escape, secret access, egress bypass and resource exhaustion;
- MCP manifest drift, tool-name collision and dependency compromise;
- duplicate side effects, cascading retries, budget bypass and kill-switch
  response;
- audit gaps, log injection, trace correlation failure and incident replay.

Promotion requires zero deterministic authorization bypasses in the protected
suite. Detection rates for probabilistic scanners must be reported separately
with false positives and adaptive attacks.

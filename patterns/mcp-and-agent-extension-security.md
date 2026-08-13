---
id: pattern-mcp-and-agent-extension-security
type: pattern
title: MCP and Agent Extension Security
status: reviewed
privacy: public
confidence: 0.92
created_at: 2026-08-13T16:55:00+02:00
updated_at: 2026-08-13T16:55:00+02:00
review_at: 2026-10-13
source_ids: [source-agentic-security-verification-2026-08]
relations:
  - predicate: derived_from
    target: source-agentic-security-verification-2026-08
  - predicate: applies_to
    target: pattern-agentic-runtime-security-boundary
---

# MCP and Agent Extension Security

## Authority chain

```text
extension source -> admission -> pinned artifact + manifest
       -> user/client consent -> resource-bound identity
       -> strict tool contract -> deterministic policy
       -> isolated execution -> validated result -> audit
```

Project files, pull requests, skills, plugins, tool descriptions and one-click
MCP installation commands are untrusted until reviewed. Never auto-enable
project-supplied servers in a privileged CI or developer session. Display the
exact command, arguments, requested directories, network destinations and
scopes before consent; bind approval to the immutable artifact and manifest.

For protected remote MCP servers, validate issuer, audience and resource,
rotate short-lived tokens and never pass an inbound token through to an
upstream API. Sessions are correlation state, not authentication. Scope consent
per client and tool, reject unknown realms and fail closed on missing policy.

Tool schemas use strict types, enums, path roots, URL allowlists, byte and item
limits and explicit side-effect classification. Reject undeclared arguments,
traversal, shell interpolation and ambiguous free-form parameters. Treat tool
output as untrusted evidence and keep it unable to grant further authority.

## Supply-chain and operations gate

- pin immutable releases and transitive dependencies;
- require security policy, advisory monitoring and an upgrade owner;
- rescan manifest, code and dependencies on every change;
- isolate local servers from host secrets, broad filesystem and unrestricted
  egress;
- test SSRF, command injection, path traversal, serialization, session mix-up,
  confused deputy, prompt injection and malicious update paths;
- retain a fast disable/revoke path and previous known-good artifact.

Static or LLM-assisted scanners reduce review load but can miss encrypted,
multimodal, staged or environment-dependent behavior. A clean scan never grants
runtime authority by itself.

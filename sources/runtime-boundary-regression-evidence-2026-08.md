---
id: source-runtime-boundary-regression-evidence-2026-08
type: source
title: Runtime Boundary Regression Evidence Audit August 2026
status: reviewed
privacy: public
confidence: 0.8
created_at: 2026-08-17T08:05:00+02:00
updated_at: 2026-08-17T08:05:00+02:00
review_at: 2026-09-17
source_ids: []
relations: []
---

# Runtime Boundary Regression Evidence Audit — August 2026

Primary advisories and maintainer reports checked on 2026-08-17:

- [Pydantic AI provider-file confused deputy](https://github.com/advisories/GHSA-h7p7-w5gc-xj3w)
- [Token Optimizer MCP command injection](https://github.com/advisories/GHSA-49mq-fc6q-3h46)
- [Token Optimizer MCP path traversal](https://github.com/advisories/GHSA-76pc-mqxp-3rq5)
- [Stata MCP newline command injection](https://github.com/advisories/GHSA-49m4-vp58-wgc9)
- [ContextForge DNS-rebinding SSRF](https://github.com/advisories/GHSA-9hgc-g3w5-67cm)
- [atomic-agents-stack dashboard path traversal](https://github.com/advisories/GHSA-rm43-82j9-r4mj)
- [Microsoft Agent Framework snapshot isolation issue](https://github.com/microsoft/agent-framework/issues/7683)
- [Microsoft Agent Framework checkpoint lineage issue](https://github.com/microsoft/agent-framework/issues/7647)
- [Microsoft Agent Framework pending-request restore issue](https://github.com/microsoft/agent-framework/issues/7618)

## Evidence boundary

The advisories establish affected and patched release ranges through upstream
provenance. They are not independent reproductions and do not show that schema
validation, a container or framework checkpointing is sufficient on its own.
The Microsoft reports are open maintainer-repository issues; they establish
release-specific adoption risks but do not demonstrate duplicate or omitted
external effects.

## Durable recommendation

Treat model- or client-controlled references and arguments as delegated
authority requests. Canonicalize and authorize the resolved object, path,
hostname and effect immediately before execution, and retain fixed-version
negative controls when an affected dependency is adopted. A checkpointing
runtime must pass immutable-snapshot, storage-read isolation, lineage,
serialization, upgrade and crash-around-effect tests on the exact release. Run
product-specific vulnerable/fixed replays only during adoption or when the
dependency is deployed; the architecture knowledge base retains the generic
failure contract rather than a permanent vulnerable-product test farm.

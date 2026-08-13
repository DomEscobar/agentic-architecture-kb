---
id: pattern-agent-sandbox-selection
type: pattern
title: Agent Sandbox Selection and Validation
status: reviewed
privacy: public
confidence: 0.89
created_at: 2026-08-13T16:55:00+02:00
updated_at: 2026-08-13T16:55:00+02:00
review_at: 2026-10-13
source_ids: [source-agentic-security-verification-2026-08, source-agentic-security-landscape-2026-08]
relations:
  - predicate: derived_from
    target: source-agentic-security-verification-2026-08
  - predicate: applies_to
    target: pattern-agentic-runtime-security-boundary
---

# Agent Sandbox Selection and Validation

## Selection rule

Choose the isolation boundary from the adversary and consequence, not startup
time. Hardened containers fit trusted single-tenant tools and build isolation.
User-controlled or model-generated code with secrets, multiple tenants or high-
impact access generally needs a stronger userspace-kernel or per-workload VM
boundary. Regulated deployments may require dedicated nodes or accounts in
addition to a microVM.

Kubernetes SIGs Agent Sandbox is a lifecycle abstraction, not one fixed security
boundary. OpenSandbox supports several runtime classes, including standard
containers, gVisor and Kata or Firecracker configurations. Azure Container Apps
dynamic sessions provide a managed Hyper-V-isolated option. These are candidates
whose exact version and configuration must pass the same application tests.

## Non-negotiable profile

- non-root execution, dropped capabilities and no host or container-runtime
  socket;
- explicit read-only and writable mounts with tenant-specific storage;
- no ambient cloud or developer credentials; broker narrowly scoped tokens;
- deny-by-default egress through an authenticated allowlist proxy;
- CPU, memory, process, disk, output, time and concurrent-session limits;
- immutable base image, signed provenance, vulnerability policy and bounded
  dependency installation;
- per-tenant identity, logs and lifecycle cleanup; no cross-session reuse unless
  explicitly scrubbed and tested;
- kill, revoke, snapshot-for-forensics and destroy operations controlled outside
  the guest.

Validate host escape, metadata and secret access, DNS and redirect egress,
symlink and mount traversal, fork and disk exhaustion, cross-tenant state,
snapshot restoration, cleanup failure and control-plane authorization. Product
claims of strong isolation are implementation evidence, not substitutes for
these tests.

---
id: case-public-ai-architect-v1
type: case
title: Public AI Architect V1
status: reviewed
privacy: internal
confidence: 0.91
created_at: 2026-08-12T18:43:00+02:00
updated_at: 2026-08-14T20:02:00+02:00
review_at: 2026-09-12
source_ids:
  - source-public-ai-architect-validation-2026-08
relations:
  - predicate: derived_from
    target: source-public-ai-architect-validation-2026-08
  - predicate: evaluated_by
    target: pattern-evidence-first-agent-evaluation
---

# Case: Public AI Architect V1

## Context and constraints

A public, stateless architecture-advice chat serves a curated public wiki. It
must not connect to the privileged internal agent, private filesystem, shell or
tools. It runs in a hardened container and calls a bounded model API.

## Selected pattern

`browser → host TLS proxy → stateless bounded controller → structured public wiki v3 → model API`

The runtime decomposes each turn into checkable questions, retrieves candidate
sections and claims, assesses support, scope and gaps, and may execute one
targeted follow-up search. The draft streams to the browser, but only a final
answer that passes exact-citation, runtime-consistency, disclosure and diagram
schema gates is accepted. One bounded repair is allowed. The model has no tools;
sessions stay in the browser.

## Measured outcome

The structured public artifact contains 342 exact-addressable chunks, 24 public
claims, 31 relations and six navigation lanes. No private page was promoted to
expose the two canonical contradiction edges; contradiction traversal is tested
synthetically and will activate only when public-reviewed edges exist.

The deployed evidence-investigator runtime passed 23 deterministic unit,
contract, privacy and release tests. A real three-turn support-agent conversation
passed streaming, evidence-metadata, citation-resolution and context checks. A
second adversarial live run passed 9/9 turns across irreversible side effects,
prompt injection and deliberate evidence gaps; two turns used repair, no provider
retry occurred, and observed turn latency ranged from 22.2 to 75.5 seconds.

## Decision

The runtime no longer treats top-k retrieval as grounded truth: retrieved text is
candidate evidence, the model-assisted assessor must select exact IDs and retain
scope, limitations and missing support, and deterministic gates reject unresolved
labels or hidden evidence gaps. This improves investigation discipline but is not
a truth proof; semantic support and source independence still require evals.

## Next evidence

Expand the private promotion split with human claim-to-span support labels,
upstream-provenance independence checks, contradiction cases and calibrated
abstention scoring. Compare the v3 investigator against the former flat-RAG
baseline under paired quality, latency and cost slices.

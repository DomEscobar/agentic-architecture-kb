---
id: case-public-ai-architect-v1
type: case
title: Public AI Architect V1
status: reviewed
privacy: internal
confidence: 0.91
created_at: 2026-08-12T18:43:00+02:00
updated_at: 2026-08-12T18:43:00+02:00
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

`browser → host TLS proxy → stateless Node chat → allowlisted BM25 wiki → model API`

The model receives exact evidence labels, has no tools, and returns Markdown.
Architecture requests additionally produce bounded JSON validated and rendered
as branded inline SVG. Sessions stay in the browser.

## Measured outcome

The technical runtime, multi-turn streaming and responsive diagram UI passed
their scripted checks. Visual review found and fixed CSP animation failures,
fullscreen containment/transparency, node collisions, text overflow and label
overlap. A semantic review still found an impossible metric target and an
invalid citation label.

## Decision

The public V1 is technically usable but not semantically promoted as a reliable
architecture authority. The champion remains gated by citation validity,
unsupported-claim rate, calibrated decision quality and abuse/cost sentinels.

## Next evidence

Run the architecture-advice eval pack with blinded human labels, deterministic
citation checks, prompt-injection and budget sentinels, then reserve a private
promotion split. Store model, wiki snapshot, prompt and runtime hashes per run.

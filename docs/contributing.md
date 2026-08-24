# Contributing

This page covers repository layout, how canonical knowledge is admitted, and
the full command reference. See [System architecture](architecture.md) for the
write path, read path, and failure boundaries in detail.

## Repository layout

```text
inbox/       unreviewed inputs
sources/     primary sources and unchanged evidence
concepts/    stable concepts and mechanisms
patterns/    patterns with use and exclusion conditions
cases/       concrete architecture decisions and outcomes
entities/    people, projects, systems, and organizations
syntheses/   evidence-backed summaries derived from sources
reports/     generated quality and governance reports
changes/     append-only dated records for canonical knowledge changes
```

## What a canonical page needs

Every page under `inbox/`, `sources/`, `concepts/`, `patterns/`, `cases/`,
`entities/`, and `syntheses/` requires validated YAML frontmatter: a stable
ID, page type, status, privacy class, provenance (`source_ids`), confidence,
and a review date. See [schemas/page.schema.json](../schemas/page.schema.json)
for the required fields and [Evidence Rubric](evidence-rubric.md) for what
level of evidence a claim needs before it can be `accepted`.

## Promotion gate

```text
Chat/source -> immutable input -> extraction -> inbox
            -> schema and policy checks -> human approval
            -> canonical page -> compile/lint -> derived indexes
```

Automated extraction creates candidates, not truth. Autonomous writes to the
canonical content area are disabled; every promotion requires human approval.
See [ADR-0002: One-way Knowledge Promotion DAG](adr/0002-knowledge-promotion-dag.md)
for how downstream consumers (the Memory Wiki projection and the public
snapshot) are released without ever writing back to canonical pages.

Every canonical novelty, correction, supersession, or reversion also appends a
dated record to [`changes/ledger.jsonl`](../changes/ledger.jsonl), validated
against [schemas/change.schema.json](../schemas/change.schema.json). The
record identifies the affected page, claim, technique, or governance file and
states why the change passed the utility and evidence gates.

## Retirement gate

Admission has a gate, so removal needs one too. A technique card is retired by
moving its `lifecycle`, never by quietly editing or deleting it, so existing
citations keep resolving and the decision stays auditable.

1. Set `lifecycle` to `legacy` if the card still works but a successor
   generally dominates it, or `deprecated` if it must not be used at all.
2. Write a `retirement_reason` that names the observed deficit, not a
   preference. Add `retired_on` for `deprecated`.
3. Add `superseded_by` when a successor exists. Lint rejects a successor that
   is unknown, self-referential, itself retired, or part of a cycle, so a reader
   following the chain always lands on live material.
4. Append a record to [`changes/ledger.jsonl`](../changes/ledger.jsonl) naming
   the `technique_id`, with `change_kind` exactly `supersession`. Lint fails
   without it, and an ordinary `technique` record does not satisfy the gate — a
   retirement gets its own entry so it stays dated, attributable, and
   revertible. Retiring an old card while adding its replacement is therefore
   two records, not one.
5. Re-run `make check` and confirm no reviewed page still presents the card as
   a current option.

Promoting a card to `recommended` is the same kind of deliberate act in the
opposite direction, and belongs in the same change as the routing or catalog
page that names it as the family default. A card that no page designates stays
`situational`. `make due-reviews` reports cards whose `freshness.review` has
passed; that report identifies candidates for this gate and carries no
promotion or retirement authority of its own.

Retire rather than delete unless the content is wrong or must be removed for
policy reasons. Deletion follows the separate protocol in
[System architecture](architecture.md): remove the canonical page, rebuild all
projections, and prove with a negative test that the content is no longer
retrievable.

## Anti-bloat admission

When a new technique card overlaps an existing card in the same `techniques/`
group, declare `overlaps_with` naming the related `technique_id` values and
state in the change record whether the newcomer replaces, complements, or
narrows an existing card. Lint validates that every `overlaps_with` target
exists.

Each `techniques/` group carries a soft cap. When a group reaches its cap,
`make lint` emits a warning to review consolidation before adding more cards.
Groups with a routing catalog page must keep at least one `recommended` card;
lint warns when none is named.

## Commands

```bash
python3 -m pip install -r requirements.txt
```

| Command | Effect |
| --- | --- |
| `make lint` | Validates schemas, IDs, links, provenance, and claims. Read-only. |
| `make compile` | Lints, then writes the tracked `index.md` and `technique-index.json`, plus the ignored `build/wiki.json`, `indexes/wiki.sqlite`, and `reports/quality.json`. |
| `make index` | Rebuilds only the lexical search index. |
| `make navigation` | Regenerates `index.md` and `technique-index.json` without a full compile. |
| `make hybrid-index` | Builds the dense embedding index and reciprocal-rank fusion (opt-in; not built by `make compile`). |
| `make retrieval-benchmark` | Runs the labelled retrieval eval pack against lexical, dense, and hybrid search. |
| `make memory-projection` | Builds the downstream Memory Wiki projection. |
| `make drift` | Checks whether released consumers are stale against the current canonical build. |
| `make freshness-check` | Validates the freshness project registry and research query packs. |
| `make repo-pulse` | Records upstream project signals (default branch, releases, license) without treating activity as evidence. |
| `make due-reviews` | Reports technique cards and claims whose review date has passed. |
| `make test` | Runs the Python test suite. |
| `make check` | `lint` + `freshness-check` + `compile` + `test`. What CI runs. |

## Tracked versus generated artifacts

`index.md` and `technique-index.json` are tracked in Git and lint-verified
against the canonical pages and technique cards on every `make compile`; a
stale copy fails `make lint`. `build/`, `indexes/`, `reports/*.json`, and
`reports/retrieval-traces/` are ignored projections, fully reconstructable
from the canonical Markdown and JSON, and carry no independent authority.

GitHub Actions runs `make check` on every push and pull request.

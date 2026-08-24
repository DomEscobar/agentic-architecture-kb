# Agent consumption contract

This repository is an evidence-backed architecture knowledge base. Markdown
pages and JSON technique cards are canonical truth. Search indexes, reports and
summaries are reproducible projections and never replace a loaded section.

## Read first, search second

This corpus is small on purpose: 96 pages and 479 sections. Navigation is
cheaper and more reliable than retrieval at this size, so prefer reading whole
pages over ranking snippets.

1. Read [`index.md`](index.md) and pick the knowledge lane.
2. Read the one to three canonical pages in that lane **in full**.
3. Resolve any `technique_id` through [`technique-index.json`](technique-index.json)
   and read that card directly. This is exact; no ranking is involved.
4. Follow `depends_on`, `derived_from` and `applies_to` in page frontmatter to
   reach related pages.
5. Use search only when you do not yet know this repository's vocabulary for a
   concept.

```bash
python3 -m pip install -r requirements.txt
make compile
python3 tools/wiki.py search "<your question>" --privacy public --status reviewed --limit 5
```

Run `make hybrid-index` when queries are paraphrases rather than this
repository's terms. Lexical search alone favours exact identifiers.

## Scope

Covered lanes: retrieval and RAG, document parsing, chunking, embeddings,
multimodal retrieval, agent runtimes and orchestration, agent memory,
evaluation and observability, agentic security, bounded self-improvement, and
coding-agent project harness.

Not covered: general API and service design, data modelling, frontend, mobile,
embedded, infrastructure and deployment, identity and authorization for
ordinary applications, and classical ML training pipelines.

If a question falls outside the covered lanes, say so. Do not stretch an
agentic pattern to cover unrelated work.

## Search confidence

`tools/wiki.py search` reports `match_mode`, `confidence` and `advisory`.
Confidence describes term-match strength only. It is never evidence that an
answer is correct.

| `confidence` | Meaning | Action |
| --- | --- | --- |
| `high` | Every query term matched a section | Load the section and verify it answers the question |
| `medium` | Relaxed match with adequate term coverage | Confirm relevance before citing |
| `low` | Relaxed match, weak coverage | Treat as closest available material, not coverage; re-check the lane in `index.md` |
| `none` | Nothing matched the selective terms | Report the topic as not covered |

Never cite a snippet. Load the canonical section first.

## Coding-agent questions

| Question | First load |
| --- | --- |
| Repository-specific agent setup | [`patterns/project-coding-agent-harness.md`](patterns/project-coding-agent-harness.md) |
| Instruction files and precedence | [`techniques/runtime/coding-agent-instruction-stack.json`](techniques/runtime/coding-agent-instruction-stack.json) |
| Skill admission and promotion | [`techniques/runtime/evaluated-project-skill-package.json`](techniques/runtime/evaluated-project-skill-package.json) |
| Harness replay and attribution | [`techniques/evaluation/coding-agent-project-replay.json`](techniques/evaluation/coding-agent-project-replay.json) |
| Evidence audit | [`sources/coding-agent-harness-and-skills-evidence-2026-08.md`](sources/coding-agent-harness-and-skills-evidence-2026-08.md) |

Do not invent project facts. State which assumptions still require inspection
of the caller's repository, constraints or runtime.

## Citation rules

- Cite stable section IDs from loaded pages, not shortened labels.
- Distinguish empirical claims from normative requirements.
- Prefer reviewed patterns and technique cards over inbox or draft material.
- When evidence is contested or scope-limited, say so explicitly.
- Record the Git commit SHA when the decision is consequential.

## Do not

- Treat search snippets, `build/wiki.json` or `index.md` as authoritative
  without loading the canonical section.
- Read topic coverage into a `low` or `none` confidence result set.
- Recommend a harness, skill or instruction change without naming the eval
  slice that would justify it.
- Apply this repository's governance rigour to work whose risk does not
  warrant it; the patterns state their own smallest starting point.
- Copy generic product guidance as project-specific fit.

See [`README.md`](README.md) for setup, quality checks and the public API.

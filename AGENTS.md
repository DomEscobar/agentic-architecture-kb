# Agent consumption contract

This repository is an evidence-backed architecture knowledge base. When you
work from it, treat Markdown pages and JSON technique cards as canonical truth.
Generated indexes and summaries are retrieval aids only.

## Start here

1. Read [`index.md`](index.md) and choose the relevant knowledge lane.
2. For coding-agent setup, start with the **Coding agents and project harness**
   lane, then load only the linked patterns, sources and technique cards.
3. Search before recommending:

```bash
python3 -m pip install -r requirements.txt
make compile
python3 tools/wiki.py search "<your question>" --privacy public --status reviewed --limit 5
```

4. Resolve `technique_id` values through [`technique-index.json`](technique-index.json).
5. Load the cited sections and preserve exact source references in your answer.
6. Record the Git commit SHA when the decision is consequential.

## Coding-agent questions

| Question | First load |
| --- | --- |
| Repository-specific agent setup | [`patterns/project-coding-agent-harness.md`](patterns/project-coding-agent-harness.md) |
| Instruction files and precedence | [`techniques/runtime/coding-agent-instruction-stack.json`](techniques/runtime/coding-agent-instruction-stack.json) |
| Skill admission and promotion | [`techniques/runtime/evaluated-project-skill-package.json`](techniques/runtime/evaluated-project-skill-package.json) |
| Harness replay and attribution | [`techniques/evaluation/coding-agent-project-replay.json`](techniques/evaluation/coding-agent-project-replay.json) |
| Evidence audit | [`sources/coding-agent-harness-and-skills-evidence-2026-08.md`](sources/coding-agent-harness-and-skills-evidence-2026-08.md) |

Do not invent project facts. State which assumptions still require inspection
of the caller's repository, constraints, or runtime.

## Citation rules

- Cite stable section IDs from loaded pages, not shortened labels.
- Distinguish empirical claims from normative requirements.
- Prefer reviewed patterns and technique cards over inbox or draft material.
- When evidence is contested or scope-limited, say so explicitly.

## Do not

- Treat search snippets or `build/wiki.json` as authoritative without loading
  the canonical section.
- Recommend a harness, skill, or instruction change without naming the eval
  slice that would justify it.
- Copy generic product guidance as project-specific fit.

See [`README.md`](README.md) for setup, quality checks, and the public API.

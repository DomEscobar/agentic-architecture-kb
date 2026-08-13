# Agentic Architecture Knowledge Base

A Git-versioned, local knowledge base for evidence-backed architecture decisions
across RAG, agent runtimes, agent memory, evaluation, and bounded
self-improvement.

## Core principle

Markdown is the canonical source. Search indexes, graphs, reports, and LLM
summaries are reproducible projections and must never replace the original
sources.

## How to use

### Browse or give it to a coding agent

Clone the repository and point your coding agent at the relevant lane:

```bash
git clone https://github.com/DomEscobar/agentic-architecture-kb.git
cd agentic-architecture-kb
```

Then ask the agent to search before recommending, for example:

```text
Use this knowledge base to design recovery semantics for my tool-using agent.
Start with the relevant runtime patterns and technique cards, preserve exact
source references, and state which assumptions require repository inspection.
```

Start with `patterns/` for decision guidance, `techniques/` for machine-readable
experiment candidates, `sources/` for evidence audits, and `cases/` for reusable
application records. For consequential decisions, record the commit SHA used.

### Search locally

```bash
python3 -m pip install -r requirements.txt
make compile
python3 tools/wiki.py search "tool-using agent recovery semantics" \
  --privacy internal --status reviewed --limit 5
```

### Ask the public service

For a quick single-turn lookup, call the stateless public API:

```bash
curl --fail-with-body https://ai-architect.huecki.com/api/v1/ask \
  --header 'content-type: application/json' \
  --data '{"question":"Design recovery semantics for a tool-using agent."}'
```

The API does not inspect the caller's repository and does not retain multi-turn
state. Use the cloned knowledge base when the decision depends on local code,
constraints, or continued agent work.

## Documentation

- [System architecture](docs/architecture.md)
- [Research and tool selection](docs/research.md)
- [MVP and roadmap](docs/roadmap.md)
- [ADR-0001: Markdown and Git as the source of truth](docs/adr/0001-markdown-git-source-of-truth.md)
- [Page schema](schemas/page.schema.json)
- [Memory evaluation](evals/README.md)
- [Runtime techniques: structured synthesis](syntheses/agentic-runtime-techniques.md)
- [Runtime Decision Guide](patterns/runtime-decision-guide.md)
- [Runtime Safety Baseline](patterns/runtime-safety-baseline.md)
- [Runtime Build Versus Adopt Decision](patterns/runtime-build-vs-adopt.md)
- [Document-centric Hybrid RAG](patterns/document-centric-hybrid-rag.md)
- [Case: Bauhelfer AI RAG](cases/bauhelfer-ai-rag.md)
- [RAG Pipeline Taxonomy](syntheses/rag-pipeline-taxonomy.md)
- [PageIndex / Reasoning Tree Retrieval](patterns/pageindex-reasoning-tree-retrieval.md)
- [Contextual Retrieval](patterns/contextual-retrieval.md)
- [Graph-based Retrieval](patterns/graph-based-retrieval.md)
- [Agentic and Corrective Retrieval](patterns/agentic-corrective-retrieval.md)
- [Visual Late-interaction Retrieval](patterns/visual-late-interaction-retrieval.md)
- [Agent Evaluation Techniques](syntheses/agent-evaluation-techniques.md)
- [Evidence-first Agent Evaluation](patterns/evidence-first-agent-evaluation.md)
- [Eval-guided Bounded Improvement Loop](patterns/eval-guided-improvement-loop.md)
- [Evaluation Consulting Playbook](docs/evaluation-consulting-playbook.md)
- [Evaluation Workload Blueprints](syntheses/evaluation-workload-blueprints.md)
- [Evaluation Metric Catalog](concepts/evaluation-metric-catalog.md)
- [LLM Judge Calibration](patterns/llm-judge-calibration.md)
- [Online Evaluation and Rollout](patterns/online-evaluation-and-rollout.md)

## Knowledge-base structure

```text
inbox/       unreviewed inputs
sources/     primary sources and unchanged evidence
concepts/    stable concepts and mechanisms
patterns/    patterns with use and exclusion conditions
cases/       concrete architecture decisions and outcomes
entities/    people, projects, systems, and organizations
syntheses/   evidence-backed summaries derived from sources
reports/     generated quality and governance reports
```

## Status

The deterministic toolchain validates schemas, IDs, page types, local links,
provenance, and relation targets. It compiles every canonical page into a fully
reconstructable JSON projection. Autonomous writes to the canonical content
area are disabled.

## Local quality checks

```bash
python3 -m pip install -r requirements.txt
make check
```

`make lint` does not modify files. `make compile` writes only the ignored
projections `build/wiki.json` and `reports/quality.json`. GitHub Actions runs the
same checks for pushes and pull requests.

## Local search

`make compile` also creates `indexes/wiki.sqlite`. Every Markdown section gets a
stable, citable ID derived from its page ID and heading path.

```bash
python3 tools/wiki.py search "hybrid retrieval BM25" \
  --privacy internal --status reviewed --limit 5
```

Search starts with strict FTS5 AND matching and falls back to OR matching when
there are no results. JSON traces under `reports/retrieval-traces/` contain the
query, filters, all ranked candidates, and the full sections that were loaded.
Indexes and traces are reconstructable projections ignored by Git.

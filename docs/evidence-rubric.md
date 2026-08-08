# Evidence Rubric

This rubric controls what may become durable technical knowledge in this wiki.
Popularity, confident prose and repeated secondary coverage are not evidence.

## Evidence levels

### E4 — Reproduced or convergent evidence

- independent reproduction, or multiple methodologically credible studies;
- comparable task, corpus, metrics and operating constraints;
- artifacts sufficient to audit the result.

Use for strong recommendations within the tested scope. Never generalize beyond
the evaluated workload without an explicit inference label.

### E3 — Strong primary evidence

- peer-reviewed paper or unusually complete preprint;
- public data/code/configuration or detailed experimental protocol;
- meaningful baselines, ablations, uncertainty and failure analysis.

Use for provisional patterns and evaluated alternatives. Record missing
replication and external-validity risks.

### E2 — Primary claim with material limitations

- vendor experiment, repository benchmark, small study or incomplete preprint;
- method and scope are inspectable, but independence, controls or artifacts are
  weak or absent.

Use as a candidate or canary, not a default. Attribute every numeric result.

### E1 — Practitioner signal

- technical blog, incident report, forum thread or detailed anecdote;
- useful for discovering failure modes and test hypotheses;
- uncontrolled and usually subject to selection and reporting bias.

Store under “Voices” or open questions. Never use alone to claim superiority.

### E0 — Discovery only

- marketing copy, social-media summary, star count, trend ranking, anonymous
  benchmark screenshot, SEO listicle or unattributed statistic.

Do not promote into synthesis. Retain only when needed to document a claim that
was checked and rejected.

## Admission checklist

A durable claim must answer:

1. What exact mechanism or system was tested?
2. Against which baselines and under which fixed conditions?
3. What corpus, query distribution, language and modality were used?
4. Are retrieval, context construction and generation measured separately?
5. What metric, sample size, uncertainty and judge protocol apply?
6. Are code, data, prompts, model versions and index settings available?
7. Is the result independent, replicated, peer reviewed or only author-reported?
8. What latency, token, storage, construction and maintenance costs were counted?
9. What failure slices, negative results and transfer limits are known?
10. What evidence would falsify or change the claim?

If four or more material answers are missing, keep the item in the source audit
or inbox. Do not create a reviewed pattern from it.

## Numeric-claim rule

Every number must include its denominator, metric, evaluation scope and source.
Relative improvements must be labelled relative. LLM-judge results must name the
judge and rubric when known. “Production”, “state of the art”, “X% fewer
hallucinations” and “used by most companies” are rejected unless operationally
defined and evidenced.

## Voices rule

Practitioner voices are valuable when they disagree. Record the concrete
failure, workload and measurement if available. Treat consensus in social feeds
as correlated testimony, not independent confirmation. Convert voices into eval
slices; do not convert them directly into defaults.

## Promotion and review

- E0/E1: discovery or hypothesis only;
- E2: experimental candidate behind a feature flag;
- E3: provisional recommendation for matching workloads;
- E4: strong recommendation within demonstrated bounds.

Fast-moving claims receive a review date within 60–90 days. Promotion requires
paired evaluation against the shared baseline. Regression, contradiction or
failed replication changes status to `contested` or `superseded`; it is not
silently overwritten.


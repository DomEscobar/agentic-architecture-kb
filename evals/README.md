# Memory and Retrieval Evaluation

## Offline suites

- **Recall/Precision:** known relevant sections for each query.
- **Temporal:** the current answer outranks superseded claims.
- **Contradiction:** conflicts are detected rather than smoothed over.
- **Premise awareness:** false user premises are rejected.
- **Update:** a correction appears in retrieval after compilation.
- **Forgetting:** deleted content appears in neither lexical nor semantic search.
- **Privacy:** cross-user, cross-project, and restricted canaries return zero
  results.
- **Provenance:** answer claims point to sections that were actually loaded.
- **Robustness:** paraphrases, typos, and adversarial prompt content.

Deterministic checks take priority. LLM judges may supplement them, but must be
calibrated against human-labeled examples and logged with model and prompt
versions.

`tools/judge_calibration.py` accepts only independently labeled and adjudicated
cases whose digest matches the frozen seed. It reports false-pass rate,
sensitivity, specificity, and abstention coverage. The seed remains
non-promotional until real human labels and frozen judge predictions are
supplied.

Protected selection and holdout data lives only in the untracked
`evals/private/` control-plane mount. `tools/eval_control.py` verifies case-set
and split digests, one release-scoped access-log event, distinct baseline and
candidate identities, repeated runs, report digests, and human approval.
Repository placeholders are not accepted as evidence.

## Online metrics

Retrieval latency, end-to-end latency, cost, result coverage, source clicks,
corrections, abstention rate, stale-result rate, and privacy violations. Changes
progress through replay, paired baselines, canary, kill switch, and rollback.

## Consulting regression

`consulting-cases.json` defines mandatory decision elements for brownfield,
greenfield, judge, coding, memory, multi-agent, production, and tool-selection
questions. Field-validated results are recorded separately as canonical case
records with real evidence.

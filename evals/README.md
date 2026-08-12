# Memory- und Retrieval-Evaluation

## Offline-Suiten

- **Recall/Precision:** bekannte relevante Abschnitte pro Anfrage.
- **Temporal:** aktuelle Antwort gewinnt gegen superseded Claims.
- **Contradiction:** Konflikt wird erkannt und nicht glattgebügelt.
- **Premise awareness:** falsche Nutzerprämissen werden zurückgewiesen.
- **Update:** Korrektur erscheint nach Compile im Retrieval.
- **Forgetting:** gelöschter Inhalt erscheint weder lexikalisch noch semantisch.
- **Privacy:** Cross-user-, Cross-project- und Restricted-Canaries liefern null
  Treffer.
- **Provenance:** Antwort-Claims zeigen auf tatsächlich geladene Abschnitte.
- **Robustness:** Paraphrasen, Tippfehler und adversariale Prompt-Inhalte.

Deterministische Checks haben Vorrang. LLM-Judges dürfen ergänzen, müssen aber
gegen menschlich gelabelte Beispiele kalibriert und mit Modell-/Prompt-Version
protokolliert werden.

`tools/judge_calibration.py` accepts only independently labeled and adjudicated
cases whose digest matches the frozen seed. It reports false-pass rate,
sensitivity, specificity and abstention coverage. The seed remains non-
promotional until real human labels and frozen judge predictions are supplied.

Protected selection/holdout data lives only in the untracked `evals/private/`
control-plane mount. `tools/eval_control.py` verifies case-set and split digests,
one release-scoped access-log event, distinct baseline/candidate identities,
repeated runs, report digests and human approval. Repository placeholders are
not accepted as evidence.

## Online-Metriken

Retrieval-Latenz, End-to-End-Latenz, Kosten, Ergebnis-Abdeckung, Quellenklicks,
Korrekturen, Abstentionsrate, Stale-Quote und Privacy-Verstöße. Änderungen gehen
über Replay, gepaarte Baseline, Canary, Kill Switch und Rollback.

## Consulting-Regression

`consulting-cases.json` definiert verpflichtende Entscheidungselemente für
Brownfield-, Greenfield-, Judge-, Coding-, Memory-, Multi-Agent-, Production-
und Toolauswahlfragen. Feldvalidierte Ergebnisse werden getrennt als kanonische
Case Records mit realer Evidenz aufgenommen.

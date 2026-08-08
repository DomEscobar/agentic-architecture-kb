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

## Online-Metriken

Retrieval-Latenz, End-to-End-Latenz, Kosten, Ergebnis-Abdeckung, Quellenklicks,
Korrekturen, Abstentionsrate, Stale-Quote und Privacy-Verstöße. Änderungen gehen
über Replay, gepaarte Baseline, Canary, Kill Switch und Rollback.

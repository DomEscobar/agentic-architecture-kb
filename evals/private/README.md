# Protected evaluation mount

This directory is a control-plane boundary, not a repository dataset. Real
selection and holdout cases, human labels, access logs, and promotion evidence
must stay untracked. `.gitignore` denies all contents except this README and the
ignore policy.

Activation requires a digest-pinned case set, exactly one matching access event
for the release, separate baseline/candidate identities, repeated runs, concrete
red-team and hard-gate report digests, judge-calibration evidence when a judge is
used, and explicit human approval. Empty placeholders never count as evidence.

#!/usr/bin/env python3
"""Validate human labels and score a frozen binary/abstaining LLM judge."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "evals/judge-validation-seed-v1.json"
LABEL_SCHEMA = json.loads((ROOT / "schemas/judge-labels.schema.json").read_text())


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def calibrate(labels_path: Path, predictions_path: Path) -> dict:
    labels = json.loads(labels_path.read_text())
    predictions = json.loads(predictions_path.read_text())
    errors = [issue.message for issue in jsonschema.Draft202012Validator(LABEL_SCHEMA).iter_errors(labels)]
    if labels.get("dataset_sha256") != digest(DATASET):
        errors.append("human-label dataset digest mismatch")
    dataset_ids = {item["id"] for item in json.loads(DATASET.read_text())["cases"]}
    adjudicated = {item["case_id"]: item["adjudicated_label"] for item in labels.get("labels", [])}
    predicted = {item["case_id"]: item["prediction"] for item in predictions.get("predictions", [])}
    if not set(adjudicated).issubset(dataset_ids):
        errors.append("human labels contain unknown case IDs")
    if set(predicted) != set(adjudicated):
        errors.append("prediction IDs do not exactly match adjudicated label IDs")
    usable = {key: value for key, value in adjudicated.items() if value != "exclude"}
    counts = {"tp": 0, "tn": 0, "fp": 0, "fn": 0, "abstain": 0}
    for case_id, truth in usable.items():
        guess = predicted.get(case_id)
        if guess == "abstain": counts["abstain"] += 1
        elif truth == "pass" and guess == "pass": counts["tp"] += 1
        elif truth == "fail" and guess == "fail": counts["tn"] += 1
        elif truth == "fail" and guess == "pass": counts["fp"] += 1
        elif truth == "pass" and guess == "fail": counts["fn"] += 1
        else: errors.append(f"invalid prediction for {case_id}")
    negatives = counts["tn"] + counts["fp"]
    positives = counts["tp"] + counts["fn"]
    return {"ok": not errors, "status": "calibrated" if not errors and usable else "not-calibrated", "dataset_sha256": digest(DATASET), "labels_sha256": digest(labels_path), "predictions_sha256": digest(predictions_path), "case_count": len(usable), "counts": counts, "false_pass_rate": counts["fp"] / negatives if negatives else None, "sensitivity": counts["tp"] / positives if positives else None, "specificity": counts["tn"] / negatives if negatives else None, "coverage": (len(usable) - counts["abstain"]) / len(usable) if usable else 0.0, "errors": sorted(errors), "promotion_authority": False}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("labels", type=Path)
    parser.add_argument("predictions", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT / "reports/judge-calibration.json")
    args = parser.parse_args()
    report = calibrate(args.labels, args.predictions)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

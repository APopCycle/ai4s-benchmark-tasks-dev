"""Verifier tests and structured frontier-evaluation output."""

import json
from pathlib import Path

from certify import evaluate

CANDIDATE = Path("/root/results/candidate.json")
VERIFIER_DIR = Path("/logs/verifier")
VERIFIER_DIR.mkdir(parents=True, exist_ok=True)
DETAILS = evaluate(CANDIDATE)
(VERIFIER_DIR / "reward-details.json").write_text(json.dumps(DETAILS, indent=2) + "\n")
reward = 1 if DETAILS.get("reward") == 1 else 0
(VERIFIER_DIR / "reward.txt").write_text(f"{reward}\n")


def test_submission_is_valid():
    assert DETAILS["valid"], DETAILS.get("error", "submission is invalid")


def test_scientific_score_is_exactly_certified():
    assert DETAILS["certified"], "scientific score was not certified"


def test_frontier_breakthrough_exceeds_frozen_sota():
    assert DETAILS["reward"] == 1, (
        "valid result, but it does not improve the frozen SOTA by the required 1e-8; "
        f"match_sota={DETAILS['match_sota']}, score={DETAILS.get('scientific_score_decimal')}"
    )

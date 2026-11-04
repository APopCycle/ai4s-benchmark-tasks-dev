#!/usr/bin/env python3
"""Check the minimal AI4S additions to an otherwise native TBS/Harbor task."""

from __future__ import annotations

import argparse
import re
import sys
import tomllib
from fractions import Fraction
from pathlib import Path


TASK_TYPES = {"workflow_automation", "frontier_research"}
FRONTIER_REQUIRED = {
    "metric",
    "direction",
    "sota_as_of",
    "sota_source",
    "sota_agent",
    "sota_submission_id",
    "sota_artifact_sha256",
    "sota_exact_numerator",
    "sota_exact_denominator",
    "minimum_meaningful_improvement",
    "reference_expected_reward",
    "reference_expected_valid",
    "reference_expected_match_sota",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task_dir", type=Path)
    parser.add_argument("--reference", action="store_true")
    args = parser.parse_args()
    task_dir = args.task_dir.resolve()
    with (task_dir / "task.toml").open("rb") as handle:
        config = tomllib.load(handle)
    metadata = config.get("metadata", {})
    errors: list[str] = []
    for key in ("proposal_id", "proposal_path", "task_type"):
        if not str(metadata.get(key, "")).strip():
            errors.append(f"[metadata].{key} is required")
    if metadata.get("task_type") not in TASK_TYPES:
        errors.append("[metadata].task_type must be workflow_automation or frontier_research")
    frontier = metadata.get("frontier")
    if metadata.get("task_type") == "frontier_research":
        if not isinstance(frontier, dict):
            errors.append("frontier_research requires a [metadata.frontier] table")
        else:
            missing = sorted(key for key in FRONTIER_REQUIRED if key not in frontier)
            if missing:
                errors.append("[metadata.frontier] is missing: " + ", ".join(missing))
            if frontier.get("direction") not in {"minimize", "maximize"}:
                errors.append("[metadata.frontier].direction must be minimize or maximize")
            for key in (
                "metric",
                "sota_as_of",
                "sota_source",
                "sota_agent",
                "sota_artifact_sha256",
                "sota_exact_numerator",
                "sota_exact_denominator",
                "minimum_meaningful_improvement",
            ):
                if not str(frontier.get(key, "")).strip():
                    errors.append(f"[metadata.frontier].{key} must be non-empty")
            if not re.fullmatch(r"[0-9a-f]{64}", str(frontier.get("sota_artifact_sha256", ""))):
                errors.append("[metadata.frontier].sota_artifact_sha256 must be lowercase SHA-256")
            try:
                numerator = int(frontier.get("sota_exact_numerator", ""))
                denominator = int(frontier.get("sota_exact_denominator", ""))
                if denominator <= 0 or numerator < 0:
                    raise ValueError
            except (TypeError, ValueError):
                errors.append("frontier SOTA numerator/denominator must define a nonnegative fraction")
            try:
                if Fraction(str(frontier.get("minimum_meaningful_improvement", ""))) <= 0:
                    raise ValueError
            except (ValueError, ZeroDivisionError):
                errors.append("[metadata.frontier].minimum_meaningful_improvement must be positive")
            if frontier.get("reference_expected_reward") != 0:
                errors.append("frontier oracle reference_expected_reward must be 0")
            if frontier.get("reference_expected_valid") is not True:
                errors.append("frontier oracle reference_expected_valid must be true")
            if frontier.get("reference_expected_match_sota") is not True:
                errors.append("frontier oracle reference_expected_match_sota must be true")
    elif frontier is not None:
        errors.append("[metadata.frontier] is only valid when task_type=frontier_research")
    proposal_id = metadata.get("proposal_id", "")
    if proposal_id and not re.fullmatch(r"AI4S-[A-Z0-9]+(?:-[A-Z0-9]+)+", proposal_id):
        errors.append("[metadata].proposal_id must use uppercase AI4S-... kebab form")
    proposal_path = str(metadata.get("proposal_path", ""))
    if proposal_path and (not proposal_path.startswith("proposals/") or not proposal_path.endswith(".md")):
        errors.append("[metadata].proposal_path must be a proposals/...md repo-relative path")
    if not args.reference and metadata.get("benchmark_status") == "reference":
        errors.append("formal tasks may not set benchmark_status=reference")
    task = config.get("task", {})
    expected_name = f"ai4s-benchmark/{task_dir.name}"
    if task.get("name") != expected_name:
        errors.append(f"[task].name must equal {expected_name!r}")
    if errors:
        print(f"FAIL {task_dir}")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"PASS {task_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

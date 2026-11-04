#!/usr/bin/env python3
"""Check the minimal AI4S additions to an otherwise native TBS/Harbor task."""

from __future__ import annotations

import argparse
import re
import sys
import tomllib
from pathlib import Path


TASK_TYPES = {"workflow_automation", "frontier_research"}


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

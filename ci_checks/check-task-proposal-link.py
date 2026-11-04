#!/usr/bin/env python3
"""Verify that a task points to an already-present, matching Markdown proposal."""

from __future__ import annotations

import argparse
import re
import sys
import tomllib
from pathlib import Path


def proposal_value(text: str, label: str) -> str | None:
    match = re.search(
        rf"^-\s*{re.escape(label)}\s*:\s*(.+?)\s*$",
        text,
        re.MULTILINE | re.IGNORECASE,
    )
    return match.group(1).strip().strip("`") if match else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task_dir", type=Path)
    parser.add_argument("--base-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    with (args.task_dir / "task.toml").open("rb") as handle:
        config = tomllib.load(handle)
    metadata = config.get("metadata", {})
    proposal_path = metadata.get("proposal_path")
    proposal_id = metadata.get("proposal_id")
    task_type = metadata.get("task_type")
    if not isinstance(proposal_path, str) or not proposal_path.startswith("proposals/"):
        print("FAIL: task.toml must contain a repo-relative proposals/... proposal_path")
        return 1
    candidate = (args.base_root.resolve() / proposal_path).resolve()
    proposals_root = (args.base_root.resolve() / "proposals").resolve()
    try:
        candidate.relative_to(proposals_root)
    except ValueError:
        print("FAIL: proposal_path escapes proposals/")
        return 1
    if not candidate.is_file():
        print(f"FAIL: approved proposal is absent from base branch: {proposal_path}")
        return 1
    text = candidate.read_text(encoding="utf-8")
    expected = {
        "Proposal ID": proposal_id,
        "Task type": task_type,
        "Primary domain": metadata.get("domain"),
        "Primary field": metadata.get("field"),
    }
    failed = False
    for label, task_value in expected.items():
        proposal = proposal_value(text, label)
        if proposal != task_value:
            print(f"FAIL: {label} mismatch: proposal={proposal!r}, task.toml={task_value!r}")
            failed = True
    if failed:
        return 1
    print(f"PASS: {args.task_dir} links approved proposal {proposal_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Validate a file-based AI4S task proposal using only the standard library."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DOMAINS = {
    "mathematical-sciences",
    "physical-sciences",
    "chemical-materials-sciences",
    "life-sciences",
    "medical-neuroscience-health-sciences",
    "earth-environmental-sciences",
    "computer-information-sciences",
    "engineering-sciences",
}
TASK_TYPES = {"workflow_automation", "frontier_research"}
REQUIRED_SECTIONS = tuple(range(0, 12))
PLACEHOLDER = re.compile(r"(?i)(\bTODO\b|REPLACE WITH|replace-domain|replace-field|<[^>]+>)")


def metadata_value(text: str, label: str) -> str | None:
    match = re.search(
        rf"^-\s*{re.escape(label)}\s*:\s*(.+?)\s*$",
        text,
        re.MULTILINE | re.IGNORECASE,
    )
    return match.group(1).strip().strip("`") if match else None


def sections(text: str) -> dict[int, str]:
    found: dict[int, tuple[int, int]] = {}
    matches = list(re.finditer(r"^##\s+(\d+)\.\s+.+$", text, re.MULTILINE))
    for index, match in enumerate(matches):
        number = int(match.group(1))
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        found[number] = (match.end(), end)
    return {number: text[start:end].strip() for number, (start, end) in found.items()}


def validate(path: Path, repo_root: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    proposal_id = metadata_value(text, "Proposal ID")
    domain = metadata_value(text, "Primary domain")
    field = metadata_value(text, "Primary field")
    task_type = metadata_value(text, "Task type")

    if not proposal_id or not re.fullmatch(r"AI4S-[A-Z0-9]+(?:-[A-Z0-9]+)+", proposal_id):
        errors.append("Proposal ID must use uppercase AI4S-... kebab form")
    if domain not in DOMAINS:
        errors.append(f"Primary domain must be one of: {', '.join(sorted(DOMAINS))}")
    if not field or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", field):
        errors.append("Primary field must be a non-empty lowercase kebab-case value")
    if task_type not in TASK_TYPES:
        errors.append("Task type must be workflow_automation or frontier_research")

    parsed = sections(text)
    for number in REQUIRED_SECTIONS:
        if number not in parsed:
            errors.append(f"Missing section: ## {number}.")
        elif not parsed[number]:
            errors.append(f"Section {number} is empty")

    if PLACEHOLDER.search(text):
        errors.append("Proposal still contains TODO/template placeholders")

    required_values = {
        1: (
            "姓名 / Name",
            "联系方式 / Contact",
            "机构 / Affiliation",
            "研究领域 / Research area",
            "代表性研究 / Representative research",
            "与任务相关的经验 / Relevant experience",
            "利益冲突 / Conflicts of interest",
        ),
        2: (
            "任务目标 / Goal",
            "科学价值 / Scientific value",
            "应用价值 / Application value",
            "现实使用者 / Who performs or needs this work",
            "价值证据 / Evidence",
        ),
        5: (
            "Agent-visible inputs",
            "Required outputs",
            "Main research stages",
            "Consequential decisions left to the agent",
            "Valid alternative approaches",
        ),
        6: (
            "Data/source/version",
            "License or data-use agreement",
            "Public or private",
            "Sensitive/personal/clinical data",
            "Immutable revision and checksum",
        ),
        7: (
            "Software and versions",
            "CPU/RAM/storage/GPU",
            "Network or sidecars",
            "Wall-clock budget",
            "CUA requirement",
        ),
        8: (
            "Success criterion",
            "Programmatic metrics or binary rubric",
            "Ground-truth provenance",
            "Threshold rationale",
            "Correct alternatives expected to pass",
            "Trivial/shortcut submissions expected to fail",
        ),
        9: (
            "Assumed expert profile",
            "Human expert time estimate",
            "Work breakdown",
            "Expected frontier-model performance",
            "Expected model failure modes",
        ),
    }
    for number, labels in required_values.items():
        if number not in parsed:
            continue
        for label in labels:
            value = metadata_value(parsed[number], label)
            if not value:
                errors.append(f"Section {number} requires '{label}'")

    if task_type == "frontier_research" and 4 in parsed:
        required_frontier = (
            "领域内意义 / Domain significance",
            "当前 SOTA / Current SOTA",
            "SOTA 证据与日期 / Evidence and date",
            "预注册突破标准 / Preregistered progress threshold",
        )
        for label in required_frontier:
            value = metadata_value(parsed[4], label)
            if not value or value.lower().startswith("not applicable") or value.lower() == "none":
                errors.append(f"Frontier task requires substantive '{label}'")

    if path.name != "TEMPLATE.md" and "examples" not in path.parts:
        try:
            relative = path.resolve().relative_to((repo_root / "proposals").resolve())
        except ValueError:
            errors.append("Proposal must live under proposals/<domain>/<task-slug>.md")
        else:
            if len(relative.parts) != 2:
                errors.append("Proposal path must be proposals/<domain>/<task-slug>.md")
            elif domain and relative.parts[0] != domain:
                errors.append("Proposal directory must match Primary domain")
            expected_slug = path.stem
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", expected_slug):
                errors.append("Proposal filename must be lowercase kebab-case")

    if proposal_id:
        for other in (repo_root / "proposals").rglob("*.md"):
            if other.resolve() == path.resolve() or other.name == "TEMPLATE.md":
                continue
            other_id = metadata_value(other.read_text(encoding="utf-8"), "Proposal ID")
            if other_id == proposal_id:
                errors.append(f"Duplicate Proposal ID also used by {other.relative_to(repo_root)}")
                break
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("proposal", type=Path, nargs="+")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    failed = False
    for path in args.proposal:
        errors = validate(path, args.repo_root)
        if errors:
            failed = True
            print(f"FAIL {path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {path}")
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())

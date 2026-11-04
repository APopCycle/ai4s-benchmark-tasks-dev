# Contributing tasks

This is an invitation-only development preview. Task format, verifier isolation,
runtime rules and implementation quality follow Terminal-Bench-Science unless
[AI4S_DELTA.md](docs/AI4S_DELTA.md) explicitly says otherwise.

## 1. Submit a proposal first

Copy `proposals/TEMPLATE.md` to
`proposals/<domain>/<task-slug>.md`, fill it, and run:

```bash
python3 scripts/check_proposal.py proposals/<domain>/<task-slug>.md
```

Open a proposal-only PR. One conflict-free domain reviewer must approve it.
Merge is the approval record; implementation begins afterward.

## 2. Create the Harbor task

```bash
uv tool install --force "harbor==0.24.0"
harbor tasks init <task-slug> \
  --include-canary-strings \
  --metadata-template task-template.toml \
  -p tasks/<domain>/<field>/
```

Required layout:

```text
tasks/<domain>/<field>/<task-slug>/
├── task.toml
├── instruction.md
├── README.md
├── environment/
├── solution/
├── tests/
└── authoring/       # optional, never agent-visible
```

Keep the TBS rules: explicit artifacts, separate no-network verifier, pinned
dependencies, fixed input revisions/checksums, outcome-based grading, binary
main reward, CTRF for discrete tests, and the standard 28800-second instruction
suffix.

`task.toml` additionally requires:

```toml
[metadata]
proposal_id = "AI4S-2026-domain-task-slug"
proposal_path = "proposals/domain/task-slug.md"
task_type = "workflow_automation" # or frontier_research
```

## 3. Test locally

```bash
bash scripts/run_task_checks.sh tasks/<domain>/<field>/<task-slug>
harbor run -p tasks/<domain>/<field>/<task-slug> -a oracle -k 5
harbor run -p tasks/<domain>/<field>/<task-slug> -a nop
```

Then run at least one available frontier agent/model and inspect the trajectory.
A model failure caused by infrastructure, ambiguity or a faulty verifier does
not demonstrate task difficulty.

## 4. Open the task PR

One PR contains one task. Include:

- approved proposal path and ID;
- oracle and nop results;
- model trials and trajectory analysis when available;
- verifier positive, near-miss, malformed and shortcut tests;
- data provenance, license, immutable revisions and checksums;
- disclosed conflicts, ethics and safety considerations.

## 5. Review

After mechanical checks, one domain reviewer and one technical reviewer review
in parallel. A distinct final reviewer acts as bar-raiser after both approve.
During the Dev preview, maintainers assign these roles manually.

## Task types

### workflow_automation

Complete a real existing workflow. A full oracle is expected, and the verifier
grades the outcome rather than one prescribed method.

### frontier_research

Freeze the problem, baseline, inputs, budget, metric and progress threshold
before trials. Use hidden instances or equivalent held-out evaluation. An
oracle exception requires explicit reviewer approval and strong feasibility
evidence; the verifier itself must remain objective.

## Repair and maintenance

Authors remain responsible for defects discovered after merge. Repairs require
an issue, a focused PR, reproduced evidence and the same scientific/technical
review standard.

# Contributing tasks

This is an invitation-only development preview. Follow the start-to-finish
[quickstart in README.md](README.md#quickstart).

## Proposal

Copy `proposals/TEMPLATE.md` to
`proposals/<primary-domain>/<task-slug>.md`, use `proposals/examples/` as a
reference, and validate it:

```bash
python3 scripts/check_proposal.py proposals/<primary-domain>/<task-slug>.md
```

Open one proposal-only PR. Begin implementation after the Domain Chair and Tech
Group approve the proposal and it is merged.

## Task

Initialize the task with Harbor and `task-template.toml`, then complete its
instruction, environment, oracle solution, verifier, metadata, and required
README. The root README gives both non-engineering and Engineering Sciences
commands.

```bash
bash scripts/run_task_checks.sh <task-path>
harbor run -p <task-path> -a oracle -k 5
harbor run -p <task-path> -a nop
```

Run the LLM review and model trials described in the root README, then open one
task PR linked to the merged proposal.

## Review

Proposal review, task review, frontier-model evaluation, and final confirmation
follow the seven-stage process in [REVIEWING.md](REVIEWING.md). Authors remain
responsible for fixing defects found after merge.

# 15-minute quickstart

## Install

Requirements: Git, Docker, Python 3.11+ and `uv`.

```bash
uv tool install --force "harbor==0.24.0"
docker version
harbor --version
```

## Run a real reference task

Start with the CPU-only assimilation task:

```bash
TASK=reference-tasks/earth-environmental-sciences/atmospheric-sciences/sparse-network-assimilation
bash scripts/run_task_checks.sh --reference "$TASK"
harbor run -p "$TASK" -a oracle
harbor run -p "$TASK" -a nop
```

Expected result: oracle reward 1 and nop reward 0. First build can take several
minutes. See `reference-tasks/README.md` for heavier examples.

## Propose a task

```bash
mkdir -p proposals/<domain>
cp proposals/TEMPLATE.md proposals/<domain>/<task-slug>.md
python3 scripts/check_proposal.py proposals/<domain>/<task-slug>.md
```

Open a proposal-only PR. Implement only after it is reviewed and merged.

## Build a task

```bash
harbor tasks init <task-slug> \
  --include-canary-strings \
  --metadata-template task-template.toml \
  -p tasks/<domain>/<field>/
```

Fill the task, then:

```bash
bash scripts/run_task_checks.sh tasks/<domain>/<field>/<task-slug>
harbor run -p tasks/<domain>/<field>/<task-slug> -a oracle -k 5
harbor run -p tasks/<domain>/<field>/<task-slug> -a nop
```

## Evaluate an agent

Agent/model flags depend on your Harbor adapter. A typical command is:

```bash
harbor run -p tasks/<domain>/<field>/<task-slug> \
  --agent <agent-adapter> --model <provider/model> -k 3
```

Retain run configuration, trajectories, artifacts, verifier diagnostics, cost
and wall time. Do not interpret infrastructure failures as model failures.

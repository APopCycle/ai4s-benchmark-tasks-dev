# Dev preview automation

## Required checks

`static-checks.yml` validates every proposal and runs the TBS-derived static
checks over formal tasks. `validate-task.yml` builds changed formal tasks and
runs oracle/nop using Harbor 0.24.0 without model API keys.

Local equivalents:

```bash
python3 scripts/check_proposal.py proposals/<domain>/<task>.md
bash scripts/run_task_checks.sh tasks/<domain>/<field>/<task>
```

Reference tasks use:

```bash
bash scripts/run_task_checks.sh --reference reference-tasks/<domain>/<field>/<task>
```

Reference tasks retain the upstream canary, so the local reference mode omits
the AI4S-canary and formal-path checks while retaining implementation checks.

## Optional evaluation

Frontier-model runs, trajectory analysis and cheat trials are initially local
or manually dispatched because they require model/API/cloud credentials. They
remain required review evidence when available but are not default CI jobs.

## Deliberately absent TBS integrations

The Dev repo does not call TBS Discord, dashboard, Zenodo, model gateways,
Harbor Hub organization, proposal Discussions or authorship-detection services.

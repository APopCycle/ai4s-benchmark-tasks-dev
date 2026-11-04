# Dev preview automation

## Required checks

`static-checks.yml` validates every proposal and runs the TBS-derived static
checks over formal tasks. `validate-task.yml` builds changed formal tasks and
runs oracle/nop using Harbor 0.24.0 without model API keys. Workflow oracle is
expected to score 1; frontier oracle is expected to score 0 while reporting
`valid=true` and `match_sota=true`.

Local equivalents:

```bash
python3 scripts/check_proposal.py proposals/<domain>/<task>.md
bash scripts/run_task_checks.sh <task-path>
```

Reference tasks use:

```bash
bash scripts/run_task_checks.sh --reference <reference-task-path>
```

Reference tasks retain the upstream canary, so the local reference mode omits
the AI4S-canary and formal-path checks while retaining implementation checks.

## Model-based evaluation

LLM rubric reviews, GLM pass-rate trials, Opus/GPT evaluation, trajectory
analysis, and adversarial cheat trials are initially local or manually
dispatched because they require model/API/cloud credentials. They are review
stages rather than default secret-free CI jobs. See Harbor's
[agent list](https://docs.harborframework.com/agents/pre-integrated-agents) and
[authentication guide](https://docs.harborframework.com/agents/agent-auth-resolution)
for model and API-key configuration.

## Deliberately absent TBS integrations

The Dev repo does not call TBS Discord, dashboard, Zenodo, model gateways,
Harbor Hub organization, proposal Discussions or authorship-detection services.

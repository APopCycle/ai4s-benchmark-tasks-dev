# Runnable reference tasks

These complete tasks demonstrate this repo's namespace, proposal linkage, task
types and taxonomy-aware layout. The four workflow examples retain their
official upstream scientific content; the AC1 example demonstrates the distinct
frozen-SOTA contract for frontier research. They are not part of the release
allowlist in `tasks/dataset.toml`.

| Task | Type | What it demonstrates | Relative cost |
|---|---|---|---|
| sparse-network-assimilation | workflow | inverse problem, hidden truth, multiple gates | CPU, recommended first |
| reactor-safety-control | workflow | simulation, safe control, hidden faults | CPU, longer verifier |
| protein-active-learning | workflow | multi-container hidden assay | CPU, Docker Compose |
| onsager-ising-lean | workflow | research-scale Lean kernel verification | CPU, large build |
| first-autocorrelation-inequality | frontier | exact scoring against a frozen current SOTA | CPU, recommended frontier example |

Example:

```bash
TASK=reference-tasks/earth-environmental-sciences/sparse-network-assimilation
bash scripts/run_task_checks.sh --reference "$TASK"
harbor run -p "$TASK" -a oracle
harbor run -p "$TASK" -a nop
```

For the frontier example, the expected oracle result is reward `0` with
`valid=true` and `match_sota=true` in `reward-details.json`:

```bash
TASK=reference-tasks/mathematical-sciences/first-autocorrelation-inequality
bash scripts/run_task_checks.sh --reference "$TASK"
bash scripts/validate_task.sh "$TASK"
```

The matching proposal for every task is in `proposals/examples/`. Upstream-derived
tasks retain their original authorship and revision metadata; the frontier example
records its SOTA source, frozen artifact digest and exact baseline in `task.toml`.

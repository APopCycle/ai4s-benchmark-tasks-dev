# Runnable reference tasks

These are complete official TBS tasks adapted only enough to demonstrate this
repo's namespace, proposal linkage, task types and taxonomy-aware layout. Their
scientific task content, environments, solutions and verifiers remain unchanged.
They are not part of the release allowlist in `tasks/dataset.toml`.

| Task | Type | What it demonstrates | Relative cost |
|---|---|---|---|
| sparse-network-assimilation | workflow | inverse problem, hidden truth, multiple gates | CPU, recommended first |
| reactor-safety-control | workflow | simulation, safe control, hidden faults | CPU, longer verifier |
| protein-active-learning | workflow | multi-container hidden assay | CPU, Docker Compose |
| onsager-ising-lean | workflow | research-scale Lean kernel verification | CPU, large build |

Example:

```bash
TASK=reference-tasks/earth-environmental-sciences/sparse-network-assimilation
bash scripts/run_task_checks.sh --reference "$TASK"
harbor run -p "$TASK" -a oracle
harbor run -p "$TASK" -a nop
```

Each task retains original authorship and the TBS canary. The matching normalized
proposal is in `proposals/examples/` and the exact upstream revision is stored in
task metadata and `UPSTREAM.md`.

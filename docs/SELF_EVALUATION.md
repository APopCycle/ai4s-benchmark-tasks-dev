# Task self-evaluation

Before opening a task PR:

## 1. Static checks

```bash
bash scripts/run_task_checks.sh tasks/<domain>/<field>/<task>
```

Resolve every failure. Review warnings rather than suppressing them blindly.

## 2. Solvability and negative control

```bash
harbor run -p tasks/<domain>/<field>/<task> -a oracle -k 5
harbor run -p tasks/<domain>/<field>/<task> -a nop
```

Oracle must be stable; nop must receive zero. Also test malformed output, empty
output, near-miss science, trivial baselines and anticipated reward hacks.

## 3. Alternative correct methods

The verifier must accept scientifically equivalent solutions rather than one
implementation. Add at least one independent correct method where practical.

## 4. Frontier agents

Run at least one available frontier agent/model, preferably two model families,
with repeated trials. Save trajectories and explain the causal failure mode.
Task ambiguity, dependency failure, timeout miscalibration and verifier bugs are
task defects, not desirable difficulty.

## 5. Reproducibility and safety

Pin packages and image/data revisions; record checksums; keep solution, tests and
hidden truth out of the agent image; treat agent artifacts as hostile input;
document licenses, privacy, ethics, biosecurity and dual use.

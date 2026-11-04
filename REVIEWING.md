# Reviewing proposals and tasks

## Proposal

One conflict-free domain reviewer checks author-task fit, real scientific value,
task type, objective verifiability, feasibility and meaningful difficulty. For
frontier tasks, also check the dated SOTA evidence and preregistered progress
threshold. Approval plus merge means the idea may be implemented; it does not
guarantee task acceptance.

## Task implementation

The TBS three-slot process is retained:

1. **Domain reviewer**: scientific validity, value, field conventions, metrics,
   thresholds, human-time estimate and acceptable alternative methods.
2. **Technical reviewer**: Harbor implementation, isolation, reproducibility,
   canary, artifact safety, oracle/nop, reward integrity and anti-cheat tests.
3. **Final reviewer**: distinct bar-raiser checking the complete evidence chain,
   task difficulty and portfolio value.

Domain and technical review run in parallel. Final review starts only after both
approve. LLM rubric results and model trials are evidence, never human approval.

## Minimum evidence

- static checks pass;
- oracle passes repeatedly and nop fails;
- correct alternatives pass; malformed/trivial/shortcut attempts fail;
- a trajectory review separates scientific failure from infrastructure failure;
- data, dependencies, ethics and conflicts are documented;
- instruction requirements and verifier gates map both ways.

Use `rubrics/task-implementation.toml` and `rubrics/trial-analysis.toml` as the
detailed TBS-derived checklists.

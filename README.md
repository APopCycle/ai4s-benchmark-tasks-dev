# AI4S Benchmark Tasks — Dev Preview

> This `-dev` repository is an invitation-only preview for testing task
> authoring, submission and evaluation. A separate production repository will
> be created after this workflow is validated with the first expert cohort.

This repository evaluates research agents on two task types:

- `workflow_automation`: complete a real, established scientific workflow;
- `frontier_research`: make preregistered, objectively verifiable progress on
  a frontier research problem.

Task execution uses [Harbor](https://github.com/harbor-framework/harbor). The
task format and quality bar are inherited from
[Terminal-Bench-Science](https://github.com/harbor-framework/terminal-bench-science)
at the revision recorded in [UPSTREAM.md](UPSTREAM.md). AI4S changes only the
proposal mechanism, task type and preview taxonomy.

## Start here

- [15-minute quickstart](docs/QUICKSTART.md)
- [Proposal guide](docs/PROPOSAL_GUIDE.md)
- [Task contribution guide](CONTRIBUTING.md)
- [Self-evaluation guide](docs/SELF_EVALUATION.md)
- [Human review process](REVIEWING.md)
- [AI4S differences from TBS](docs/AI4S_DELTA.md)
- [Runnable reference tasks](reference-tasks/README.md)

## Contributor flow

```text
proposal Markdown PR
        ↓ one domain approval + merge
Harbor task implementation PR
        ↓ static checks + oracle/nop
domain review ∥ technical review
        ↓
final bar-raiser
```

Merge does not automatically place a task in a benchmark release.
`tasks/dataset.toml` is the release allowlist.

## Quick commands

```bash
uv tool install --force "harbor==0.24.0"

python3 scripts/check_proposal.py proposals/<domain>/<task-slug>.md
bash scripts/run_task_checks.sh tasks/<domain>/<field>/<task-slug>

harbor run -p reference-tasks/earth-environmental-sciences/atmospheric-sciences/sparse-network-assimilation -a oracle
harbor run -p reference-tasks/earth-environmental-sciences/atmospheric-sciences/sparse-network-assimilation -a nop
```

## Preview domains

1. Mathematical Sciences
2. Physical Sciences
3. Chemical and Materials Sciences
4. Life Sciences
5. Medical, Neuroscience and Health Sciences
6. Earth and Environmental Sciences
7. Computer and Information Sciences
8. Engineering Sciences

The field registry is in `.github/reviewer-pool.yml`. Empty reviewer lists mean
manual assignment during the preview, not absent quality review.

## License and provenance

Apache-2.0. TBS-derived components and reference tasks retain upstream
attribution and canaries; see [NOTICE](NOTICE) and [UPSTREAM.md](UPSTREAM.md).

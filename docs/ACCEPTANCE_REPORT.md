# Dev preview acceptance report

Date: 2026-11-04 (Asia/Shanghai)

## Outcome

The local Dev repository is ready for the first invited expert cohort. The
proposal/task gates, secret-free CI, four adapted TBS examples, and two-domain
Harbor runtime bar have been exercised. Creating and pushing the external
GitHub repository remains intentionally pending owner decisions.

## Reproducibility baseline

- TBS source: `harbor-framework/terminal-bench-science` at
  `b4068a05dd71af986ad2d82988ae5dc0a931bbfe`
- Harbor: `0.24.0`
- Docker: `28.1.1`
- Python: `3.12.13`
- Git: `2.25.1`
- Formal release allowlist: empty (`tasks/dataset.toml`)

## Runtime evidence

| Reference task | Domain / shape | Oracle | nop | Result root |
|---|---|---:|---:|---|
| `reactor-safety-control` | engineering / separate verifier | 1.000 | 0.000 | `/tmp/ai4s-harbor-validation.2Mwrng` |
| `protein-active-learning` | life science / three-service environment | 1.000 | 0.000 | `/tmp/ai4s-harbor-validation.KVt9X0` |
| `protein-active-learning` repeat | flake check | 1.000 | — | `/tmp/ai4s-harbor-repeat.xyCxSM` |

All listed jobs completed with one trial, zero exceptions and zero retries.
The result roots are local evidence, not repository content. Docker builds on
this host required a temporary host-network/proxy compose override because its
daemon cannot reach the host's loopback proxy; those overrides were removed
before the final regression and are not part of the delivered repository.

## Deterministic validation

The exact default static-workflow sequence passed locally:

```bash
python3 scripts/check_proposal.py proposals/examples/*.md
bash scripts/test_validators.sh
bash scripts/test_task_gateways.sh
find reference-tasks -name task.toml -print | sort |
  while read -r f; do bash scripts/run_task_checks.sh --reference "$(dirname "$f")"; done
python3 ci_checks/check-rubric-consistency.py \
  task-template.toml rubrics/task-implementation.toml
```

Covered negative fixtures include invalid task type/domain, missing contact,
empty proposal section, missing frontier SOTA, duplicate proposal ID, invalid
formal task domain, metadata/path mismatch, missing proposal metadata, absent
approved proposal and missing AI4S canary. The inherited task checks cover
separate verifier, absolute paths, timeout, binary reward, host binds, pinned
dependencies and trial-time installs.

Additional checks passed:

- both GitHub workflow YAML files parse;
- every repository-relative Markdown link resolves;
- `git diff --check` reports no whitespace errors;
- no Git remote, credential, credible API key or personal local absolute path is
  present; a generic AWS-key regex matches `AKIA...` substrings in public protein
  sequences, which were manually confirmed as biological-data false positives;
- four reference tasks are excluded from the release allowlist;
- default workflows require no model or TBS-private secret;
- formal-task gateway tests exercise the same scripts used by Actions.

## A–H acceptance summary

| Area | Status | Evidence / boundary |
|---|---|---|
| A. Source and hygiene | Pass | pinned upstream, NOTICE/LICENSE, independent Git history, AI4S canary, clean final worktree |
| B. Documentation | Pass | README, 15-minute quickstart, proposal/task/review/self-evaluation guides, checked links |
| C. Proposal validation | Pass | workflow/frontier examples plus seven negative regression cases |
| D. Task static gates | Pass | four full references plus six formal gateway cases and inherited checks |
| E. Harbor/runtime | Pass | two domains oracle=1/nop=0; multi-container passed; repeated oracle passed |
| F. GitHub/CI portability | Pass locally | secret-free workflows and empty reviewer handles; external repo not yet created |
| G. Expert walkthrough | Pass locally | proposal examples, task gateway fixture, runnable full references and PR templates |
| H. Regression/record | Pass | commands and versions recorded here; temporary build overrides excluded |

## Deliberately deferred

- Computer-use/MCP enhancement is outside this preview.
- Frontier-model trials need the future project's model gateway and credentials;
  the repository documents the command but does not require secrets in CI.
- `onsager-ising-lean` is statically accepted but was not selected for the
  two-task runtime gate because its Lean build is substantially heavier.
- `sparse-network-assimilation` passed all static gates and its oracle solver
  produced `result.npz`; its additional verifier image build was stopped after
  the host's unproxied Docker network stalled. It is not counted as a runtime
  pass. The two required end-to-end passes above are unaffected.
- Hosted Harbor Hub publication, leaderboard release and automated reviewer
  assignment are production-repository work.

## GitHub creation gate

Before the first push, the owner must provide:

1. GitHub account or organization;
2. confirmation of `ai4s-benchmark-tasks-dev` as the repository name;
3. public/private visibility;
4. permission to create and push the external repository.

No repository secret is needed for the initial Dev CI. Branch protection should
require `static-checks / deterministic` and `validate-task-oracle-nop / validate`
for task PRs, plus at least one human approval during the preview.

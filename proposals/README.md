# Task proposals

This dev repository uses versioned Markdown proposals.

1. Copy `TEMPLATE.md` to `proposals/<domain>/<task-slug>.md`.
2. Fill every required field and run `python3 scripts/check_proposal.py <file>`.
3. Open a proposal-only pull request.
4. One conflict-free domain reviewer approves it. Merge means proposal approval.
5. Submit the implementation in a later PR. Its `task.toml` must point to the
   already-merged proposal through `proposal_id` and `proposal_path`.

Files in `proposals/examples/` document imported reference tasks and are not new
proposal applications.

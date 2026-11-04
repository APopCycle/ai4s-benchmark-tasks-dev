# Updating from TBS

1. Record the candidate upstream commit.
2. Compare only imported files listed in `UPSTREAM.md`.
3. Port security, Harbor compatibility and deterministic validation fixes as
   focused commits; do not merge upstream wholesale.
4. Reapply the namespace, canary, domains and file-proposal delta.
5. Run proposal fixtures, all static checks and reference oracle/nop regression.
6. Update `UPSTREAM.md` only after review.

Preserve upstream authorship and Apache-2.0 notices for every copied change.

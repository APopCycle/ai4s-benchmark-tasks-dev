# Proposal guide

The proposal is the scientific contract signed before implementation. It should
be understandable without reading hidden tests.

## What reviewers need to decide

- Is the author qualified to define and grade this work?
- Is the work real research rather than a textbook or generic coding exercise?
- Is its value specific and supported by evidence?
- Is the type determined by the final success criterion?
- Can an outcome verifier distinguish completion from shortcuts?
- Is it feasible within the stated compute and data-access model?
- Is difficulty scientific rather than clerical or environmental?

## Frontier research additions

State a dated baseline/SOTA, its evidence, why progress matters, the frozen
held-out evaluation and the numerical or formally checkable progress threshold.
Do not define success after seeing agent results.

## File and PR rules

- Path: `proposals/<domain>/<task-slug>.md`;
- one proposal per PR;
- no task implementation in the proposal PR;
- merge records approval;
- task PR references the merged file via `proposal_path` and `proposal_id`.

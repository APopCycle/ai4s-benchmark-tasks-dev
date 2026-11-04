# Reviewing proposals and tasks

## Roles

- **Domain Chairs** assess scientific validity, importance, difficulty, and
  field-appropriate evaluation.
- **Tech Reviewers / Tech Group** assess Harbor implementation, reproducibility,
  verifier integrity, automated reviews, and model trials.
- **Project Core Community / Core Committee** makes the final portfolio and
  release decision with the Tech Group and contributor.

## Review process

1. **Contributor task proposal + self quality check:** the contributor completes
   the proposal and runs a rubric-based LLM review.
2. **Task Proposal Review — Domain Chair + Tech Group:** review scientific fit,
   value, feasibility, objective evaluation, and proposed difficulty.
3. **Contributor task construction + self quality check:** implement the task;
   run mechanical checks, LLM implementation review, and GLM pass-rate trials.
4. **Task Review — Domain Chair + Tech Group:** review the scientific contract
   and the complete Harbor implementation.
5. **Frontier Model Evaluation:** measure Opus/GPT pass rates, review trajectories
   with an LLM, and run adversarial cheat review.
6. **Final Task Review — Tech Group + Core Committee + Contributor:** resolve
   remaining scientific, technical, and evaluation issues.
7. **Final Task Confirmation & Formal Evaluation:** confirm inclusion and run the
   formal evaluation configuration.

Automated checks and LLM reviews provide evidence; accountable humans make all
approval and release decisions. Detailed rubrics live under `rubrics/`.

# Upstream provenance

This development repository was bootstrapped from selected files in the official
[Terminal-Bench-Science](https://github.com/harbor-framework/terminal-bench-science)
repository.

- Upstream commit: `b4068a05dd71af986ad2d82988ae5dc0a931bbfe`
- Snapshot date: 2026-11-04
- Upstream license: Apache-2.0
- Harbor version used by this preview: `0.24.0`

## Imported components

- Harbor task templates and authoring conventions;
- deterministic static checks under `ci_checks/`;
- task implementation, trial-analysis and author-fit rubrics;
- task README tooling;
- four official tasks, retained under `reference-tasks/` with their original
  authorship, attribution, license notices and upstream canary.

## Local changes

- AI4S branding and namespace;
- eight-domain preview taxonomy;
- file-based Markdown proposals instead of Airtable/GitHub Discussions;
- two task types: `workflow_automation` and `frontier_research`;
- file-based proposal-to-task linkage;
- workflows that do not require Terminal-Bench-Science private services.

Do not merge upstream `main` automatically. Review changes against the pinned
commit and port individual fixes with attribution.

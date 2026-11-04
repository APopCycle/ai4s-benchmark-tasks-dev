# AI4S formal tasks

This directory contains proposed AI4S benchmark tasks. Non-engineering tasks use:

```text
tasks/<primary-domain>/<task-slug>/
```

Engineering Sciences tasks use
`tasks/engineering-sciences/<secondary-discipline>/<task-slug>/`. See
the [taxonomy in the root README](../README.md#3-classify-the-task). A more specific research area is
required free text in task metadata and does not appear in the path.

Only tasks listed in `dataset.toml` belong to a release. During the Dev preview
that allowlist is intentionally empty; runnable examples live under
[`reference-tasks/`](../reference-tasks/README.md).

Start with the [root quickstart](../README.md#quickstart-from-setup-to-submission).
Do not add a task implementation
before its Markdown proposal has been approved and merged.

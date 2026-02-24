# Static workflow badges (manual setup)

You can add workflow status badges to any Markdown (e.g. this repo’s README or another repo’s README) so they show pass/fail at a glance. Badges update when the workflow runs.

## How to add a badge

1. In the **repository** that has the workflow, open **Actions** and select the workflow.
2. Click the **⋯** menu next to the workflow, then **Create status badge**.
3. Copy the Markdown or image URL and paste it into your document.

Badge URL pattern (replace `ORG`, `REPO`, and workflow name):

```text
https://github.com/ORG/REPO/workflows/WORKFLOW%20NAME/badge.svg
```

## Example table

| Repository | Workflow   | Status |
|------------|------------|--------|
| repo1      | CI Build   | ![CI Build](https://github.com/your-org/repo1/workflows/CI%20Build/badge.svg) |
| repo2      | Tests      | ![Tests](https://github.com/your-org/repo2/workflows/Tests/badge.svg) |

**Note:** For an automated list of all workflows across the organization, use the generated [statuses.md](../statuses.md) instead of maintaining badges by hand.

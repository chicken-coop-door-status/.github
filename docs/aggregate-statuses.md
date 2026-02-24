# Aggregate Workflow Statuses

The [Aggregate Workflow Statuses](../.github/workflows/aggregate-statuses.yml) workflow collects the latest run status of every GitHub Actions workflow in every repository in the organization and writes them to [statuses.md](../statuses.md).

## Triggers

- **Schedule:** runs hourly (cron `0 * * * *`). To change the schedule, edit the `schedule` section in `.github/workflows/aggregate-statuses.yml`.
- **Manual:** run from the Actions tab via **Workflow dispatch**.

## Authentication

- **Default:** The job uses `GITHUB_TOKEN`, which can list and read workflows only for repositories the token has access to within the org.
- **Private repos:** To include private organization repositories, add a [Personal Access Token](https://github.com/settings/tokens) with scopes `repo` and `admin:org` (read org and repos), and store it as a **repository secret** named `GH_TOKEN`. The workflow uses `GH_TOKEN` when set, otherwise `GITHUB_TOKEN`.

## Output

- **File:** `statuses.md` in the repository root (generated; do not edit by hand).
- **Content:** Markdown table with columns: Repository, Workflow, Status (✅ Passed / ❌ Failed), Last Run. A trailing “Updated: …” line records the last run time.

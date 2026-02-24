# Aggregate Workflow Statuses

The [pipeline](.github/workflows/pipeline.yml) collects the latest run status of every GitHub Actions workflow in every repository in the organization and writes them to [statuses.md](../statuses.md). It also updates the table in [profile/README.md](../profile/README.md), which is what appears on the **organization’s Overview page**.

## Org Overview (profile README)

- **What shows on the org main page:** GitHub uses the file **`profile/README.md`** in this repo, not the repo root `README.md`.
- **Visibility:** The **`.github` repository must be public** for the org profile README to appear on the Overview tab. If `.github` is private, the Overview page will not show any README.

## Triggers

- **Push:** runs on every push to `main` (so you see a run after each merge).
- **Schedule:** runs hourly (cron `0 * * * *`). To change it, edit `.github/workflows/pipeline.yml`.
- **Manual:** run from the Actions tab via **Run workflow** (workflow_dispatch).

## Authentication (private / internal repos)

- **Required for private repos:** The default `GITHUB_TOKEN` cannot list other private repos in the org. You **must** add a [Personal Access Token](https://github.com/settings/tokens) with scopes `repo` and `admin:org` (read org and repos) and store it as a **repository secret** named **`GH_TOKEN`**. The workflow uses `GH_TOKEN` when set; otherwise it uses `GITHUB_TOKEN` (which will not see other private repos).
- After adding `GH_TOKEN`, trigger a run via **Actions → Aggregate Workflow Statuses → Run workflow** to populate the status table.

## Output

- **statuses.md** (repo root): full table (generated; do not edit by hand).
- **README.md** (repo root) and **profile/README.md**: same table injected between the marker comments. Only **profile/README.md** is shown on the org Overview page.

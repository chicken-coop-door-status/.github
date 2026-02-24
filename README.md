# .github

One repo to rule them all...

**Org Overview page:** The content on the organization’s main Overview tab comes from **[profile/README.md](profile/README.md)** in this repo. **If you see nothing on the org page:** the `.github` repo must be **public** (Settings → General → Danger Zone → Change visibility). See [docs/org-profile-readme.md](docs/org-profile-readme.md).

## Workflow statuses

The table below is updated automatically by the [pipeline](.github/workflows/pipeline.yml) (on push to main, hourly, and manual run).

<!-- WORKFLOW_STATUS_TABLE -->
| Repository | Workflow | Status | Last Run |
|------------|----------|--------|----------|
| c2ds-bootstrap | Auto-Deploy (Push to Main) | ❌ Failed | 2026-02-09 17:39 |
| c2ds-bootstrap | Pipeline (Build → Test → Deploy) | ✅ Passed | 2026-02-22 21:45 |
| c2ds-mobile-app | Flutter Tests | ✅ Passed | 2026-02-09 16:18 |
| c2ds-mobile-app | Pipeline | ✅ Passed | 2026-02-22 18:48 |
| c2ds-door-sensor-assignments | Update IoT Device Shadows | ❌ Failed | 2026-02-11 23:41 |
| c2ds-api | Deploy SAM App | ✅ Passed | 2026-02-17 20:49 |
| c2ds-lambdas | Pipeline (Safety → Deploy) | ✅ Passed | 2026-02-24 14:51 |
| c2ds-cognator | pipeline | ✅ Passed | 2026-02-24 14:03 |
| esp-web-tools | CI | ❌ Failed | 2026-02-14 15:56 |
| esp-web-tools | Deploy to Amplify | ❌ Failed | 2026-02-14 15:56 |
| esp-web-tools | Release Drafter | ✅ Passed | 2026-02-14 15:56 |
| esp-web-tools | CodeQL | ✅ Passed | 2026-02-23 17:04 |
| ESPConnect | CodeQL | ✅ Passed | 2026-02-22 15:12 |
| c2ds-brood | Deploy Firmware to S3 | ❌ Failed | 2026-02-11 02:24 |
| c2ds-brood | Pipeline | ✅ Passed | 2026-02-22 22:27 |
| c2ds-app-common | Bump downstream on release | ❌ Failed | 2026-02-09 12:51 |
| c2ds-app-common | Pipeline | ✅ Passed | 2026-02-22 21:38 |
| c2ds-proforma | Build | ❌ Failed | 2026-02-24 02:00 |
| .github | Aggregate Workflow Statuses | ⏳ Running | 2026-02-24 16:01 |
Updated: 2026-02-24 16:02:42 UTC
<!-- /WORKFLOW_STATUS_TABLE -->

Full list and history: [statuses.md](statuses.md). For triggers and optional `GH_TOKEN` (PAT for private repos), see [Aggregate statuses](docs/aggregate-statuses.md). For manual badge setup, see [Static badges](docs/static-badges.md).

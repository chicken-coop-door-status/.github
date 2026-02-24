# .github

One repo to rule them all...

> **Org Overview empty?** The org’s main page only shows content when this repo is **Public**.  
> **Fix:** [Settings → General → Danger Zone → Change visibility → Public](https://github.com/chicken-coop-door-status/.github/settings).  
> Details: [PROFILE_VISIBILITY_REQUIRED.md](PROFILE_VISIBILITY_REQUIRED.md) and [docs/org-profile-readme.md](docs/org-profile-readme.md).

**Org Overview page:** The org’s main page shows **[profile/README.md](profile/README.md)** (when this repo is public). The [pipeline](.github/workflows/pipeline.yml) updates **only** that file with the workflow status table—not this repo README.

Full status list: [statuses.md](statuses.md). For triggers and `GH_TOKEN`, see [Aggregate statuses](docs/aggregate-statuses.md). For manual badges, see [Static badges](docs/static-badges.md).

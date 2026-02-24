# Showing a README on the organization’s main page

GitHub shows the org’s **Overview** tab from one place only: **`profile/README.md`** in the **`.github`** repository. The repo root `README.md` is **not** used for the org page.

## Why nothing appears on the org page

**The `.github` repository must be public.** If it is private or internal, the Overview tab will not show any README, even though `profile/README.md` exists.

## Steps to show the README on the org Overview

1. **Make this repository (`.github`) public**
   - Open the repo: `https://github.com/chicken-coop-door-status/.github`
   - Go to **Settings** → **General**
   - Scroll to **Danger Zone**
   - Click **Change repository visibility** → choose **Public** → confirm

2. **Confirm `profile/README.md` exists**
   - The file should be at the path `profile/README.md` in this repo (it is).
   - The pipeline updates the status table in this file.

3. **Visit the org’s main page**
   - Go to `https://github.com/chicken-coop-door-status`
   - The **Overview** tab should now show the content of `profile/README.md`.

## If you need to keep `.github` private

- The **public** org Overview will stay empty.
- You can use a **member-only** README: create a **private** repository named **`.github-private`**, add a `profile` folder with `README.md` inside it. Org members will see that README when they open the org profile and switch to the **member** view. The public view will still show nothing.

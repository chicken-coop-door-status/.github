#!/usr/bin/env python3
"""
Aggregate GitHub Actions workflow run statuses across all repos in an organization.
Writes a Markdown table to statuses.md (or a given path).
Uses env: GITHUB_ORG (or --org), GH_TOKEN (required).
"""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timezone


def conclusion_to_status(conclusion: str | None) -> str:
    """Map workflow run conclusion to display status. Pure function for testing."""
    if conclusion == "success":
        return "✅ Passed"
    if conclusion in ("failure", "cancelled", "timed_out", "action_required"):
        return "❌ Failed"
    if conclusion is None:
        return "⏳ Running"
    return f"❓ {conclusion}"


def row_from_run(
    repo_name: str,
    workflow_name: str,
    conclusion: str | None,
    created_at: datetime | None,
) -> str:
    """Build a single Markdown table row. Pure function for testing."""
    status = conclusion_to_status(conclusion)
    last_run = (
        created_at.strftime("%Y-%m-%d %H:%M")
        if created_at
        else "—"
    )
    return f"| {repo_name} | {workflow_name} | {status} | {last_run} |"


def table_from_rows(rows: list[str], updated_iso: str) -> str:
    """Build full Markdown content from header + rows. Pure function for testing."""
    header = (
        "# Workflow Statuses Across Organization\n\n"
        "| Repository | Workflow | Status | Last Run |\n"
        "|------------|----------|--------|----------|\n"
    )
    body = "\n".join(rows) if rows else ""
    footer = f"\n\nUpdated: {updated_iso}\n"
    return header + body + footer


def collect_rows_from_org(org_name: str, token: str) -> list[str]:
    """
    Use PyGithub to list org repos, workflows, and latest run per workflow.
    Returns list of table row strings. Logs errors per repo but continues.
    """
    try:
        from github import Github
    except ImportError:
        print("PyGithub is required: pip install PyGithub", file=sys.stderr)
        sys.exit(1)

    gh = Github(token)
    try:
        org = gh.get_organization(org_name)
    except Exception as e:
        print(f"Failed to get organization {org_name!r}: {e}", file=sys.stderr)
        sys.exit(1)

    rows: list[str] = []
    for repo in org.get_repos():
        try:
            repo_rows = _rows_for_repo(repo)
            rows.extend(repo_rows)
        except Exception as e:
            print(f"Error processing {repo.name}: {e}", file=sys.stderr)

    return rows


def _rows_for_repo(repo) -> list[str]:
    """Fetch workflow runs for one repo; return list of table rows."""
    rows: list[str] = []
    try:
        workflows = repo.get_workflows()
    except Exception:
        return rows

    for workflow in workflows:
        try:
            runs = workflow.get_runs().get_page(0)
            if runs:
                run = runs[0]
                row = row_from_run(
                    repo.name,
                    workflow.name,
                    run.conclusion,
                    run.created_at,
                )
                rows.append(row)
            else:
                row = row_from_run(repo.name, workflow.name, None, None)
                rows.append(row)
        except Exception as e:
            print(f"  {repo.name} / {workflow.name}: {e}", file=sys.stderr)

    return rows


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Aggregate workflow statuses and write statuses.md"
    )
    parser.add_argument(
        "--org",
        default=os.environ.get("GITHUB_ORG"),
        help="GitHub organization name (default: GITHUB_ORG)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="statuses.md",
        metavar="FILE",
        help="Output Markdown file path (default: statuses.md)",
    )
    args = parser.parse_args()

    token = os.environ.get("GH_TOKEN")
    if not token:
        print("GH_TOKEN environment variable is required", file=sys.stderr)
        sys.exit(1)
    if not args.org:
        print("Organization required: set GITHUB_ORG or use --org", file=sys.stderr)
        sys.exit(1)

    rows = collect_rows_from_org(args.org, token)
    updated_iso = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    content = table_from_rows(rows, updated_iso)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    main()

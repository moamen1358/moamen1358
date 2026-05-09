#!/usr/bin/env python3
"""Update README.md dashboard sections from the live GitHub API.

Replaces the content between marker pairs:
  <!-- recent_commits starts --> ... <!-- recent_commits ends -->
  <!-- active_projects starts --> ... <!-- active_projects ends -->
  <!-- recent_projects starts --> ... <!-- recent_projects ends -->
"""
from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

USER = "moamen1358"
README = Path(__file__).resolve().parents[2] / "README.md"


def gh_api(path: str) -> list | dict:
    token = os.environ.get("GITHUB_TOKEN", "")
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "moamen-dashboard",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = Request(f"https://api.github.com{path}", headers=headers)
    try:
        with urlopen(req, timeout=20) as r:
            return json.load(r)
    except HTTPError as e:
        print(f"API error on {path}: {e.code} {e.reason}", file=sys.stderr)
        raise


def relative_time(iso: str) -> str:
    then = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    delta = datetime.now(timezone.utc) - then
    if delta.days >= 365:
        return f"{delta.days // 365}y ago"
    if delta.days >= 30:
        return f"{delta.days // 30}mo ago"
    if delta.days >= 1:
        return f"{delta.days}d ago"
    hours = delta.seconds // 3600
    if hours >= 1:
        return f"{hours}h ago"
    return "just now"


def build_recent_commits() -> str:
    """Last 5 commits as a clean markdown table — | When | Commit | Repo |."""
    events = gh_api(f"/users/{USER}/events/public?per_page=60")
    seen: set[str] = set()
    rows: list[tuple[str, str, str, str]] = []
    for e in events:
        if e["type"] != "PushEvent":
            continue
        head_sha = e["payload"].get("head")
        repo_full = e["repo"]["name"]
        if not head_sha or head_sha in seen:
            continue
        seen.add(head_sha)
        try:
            commit = gh_api(f"/repos/{repo_full}/commits/{head_sha}")
        except HTTPError:
            continue
        author = (commit.get("author") or {}).get("login")
        if author and author != USER:
            continue
        msg = commit["commit"]["message"].split("\n")[0]
        for prefix in ("feat:", "fix:", "chore:", "docs:", "refactor:", "readme:", "profile:", "security:", "dashboard:"):
            if msg.lower().startswith(prefix):
                msg = msg[len(prefix):].strip()
                break
        # Markdown-table cells: keep messages short enough to not blow up
        # column width, but readable.
        if len(msg) > 60:
            msg = msg[:57].rstrip() + "..."
        repo = repo_full.split("/")[-1]
        url = f"https://github.com/{repo_full}/commit/{head_sha}"
        when = relative_time(e["created_at"])
        rows.append((when, msg, repo, url))
        if len(rows) >= 5:
            break

    if not rows:
        return "_No recent activity._"
    out = ["| When | Commit | Repo |", "|:---|:---|:---|"]
    for when, msg, repo, url in rows:
        out.append(f"| _{when}_ | [{msg}]({url}) | **{repo}** |")
    return "\n".join(out)


def list_owned_repos(sort: str) -> list[dict]:
    """Public, non-fork, non-archived repos. sort = pushed | created."""
    repos = gh_api(f"/users/{USER}/repos?sort={sort}&per_page=20&type=public")
    return [r for r in repos if not r["fork"] and not r["archived"] and r["name"] != USER]


def build_active_projects() -> str:
    """Top 4 most-recently-pushed public repos."""
    repos = list_owned_repos("pushed")[:4]
    return "\n\n".join(_render_repo(r, key="pushed_at", verb="Pushed") for r in repos)


def build_recent_projects() -> str:
    """Top 4 most-recently-created public repos."""
    repos = list_owned_repos("created")[:4]
    return "\n\n".join(_render_repo(r, key="created_at", verb="Created") for r in repos)


def _render_repo(r: dict, key: str, verb: str) -> str:
    """Repo name + relative time. No description — the name carries the meaning,
    and short rows fit a 33% column width without wrapping."""
    name = r["name"]
    url = f"https://github.com/{USER}/{name}"
    when = relative_time(r[key])
    return f"[**{name}**]({url}) · _{when}_"


def replace_section(content: str, marker: str, payload: str) -> str:
    pattern = rf"<!-- {marker} starts -->.*?<!-- {marker} ends -->"
    replacement = f"<!-- {marker} starts -->\n{payload}\n<!-- {marker} ends -->"
    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def main() -> int:
    if not README.exists():
        print(f"README not found at {README}", file=sys.stderr)
        return 1
    content = README.read_text()
    content = replace_section(content, "recent_commits", build_recent_commits())
    content = replace_section(content, "active_projects", build_active_projects())
    content = replace_section(content, "recent_projects", build_recent_projects())
    README.write_text(content)
    print(f"Wrote {README}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

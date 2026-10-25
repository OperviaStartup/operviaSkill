#!/usr/bin/env python3
"""Install the Opervia skill for one or more supported coding agents."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile


PACKAGE_ID = "github.com/OperviaStartup/operviaSkill"
SKILL_NAME = "opervia"
MARKER_NAME = ".opervia-install.json"
AGENTS = ("codex", "claude", "cursor", "generic")


def agent_root(agent: str, home: Path, env: dict[str, str]) -> Path:
    if agent == "codex":
        return Path(env.get("CODEX_HOME", str(home / ".codex"))).expanduser() / "skills"
    if agent == "claude":
        return home / ".claude" / "skills"
    if agent == "cursor":
        return home / ".cursor" / "skills"
    if agent == "generic":
        return home / ".agents" / "skills"
    raise ValueError(f"Unsupported agent: {agent}")


def detect_agents(home: Path, env: dict[str, str]) -> list[str]:
    bases = {
        "codex": Path(env.get("CODEX_HOME", str(home / ".codex"))).expanduser(),
        "claude": home / ".claude",
        "cursor": home / ".cursor",
        "generic": home / ".agents",
    }
    detected = [agent for agent, base in bases.items() if base.exists()]
    return detected or ["generic"]


def owned_destination(destination: Path) -> bool:
    marker = destination / MARKER_NAME
    if not marker.is_file():
        return False
    try:
        data = json.loads(marker.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return data.get("package") == PACKAGE_ID and data.get("skill") == SKILL_NAME


def install_skill(source: Path, destination: Path, dry_run: bool = False) -> str:
    if not (source / "SKILL.md").is_file():
        raise RuntimeError(f"Skill source is invalid: {source}")
    if destination.exists() and not owned_destination(destination):
        raise RuntimeError(
            f"Refusing to overwrite an unmanaged destination: {destination}. "
            "Move it aside or install with --target to another empty path."
        )
    if dry_run:
        return f"Would install {source} -> {destination}"

    destination.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{SKILL_NAME}-", dir=destination.parent))
    try:
        shutil.copytree(source, staging, dirs_exist_ok=True)
        (staging / MARKER_NAME).write_text(
            json.dumps({"package": PACKAGE_ID, "skill": SKILL_NAME}, indent=2) + "\n",
            encoding="utf-8",
        )
        if destination.exists():
            shutil.rmtree(destination)
        staging.replace(destination)
    except Exception:
        if staging.exists():
            shutil.rmtree(staging)
        raise
    return f"Installed {SKILL_NAME} -> {destination}"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install the Opervia agent skill.")
    parser.add_argument(
        "--agent",
        action="append",
        choices=("auto", "all", *AGENTS),
        help="Target agent; repeat for several. Defaults to auto detection.",
    )
    parser.add_argument(
        "--target",
        type=Path,
        help="Custom skill directory for an unsupported agent; cannot be combined with --agent.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Show destinations without writing.")
    return parser.parse_args(argv)


def selected_agents(values: list[str] | None, home: Path, env: dict[str, str]) -> list[str]:
    requested = values or ["auto"]
    selected: list[str] = []
    for value in requested:
        if value == "auto":
            additions = detect_agents(home, env)
        elif value == "all":
            additions = list(AGENTS)
        else:
            additions = [value]
        for agent in additions:
            if agent not in selected:
                selected.append(agent)
    return selected


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.target is not None and args.agent:
        print("error: --target cannot be combined with --agent", file=sys.stderr)
        return 2

    repo_root = Path(__file__).resolve().parent
    source = repo_root / "skills" / SKILL_NAME
    home = Path.home()
    env = dict(os.environ)
    if args.target:
        destinations = [args.target.expanduser()]
    else:
        destinations = [
            agent_root(agent, home, env) / SKILL_NAME
            for agent in selected_agents(args.agent, home, env)
        ]

    try:
        for destination in destinations:
            print(install_skill(source, destination, args.dry_run))
    except (OSError, RuntimeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

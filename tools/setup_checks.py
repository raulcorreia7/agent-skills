"""Behavior checks for the public skills installer."""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

from lib import ROOT, SetupError, TreeTask, matches, skill_names, tree_entry_map


def invoke(home: Path, project: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    environment.pop("CODEX_HOME", None)
    environment.update(HOME=str(home), USERPROFILE=str(home))
    return subprocess.run(
        [sys.executable, "-S", str(ROOT / "skills.py"), *arguments],
        check=False,
        capture_output=True,
        text=True,
        env=environment,
        cwd=project,
    )


def invoke_wizard(home: Path, project: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    environment.pop("CODEX_HOME", None)
    environment.update(HOME=str(home), USERPROFILE=str(home))
    return subprocess.run(
        [sys.executable, "-S", str(ROOT / "wizard.py"), *arguments],
        check=False,
        capture_output=True,
        text=True,
        stdin=subprocess.DEVNULL,
        env=environment,
        cwd=project,
    )


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SetupError(f"setup check failed: {message}")


def require_baseline_files(root: Path, label: str) -> None:
    for path in sorted((ROOT / "baselines").iterdir()):
        if not path.is_file():
            continue
        installed = root / path.name
        require(installed.is_file() and installed.read_bytes() == path.read_bytes(), f"{label}: {path.name}")


def run() -> list[str]:
    try:
        with tempfile.TemporaryDirectory(prefix="agent-skills-", dir=ROOT) as temporary:
            root = Path(temporary)
            home, project = root / "home", root / "project"
            home.mkdir()
            home.joinpath(".claude").mkdir()
            project.mkdir()

            source_tree = root / "source-tree"
            source_tree.joinpath("__pycache__").mkdir(parents=True)
            source_tree.joinpath("kept.txt").write_text("kept\n", encoding="utf-8")
            source_tree.joinpath("ignored.pyc").write_bytes(b"generated")
            source_tree.joinpath("__pycache__/ignored.pyc").write_bytes(b"generated")
            require(set(tree_entry_map(source_tree)) == {Path("kept.txt")}, "generated tree entries excluded")

            require(invoke(home, project, "--help").returncode == 0, "root help")
            help_result = invoke(home, project, "install", "--help")
            require(help_result.returncode == 0, "install help")
            require("install docs" in help_result.stdout and "install --all" in help_result.stdout, "help examples")
            require("--project" in help_result.stdout, "project scope option documented")
            require(invoke_wizard(home, project, "--help").returncode == 0, "wizard help")
            wizard_result = invoke_wizard(home, project)
            require(
                wizard_result.returncode == 2 and "skills.py" in wizard_result.stderr,
                "wizard refuses a non-interactive terminal",
            )
            for obsolete in ("--bundle", "--skill", "--scope", "--tool", "--target", "--baseline", "--agent"):
                require(obsolete not in help_result.stdout, f"obsolete option in help: {obsolete}")

            result = invoke(home, project, "install")
            require(result.returncode == 2 and "select one skill" in result.stderr, "bare install rejected")
            result = invoke(home, project, "install", "missing-skill")
            require(result.returncode == 2 and "unknown skill" in result.stderr, "unknown skill rejected")
            result = invoke(home, project, "install", "docs", "--all")
            require(result.returncode == 2 and "select one skill" in result.stderr, "two selectors rejected")
            require(invoke(home, project, "install", "docs", "code").returncode == 2, "two skills rejected")

            result = invoke(home, project, "install", "docs", "--project", "--dry-run")
            require(result.returncode == 0, "dry run")
            require(not (project / ".agents/skills/docs").exists(), "dry run must not install")
            require(not (project / ".agents/skills/README.md").exists(), "dry run must not install catalog")
            require(not (home / ".codex").exists(), "local dry run must not install baseline")

            result = invoke(home, project, "install", "docs", "--project")
            project_skills = project / ".agents/skills"
            require(result.returncode == 0 and (project_skills / "docs/SKILL.md").is_file(), "project install")
            require(not project_skills.joinpath("README.md").exists(), "partial install omits catalog")
            require(invoke(home, project, "install", "docs", "--project").returncode == 0, "idempotent install")

            result = invoke(home, project, "install", "scripts")
            require(result.returncode == 0 and (home / ".agents/skills/scripts/SKILL.md").is_file(), "global install")
            codex_root = home / ".codex"
            agents_root = home / ".agents"
            require_baseline_files(codex_root, "global baseline")
            require(
                matches(TreeTask(ROOT / "baselines/guardrails", codex_root / "guardrails", codex_root)),
                "global guardrails install",
            )
            require_baseline_files(agents_root, "shared baseline")
            require(
                matches(TreeTask(ROOT / "baselines/guardrails", agents_root / "guardrails", agents_root)),
                "shared guardrails install",
            )
            require(
                (home / ".claude/CLAUDE.md").read_bytes() == (ROOT / "baselines/claude/CLAUDE.md").read_bytes(),
                "claude bridge install",
            )
            require(
                invoke(home, project, "install", "scripts", "--global").returncode == 0,
                "idempotent global install",
            )

            codex_root.joinpath("AGENTS.md").write_text("local change\n", encoding="utf-8")
            codex_root.joinpath("guardrails/local-extra.md").write_text("local change\n", encoding="utf-8")
            agents_root.joinpath("AGENTS.md").write_text("local change\n", encoding="utf-8")
            agents_root.joinpath("guardrails/local-extra.md").write_text("local change\n", encoding="utf-8")
            home.joinpath(".claude/CLAUDE.md").write_text("local change\n", encoding="utf-8")
            result = invoke(home, project, "install", "docs", "--global")
            require(
                result.returncode == 0 and not codex_root.joinpath("guardrails/local-extra.md").exists(),
                "automatic baseline synchronization",
            )
            require_baseline_files(codex_root, "baseline file overwrite")
            require(
                not agents_root.joinpath("guardrails/local-extra.md").exists(),
                "automatic shared baseline synchronization",
            )
            require_baseline_files(agents_root, "shared baseline file overwrite")
            require(
                home.joinpath(".claude/CLAUDE.md").read_text(encoding="utf-8") == "local change\n",
                "claude bridge left untouched",
            )

            result = invoke(home, project, "install", "--all", "--project")
            require(result.returncode == 0, "all install")
            require(
                {path.name for path in project_skills.iterdir()} == {*skill_names(), "README.md"},
                "all boundary",
            )
            require(
                project_skills.joinpath("README.md").read_bytes() == (ROOT / "skills/README.md").read_bytes(),
                "catalog install",
            )

            docs_root = project_skills / "docs"
            docs_root.joinpath("SKILL.md").write_text("local change\n", encoding="utf-8")
            docs_root.joinpath("local-extra.txt").write_text("local change\n", encoding="utf-8")
            project_skills.joinpath("README.md").write_text("local change\n", encoding="utf-8")
            result = invoke(home, project, "install", "docs", "--project")
            require(result.returncode == 2 and docs_root.joinpath("local-extra.txt").exists(), "conflict refusal")
            result = invoke(home, project, "install", "docs", "--project", "--overwrite")
            require(result.returncode == 0 and not docs_root.joinpath("local-extra.txt").exists(), "overwrite")
            require(
                project_skills.joinpath("README.md").read_bytes() == (ROOT / "skills/README.md").read_bytes(),
                "catalog overwrite",
            )

            blocked_project = root / "blocked-project"
            blocked_project.mkdir()
            blocked = blocked_project / ".agents"
            blocked.write_text("file\n", encoding="utf-8")
            result = invoke(home, blocked_project, "install", "docs", "--project")
            require(result.returncode == 2 and blocked.is_file(), "regular-file ancestor")

            if hasattr(os, "symlink"):
                real, link = root / "real", project / ".agents"
                real.mkdir()
                project_agents = project / ".agents"
                if project_agents.exists():
                    project_agents.rename(project / ".agents-installed")
                try:
                    link.symlink_to(real, target_is_directory=True)
                except OSError:
                    pass
                else:
                    result = invoke(home, project, "install", "docs", "--project")
                    require(result.returncode == 2, "symlink destination")

    except (OSError, SetupError) as error:
        return [str(error)]
    return []

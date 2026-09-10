#!/usr/bin/env python3
"""Install one skill or all skills from this repository."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
import tempfile
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

from tools.lib import (
    BASELINES,
    SKILLS,
    SetupError,
    TreeTask,
    ensure_safe_destination,
    matches,
    skill_names,
    tree_entries,
    tree_entry_map,
)

EXAMPLES = """Examples:
  python skills.py install docs
  python skills.py install --all
  python skills.py install docs --global
  python skills.py install --all --global
"""

CLAUDE_BRIDGE = BASELINES / "claude/CLAUDE.md"


@dataclass(frozen=True)
class FileTask:
    source: Path
    destination: Path
    managed_root: Path
    replace_different: bool = False


def selected_skills(args: argparse.Namespace) -> tuple[str, ...]:
    if bool(args.skill) == args.all_skills:
        raise SetupError("select one skill by name or use --all")
    if args.all_skills:
        return skill_names()
    available = set(skill_names())
    if args.skill not in available:
        raise SetupError(f"unknown skill: {args.skill}")
    return (args.skill,)


def user_home() -> Path:
    home_value = os.environ.get("HOME") or os.environ.get("USERPROFILE")
    if not home_value:
        raise SetupError("HOME (or USERPROFILE on Windows) is not set")
    home = Path(home_value).expanduser().resolve()
    if home == Path(home.anchor):
        raise SetupError(f"HOME must not be the filesystem root: {home}")
    return home


def installation_root(*, global_scope: bool) -> Path:
    base = user_home() if global_scope else Path.cwd().resolve()
    label = "HOME" if global_scope else "project"
    if base == Path(base.anchor):
        raise SetupError(f"{label} must not be the filesystem root: {base}")
    return base / ".agents" / "skills"


def codex_baseline_root() -> Path:
    configured = os.environ.get("CODEX_HOME")
    root = Path(configured).expanduser().absolute() if configured else user_home() / ".codex"
    if root == Path(root.anchor):
        raise SetupError(f"CODEX_HOME must not be the filesystem root: {root}")
    return root


def tasks_for(args: argparse.Namespace) -> list[TreeTask]:
    root = installation_root(global_scope=args.global_scope)
    return [TreeTask(SKILLS / name, root / name, root) for name in selected_skills(args)]


def baseline_tasks(args: argparse.Namespace) -> tuple[tuple[TreeTask, tuple[FileTask, ...]], ...]:
    if not args.global_scope:
        return ()
    agents_root = installation_root(global_scope=True).parent
    roots = tuple(dict.fromkeys((agents_root, codex_baseline_root())))
    return tuple(
        (
            TreeTask(BASELINES / "guardrails", root / "guardrails", root, replace_different=True),
            baseline_file_tasks(root),
        )
        for root in roots
    )


def baseline_file_tasks(root: Path) -> tuple[FileTask, ...]:
    """Ship every file directly under baselines/ to a baseline root."""
    return tuple(
        FileTask(path, root / path.name, root, replace_different=True)
        for path in sorted(BASELINES.iterdir())
        if path.is_file()
    )


def catalog_task(args: argparse.Namespace) -> FileTask | None:
    root = installation_root(global_scope=args.global_scope)
    destination = root / "README.md"
    if not args.all_skills and not destination.exists():
        return None
    return FileTask(SKILLS / "README.md", destination, root)


def ensure_safe_file_destination(task: FileTask) -> None:
    if not task.source.is_file() or task.source.is_symlink():
        raise SetupError(f"invalid source file: {task.source}")
    destination = task.destination.absolute()
    managed_root = task.managed_root.absolute()
    try:
        relative = destination.relative_to(managed_root)
    except ValueError as error:
        raise SetupError(f"destination escapes managed root: {destination}") from error
    if not relative.parts:
        raise SetupError(f"refusing to manage root directly: {destination}")
    current = Path(destination.anchor)
    for part in destination.parts[1:]:
        current /= part
        if current.is_symlink():
            raise SetupError(f"refusing destination symlink: {current}")
        if current.exists() and current != destination and not current.is_dir():
            raise SetupError(f"destination ancestor is not a directory: {current}")
    if task.destination.exists() and not task.destination.is_file():
        raise SetupError(f"destination is not a file: {task.destination}")


def file_matches(task: FileTask) -> bool:
    return task.destination.is_file() and task.source.read_bytes() == task.destination.read_bytes()


def preflight(
    tree_tasks: Sequence[TreeTask],
    file_tasks: Sequence[FileTask],
    *,
    allow_different: bool,
) -> None:
    conflicts: list[Path] = []
    for task in tree_tasks:
        tree_entry_map(task.source)
        ensure_safe_destination(task)
        if task.destination.exists() and not matches(task) and not (allow_different or task.replace_different):
            conflicts.append(task.destination)
    for task in file_tasks:
        ensure_safe_file_destination(task)
        if task.destination.exists() and not file_matches(task) and not (allow_different or task.replace_different):
            conflicts.append(task.destination)
    if conflicts and not allow_different:
        joined = "\n".join(f"conflict: {path}" for path in conflicts)
        raise SetupError(f"{joined}\nNo files changed. Re-run with --overwrite.")


def atomic_copy_tree(task: TreeTask) -> None:
    task.destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=f".{task.destination.name}-", dir=task.destination.parent))
    backup: Path | None = None
    try:
        for source in tree_entries(task.source):
            relative = source.relative_to(task.source)
            destination = temporary / relative
            if source.is_dir():
                destination.mkdir(exist_ok=True)
            elif source.is_file():
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, destination)
                shutil.copymode(source, destination)
        if task.destination.exists():
            backup = task.destination.parent / f".{task.destination.name}-backup"
            if backup.exists():
                raise SetupError(f"temporary replacement path already exists: {backup}")
            task.destination.replace(backup)
        temporary.replace(task.destination)
        temporary = None
        if backup:
            shutil.rmtree(backup)
    finally:
        if temporary and temporary.exists():
            shutil.rmtree(temporary)
        if backup and backup.exists() and not task.destination.exists():
            backup.replace(task.destination)


def atomic_copy_file(task: FileTask) -> None:
    task.destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{task.destination.name}-",
        dir=task.destination.parent,
    )
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        shutil.copyfile(task.source, temporary)
        shutil.copymode(task.source, temporary)
        temporary.replace(task.destination)
    finally:
        if temporary.exists():
            temporary.unlink()


def sync_claude_bridge(*, dry_run: bool, verbose: bool) -> str:
    """Create the Claude Code bridge once, and never edit an existing file."""
    claude_root = user_home() / ".claude"
    bridge = claude_root / "CLAUDE.md"
    if not claude_root.is_dir():
        if dry_run:
            print(f"no bridge: {claude_root} does not exist")
        return "skipped"
    if bridge.exists():
        state = "unchanged" if bridge.read_bytes() == CLAUDE_BRIDGE.read_bytes() else "kept"
        if verbose or dry_run:
            print(f"{state} bridge {bridge}")
        return state
    if dry_run:
        print(f"would install bridge: {bridge}")
        return "would install"
    atomic_copy_file(FileTask(CLAUDE_BRIDGE, bridge, claude_root))
    if verbose:
        print(f"installed bridge {bridge}")
    return "installed"


def run_install(args: argparse.Namespace) -> int:
    skill_tasks = tasks_for(args)
    catalog = catalog_task(args)
    baselines = baseline_tasks(args)
    tree_tasks = [*skill_tasks, *(tree for tree, _ in baselines)]
    file_tasks = [*([catalog] if catalog else []), *(file for _, files in baselines for file in files)]
    preflight(tree_tasks, file_tasks, allow_different=args.overwrite or args.dry_run)
    if args.dry_run:
        pending = [task.destination for task in skill_tasks if not matches(task)]
        for destination in pending:
            action = "replace" if destination.exists() else "install"
            print(f"would {action}: {destination}")
        catalog_pending = catalog is not None and not file_matches(catalog)
        if catalog and catalog_pending:
            action = "replace" if catalog.destination.exists() else "install"
            print(f"would {action} catalog: {catalog.destination}")
        baseline_pending = any(
            not matches(tree) or any(not file_matches(file) for file in files)
            for tree, files in baselines
        )
        if baseline_pending:
            for tree, files in baselines:
                if not matches(tree) or any(not file_matches(file) for file in files):
                    for destination in (*(file.destination for file in files), tree.destination):
                        action = "replace" if destination.exists() else "install"
                        print(f"would {action} baseline: {destination}")
        bridge_state = sync_claude_bridge(dry_run=True, verbose=args.verbose) if baselines else "skipped"
        summary = f"{len(pending)} skill{'s' if len(pending) != 1 else ''}"
        if catalog_pending:
            summary += " and the catalog"
        if baseline_pending:
            summary += " and the baseline"
        if bridge_state == "would install":
            summary += " and the Claude bridge"
        print(f"Would install {summary}. No files changed.")
        return 0

    changed = 0
    for task in skill_tasks:
        if matches(task):
            if args.verbose:
                print(f"unchanged {task.destination}")
            continue
        atomic_copy_tree(task)
        changed += 1
        if args.verbose:
            print(f"installed {task.destination}")
    catalog_changed = catalog is not None and not file_matches(catalog)
    if catalog and catalog_changed:
        atomic_copy_file(catalog)
        if args.verbose:
            print(f"installed catalog {catalog.destination}")
    baseline_changed = any(
        not matches(tree) or any(not file_matches(file) for file in files)
        for tree, files in baselines
    )
    if baseline_changed:
        for tree, files in baselines:
            target_changed = not matches(tree) or any(not file_matches(file) for file in files)
            if not matches(tree):
                atomic_copy_tree(tree)
            for file in files:
                if not file_matches(file):
                    atomic_copy_file(file)
            if args.verbose and target_changed:
                print(f"installed baseline {tree.managed_root}")
    bridge_state = sync_claude_bridge(dry_run=False, verbose=args.verbose) if baselines else "skipped"
    baseline_summary = ""
    if baselines:
        baseline_summary = f"; baseline {'updated' if baseline_changed else 'unchanged'}"
        if bridge_state != "skipped":
            baseline_summary += f"; bridge {bridge_state}"
    if catalog is not None:
        catalog_result = "updated" if catalog_changed else "unchanged"
        print(
            f"Installed {changed} skill{'s' if changed != 1 else ''}; "
            f"catalog {catalog_result}{baseline_summary}."
        )
    else:
        print(f"Installed {changed} skill{'s' if changed != 1 else ''}{baseline_summary}.")
    return 0


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(
        description=__doc__,
        epilog=EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    commands = result.add_subparsers(dest="command", required=True)
    install = commands.add_parser(
        "install",
        help="Install one skill or all skills.",
        description=(
            "Install one skill or all skills for the current project by default. "
            "Global installs synchronize the shared and Codex baselines."
        ),
        epilog=EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    install.add_argument("skill", nargs="?", help="Name of one skill to install.")
    install.add_argument("--all", dest="all_skills", action="store_true", help="Install all skills.")
    install.add_argument(
        "-g",
        "--global",
        dest="global_scope",
        action="store_true",
        help="Install for the user and synchronize the shared and Codex baselines.",
    )
    install.add_argument("-n", "--dry-run", action="store_true", help="Preview changes without modifying files.")
    install.add_argument("--overwrite", action="store_true", help="Replace differing installed skill directories.")
    install.add_argument("-v", "--verbose", action="store_true", help="Show each changed or unchanged skill.")
    install.set_defaults(func=run_install)
    return result


def main(argv: Sequence[str] | None = None) -> int:
    try:
        args = parser().parse_args(argv)
        return args.func(args)
    except SetupError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

"""Shared repository paths and safe skill-tree helpers."""

from __future__ import annotations

import os
import stat
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
AGENTS = ROOT / "agents"
BASELINES = ROOT / "baselines"
EXCLUDED_TREE_NAMES = frozenset({"__pycache__", ".DS_Store"})
EXCLUDED_TREE_SUFFIXES = frozenset({".pyc", ".pyo"})


class SetupError(Exception):
    """Report a user-actionable setup failure."""


@dataclass(frozen=True)
class TreeTask:
    source: Path
    destination: Path
    managed_root: Path
    replace_different: bool = False


def skill_names() -> tuple[str, ...]:
    return tuple(path.name for path in sorted(SKILLS.iterdir()) if path.is_dir() and (path / "SKILL.md").is_file())


def tree_entries(root: Path) -> Iterable[Path]:
    if not root.is_dir() or root.is_symlink():
        raise SetupError(f"invalid tree directory: {root}")
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if any(part in EXCLUDED_TREE_NAMES for part in relative.parts) or path.suffix in EXCLUDED_TREE_SUFFIXES:
            continue
        if path.is_symlink():
            raise SetupError(f"tree symlinks are not supported: {path}")
        if not path.is_dir() and not path.is_file():
            raise SetupError(f"invalid tree entry: {path}")
        yield path


def tree_entry_map(root: Path) -> dict[Path, Path]:
    return {path.relative_to(root): path for path in tree_entries(root)}


def ensure_safe_destination(task: TreeTask) -> None:
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
    if task.destination.exists() and not task.destination.is_dir():
        raise SetupError(f"destination is not a directory: {task.destination}")
    if task.destination.is_dir():
        for path in task.destination.rglob("*"):
            if path.is_symlink():
                raise SetupError(f"refusing destination symlink: {path}")


def executable(path: Path) -> bool:
    if os.name == "nt":
        return False
    return bool(path.stat().st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH))


def matches(task: TreeTask) -> bool:
    if not task.destination.is_dir():
        return False
    source_entries = tree_entry_map(task.source)
    destination_entries = tree_entry_map(task.destination)
    if source_entries.keys() != destination_entries.keys():
        return False
    for relative, source in source_entries.items():
        destination = destination_entries[relative]
        if source.is_dir() != destination.is_dir() or source.is_file() != destination.is_file():
            return False
        if source.is_file() and (
            source.read_bytes() != destination.read_bytes() or executable(source) != executable(destination)
        ):
            return False
    return True

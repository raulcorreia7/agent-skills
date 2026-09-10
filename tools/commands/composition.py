"""Validate skill references: reachable files, acyclic composition, plain naming."""

from __future__ import annotations

import fnmatch
import re
from collections.abc import Iterator
from pathlib import Path

from lib import ROOT, SKILLS, skill_names

MENTION = re.compile(r"`([^`]*)`|\$([a-z][a-z0-9-]*)")
LABEL = re.compile(r"^\s*[-*]\s+`[^`]+`\s*:")
SIGIL = re.compile(r"(?<![\w./\\:>-])([$/])([a-z][a-z0-9-]*)(?![\w-])")
WORD = re.compile(r"[A-Za-z0-9_./-]+")


def _content_lines(path: Path) -> Iterator[tuple[int, str]]:
    """Yield lines outside fenced code blocks."""
    fenced = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            yield number, line


def _mentioned(line: str) -> set[str]:
    """Collect whole name tokens from backticked spans and `$name` mentions."""
    found: set[str] = set()
    for backticked, bare in MENTION.findall(line):
        found.add((backticked or bare).strip().removeprefix("$"))
    return found


def composition_graph() -> dict[str, dict[str, str]]:
    """Map each skill to its referenced siblings and the first mention site.

    Table rows and label bullets (``- `branch`: ...``) hold names that are not
    routing references.
    """
    names = set(skill_names())
    graph: dict[str, dict[str, str]] = {name: {} for name in sorted(names)}
    for name in sorted(names):
        for path in sorted((SKILLS / name).rglob("*.md")):
            for number, line in _content_lines(path):
                if line.lstrip().startswith("|") or LABEL.match(line):
                    continue
                for token in _mentioned(line) & names:
                    if token != name:
                        graph[name].setdefault(token, f"{path.relative_to(ROOT)}:{number}")
    return graph


def _reachable(graph: dict[str, dict[str, str]], start: str) -> set[str]:
    seen: set[str] = set()
    pending = [start]
    while pending:
        for target in graph[pending.pop()]:
            if target not in seen:
                seen.add(target)
                pending.append(target)
    return seen


def _cycles(graph: dict[str, dict[str, str]]) -> list[tuple[str, ...]]:
    """Return each mutually reachable group of skills once."""
    forward = {name: _reachable(graph, name) for name in graph}
    components: set[tuple[str, ...]] = set()
    for name in graph:
        members = {name}
        members.update(other for other in graph if other != name and other in forward[name] and name in forward[other])
        if len(members) > 1:
            components.add(tuple(sorted(members)))
    return sorted(components)


def _reference_paths() -> list[Path]:
    """Every distributable file that names a skill in plain text.

    Client adapters (`agents/`) carry the client's own invocation form and are
    not scanned.
    """
    catalog = SKILLS / "README.md"
    paths = [catalog] if catalog.is_file() else []
    for name in skill_names():
        for pattern in ("*.md", "*.yaml", "*.yml"):
            paths.extend(sorted((SKILLS / name).rglob(pattern)))
    for root in ("baselines", "templates"):
        for pattern in ("*.md", "*.yaml"):
            paths.extend(sorted((ROOT / root).rglob(pattern)))
    return [path for path in paths if "agents" not in path.parts]


def _sigil_errors() -> list[str]:
    names = set(skill_names())
    errors: list[str] = []
    for path in _reference_paths():
        for number, line in _content_lines(path):
            for sigil, name in SIGIL.findall(line):
                if name in names:
                    errors.append(f"{path.relative_to(ROOT)}:{number}: client-specific invocation {sigil}{name}")
    return errors


def _package_files(base: Path) -> set[str]:
    """Every file a reader of the skill may need, besides SKILL.md and adapters."""
    return {
        str(path.relative_to(base))
        for path in base.rglob("*")
        if path.is_file()
        and path.name != "SKILL.md"
        and "agents" not in path.relative_to(base).parts
        and "__pycache__" not in path.relative_to(base).parts
    }


def _candidate_paths(source: Path, base: Path, token: str) -> set[str]:
    """Resolve a mention against the skill root and the mentioning file's folder."""
    relative = source.parent.relative_to(base)
    return {path for path in (token.lstrip("/"), str(relative / token)) if path not in {"", "."}}


def _unreachable_files() -> list[str]:
    errors: list[str] = []
    for name in skill_names():
        base = SKILLS / name
        files = _package_files(base)
        reachable: set[str] = set()
        pending = [base / "SKILL.md"]
        while pending:
            source = pending.pop()
            for token in set(WORD.findall(source.read_text(encoding="utf-8"))):
                for candidate in _candidate_paths(source, base, token):
                    if "*" in candidate or "?" in candidate:
                        hits = fnmatch.filter(files, candidate)
                    else:
                        hits = [candidate] if candidate in files else []
                    for hit in hits:
                        if hit not in reachable:
                            reachable.add(hit)
                            pending.append(base / hit)
        errors.extend(
            f"skills/{name}/{path}: not reachable from skills/{name}/SKILL.md" for path in sorted(files - reachable)
        )
    return errors


def validate() -> list[str]:
    graph = composition_graph()
    errors: list[str] = []
    for component in _cycles(graph):
        hops = sorted(
            f"{source} -> {target} ({graph[source][target]})"
            for source in component
            for target in graph[source]
            if target in component
        )
        errors.append("composition cycle among " + ", ".join(component) + ": " + ", ".join(hops))
    errors.extend(_sigil_errors())
    errors.extend(_unreachable_files())
    return errors

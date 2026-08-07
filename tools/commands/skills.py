"""Validate skill packages, templates, and the curated catalog."""

from __future__ import annotations

import re
from pathlib import Path

from lib import ROOT, SKILLS, skill_names

from .common import frontmatter, load_yaml

CATALOG = SKILLS / "README.md"
SKILL_TEMPLATE = ROOT / "templates/skill"
CATALOG_ROW = re.compile(r"^\| \[`\$([a-z][a-z0-9-]*)`\]\(([^/]+)/SKILL\.md\) \| `(implicit|manual)` \|")
MANUAL_MARKER = "Manual invocation only."
SHORT_DESCRIPTION_MAX = 64


def skill_dirs() -> list[Path]:
    return [SKILLS / name for name in skill_names()]


def validate_skill(skill: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill / "SKILL.md"
    relative = skill.relative_to(ROOT)
    try:
        metadata = frontmatter(skill_file)
    except ValueError as exc:
        return [str(exc)]

    if set(metadata) != {"name", "description"}:
        errors.append(f"{relative}/SKILL.md: frontmatter keys must be name and description")
    if metadata.get("name") != skill.name:
        errors.append(f"{relative}/SKILL.md: name must match the directory")
    description = metadata.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{relative}/SKILL.md: description must be a non-empty string")

    text = skill_file.read_text(encoding="utf-8")
    output = re.search(r"^## Output\n\n(.+?)(?=\n## |\Z)", text, re.MULTILINE | re.DOTALL)
    if not output or not output.group(1).strip():
        errors.append(f"{relative}/SKILL.md: explicit non-empty Output contract required")

    adapter = skill / "agents/openai.yaml"
    if not adapter.is_file():
        errors.append(f"{adapter.relative_to(ROOT)}: missing adapter")
    else:
        try:
            config = load_yaml(adapter)
        except ValueError as exc:
            errors.append(str(exc))
        else:
            interface, policy = config.get("interface"), config.get("policy")
            if not isinstance(interface, dict) or not isinstance(policy, dict):
                errors.append(f"{adapter.relative_to(ROOT)}: interface and policy required")
            else:
                short = interface.get("short_description")
                prompt = interface.get("default_prompt")
                implicit = policy.get("allow_implicit_invocation")
                if not isinstance(short, str) or not short.strip() or len(short) > SHORT_DESCRIPTION_MAX:
                    errors.append(f"{adapter.relative_to(ROOT)}: short_description must be 1-64 characters")
                if not isinstance(prompt, str) or f"${skill.name}" not in prompt:
                    errors.append(f"{adapter.relative_to(ROOT)}: default_prompt must name ${skill.name}")
                if not isinstance(implicit, bool):
                    errors.append(f"{adapter.relative_to(ROOT)}: invocation policy must be boolean")
                elif isinstance(description, str) and description.startswith(MANUAL_MARKER) == implicit:
                    errors.append(f"{relative}: manual description and adapter policy disagree")

    references = skill / "references"
    if references.is_dir():
        for path in sorted(references.rglob("*")):
            if path.is_symlink():
                errors.append(f"{path.relative_to(ROOT)}: symlinks are not allowed")
            if not path.is_file():
                continue
            if path.name in {"sources.yml", "sources.yaml"}:
                try:
                    load_yaml(path)
                except ValueError as exc:
                    errors.append(str(exc))
    for path in skill.rglob("*"):
        if path.is_symlink():
            errors.append(f"{path.relative_to(ROOT)}: skill packages must not contain symlinks")
    return errors


def validate_templates() -> list[str]:
    errors: list[str] = []
    required = (SKILL_TEMPLATE / "SKILL.md", SKILL_TEMPLATE / "agents/openai.yaml")
    for path in required:
        if not path.is_file():
            errors.append(f"{path.relative_to(ROOT)}: required template file missing")
    try:
        metadata = frontmatter(SKILL_TEMPLATE / "SKILL.md")
        adapter = load_yaml(SKILL_TEMPLATE / "agents/openai.yaml")
    except (OSError, ValueError) as exc:
        return [*errors, f"template: {exc}"]
    if set(metadata) != {"name", "description"}:
        errors.append("templates/skill/SKILL.md: invalid frontmatter contract")
    if set(adapter) != {"interface", "policy"}:
        errors.append("templates/skill/agents/openai.yaml: interface and policy required")
    return errors


def validate_catalog() -> list[str]:
    errors: list[str] = []
    rows: list[tuple[str, str, str]] = []
    for number, line in enumerate(CATALOG.read_text(encoding="utf-8").splitlines(), 1):
        if not line.startswith("| [`$"):
            continue
        match = CATALOG_ROW.match(line)
        if not match:
            errors.append(f"skills/README.md:{number}: malformed catalog row")
        else:
            rows.append(match.groups())
    names = [row[0] for row in rows]
    if set(names) != set(skill_names()) or len(names) != len(set(names)):
        errors.append("skills/README.md: every distributable skill must appear exactly once")
    for name, linked_name, mode in rows:
        if name != linked_name:
            errors.append(f"skills/README.md: {name} links to {linked_name}")
            continue
        adapter = load_yaml(SKILLS / name / "agents/openai.yaml")
        expected = "implicit" if adapter.get("policy", {}).get("allow_implicit_invocation") is True else "manual"
        if mode != expected:
            errors.append(f"skills/README.md: {name} is {mode}, adapter is {expected}")
    return errors


def validate() -> list[str]:
    errors: list[str] = []
    for skill in skill_dirs():
        errors.extend(validate_skill(skill))
    errors.extend(validate_templates())
    errors.extend(validate_catalog())
    return errors

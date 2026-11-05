"""Validate skill packages, templates, and the curated catalog."""

from __future__ import annotations

import datetime as dt
import os
import re
from collections.abc import Iterator
from pathlib import Path

from lib import ROOT, SKILLS, skill_names

from .common import frontmatter, load_yaml

CATALOG = SKILLS / "README.md"
SKILL_TEMPLATE = ROOT / "templates/skill"
CATALOG_ROW = re.compile(r"^\| \[`([a-z][a-z0-9-]*)`\]\(([^/]+)/SKILL\.md\) \| `(implicit|manual)` \|")
MANUAL_MARKER = "Manual invocation only."
SHORT_DESCRIPTION_MAX = 64
CONTRIBUTING = ROOT / "CONTRIBUTING.md"

# Template order. Any other heading is a domain section and sits between the
# Steps/Flow block and Guardrails.
LEADING_SECTIONS = ("Job", "Modes", "Depth", "Steps", "Flow")
TRAILING_SECTIONS = ("Guardrails", "Composition", "Output")
REQUIRED_SECTIONS = ("Job", "Steps", "Output")
FLOW_STEP_THRESHOLD = 3
HEADING = re.compile(r"^## (.+)$", re.MULTILINE)
STEP = re.compile(r"^(\d+)\. ", re.MULTILINE)
CRITERION = "Complete when"
SEVERITY_START = "- `Critical`:"
PRIORITY_START = "Review priorities map to severity:"
SEVERITY_TERM = r"(?:\*\*)?`?(?:Critical|High|Medium|Low)`?(?:\*\*)?"
# A severity definition: a bullet that opens with the term and a separator, or a
# two- or three-cell table row whose first cell is the term.
SEVERITY_BULLET = re.compile(rf"^\s*[-*]\s+{SEVERITY_TERM}\s*[:\u2014\u2013-]", re.MULTILINE)
SEVERITY_ROW = re.compile(rf"^\|\s*{SEVERITY_TERM}\s*\|[^|\n]*(?:\|[^|\n]*)?\|\s*$", re.MULTILINE)
PRIORITY_MAP = re.compile(r"`?P0`?\s*(?:=|:|\u2192|->)\s*`?Critical")
FLOW_BLOCK = re.compile(r"^## Flow\n.*?^```[^\n]*\n(.*?)^```", re.MULTILINE | re.DOTALL)
FLOW_LINES = ("input \u2190", "stop:")
SOURCE_FILES = frozenset({"sources.yml", "sources.yaml"})
SOURCE_MAX_AGE_DAYS = 365
TODAY_ENV = "SKILLS_TODAY"


def sections(text: str) -> dict[str, str]:
    """Map each `## ` heading to its body, outside fenced code."""
    body = re.sub(r"^```.*?^```", "", text, flags=re.MULTILINE | re.DOTALL)
    parts = HEADING.split(body)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}


def section_order_errors(names: list[str]) -> list[str]:
    def rank(name: str) -> int:
        if name in LEADING_SECTIONS:
            return LEADING_SECTIONS.index(name)
        if name in TRAILING_SECTIONS:
            return len(LEADING_SECTIONS) + 1 + TRAILING_SECTIONS.index(name)
        return len(LEADING_SECTIONS)

    errors = [f"missing section: {name}" for name in REQUIRED_SECTIONS if name not in names]
    ranks = [rank(name) for name in names]
    for previous, current, name in zip(ranks, ranks[1:], names[1:], strict=False):
        if current < previous:
            errors.append(f"section out of template order: {name}")
    return errors


def steps(body: str) -> list[str]:
    """Split a Steps body into its top-level numbered items."""
    starts = [match.start() for match in STEP.finditer(body)]
    return [body[start:end] for start, end in zip(starts, [*starts[1:], len(body)], strict=False)]


def _paragraph(start_marker: str) -> str:
    """The CONTRIBUTING.md paragraph that starts with the marker."""
    text = CONTRIBUTING.read_text(encoding="utf-8")
    start = text.index(start_marker)
    end = text.index("\n\n", start)
    return text[start:end]


def severity_errors(path: Path) -> list[str]:
    """A file that defines the severity scale or the P-map copies CONTRIBUTING.md byte for byte."""
    text = path.read_text(encoding="utf-8")
    relative = path.relative_to(ROOT)
    errors: list[str] = []
    if (SEVERITY_BULLET.search(text) or SEVERITY_ROW.search(text)) and _paragraph(SEVERITY_START) not in text:
        errors.append(f"{relative}: severity scale differs from CONTRIBUTING.md")
    if PRIORITY_MAP.search(text) and _paragraph(PRIORITY_START) not in text:
        errors.append(f"{relative}: priority-to-severity map differs from CONTRIBUTING.md")
    return errors


def description_errors(description: str) -> list[str]:
    if description.startswith(MANUAL_MARKER):
        verb = description.removeprefix(MANUAL_MARKER).split(maxsplit=1)[:1]
        word = verb[0].rstrip(",;:") if verb else ""
        if not word[:1].isupper() or not word.endswith("s"):
            return [f"manual description needs a verb such as 'Runs' after '{MANUAL_MARKER}'"]
        return []
    return [
        f"implicit description needs '{phrase}'"
        for phrase in ("Use when", "primary deliverable")
        if phrase not in description
    ]


def flow_errors(text: str) -> list[str]:
    block = FLOW_BLOCK.search(text)
    if not block:
        return []
    lines = block.group(1).splitlines()
    return [
        f"Flow needs a line starting '{start}'"
        for start in FLOW_LINES
        if not any(line.startswith(start) for line in lines)
    ]


def _review_dates(value: object) -> Iterator[object]:
    if isinstance(value, dict):
        for key, item in value.items():
            if key == "reviewed_on":
                yield item
            else:
                yield from _review_dates(item)
    elif isinstance(value, list):
        for item in value:
            yield from _review_dates(item)


def source_record(path: Path) -> tuple[list[str], dt.date | None]:
    """Check a source record's required keys; return its errors and newest review date."""
    relative = path.relative_to(ROOT)
    try:
        record = load_yaml(path)
    except ValueError as exc:
        return [str(exc)], None
    errors = [] if "sources" in record else [f"{relative}: top-level 'sources' key required"]
    dates: list[dt.date] = []
    for raw in _review_dates({"reviewed_on": record.get("reviewed_on"), "sources": record.get("sources")}):
        if raw is None:
            continue
        try:
            dates.append(raw if isinstance(raw, dt.date) else dt.date.fromisoformat(str(raw)))
        except ValueError:
            errors.append(f"{relative}: reviewed_on must be an ISO date, got {raw!r}")
    if not dates and not errors:
        errors.append(f"{relative}: 'reviewed_on' required at top level or per source")
    return errors, max(dates, default=None)


def source_files() -> list[Path]:
    return [path for skill in skill_dirs() for path in sorted(skill.rglob("*")) if path.name in SOURCE_FILES]


def today() -> dt.date:
    """Today, or the ISO date in SKILLS_TODAY for reproducible runs."""
    override = os.environ.get(TODAY_ENV)
    return dt.date.fromisoformat(override) if override else dt.date.today()


def warnings() -> list[str]:
    """Source records whose newest review is more than a year old."""
    found: list[str] = []
    now = today()
    for path in source_files():
        _, newest = source_record(path)
        if newest and (now - newest).days > SOURCE_MAX_AGE_DAYS:
            found.append(
                f"{path.relative_to(ROOT)}: newest reviewed_on {newest} is over {SOURCE_MAX_AGE_DAYS} days old"
            )
    return found


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

    found = sections(text)
    for problem in section_order_errors(list(found)):
        errors.append(f"{relative}/SKILL.md: {problem}")
    items = steps(found.get("Steps", ""))
    for number, item in enumerate(items, 1):
        if CRITERION not in item:
            errors.append(f"{relative}/SKILL.md: step {number} needs a '{CRITERION} ...' criterion")
    if len(items) > FLOW_STEP_THRESHOLD and "Flow" not in found:
        errors.append(f"{relative}/SKILL.md: more than {FLOW_STEP_THRESHOLD} steps need a Flow")
    if isinstance(description, str):
        errors.extend(f"{relative}/SKILL.md: {problem}" for problem in description_errors(description))
    errors.extend(f"{relative}/SKILL.md: {problem}" for problem in flow_errors(text))
    for path in [skill_file, *sorted((skill / "references").rglob("*.md"))]:
        errors.extend(severity_errors(path))

    # Adapters are optional; check one only when it is present.
    adapter = skill / "agents/openai.yaml"
    if adapter.is_file():
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
                if not isinstance(prompt, str) or not re.search(rf"(?<![\w-]){re.escape(skill.name)}(?![\w-])", prompt):
                    errors.append(f"{adapter.relative_to(ROOT)}: default_prompt must name {skill.name}")
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
            if path.name in SOURCE_FILES:
                errors.extend(source_record(path)[0])
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
        if not line.startswith("| [`"):
            continue
        match = CATALOG_ROW.match(line)
        if not match:
            errors.append(f"skills/README.md:{number}: malformed catalog row")
            continue
        catalog_name, linked_name, mode = match.groups()
        rows.append((catalog_name, linked_name, mode))
    names = [row[0] for row in rows]
    if set(names) != set(skill_names()) or len(names) != len(set(names)):
        errors.append("skills/README.md: every distributable skill must appear exactly once")
    for name, linked_name, mode in rows:
        if name != linked_name:
            errors.append(f"skills/README.md: {name} links to {linked_name}")
            continue
        description = frontmatter(SKILLS / name / "SKILL.md").get("description", "")
        expected = "manual" if str(description).startswith(MANUAL_MARKER) else "implicit"
        if mode != expected:
            errors.append(f"skills/README.md: {name} is {mode}, description is {expected}")
    return errors


def validate() -> list[str]:
    errors: list[str] = []
    for skill in skill_dirs():
        errors.extend(validate_skill(skill))
    errors.extend(validate_templates())
    errors.extend(validate_catalog())
    return errors

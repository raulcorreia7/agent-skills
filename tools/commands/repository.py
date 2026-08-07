"""Validate the repository baseline and local documentation links."""

from __future__ import annotations
import ipaddress
import re
from pathlib import Path
from urllib.parse import urlsplit

from .common import ROOT

REQUIRED_ROOT_FILES = (
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "README.md",
    "pyproject.toml",
)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REFERENCE_TICK = re.compile(r"`([^`]*?references/[^`]*?)`")
URL = re.compile(r"https?://[^\s\"')\]>]+")
NONPUBLIC_SUFFIXES = (
    ".internal",
    ".local",
    ".corp",
    ".home",
    ".lan",
    ".intranet",
    ".test",
    ".localhost",
)


def markdown_files() -> list[Path]:
    roots = (
        ROOT / "agents",
        ROOT / "skills",
        ROOT / "templates",
        ROOT / ".agents",
        ROOT / "baselines",
        ROOT / "docs",
    )
    files = [ROOT / name for name in ("README.md", "AGENTS.md", "CONTRIBUTING.md")]
    for root in roots:
        files.extend(root.rglob("*.md"))
    return sorted(set(path for path in files if path.is_file()))


def validate_links() -> list[str]:
    errors: list[str] = []
    for source in markdown_files():
        for match in MARKDOWN_LINK.finditer(source.read_text(encoding="utf-8")):
            raw = match.group(1).strip().strip("<>").split(maxsplit=1)[0]
            target = raw.split("#", 1)[0].split("?", 1)[0]
            if not target or "://" in target or target.startswith(("#", "mailto:")):
                continue
            resolved = (source.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(f"{source.relative_to(ROOT)}: link escapes repository: {raw}")
                continue
            if not resolved.exists():
                errors.append(f"{source.relative_to(ROOT)}: missing link target: {raw}")
    return errors


def _resolve_local(source: Path, raw: str) -> Path | None:
    target = raw.split("#", 1)[0].split("?", 1)[0].rstrip(".,;:!?)")
    if not target:
        return None
    resolved = (source.parent / target).resolve()
    try:
        resolved.relative_to(ROOT)
    except ValueError:
        return None
    return resolved


def validate_reference_routes() -> list[str]:
    errors: list[str] = []
    for source in markdown_files():
        text = source.read_text(encoding="utf-8")
        for match in REFERENCE_TICK.finditer(text):
            token = match.group(1).strip()
            if any(char in token for char in "*<>$ \t{}[]()") or "://" in token:
                continue
            if not token.endswith((".md", ".yml", ".yaml")):
                continue
            resolved = _resolve_local(source, token)
            if resolved is not None and resolved.exists():
                continue
            if resolved is None:
                errors.append(f"{source.relative_to(ROOT)}: reference escapes repository: {token}")
                continue
            if (ROOT / token).is_file():
                continue
            errors.append(f"{source.relative_to(ROOT)}: dangling reference: {token}")
    return errors


def _is_nonpublic_host(host: str) -> bool:
    host = host.strip("[]").lower()
    if host == "localhost" or host.endswith(NONPUBLIC_SUFFIXES):
        return True
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        return "." not in host
    return address.is_loopback or address.is_link_local or address.is_private


def validate_external_hosts() -> list[str]:
    errors: list[str] = []
    for source in markdown_files():
        text = source.read_text(encoding="utf-8")
        for match in URL.finditer(text):
            raw = match.group(0).rstrip(".,;:!?)")
            host = urlsplit(raw).hostname or ""
            if _is_nonpublic_host(host):
                errors.append(f"{source.relative_to(ROOT)}: non-public URL host: {raw}")
    return errors


def validate() -> list[str]:
    errors = [name for name in REQUIRED_ROOT_FILES if not (ROOT / name).is_file()]
    errors = [f"{name}: required repository baseline file missing" for name in errors]
    errors.extend(validate_links())
    errors.extend(validate_reference_routes())
    errors.extend(validate_external_hosts())
    return errors

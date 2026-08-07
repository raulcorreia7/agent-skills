#!/usr/bin/env python3
"""Validate the Agent Skills repository."""

from __future__ import annotations

import argparse
import sys
import tomllib
from collections.abc import Callable, Sequence

from commands import repository, skills
from lib import AGENTS, ROOT
from setup_checks import run as run_setup_checks

Check = Callable[[], list[str]]
EXAMPLES = """Examples:
  uv run tools/validate.py
  uv run tools/validate.py skills
  uv run tools/validate.py repository toml
  uv run tools/validate.py --quiet
"""


def validate_toml() -> list[str]:
    errors: list[str] = []
    paths = [*AGENTS.rglob("*.toml"), *(ROOT / "templates/agent").glob("*.toml")]
    for path in sorted(paths):
        try:
            tomllib.loads(path.read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError) as exc:
            errors.append(f"{path.relative_to(AGENTS.parent)}: {exc}")
    return errors


CHECKS: dict[str, Check] = {
    "skills": skills.validate,
    "repository": repository.validate,
    "toml": validate_toml,
    "setup": run_setup_checks,
}


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog=EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("checks", nargs="*", choices=tuple(CHECKS), help="Checks to run; defaults to all checks.")
    parser.add_argument("-q", "--quiet", action="store_true", help="Print only failures.")
    return parser.parse_args(argv)


def run(selected: Sequence[str], *, quiet: bool) -> int:
    failed = False
    for name in selected:
        if not quiet:
            print(f"Checking {name}...")
        errors = CHECKS[name]()
        if errors:
            failed = True
            print(f"{name} failed:", file=sys.stderr)
            for error in errors:
                print(f"- {error}", file=sys.stderr)
        elif not quiet:
            print(f"{name} passed.")
    if not quiet:
        print("Validation failed." if failed else "Validation passed.")
    return 1 if failed else 0


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    return run(args.checks or tuple(CHECKS), quiet=args.quiet)


if __name__ == "__main__":
    raise SystemExit(main())

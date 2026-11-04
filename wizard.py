#!/usr/bin/env python3
"""Walk a human through installing this kit.

The wizard is a terminal-only front end over skills.py: it detects the current
state, asks three questions, shows the exact plan, then installs and validates.
Prompts come from questionary, so this script needs it installed; skills.py
stays standard-library only.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import textwrap
from collections.abc import Sequence
from dataclasses import dataclass
from types import ModuleType

import skills
from tools.lib import ROOT, SetupError

EXAMPLES = """Examples:
  python wizard.py
  python wizard.py --help
"""

DEPENDENCY_HINT = (
    "error: the wizard needs questionary. Run `uv run python wizard.py`, or `pip install questionary` first; "
    "`python skills.py install --all` needs nothing extra."
)
SCOPE_GLOBAL = "Global  (~/.agents/skills)"
SCOPE_REPOSITORY = "Current repository  (./.agents/skills)"
ACTION_PREVIEW = "Preview (dry run)"
ACTION_INSTALL = "Install"
ACTION_CANCEL = "Cancel"

# Green accent, colour only: the cursor row is bold green with a pointer, ticked
# rows are plain green, hints are dim. `noreverse` stops terminals from painting
# rows as white blocks.
STYLE_RULES = [
    ("qmark", "fg:ansigreen bold"),
    ("question", "bold"),
    ("answer", "fg:ansigreen bold"),
    ("pointer", "fg:ansigreen bold noreverse"),
    ("highlighted", "fg:ansigreen bold noreverse"),
    ("selected", "fg:ansigreen noreverse"),
    ("instruction", "fg:ansibrightblack noreverse"),
    ("text", "noreverse"),
    ("separator", "fg:ansibrightblack"),
]
POINTER = "❯"
SELECT_HINT = "(↑/↓ move, enter confirms)"
CHECKBOX_HINT = "(↑/↓ move, space toggles, a all/none, i invert, enter confirms)"


@dataclass(frozen=True)
class Survey:
    pending: int
    conflicts: int
    catalog_pending: bool
    baseline_pending: bool


def namespace(
    *, skill: str | None, all_skills: bool, global_scope: bool, dry_run: bool, overwrite: bool
) -> argparse.Namespace:
    return argparse.Namespace(
        skill=skill,
        all_skills=all_skills,
        global_scope=global_scope,
        dry_run=dry_run,
        overwrite=overwrite,
        verbose=False,
    )


def survey(chosen: Sequence[str], *, global_scope: bool) -> Survey:
    pending = conflicts = 0
    for name in chosen:
        single = namespace(skill=name, all_skills=False, global_scope=global_scope, dry_run=True, overwrite=False)
        for task in skills.tasks_for(single):
            if not skills.matches(task):
                pending += 1
                conflicts += 1 if task.destination.exists() else 0
    wide = namespace(skill=None, all_skills=True, global_scope=global_scope, dry_run=True, overwrite=False)
    catalog = skills.catalog_task(wide)
    baseline_changed = False
    for tree, files in skills.baseline_tasks(wide):
        if not skills.matches(tree) or any(not skills.file_matches(file) for file in files):
            baseline_changed = True
            break
    return Survey(
        pending=pending,
        conflicts=conflicts,
        catalog_pending=bool(catalog and not skills.file_matches(catalog)),
        baseline_pending=baseline_changed,
    )


def calls_for(chosen: Sequence[str], *, global_scope: bool, dry_run: bool, overwrite: bool) -> list[argparse.Namespace]:
    if list(chosen) == list(skills.skill_names()):
        return [namespace(skill=None, all_skills=True, global_scope=global_scope, dry_run=dry_run, overwrite=overwrite)]
    return [
        namespace(skill=name, all_skills=False, global_scope=global_scope, dry_run=dry_run, overwrite=overwrite)
        for name in chosen
    ]


def show_plan(chosen: Sequence[str], state: Survey, bridge: str, *, global_scope: bool) -> None:
    where = "global" if global_scope else "current repository"
    shown = ", ".join(chosen[:4]) + (", …" if len(chosen) > 4 else "")
    lines = [f"scope      {where}", f"skills     {len(chosen)} ({shown})"]
    if global_scope:
        lines.append("baselines  ~/.agents/{AGENTS.md, TOOLS.md, TASTE.md, guardrails/}")
        lines.append(f"bridge     ~/.claude/CLAUDE.md  ({bridge})")
    lines.append(f"update     {state.pending} skill director{'y' if state.pending == 1 else 'ies'}")
    if state.conflicts:
        lines.append(f"conflicts  {state.conflicts} differ from this checkout")
    if state.catalog_pending:
        lines.append("catalog    refresh")
    if state.baseline_pending:
        lines.append("baselines  refresh")
    print("\nPlan")
    for line in lines:
        print(f"  {line}")


def validate() -> int:
    print("\nValidating…")
    result = subprocess.run([sys.executable, str(ROOT / "tools/validate.py"), "--quiet"], cwd=ROOT, check=False)
    if result.returncode != 0:
        print("validation reported issues; run tools/validate.py for detail", file=sys.stderr)
        return result.returncode
    print("validation passed.")
    print("\nNext: restart your client, then read the catalog beside the installed skills.")
    return 0


def pick(questionary: ModuleType, message: str, options: Sequence[tuple[str, object]], style: object) -> object:
    """Single-choice prompt; the first option is the default. Returns None on Ctrl-C."""
    choices = [questionary.Choice(label, value=value) for label, value in options]
    return questionary.select(
        message, choices=choices, default=options[0][1], style=style, pointer=POINTER, instruction=SELECT_HINT
    ).ask()


def pick_skills(questionary: ModuleType, names: Sequence[str], style: object) -> list[str] | None:
    """Checklist with every skill ticked; refuses an empty selection so Enter never ends in a dead end."""
    return questionary.checkbox(
        "Choose skills",
        choices=[questionary.Choice(name, checked=True) for name in names],
        style=style,
        pointer=POINTER,
        instruction=CHECKBOX_HINT,
        validate=lambda picked: bool(picked) or "Pick at least one skill, or press Ctrl-C to cancel.",
    ).ask()


def run(questionary: ModuleType) -> int:
    print(textwrap.fill("Agent Skills installer: three questions, one plan, then install and validate.", width=80))
    style = questionary.Style(STYLE_RULES)

    global_scope = pick(
        questionary, "Where should the skills live?", [(SCOPE_GLOBAL, True), (SCOPE_REPOSITORY, False)], style
    )
    if global_scope is None:
        return cancel()

    names = list(skills.skill_names())
    everything = pick(
        questionary, "Which skills?", [(f"All ({len(names)})", True), ("Choose from a list", False)], style
    )
    if everything is None:
        return cancel()
    chosen = names if everything else pick_skills(questionary, names, style)
    if chosen is None:
        return cancel()

    state = survey(chosen, global_scope=global_scope)
    bridge = skills.sync_claude_bridge(dry_run=True, verbose=False) if global_scope else "skipped"
    show_plan(chosen, state, bridge, global_scope=global_scope)

    action = pick(
        questionary,
        "Now what?",
        [(ACTION_PREVIEW, "preview"), (ACTION_INSTALL, "install"), (ACTION_CANCEL, "cancel")],
        style,
    )
    if action is None or action == "cancel":
        return cancel()
    if action == "preview":
        for pending in calls_for(chosen, global_scope=global_scope, dry_run=True, overwrite=False):
            skills.run_install(pending)
        if not questionary.confirm("Install for real now?", default=False, style=style).ask():
            print("nothing written.")
            return 0

    overwrite = False
    if state.conflicts:
        plural = "y" if state.conflicts == 1 else "ies"
        print(f"\n{state.conflicts} installed director{plural} differ from this checkout.")
        overwrite = bool(questionary.confirm("Replace them with this checkout?", default=False, style=style).ask())
        if not overwrite:
            print("nothing written. Re-run and choose to replace when you are ready.")
            return 0

    for call in calls_for(chosen, global_scope=global_scope, dry_run=False, overwrite=overwrite):
        try:
            skills.run_install(call)
        except SetupError as error:
            print(f"error: {error}", file=sys.stderr)
            return 2
    return validate()


def cancel() -> int:
    print("nothing written.")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog=EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.parse_args(argv)
    if not (sys.stdin.isatty() and sys.stdout.isatty()):
        message = "error: wizard.py needs an interactive terminal; use `python skills.py` for scripted installs."
        print(message, file=sys.stderr)
        return 2
    try:
        import questionary
    except ImportError:
        print(DEPENDENCY_HINT, file=sys.stderr)
        return 2
    try:
        return run(questionary)
    except KeyboardInterrupt:
        print("\ncancelled; re-run the wizard to continue.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())

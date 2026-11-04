# AGENTS.md: Agent Skills repository

This repository is the source of truth for the Agent Skills kit. Rules for
every artifact live in `CONTRIBUTING.md`; this file only routes.

## Map

| Path | Holds |
| --- | --- |
| `skills/<name>/` | One distributable skill each; `skills/README.md` is the curated catalog. |
| `baselines/` | User-level guidance the installer copies to `~/.agents/` (and the Claude bridge in `claude/`). |
| `templates/` | Starting points for new skills and agents. |
| `agents/` | Shared agent packages (none packaged yet). |
| `skills.py`, `wizard.py` | Installer and its guided front end. |
| `tools/` | Validator (`validate.py`), its checks (`commands/`), shared code (`lib.py`), installer checks (`setup_checks.py`). |
| `docs/` | Research reports and the diagram gallery; they never override a contract. |

## Loading

```text
task touches a skill    → skills/README.md → skills/<name>/SKILL.md → the references it names
task writes or reshapes a skill, reference, baseline, or command → CONTRIBUTING.md first
task changes install behaviour → CONTRIBUTING.md › Command contract, then README.md › What gets installed
```

## Rules

- Before adding guidance, find its current owner in `CONTRIBUTING.md` and edit
  it there; elsewhere, point to it.
- Keep every distributable skill unless its retirement is explicitly approved.
- When two repository contracts disagree and the choice changes behaviour or
  risk, report the conflict and ask which wins.
- Run `uv run poe check` before handing off a change.

# Agent Skills

> Portable, reviewed workflows for consistent agent-assisted work.

The kit provides independently portable skills. Shared Codex agents remain
optional and separate from the skills installer.

## Install

You need Git, Python 3.11 or newer, [uv](https://docs.astral.sh/uv/), and an
Agent Skills-compatible client.

```text
git clone https://github.com/raulcorreia7/agent-skills.git
cd agent-skills
uv run python wizard.py
```

The wizard asks where to install and which skills to install. It then shows
the plan, offers a dry run, installs, and validates. Use the arrow keys to
move, space to toggle, enter to confirm, and Ctrl-C to cancel.

To install without prompts, use `skills.py`. It needs only the Python standard
library.

| Goal                                     | Command                                    |
| ---------------------------------------- | ------------------------------------------ |
| Preview every change without writing     | `python skills.py install --all --dry-run` |
| Install all skills                       | `python skills.py install --all`           |
| Install one skill                        | `python skills.py install docs`            |
| Install one skill into this repository   | `python skills.py install docs --project`  |
| Show all options                         | `python skills.py --help`                  |

Every user install also sets up the baseline guidance described below.
After the install, Claude Code loads new skills without a restart. If the
install created the Claude skills folder, run `/reload-skills` in Claude Code.
Restart other clients.

## What gets installed

| Item              | User install (default)                              | `--project` install           |
| ----------------- | --------------------------------------------------- | ----------------------------- |
| Skills            | `~/.agents/skills/<name>`                           | `.agents/skills/<name>`       |
| Claude Code links | `~/.claude/skills/<name>`, if `~/.claude` exists    | `.claude/skills/<name>`       |
| Catalog           | `~/.agents/skills/README.md`, with `--all`          | `.agents/skills/README.md`, with `--all` |
| Baseline          | `~/.agents/`, plus `AGENTS.md` in `~/.codex/`       | Not installed                 |
| Claude bridge     | `~/.claude/CLAUDE.md`, created once                 | Not installed                 |

`.agents/skills` is the cross-client location in the
[Agent Skills convention](https://agentskills.io/client-implementation/adding-skills-support),
so it holds the only copy of each skill. Claude Code reads only
`.claude/skills`, but it follows symbolic links. The installer therefore
creates one link for each skill.

## Safety

- `--dry-run` shows every change and writes nothing. The wizard shows its plan
  before it writes.
- The installer keeps your files. It does not replace an existing entry in
  `.claude/skills` or an existing `~/.claude/CLAUDE.md`. It replaces an
  installed skill or catalog that differs from this checkout only with
  `--overwrite`.
- The installer refuses to write through a symbolic link in a destination
  path, and it replaces each skill folder and file in one atomic step.
- A partial install does not install the catalog, because the catalog lists
  skills that are not installed.
- The baseline's `AGENTS.md` and `guardrails/` follow this checkout, so each
  user install replaces local edits to them. `TASTE.md` and `TOOLS.md` are
  yours: the installer creates them once and never overwrites them. Put your
  preferences there. Codex gets a copy of `AGENTS.md` in `$CODEX_HOME`
  (default `~/.codex`).

## Maintaining

Run `uv sync --all-groups` once, then `uv run poe check` before every PR.
[Contributing](CONTRIBUTING.md) lists every task and the contracts for skills,
references, agents, and commands.

## Learn More

| Topic                                         | Documentation                                     |
| --------------------------------------------- | ------------------------------------------------- |
| Skills, invocation, and boundaries            | [Skill catalog](skills/README.md)                 |
| User baseline and guardrails                  | [Baseline guidance](baselines/AGENTS.md)          |
| Shared agents and adding future agents        | [Agent catalog](agents/README.md)                 |
| Diagram visual language gallery                | [Diagram visual design](docs/diagram-visual-design/index.html) |
| Repository maintenance and review             | [Contributing](CONTRIBUTING.md)                   |

Released under the [MIT license](LICENSE).

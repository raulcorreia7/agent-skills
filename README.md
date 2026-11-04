# Agent Skills

> Portable, reviewed workflows for consistent agent-assisted work.

You get two things:

- **Skills**: focused workflows (code, review, debug, docs, plans, diagrams, and
  more) that any [Agent Skills](https://agentskills.io) client can load. Browse
  them in the [skill catalog](skills/README.md).
- **Baseline**: a short, always-loaded `AGENTS.md` with working rules for
  evidence, scope, safety, and handoff, plus two guardrails it loads on demand.

## Install

You need Git, Python 3.11 or newer, [uv](https://docs.astral.sh/uv/), and an
Agent Skills client.

```text
git clone https://github.com/raulcorreia7/agent-skills.git
cd agent-skills
uv run python wizard.py
```

The wizard asks where to install and which skills, shows the plan, offers a
dry run, then installs and validates.

To install without prompts, use `skills.py` (standard library only):

| Goal                                     | Command                                    |
| ---------------------------------------- | ------------------------------------------ |
| Preview every change without writing     | `python skills.py install --all --dry-run` |
| Install all skills                       | `python skills.py install --all`           |
| Install one skill                        | `python skills.py install docs`            |
| Install one skill into this repository   | `python skills.py install docs --project`  |
| Show all options                         | `python skills.py --help`                  |

After installing, Claude Code picks up the skills without a restart; if the
install created its skills folder, run `/reload-skills`. Restart other clients.
To update, `git pull` and run the same command again.

## What gets installed

| Item              | User install (default)                              | `--project` install                      |
| ----------------- | --------------------------------------------------- | ---------------------------------------- |
| Skills            | `~/.agents/skills/<name>`                           | `.agents/skills/<name>`                  |
| Claude Code links | `~/.claude/skills/<name>`, if `~/.claude` exists    | `.claude/skills/<name>`                  |
| Catalog           | `~/.agents/skills/README.md`, with `--all`          | `.agents/skills/README.md`, with `--all` |
| Baseline          | `~/.agents/`, plus a copy of `AGENTS.md` in `~/.codex/` | Not installed                        |
| Claude bridge     | `~/.claude/CLAUDE.md`, created once                 | Not installed                            |

`.agents/skills` is the cross-client location in the
[Agent Skills convention](https://agentskills.io/client-implementation/adding-skills-support),
so it holds the only copy of each skill. Claude Code reads only
`.claude/skills` but follows symbolic links, so the installer adds one link per
skill. Codex reads only `$CODEX_HOME/AGENTS.md` (default `~/.codex`), so it
gets a copy of the baseline's `AGENTS.md`, which points back to `~/.agents/`.

## Your files stay yours

- `TASTE.md` and `TOOLS.md` in `~/.agents/` are yours: the installer creates
  them once and never overwrites them. Put your preferences and tool notes
  there.
- The baseline's `AGENTS.md` and `guardrails/` follow this checkout; each user
  install replaces local edits to them.
- An existing entry in `.claude/skills` or an existing `~/.claude/CLAUDE.md` is
  never replaced.
- An installed skill or catalog that differs from this checkout is replaced
  only with `--overwrite`.
- `--dry-run` shows every change and writes nothing. The installer never writes
  through a symbolic link and replaces each folder and file atomically.

## Contributing

`main` is the rolling stable branch. Read [CONTRIBUTING.md](CONTRIBUTING.md)
for the contracts, then run `uv sync --all-groups` once and
`uv run poe check` before every PR.

## Learn more

| Topic                                   | Documentation                                                  |
| --------------------------------------- | -------------------------------------------------------------- |
| Skills, invocation, and boundaries      | [Skill catalog](skills/README.md)                              |
| The baseline rules                      | [Baseline](baselines/AGENTS.md)                                |
| Shared agents                           | [Agent catalog](agents/README.md)                              |
| Research behind the rules               | [Documentation index](docs/README.md)                          |
| Diagram visual language gallery         | [Diagram visual design](docs/diagram-visual-design/index.html) |

Released under the [MIT license](LICENSE).

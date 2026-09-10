# Agent Skills

> Portable, reviewed workflows for consistent agent-assisted work.

The kit provides independently portable skills. Shared Codex agents remain
optional and separate from the skills installer.

## Quick Start

You need:

- Python 3.11 or newer.
- an Agent Skills-compatible client.
- You need Git to clone the repository.

```text
git clone https://github.com/raulcorreia7/agent-skills.git
cd agent-skills
uv run python wizard.py
```

The wizard asks three questions, shows the exact plan, offers a dry run, then
installs and validates. It needs questionary, which `uv run` installs from the
declared dependency; `python skills.py install --all` needs nothing beyond the
standard library.

This command installs every skill for the current user and synchronizes the
shared baseline. Add `--project` to install into a repository instead. A
partial install omits the catalog because it lists skills that are not present.

### Common CLI workflows

Guided install, with a preview before anything is written:

```text
uv run python wizard.py
```

Install every skill for the user, plus the shared baseline:

```text
python skills.py install --all
```

Install one skill into the current repository:

```text
python skills.py install docs --project
```

Restart your client after setup.

Run `python skills.py --help` for the complete installer interface.

## Learn More

| Topic                                         | Documentation                                     |
| --------------------------------------------- | ------------------------------------------------- |
| Skills, invocation, and boundaries            | [Skill catalog](skills/README.md)                 |
| Optional global baseline and companions       | [Baseline guidance](baselines/AGENTS.md)          |
| Shared agents and adding future agents        | [Agent catalog](agents/README.md)                 |
| Diagram visual language gallery                | [Diagram visual design](docs/diagram-visual-design/index.html) |
| Repository maintenance and review             | [Contributing](CONTRIBUTING.md)                   |

## Setup Safety

Setup checks selected directories, the applicable catalog, and the global
baseline before writing. It rejects symlink traversal and replaces each
complete tree and file atomically. It preserves changed skill and catalog
content unless replacement is explicitly allowed. Run
`python skills.py install --all --dry-run` to preview an installation.

`install --all` writes the curated catalog (`README.md`) into the selected
skills root: `~/.agents/skills/` by default, or `<repository>/.agents/skills/`
with `--project`. Later single-skill installs refresh that file when it already
exists.

Every global install synchronizes the contents of `baselines/` to the shared
`~/.agents/` location and to `$CODEX_HOME`, or `~/.codex` when `CODEX_HOME` is
not set. `~/.agents/` is the canonical shared installation location for clients
such as OpenCode. The Codex location is a compatibility mirror. The installer
keeps `AGENTS.md` and `guardrails/` adjacent so their relative references work.
These managed baseline files update automatically when their source changes:

```text
$HOME/.agents/AGENTS.md
$HOME/.agents/guardrails/*.md
$CODEX_HOME/AGENTS.md
$CODEX_HOME/guardrails/*.md
```

Released under the [MIT license](LICENSE).

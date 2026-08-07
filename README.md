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
python skills.py install docs
```

This command installs the `docs` skill in the current repository. A partial
install omits the catalog because it lists skills that are not present.

### Common CLI workflows

Install one skill for the current repository:

```text
python skills.py install docs
```

Install all skills and the shared global baseline for the current user:

```text
python skills.py install --all --global
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
`python skills.py install docs --global --dry-run` to preview an installation.

`install --all` creates the curated catalog at `.agents/skills/README.md`.
Later single-skill installs refresh that file when it already exists.

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

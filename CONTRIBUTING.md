# Contributing

Keep the kit focused, portable, and safe to install. `main` is the rolling
stable branch.

Before adding a line to an always-loaded file (skill description, `SKILL.md`,
`baselines/AGENTS.md`), ask: would removing it cause mistakes? If not, leave it
out.

## Skill contract

1. One primary outcome and a distinct trigger boundary.
2. Useful when copied alone; name skills in plain text.
3. Frontmatter carries `name` and `description` only.
4. Manual skills: the description starts with `Manual invocation only.` and the
   adapter sets `allow_implicit_invocation: false`. Model-invoked skills:
   discriminative triggers and `true`.
5. Compose by skill name; no links to another skill's files, and no composition
   cycles.
6. Sections follow the template's order: `Job`, an optional selector (such as
   `Depth`, `Modes`, or `Branches`) that picks the path, `Steps`, optional
   `Flow`, domain sections, `Guardrails`, optional `Composition`, and `Output`.
   Add `Flow` only when order, loops, or stop conditions carry the essence; keep
   it short arrow-style pseudocode. Add `Composition` when the skill routes
   adjacent jobs to other skills. Every skill ends with an explicit, useful
   `## Output`.
7. References stay local, each branch routes from `SKILL.md`, and every package
   file is reachable from it.
8. `agents/openai.yaml` stays explicit, aligned with invocation policy, and in
   the client's own form.
9. Update the curated catalog deliberately.

Start from `templates/skill/`. Check discovery behavior when a change or request
needs that evidence.

## Reference contract

- Inline what every branch uses; disclose branch-specific rules, caveats, and
  the smallest useful example behind a pointer that states its loading
  condition.
- Group the leaves one branch can need under one loading condition and state
  each route's real cardinality — one artifact or the matching set — so the
  reader loads the set in one operation.
- Point at a leaf when it completes the routing decision; use a domain index
  only for a second decision, and keep the index a map.
- Co-locate a definition with its rules and caveats; move or merge internal
  references only when every local pointer changes in the same edit; add no
  compatibility files.
- Preserve pinned source content, licenses, and provenance.
- For a substantial change, review invocation, process, completion, context
  economy, interface, output, feedback, and safety; a missing invocation,
  completion, output, or safety contract blocks release. Prefer forward checks
  over scores, and verify progressive discovery, grouped leaf loading,
  conditional routing, existing evidence tools, and bounded tool output.

## Agent contract

Start from `templates/agent/`; follow [agents/README.md](agents/README.md).
Upgrades and tool expansion are security changes: inspect schemas, annotations,
inputs, returned fields, authentication, telemetry, and side effects, then
update configuration and notes together. Allowlisting is authorization;
`readOnly` annotations alone are not. Preserve exact MCP pins and allowlists
until a new tool-policy review is complete.

## Command contract

`skills.py`, `wizard.py`, and `tools/validate.py` are the public commands; Poe
runs maintainer tasks. Conventional syntax, long options, `-h`/`--help`,
failures on stderr, results on stdout. `tools/lib.py` and `tools/commands/`
tasks never parse CLI arguments. `wizard.py` is a terminal-only front end over
the installer: it detects state, shows the plan, then installs and validates.
It depends on questionary for prompts; `skills.py` stays standard-library only.

`skills.py` is Python 3.11+, stdlib only, and preserves preflight, symlink
detection, atomic replacement, conflict protection, and explicit overwrite.
Installs target the user unless `--project` is given.

- Skills: one copy in `.agents/skills/<name>` (user or project). An all-skill
  install writes the catalog there; later single-skill installs keep it in
  sync.
- Claude Code: it does not read `.agents/skills`, so each install links every
  installed skill into `.claude/skills/<name>`. A link is created only for a
  free name; an existing entry is never replaced. A user install links only
  when `~/.claude` exists.
- Baseline (user installs only): `~/.agents` is its one home.
  `baselines/AGENTS.md` and `baselines/guardrails/` replace the installed
  copies. `TASTE.md` and `TOOLS.md` are created once and then belong to the
  user. Codex reads only `$CODEX_HOME/AGENTS.md` (default `~/.codex`), so it
  gets a copy of `AGENTS.md`, which names its companions by `~/.agents` paths.
- Claude bridge: `~/.claude/CLAUDE.md` importing `@~/.agents/AGENTS.md`,
  created when `~/.claude` exists and never edited afterward.

Run platform checks when requested or when platform risk is material.

Set up once with `uv sync --all-groups`, then run tasks with
`uv run poe <task>`:

| Task       | Purpose                                                                 |
| ---------- | ----------------------------------------------------------------------- |
| `check`    | `validate`, then `lint`. Run before every PR.                           |
| `validate` | Skills, adapters, output contracts, catalog, composition, references, naming, links, setup, TOML. |
| `lint`     | ruff and rumdl.                                                         |
| `format`   | Format the Python sources.                                              |
| `serve`    | Serve the diagram gallery locally.                                      |

Checks make no cloud contact and change no installed user files.

## Retiring a skill

Explicit approval required. Identify users and composition edges, move
still-owned guidance, remove skill, adapter, and catalog entry together, and
note that installed copies remain until users remove them.

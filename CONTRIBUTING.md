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
6. Every skill carries an explicit, useful `## Output`, in the template's order:
   `Job`, `Steps`, optional `Flow`, domain sections, `Guardrails`,
   `Composition`, `Output`. Add `Flow` only when order, loops, or stop
   conditions carry the essence; keep it short arrow-style pseudocode, not a
   full algorithm.
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
- Point at a leaf when it completes the routing decision; use a domain index
  only for a second decision, and keep the index a map.
- Co-locate a definition with its rules and caveats; move or merge internal
  references only when every local pointer changes in the same edit; add no
  compatibility files.
- Preserve pinned source content, licenses, and provenance.
- For a substantial change, review invocation, process, completion, context
  economy, interface, output, feedback, and safety; a missing invocation,
  completion, output, or safety contract blocks release. Prefer forward checks
  over scores, and verify progressive discovery, conditional routing, existing
  evidence tools, and bounded tool output.

## Agent contract

Start from `templates/agent/`; follow [agents/README.md](agents/README.md).
Upgrades and tool expansion are security changes: inspect schemas, annotations,
inputs, returned fields, authentication, telemetry, and side effects, then
update configuration and notes together. Allowlisting is authorization;
`readOnly` annotations alone are not.

## Command contract

`skills.py` and `tools/validate.py` are the public commands; Poe runs maintainer
tasks. Conventional syntax, long options, `-h`/`--help`, failures on stderr,
results on stdout. `tools/lib.py` and `tools/commands/` tasks never parse CLI
arguments.

`skills.py` is Python 3.11+, stdlib only, and preserves preflight, symlink
detection, atomic replacement, conflict protection, and explicit overwrite. A
global install replaces every file directly under `baselines/` and the
`guardrails/` tree at `~/.agents` and `$CODEX_HOME` (default `~/.codex`), and
creates `~/.claude/CLAUDE.md` importing `@~/.agents/AGENTS.md` when `~/.claude`
exists, leaving an existing file untouched. `~/.agents` is canonical; Codex
mirrors it. Installs target the user unless `--project` is given; an all-skill
install writes the catalog into the selected skills root, and later single-skill
installs keep it synchronized. Run platform checks when requested or when
platform risk is material.

Checks: `uv run poe validate` (skills, adapters, output contracts, catalog,
composition, reachable references, naming, links, baselines, setup, TOML),
`uv run poe check` (validate + ruff + rumdl), `uv run poe lint` (ruff + rumdl),
`uv run poe serve` (diagram preview). No cloud contact, no installed user files
changed; `uv` supplies dev dependencies only.

## Retiring a skill

Explicit approval required. Identify users and composition edges, move
still-owned guidance, remove skill, adapter, and catalog entry together, and
note that installed copies remain until users remove them.

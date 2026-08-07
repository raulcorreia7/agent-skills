# Contributing

Keep the kit focused, independently portable, predictable to install, and safe
to review. `main` is the rolling stable branch.

## Skill contract

1. Give each skill one primary outcome and distinct trigger boundary.
2. Keep it useful when copied without this repository.
3. Use only `name` and `description` in `SKILL.md` frontmatter.
4. Put `Manual invocation only.` in every manual skill description.
5. Keep references local and route each branch from `SKILL.md`.
6. Compose by skill name. Do not link to another skill's files.
7. Include an explicit, useful `## Output` contract.
8. Keep `agents/openai.yaml` explicit and aligned with invocation policy.
9. Update the curated catalog deliberately.

Start from `templates/skill/`. Check discovery behavior when the change or user
request needs that evidence.

For manual invocation, put `Manual invocation only.` in the description and set
`allow_implicit_invocation: false`. For model invocation, use discriminative
trigger language and set `allow_implicit_invocation: true`.

## Reference contract

Inline the steps and rules that every branch uses. Put branch-specific rules,
caveats, and the smallest useful examples in a local reference. Each context
pointer states the condition that loads its target.

Point directly to a leaf reference when it completes the routing decision. Use
a domain index only when the reader must make a second useful decision. An
index is a routing map, not a summary of its children.

Co-locate each definition with its rules and caveats. Keep parent workflow,
generic agent behavior, outputs, and repeated navigation in `SKILL.md` or the
repository guidance that owns them. Internal references can move or merge when
all local pointers change in the same edit. Do not add compatibility files for
obsolete internal paths.

Preserve pinned source content, licenses, and provenance. Keep every skill
usable when copied alone. Do not link one skill to another skill's files.

For a substantial change, review invocation, executable process, completion,
context economy, interface, output, feedback, and safety. Treat a missing
invocation, completion, output, or safety contract as a release blocker when
that dimension applies. Prefer forward checks over inspection-only scores.
Verify that the common path uses progressive discovery, routes branch-specific
context conditionally, selects existing repository or stack-aware tools when
they own the evidence, bounds tool output, and states when broader evidence is
necessary.

## Agent contract

Start from `templates/agent/` and follow [agents/README.md](agents/README.md).
Package upgrades and tool expansion are security changes: inspect schemas,
annotations, inputs, returned fields, authentication, telemetry, and side
effects, then update configuration and notes together.
Allowlisting is authorization. `readOnly` annotations alone are not.

## Skills command contract

`skills.py` supports Python 3.11+ with only the standard library. Preserve full
preflight before mutation, lexical symlink detection, atomic tree and file
replacement, skill and catalog conflict protection, and explicit overwrite. An
all-skill install creates `.agents/skills/README.md`. Later single-skill
installs keep an existing installed catalog synchronized. Every global install
also replaces the managed `AGENTS.md` and complete `guardrails/` tree from
`baselines/` at `~/.agents/` and at `$CODEX_HOME`, or `~/.codex` by default.
`~/.agents/` is the canonical shared installation location; the Codex location
is a compatibility mirror. Run platform checks when the user requests them or
when the change has a material platform risk.

## Command contract

`skills.py` and `tools/validate.py` are the public commands. Poe is the
maintainer task runner. The commands use conventional command-line syntax and
long options. They support `-h`/`--help` and keep failures on stderr. They keep
results on stdout and make the safe common path visible. Shared code in
`tools/lib.py` and validation tasks under `tools/commands/` do not parse
command-line arguments.

## Maintainer commands

Structural validation is available when a change needs it:

```text
uv run poe validate
```

The validator checks skills, adapters, output contracts, catalog entries, and
local links. It also checks baseline files, setup behavior, and TOML syntax.
It does not contact cloud services or change installed user files.

Run validation and development linters together with:

```text
uv run poe check
```

Use `uv run poe lint` for linters only. Use `uv run poe serve` to preview the
diagram gallery. `uv` supplies development dependencies for validation,
linting, and task execution only.

## Retiring a skill

Retirement requires explicit approval. Identify users and composition edges.
Move still-owned guidance. Remove the skill, adapter, and catalog entry together.
Document that existing installed copies remain until users remove them.

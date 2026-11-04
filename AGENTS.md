# AGENTS.md -- Agent Skills Repository

## Repository role

This repository is the source of truth for the shared Agent Skills kit.

- `skills/<name>/` contains independently distributable skills.
- `skills/README.md` is the complete curated catalog.
- `baselines/` holds installed user-level guidance: `AGENTS.md`, `TOOLS.md`,
  `TASTE.md`, `guardrails/`, and the Claude bridge `claude/CLAUDE.md`.
- `templates/skill/` is the canonical minimal skill template.
- `agents/<name>/` contains team-maintained shared-agent packages.
- `skills.py` installs skills, `wizard.py` walks a human through the same
  install, and `tools/validate.py` is the validator. Poe is the maintainer
  task runner. Shared Python code lives in `tools/lib.py`. Setup checks live in
  `tools/setup_checks.py`, and validation tasks live in `tools/commands/`.

## Discovery

Load on condition, never up front.

`AGENTS.md` → `skills/README.md` (catalog) → `skills/<name>/SKILL.md` → the
`references/` leaves that skill names. `baselines/` installs user guidance,
`templates/` seeds new skills and agents, `tools/commands/` holds validation
tasks, and `docs/` holds research notes and the diagram gallery.

Each skill states when to load its own references; follow those conditions
instead of reading the whole tree. Before writing or reshaping a skill,
guardrail, or baseline, read `CONTRIBUTING.md` for the contract and
`baselines/TASTE.md` for the taste.

## Change rules

- Preserve all existing distributable skills unless retirement is explicitly approved.
- Keep each skill focused, self-contained, and usable when copied alone.
- Follow the skill, reference, agent, and command contracts in
  `CONTRIBUTING.md`. Curate the catalog; validation may check it but must not
  regenerate it.
- Keep global judgment in `baselines/AGENTS.md` and task workflow depth in skills.
- Give each directive one authoritative owner. Before you add guidance, find
  its current owner. Update that contract and use a short pointer from
  other artifacts instead of copying the rule.
- Resolve instruction conflicts by the client's authority and scope rules.
  When two applicable repository contracts still disagree and the choice can
  change behavior or risk, report the conflict and ask for direction.
- Keep durable documentation focused on the current state. Put history only in an
  artifact that explicitly owns history or decision records.
- Keep the skills CLI standard-library only and cross-platform.
- Keep the skills CLI convention-based and discoverable: root and subcommand
  help must succeed, and root help must contain current executable examples.
- Avoid compatibility shims, duplicated tool documentation, and generated artifacts.

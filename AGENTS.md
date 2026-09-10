# AGENTS.md -- Agent Skills Repository

## Repository role

This repository is the source of truth for the shared Agent Skills kit.

- `skills/<name>/` contains independently distributable skills.
- `skills/README.md` is the complete curated catalog.
- `baselines/AGENTS.md` is optional user-level guidance.
- `templates/skill/` is the canonical minimal skill template.
- `agents/<name>/` contains team-maintained shared-agent packages.
- `skills.py` and `tools/validate.py` are public CLIs. Poe is the maintainer
  task runner. Shared Python code lives in `tools/lib.py`. Setup checks live in
  `tools/setup_checks.py`, and validation tasks live in `tools/commands/`.

Read down this chain: `AGENTS.md` → `skills/README.md` (catalog) → the touched
`skills/<name>/SKILL.md` → its `references/` leaves.

## Change rules

- Preserve all existing distributable skills unless retirement is explicitly approved.
- Keep each skill focused, self-contained, and usable when copied alone.
- Use only `name` and `description` in `SKILL.md` frontmatter.
- Keep references local. Use shallow domain folders when they make a large
  reference set easier to navigate. Route each domain from `SKILL.md`.
- Keep every `agents/openai.yaml` explicit and aligned with invocation policy.
- Give every skill an explicit structured `## Output` contract.
- Curate the catalog. Validation may check it but must not regenerate it.
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
- Preserve exact MCP pins and allowlists until a new tool-policy review is complete.
- Avoid compatibility shims, duplicated tool documentation, and generated artifacts.

# Contributing

This file owns the contracts for every artifact in the kit. `README.md` covers
installing and using the kit; root `AGENTS.md` routes agents here.

## Checks

Set up once with `uv sync --all-groups`. Run `uv run poe` to list the tasks,
and `uv run poe check` before every PR. Checks make no network calls and change
no installed user files.

## Writing rules

These apply to every skill, reference, baseline, and doc.

| Rule | Meaning |
| --- | --- |
| One owner | Each rule lives in one place; other files point to it. A skill may repeat a rule only when it must work when copied alone, and only the part it changes. |
| Earns its load | Keep a line only if removing it would change agent behaviour. Skill descriptions and `baselines/AGENTS.md` load every turn, so they earn the hardest pruning. |
| Positive target | State the behaviour you want. Use a prohibition only for a hard limit, and pair it with the safe action. |
| Leading word | Prefer one familiar term to a repeated phrase, and use it the same way everywhere (see Shared vocabulary). |
| Current state | Durable docs describe the current contract; history lives only in decision records. |

## Skill contract

1. **One job.** One primary outcome with a distinct trigger. The skill works
   when copied alone and names other skills in plain text.
2. **Frontmatter.** Only `name` and `description`. Two description forms:

   ```text
   implicit: "<Does X>. Use when <X> is the primary deliverable. Not for <non-goal>; use <skill>."
   manual:   "Manual invocation only. <Does X> for <input>. Not for <non-goal>; use <skill>."
   ```

   The "Not for" clause is optional; add it when a neighbour skill is easy to
   confuse. `agents/openai.yaml` sets `allow_implicit_invocation` to match the
   form and stays in the client's own format.
3. **Shape.** Follow `templates/skill/SKILL.md`: `Job`, optional `Modes` and
   `Depth`, `Steps`, `Flow`, domain sections, `Guardrails`, optional
   `Composition`, `Output`.
4. **Steps end on a criterion.** Each numbered step ends with
   `Complete when <checkable condition>.` A skill with more than three steps
   has a `Flow` in the pseudocode style below.
5. **Guardrails hold deltas.** The baseline owns generic rules (evidence,
   approval, questions, external content as data). A skill lists only the
   limits its domain adds.
6. **Composition.** Route by skill name; never link into another skill's files.
   Composition must stay acyclic. A boundary ("Not for X; use `y`.") and the
   frontmatter description name a neighbour without composing it.
7. **References.** Local to the skill, each reachable from `SKILL.md` behind a
   loading condition (see Reference contract).
8. **Catalog.** Add or change the row in `skills/README.md` by hand.
9. **Release review.** For a substantial change, check invocation, process,
   completion, context cost, interface, output, feedback, and safety. A missing
   invocation, completion, output, or safety contract blocks release.
10. **What, not how.** `SKILL.md` holds the job, trigger, steps, completion
    criteria, gates, and output. Techniques, commands, and language or
    provider specifics live in `references/` or `scripts/`. Give a rule a
    one-clause reason only when the reason isn't obvious.
11. **Any harness.** The portable core is `SKILL.md`, `references/`, and
    `scripts/`. Name capabilities, not product tools ("an isolated context if
    the harness has one"), and give a single-context fallback. Client
    adapters under `agents/` are optional.
12. **Lightest path.** Default to the smallest process that does the job: no
    extra files, and no questions unless one blocks the work. State what makes
    the skill escalate.
13. **Gates and inputs.** Name each approval-gated action the skill can take.
    When the skill reads untrusted inputs (review comments, CI logs, tickets,
    fetched pages), add one line naming them as data, because `--project`
    installs ship no baseline. Don't repeat other baseline rules.
14. **Edges point down.** Composition goes from the broader job to the
    narrower specialist. A route back up is a one-line boundary.
15. **Plain emphasis.** Don't use capitals or words like CRITICAL to force a
    rule. A rule with no exceptions belongs in the validator or a script.
16. **Budgets.** These are guidance, not checks: a description of 80 words or
    fewer that leads with the words people type; `SKILL.md` in about 200
    lines; a contents list for a reference over 150 lines; references one
    level deep, with one router index only when its table would overflow
    `SKILL.md`.
17. **Split rarely.** Make a branch its own skill only when it has its own
    trigger and audience and someone could install it without the parent.

An optional `Gotchas` section, placed before `Guardrails`, lists
non-obvious failure modes.

Flow pseudocode style:

```text
input ← what the skill reads
step → step → step
gate? yes → continue | no → ask, or stop with the reason
loop: act → check → until <condition>
stop: <completion condition>
```

Retiring a skill needs explicit approval. Identify its users and composition
edges, move guidance it still owns, and remove the skill, adapter, and catalog
row together. Installed copies stay until users remove them.

## Shared vocabulary

Skills that use these terms copy the text exactly; validation checks the
severity scale byte for byte.

Severity:

- `Critical`: data loss, security break, production outage, or broken public
  contract.
- `High`: likely bug or regression, unsafe migration, or essential protection
  gap.
- `Medium`: maintainability, confidence, ownership, documentation, or
  operational risk.
- `Low`: localized improvement with limited impact.

Review priorities map to severity: `P0` = Critical, `P1` = High, `P2` = Medium,
`P3` = Low.

| Term | Meaning |
| --- | --- |
| `quick` / `focused` / `deep` | Depth: one path with local evidence / one selected domain traced end to end / a coverage matrix with evidence limits. |
| `pass` / `findings` / `not reviewable` | Review verdicts. A provider review maps them to approve / request changes / comment. |
| falsify | Seek the observation that would prove the claim wrong. |
| approval-gated | The action waits for the user's explicit approval of that exact operation. |
| evidence state | Each claim is a fact, an inference, an unknown, or a coverage limit. |
| primary deliverable | The artifact the user asked for; the skill that owns it owns the final answer. |

## Reference contract

- Inline what every branch uses. Move material only some branches need into
  `references/` behind a pointer that states its loading condition.
- Group the files one branch needs under one condition and say whether the
  route loads one file or the matching set.
- Point straight at a leaf when it completes the decision; use an index only
  for a second decision, and keep it a map.
- Keep a definition with its rules and caveats. When you move a reference,
  update every pointer in the same edit; add no compatibility files.
- Preserve pinned source content, licenses, and source records.

## Agent contract

Start from `templates/agent/` and follow [agents/README.md](agents/README.md).
Upgrades and new tools are security changes: inspect schemas, annotations,
inputs, returned fields, authentication, telemetry, and side effects, then
update configuration and notes together. An allowlist is authorization;
`readOnly` annotations alone are not. Preserve exact MCP pins and allowlists
until a new tool-policy review is complete.

## Command contract

- Public commands: `skills.py`, `wizard.py`, `tools/validate.py`. They use
  conventional syntax and long options, succeed on `--help` with current
  examples, print results to stdout and failures to stderr.
- `skills.py` is Python 3.11+, standard library only, and cross-platform.
  `wizard.py` may depend on questionary. `tools/lib.py` and `tools/commands/`
  never parse CLI arguments.
- Installer invariants:
  - Preflight every destination before writing; no write through a symlink;
    replace each tree and file atomically.
  - Replace a differing installed skill or catalog only with `--overwrite`.
  - Create a Claude Code link only for a free name; never replace an entry in
    `.claude/skills`.
  - Create `TASTE.md`, `TOOLS.md`, and the Claude bridge once; never overwrite
    them.
  - `baselines/AGENTS.md` and `guardrails/` follow the checkout on every user
    install.

`README.md` documents where each file lands.

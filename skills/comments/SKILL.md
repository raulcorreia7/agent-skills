---
name: comments
description: Maintains, audits, or explains source comments, docstrings, API documentation, and tool directives. Use when these artifacts are the primary deliverable, not standalone documentation or published API reference pages.
---

# Comments

## Job

Keep source comments accurate, necessary, local, and compatible with their
owning tools. Prefer types, tests, and linters; comments are last.

## Modes

| Mode | Use when | Result |
| --- | --- | --- |
| `explain` | The user wants the current comment contract described | Explanation; files unchanged |
| `audit` | The user wants comments assessed | Each in-scope comment classified as keep, revise, remove, or add |
| `change` | The user wants comments changed | Requested comment changes applied and adjacent code verified |

## Steps

1. Confirm the mode, languages, files, comment types, and write boundary.
   Inspect repository guidance, local conventions, adjacent code, public
   contracts, generated boundaries, and tool directives. Complete when each
   in-scope file's conventions, generated boundaries, and directives are known.
2. Search the requested scope and load the matching references below. Classify
   each candidate as keep, revise, remove, or add by its current purpose and
   source-backed accuracy. Complete when every candidate has a classification
   backed by source evidence.
3. In `change` mode, apply the classifications: keep durable contracts and
   rationale, revise stale meaning, remove narration of obvious mechanics, and
   add text only where code cannot express the fact. Preserve native syntax,
   required placement, and generated ownership. Complete when every in-scope
   revise, remove, or add classification is applied.
4. Compare every changed comment with the current code and public contract. Run
   the owning documentation or directive check when one exists. Complete when
   every changed comment matches the code and each available owning check has
   a result.

## Flow

```text
input ← scope, adjacent code, public contracts, tool directives
scope → classify → apply → verify
mode is explain or audit? yes → report, files unchanged | no → apply within the write boundary
for candidate in scope: classify → keep | revise | remove | add
stop: every candidate classified and every edit backed by source evidence
```

## References

- Read [comment guidance](references/guidance.md) when purpose, placement,
  freshness, security, privacy, or examples affect the classification, or when
  a candidate adds or uses a `NOTE`, `WARNING`, `TODO`, `FIXME`, or `HACK`
  marker.
- Read each applicable automation leaf:
  - [directives and generated boundaries](references/automation/directives-and-generated.md)
    for suppressions, parser or tool directives, generated headers, and
    do-not-edit boundaries;
  - [script comments](references/automation/scripts.md) for Shell, Bash, or
    PowerShell;
  - [pipeline and build comments](references/automation/pipelines-and-builds.md)
    for pipeline YAML, Makefiles, build systems, and containers;
  - [infrastructure-as-code comments](references/automation/infrastructure-as-code.md)
    for IaC configuration and provider directives.
- Read `references/sources.yml` only to verify an external convention or update
  source records.

## Guardrails

- Keep standalone product or system documentation with the documentation owner.
- Preserve immutable legal text exactly. Preserve a tool directive's required
  semantics and placement; change it only when the requested scope includes
  it, then validate it with its owning tool when available.
- Report a broader code defect openly instead of wording a comment around it.

## Output

- Mode and result
- Added, revised, removed, and retained comments
- Source evidence
- Remaining stale or unverifiable text

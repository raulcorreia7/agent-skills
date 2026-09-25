---
name: comments
description: Maintains, audits, or explains source comments, docstrings, API documentation, and tool directives. Use when these artifacts are the primary deliverable, not standalone documentation or published API reference pages.
---

# Comments

## Job

Keep source comments accurate, necessary, local, and compatible with their
owning tools. Prefer types, tests, and linters; comments are last.

## Branches

- `explain`: Describe the current comment contract and keep files unchanged.
- `audit`: Classify each in-scope comment as keep, revise, remove, or add.
- `change`: Apply the requested comment changes and verify adjacent code.

## Steps

1. Confirm the branch, languages, files, comment types, and write boundary.
2. Inspect repository guidance, local conventions, adjacent code, public
   contracts, generated boundaries, and tool directives.
3. Search the requested scope. Classify each candidate by its current purpose
   and source-backed accuracy.
4. Read [comment guidance](references/guidance.md) when purpose, placement,
   freshness, security, privacy, or examples affect the classification. Then
   read each applicable automation leaf:
   - [directives and generated boundaries](references/automation/directives-and-generated.md)
     for suppressions, parser or tool directives, generated headers, and
     do-not-edit boundaries;
   - [script comments](references/automation/scripts.md) for Shell, Bash, or
     PowerShell;
   - [pipeline and build comments](references/automation/pipelines-and-builds.md)
     for pipeline YAML, Makefiles, build systems, and containers;
   - [infrastructure-as-code comments](references/automation/infrastructure-as-code.md)
     for IaC configuration and provider directives.
5. Keep durable contracts and rationale. Revise stale meaning, remove narration
   of obvious mechanics, and add text only where code cannot express the fact.
6. Preserve native syntax, required placement, generated ownership, and
   directive semantics. Change a directive only when the requested scope
   includes it, then validate it with its owning tool when available.
7. Compare every changed comment with the current code and public contract. Run
   the owning documentation or directive check when one exists.
8. Stop when every candidate has a classification and every edit has supporting
   source evidence.

## Flow

```text
for candidate in scope:
    classify → keep | revise | remove | add
    preserve syntax, placement, ownership, directive semantics
compare changed comments with current code → run owning check
stop: every candidate classified + evidenced
```

## Guardrails

- Keep standalone product or system documentation with the documentation owner.
- Preserve immutable legal text exactly. Preserve a tool directive's required
  semantics and placement; change it only in scope and with owning-tool
  validation when available.
- Report a broader code defect. A comment must not hide the defect.
- Read `references/sources.yml` only to verify an external convention or update
  provenance.

## Output

- Branch and result
- Added, revised, removed, and retained comments
- Source evidence
- Remaining stale or unverifiable text

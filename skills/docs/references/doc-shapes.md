# Documentation Shapes

Use local conventions first. When none exist, choose the smallest shape that
answers the reader's next question.

## General Page

```md
# <Title>

> <One-line purpose or outcome.>

## Quick path

1. <First useful action.>
2. <Verification.>

## Common tasks

| Task | Action or link |
|---|---|

## Contracts and constraints

Stable facts, configuration, APIs, ownership, guarantees, and failure modes.

## Examples

Small examples before large examples.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
```

Omit empty sections. Put background, trade-offs, long lists, and historical
notes after the task path.

## Common Document Types

| Type | Default order |
|---|---|
| README | Purpose, quick start, common commands, configuration, usage, validation, deeper links |
| How-to | Outcome, prerequisites, procedure, verification, recovery |
| Runbook | Trigger, prerequisites, procedure, validation, rollback, escalation |
| Reference | Stable facts in tables, source links, failure semantics |
| Explanation | Question, context, model, trade-offs, related decisions |
| Configuration | Keys, required/default values, source, purpose, security boundary |

Configuration tables should distinguish safe examples from real values:

| Key | Required | Default or example | Source | Purpose |
|---|---|---|---|---|

Never include real secrets or private live values.

---
name: <skill-name>
description: "<What it does>. Use when <trigger>. Not for <closest non-goal>; use <other-skill>."
---

<!-- Manual skills start the description with "Manual invocation only." and set
allow_implicit_invocation: false in agents/openai.yaml. -->

# <Skill Name>

## Job

<State the primary outcome in one sentence.>

## Modes

<!-- Optional selector: Depth, Modes, or Branches that pick the path. Delete if unused. -->

## Steps

1. <Inspect the inputs, local conventions, and preserved behavior.>
2. <Perform the task-specific work until its observable completion criterion is true.>

## Flow

<!-- Optional. Short pseudocode: arrows, loops, stop conditions, not a full algorithm. -->

```text
<essence as arrow-style pseudocode>
```

## Guardrails

- <State exceptional safety, scope, authority, or compatibility boundaries.>

## Composition

<!-- Optional. Keep when the skill routes adjacent jobs. -->

- <Route an adjacent job to `skill-name` when that job is the deliverable.>

## Output

- <Skill-specific artifact or answer.>

---
name: <skill-name>
description: "<Does X>. Use when <X> is the primary deliverable. Not for <non-goal>; use <other-skill>."
---

<!-- Manual skills start the description with "Manual invocation only." and set
allow_implicit_invocation: false in agents/openai.yaml. Delete optional
sections you do not use. -->

# <Skill Name>

## Job

<The outcome, in one or two sentences.>

## Modes

<!-- Optional: which path the request takes. -->

| Mode | Use when | Load |
| --- | --- | --- |
| `<mode>` | <trigger> | `references/<file>.md` |

## Depth

<!-- Optional: quick | focused | deep, as defined in CONTRIBUTING.md. -->

## Steps

1. <Inspect the inputs and the behaviour to preserve.> Complete when <checkable condition>.
2. <Do the work.> Complete when <checkable condition>.

## Flow

<!-- Required for more than three steps. -->

```text
input ← <what the skill reads>
<step> → <step> → <step>
<gate>? yes → continue | no → ask, or stop with the reason
stop: <completion condition>
```

## Gotchas

<!-- Optional: non-obvious failure modes, one line each. -->

- <One trap and the safe move.>

## Guardrails

- <An approval-gated action this skill can take.>
- <Untrusted inputs this skill reads, named as data.>
- <One limit this domain adds; the baseline owns generic rules.>

## Composition

<!-- Optional. -->

- Use `<skill-name>` when <adjacent job> is the primary deliverable.

## Output

- <The deliverable.>
- <Caveats, unknowns, and the next action.>

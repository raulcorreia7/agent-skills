---
name: clear-writing
description: "Writes, rewrites, or reviews prose for clarity. Use when clear prose is the primary deliverable. Not for standalone documentation or source comments; use docs or comments. Use ASD-STE100 only for explicit controlled-technical-English compliance, audit, vocabulary verification, or binding publication."
---

# Clear Writing

## Job

Make prose clear without changing its meaning. Use the least rigorous level
that satisfies the request. These rules govern the deliverable's prose, not
your own messages to the user.

## Modes

| Mode | Use when | Requirement |
| --- | --- | --- |
| `author` | Writing new prose | Account for all supplied facts, limits, audience, and directives. |
| `rewrite` | Revising existing prose | Preserve each source assertion or identify an unresolved question. |
| `review` | Assessing prose | Identify significant clarity or meaning risks and give a correction. |
| `formal audit` | An explicit ASD-STE100 audit | Mark each in-scope sentence pass or fail, cite the relevant rule, and give a correction for each failure. |

## Steps

1. Select the mode and the level (see Levels of rigor). Mark code, commands,
   identifiers, legal text, interface text, and immutable quotations as
   exclusions; prose in comments and docstrings remains in scope unless its
   exact wording is immutable. Complete when the mode, level, target reader,
   and exclusions are named.
2. Apply the level's rules under the mode's requirement. Complete when the
   level's finish condition holds and the mode's requirement is met for every
   in-scope sentence.

## Levels of rigor

### Default

Use this level for ordinary writing, rewriting, or review.

- State the main point plainly. Cut stale imagery, inflated wording, vague
  abstractions, and words that carry no meaning.
- Prefer a short, familiar word when it is equally exact, and active voice when
  it identifies the actor that matters or makes the sentence easier to follow.
- Keep one main point in each sentence where practical and group related facts.

Finish when every source claim remains, each sentence has one intended reading
for the target reader, and every unresolved ambiguity is named.

### Technical clarity

Use this level for the prose of procedures, descriptions, runbooks, API
documentation, safety text, and technical comments; read
[technical clarity](references/technical-clarity.md). When those artifacts are
the deliverable, the docs or comments workflow owns them and this level serves
as its prose pass.

### Formal ASD-STE100

Use this level only for an explicit ASD-STE100 compliance request, STE audit,
vocabulary verification, or binding publication requirement. Read the [formal
ASD-STE100 workflow](references/formal-asd-ste100.md), which routes every
compliance or verification claim to authoritative evidence.

### Sources

Read [clear-writing sources](references/clear-writing-sources.md) only when
source scope, attribution, or a disputed clear-writing principle matters.

## Guardrails

- Preserve meaning, identifiers, measurements, sequence, prerequisites, limits,
  legal meaning, safety meaning, and risk level.
- Request domain confirmation when a language change can alter technical or
  safety meaning.
- Complete ordinary and technical work offline from the supplied text, with no
  external tools or source document. Leave heading, link, and STE mechanics
  to Vale, rumdl, or the owning docs pipeline when they exist.

## Output

- Authored or revised text, or a review that names significant clarity risks.
- Exceptions, exclusions, assumptions, and unresolved technical or
  safety questions.
- For formal ASD-STE100 work, the compliance result, the rule IDs and
  official PDF page locators, and every unresolved word.

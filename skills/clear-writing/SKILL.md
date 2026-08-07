---
name: clear-writing
description: Writes, rewrites, or reviews prose. Use when prose clarity is the primary deliverable, not standalone documentation or source comments. Use ASD-STE100 only for explicit controlled-technical-English compliance, audit, vocabulary verification, or binding publication.
---

# Clear Writing

## Job

Make prose clear without changing its meaning. Use the least rigorous level
that satisfies the request.

## Levels

### Default

Use this level for ordinary writing, rewriting, or review.

- State the main point plainly. Remove stale imagery, inflated wording, vague
  abstractions, and words that do not carry meaning.
- Prefer a short, familiar word when it is equally exact, and active voice when
  it identifies a material actor or makes the sentence easier to follow.
- Keep one main point in each sentence where practical and group related facts.
  These checks guide rather than mechanize style: preserve a natural voice and
  break a rule when following it would make the prose worse.

Finish when every source claim remains, each sentence has one intended reading for the target reader, and every unresolved ambiguity is named.

### Technical Clarity

Use this level for procedures, descriptions, runbooks, API documentation,
safety text, and technical comments. This level does not claim ASD-STE100
compliance.

1. Classify each block as a `procedure` or `description`. Apply supplied safety
   and publication requirements.
2. Name the material actor, action, condition, sequence, and limit. Use the
   same term for the same item or concept.
3. Preserve established technical and domain terminology. Explain an unfamiliar
   term when the intended reader needs it. Do not replace an exact term with a
   less precise everyday word.
4. Use procedural structure only for instructions. Keep related conditions and
   actions together.

Finish when each block states its actor, action, conditions, sequence, limits, and required terminology without changing technical or safety meaning.

### Formal ASD-STE100

Use this level only for an explicit ASD-STE100 compliance request, STE audit,
vocabulary verification, or binding publication requirement. Read the [formal
ASD-STE100 workflow](references/formal-asd-ste100.md), which routes every
compliance or verification claim to authoritative evidence.

## Operations

Select the requested operation:

- **Author:** Account for all supplied facts, limits, audience, and directives.
- **Rewrite:** Preserve each source assertion or identify an unresolved
  question.
- **Review:** Identify material clarity or meaning risks and give a correction.
- **Formal audit:** Mark each in-scope sentence pass or fail, cite the material
  rule, and give a correction for each failure.

Mark code, commands, identifiers, legal text, interface text, and immutable
quotations as exclusions. Prose in comments and docstrings remains in scope
unless its exact wording is immutable.

Read [clear-writing sources](references/clear-writing-sources.md) only when
source scope, attribution, or a disputed clear-writing principle is material.

## Guardrails

- Preserve meaning, identifiers, measurements, sequence, prerequisites, limits,
  legal meaning, safety meaning, and risk level.
- Request domain confirmation when a language change can alter technical or
  safety meaning.
- Keep ordinary and technical work offline. Do not require external tools or a
  source document. Heading, link, and STE mechanics belong in Vale, rumdl, or
  the owning docs pipeline when they exist; this skill owns audience and
  structure judgment.

## Output

- Authored or revised text, or a review that identifies material clarity risks.
- Material exceptions, exclusions, assumptions, and unresolved technical or
  safety questions.
- For formal ASD-STE100 work, the compliance result, material rule IDs and
  official PDF page locators, and every unresolved word.

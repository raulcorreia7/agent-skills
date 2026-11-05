# Targets

Pick the profile that matches the text, then apply it on top of the natural
defaults in the skill. A repo or user style guide wins over any profile. When
the target is unclear, use the general profile. IDs point to
[sources](sources.yml).

## General profile

For a reader you can't pin down, or a mixed audience.

- Lead with what the reader must know or do.
- Spell out the links between ideas; an unknown reader may lack the
  background to fill gaps (D1, D2).
- Define a term the first time an outsider would stumble on it.
- Keep sentences short enough to read once. About 25 words is a heuristic,
  and un-nesting clauses matters more than the count (C3, C12).
- Make the text findable, understandable, and usable for the reader's purpose,
  not just short (C1).

## Technical

Readers are working. Precision and completeness come before brevity; cutting
context is the usual mistake here (C5, C7, C8, C9).

| Text | Lead with | Keep | Cut | Form |
| --- | --- | --- | --- | --- |
| Reference | The definition or signature | Every parameter, default, constraint, and error; consistent terms | Narrative and motivation | Terse sentences or tables |
| Tutorial | What the reader will build or learn | Explicit connectives, why each step matters, expected output | Options, branches, deep theory | Numbered steps with full cohesion |
| How-to guide | The goal and prerequisites | Steps, conditions, how to verify | Concept teaching, "simply", "easy" | Imperative numbered steps |
| Explanation or design text | The question or thesis | Reasoning, trade-offs, alternatives, real hedges | Step-by-step procedure | Paragraphs with connectives |
| Procedure or runbook | The outcome and when to run it | Each condition before its action, limits, expected results, the rollback | Commentary between steps | One action per numbered step |
| API description | What the call does and returns | Inputs, outputs, errors, side effects, limits | Restating the parameter name as its description | Short, consistent sentences |
| Code comment | The intent or invariant | The why, non-obvious constraints, units, hazards | What the code already says | Short, next to the code |
| Commit message | An imperative subject of about 50 characters | The problem, why this approach, rejected alternatives, scope limits | "This patch", chatter, link-only context | Subject, blank line, wrapped body |
| Pull or merge request | One line on what changed | Why, approach, shortcomings, test evidence, linked issues | "Fix bug", a line-by-line replay of the diff | Short summary, then a body |

Keep one document type per page; mixing a tutorial with a reference is the
main structural failure (C7).

## Business

Readers are busy and often lack context. Lead with the decision, request, or
impact (C6, C10).

- Email: put the ask and its deadline in the first two sentences. One topic
  per message when you can. Close with the next step if there is one, not a
  pleasantry.
- Summary or report for decision-makers: the recommendation and the key
  number first, then risks and what you need from them. Method detail goes
  last or in an appendix. Keep it under a page when the content allows.
- Announcement: what changes, for whom, and when, then what the reader
  should do. Drop the build-up and the excitement.

Hedges in business text mark real risk. Don't stack them as cover.

## Academic and research

Readers judge claims by their support.

- State the claim, then the evidence, then its limits.
- Keep hedges that mark evidence strength; they are central to scientific
  argument (D5). Remove the empty ones.
- Keep established terms of the field, and cite rather than assert.
- Watch the discussion and introduction sections most closely: they carry
  far more LLM vocabulary than methods sections do (N5).
- Check the argument across sections, not just the sentences. Model-written
  papers tend to fail at the links between sections while each paragraph
  reads well (N3).

## Web and UI copy

Readers scan and act (C5, C6, C10).

- Lead with the action or outcome. Front-load the words the reader is looking
  for.
- Fragments are fine in labels, buttons, and short messages. Use sentence case.
- An error message says what happened, why if known, and what to do next.
- Cut promotional words, "please" in instructions, exclamation marks, and
  jargon. Objective wording measurably improves usability (C10).
- Leave UI strings that must match the product exactly as they are.

## Personal and everyday

Messages, notes, posts, and letters between people.

- Write the way the author talks, with contractions and short sentences.
- Warmth comes from what you say to the person, not from adjectives.
- Keep it as long as the message needs. A thank-you note doesn't need
  structure, headings, or a summary.
- Keep the author's dialect, humour, and quirks (B4).

## Creative and marketing

The author's voice is the point. Remove only LLM noise (B1, B3, A9).

- Fiction and essays: cut stock images and creative clichés, purple prose,
  and over-explained emotion. Keep deliberate fragments, rhythm, and
  repetition the author chose.
- Don't flatten an unusual style toward a house style. A strange sentence that
  works stays.
- Marketing: persuasion is allowed, vagueness isn't. Swap superlatives for the
  specific claim they stand in for, and keep the brand's voice guide.

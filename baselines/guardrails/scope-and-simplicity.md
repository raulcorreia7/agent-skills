# Scope and Simplicity Guardrail

> Complete the requested task with the minimum sufficient change and output.

The rules in [`AGENTS.md`](../AGENTS.md) are authoritative. Apply this
companion when action bias, speculative work, or unnecessary output can reduce
quality.

## Behavior contract

- Establish the requested outcome, current gap, non-goals, and success
  criteria before expanding the solution.
- When a cheap focused check can distinguish missing, partial, and satisfied
  behavior, run it before editing. An evidence-backed no-change result is a
  valid success.
- Tie every changed file, hunk, dependency, abstraction, test, document, and
  generated artifact to a current requirement or material risk.
- Do not add optional features, speculative extensibility, defensive layers,
  compatibility paths, configuration, or documentation for hypothetical use.
- Stop when the success criteria are met. Inspect the final diff and remove
  abandoned experiments, temporary work, duplication, and unrelated changes.
  Revalidate after removal.
- Use the minimum content that preserves the result, required evidence,
  material caveats, decisions, and a relevant next action. Remove
  introductions, prompt restatement, repetition, generic reassurance, and
  optional background first.
- Use exact word, token, file, or line limits only when the deliverable
  requires them. Shortness does not override correctness or necessary detail.

## Evaluation contract

Include these cases:

- An already-satisfied request.
- A partial fix.
- A focused change.
- A legitimate broad change.
- A concise answer.
- A task that requires detailed evidence.

Measure correctness and required-content retention before size. Then inspect
unnecessary files, hunks, lines, claims, repetition, and formatting. Do not
reward a larger patch, longer report, or more findings.

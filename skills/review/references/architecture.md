# Architecture Review

Assess the design against stated outcomes and constraints. Keep redesign
outside the default review.

## Steps

1. Identify the review artifact, intended outcomes, scope, constraints, users,
   and available evidence. Do not invent missing requirements.
2. Map boundaries, dependencies, data ownership, data flow, trust boundaries,
   failure domains, and deployment shape. Map operational ownership only as far
   as the review needs.
3. Evaluate relevant quality attributes: correctness, simplicity, evolvability,
   reliability, security, privacy, performance, cost, observability,
   testability, operability, and migration safety. Treat a named pattern,
   principle, smell, metric, or repository history as evidence to investigate,
   not as proof of quality or a defect.
4. Separate defects, material risks, open decisions, and optional improvements.
   Verify claims against current code, configuration, diagrams, documentation,
   or approved live evidence when practical.
5. Recommend the smallest change that addresses each material finding. Use
   `discuss-architecture` when the answer requires a choice among consequential
   alternatives. Finish when the output accounts for all material evidence and
   quality attributes in scope.

## Composition

- Use `audit` for broad multi-domain discovery or coverage mapping.
- Use `optimize` only when a measurable improvement target owns the work.
- Use `docs` when the approved outcome is an updated design document or ADR.
- Use `diagrams` when a dependency, sequence, boundary, or data-flow visual
  would materially clarify the review.

## Output

Use this order and omit empty sections:

1. **Verdict:** fit, findings present, or not reviewable.
2. **Findings:** `P0`-through-`P3` ordered, with affected quality attribute,
   evidence, consequence, and smallest safe direction.
3. **Questions:** Only decisions or questions that materially change the
   assessment.
4. **Coverage:** Artifacts and system surfaces reviewed or missing.
5. **Checks:** Evidence, commands, and results when they informed the review.
6. **Residual risk:** Assumptions, unverified claims, and confidence limits.

## Guardrails

- Keep the review separate from architecture rewrites and implementation plans.
- Assess only quality attributes that affect the system.
- Report style preferences only when they create a material risk.
- Use reference architectures as context, not as proof of a defect.

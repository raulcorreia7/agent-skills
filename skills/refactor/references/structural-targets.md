# Structural Targets

## Choose The Target

Define a current outcome such as localizing one rule, making an expected change
safer, improving a test seam, removing demonstrated confusion, or correcting a
compatibility or fault risk.

- Find the owner before moving or extracting code.
- Add an abstraction for a stable seam, ownership, compatibility, testability,
  or repeated change. Do not extract similar syntax alone.
- Consolidate duplication when copies share one rule or change obligation. Keep
  independently evolving behavior separate.
- Use inheritance only for behavioral substitutability. Use composition or
  delegation when the goal is reuse without that contract.
- Apply a named pattern only when its problem, context, and consequences match.
- Consult functional techniques only when the user requests them, the
  repository establishes them, or a concrete proposal depends on them. Prefer
  direct local conventions when a technique would surprise maintainers or make
  debugging less obvious.
- Use smells, complexity, coupling, cohesion, churn, and co-change to locate an
  investigation target. Do not make a detector score the objective.

## Apply And Assess

Make the smallest coherent change that reaches the target. Preserve contracts,
inspect all callers, and remove a superseded path only after evidence shows no
use. Assess the intended outcome directly; a pattern name or changed metric is
not proof.

```text
Target: one pricing rule owns eligibility and rounding
Preserve: quoted amount, failures, and public result shape
Evidence: caller trace and existing focused checks
Result: every caller uses the one policy; no copied rule remains
```

Sources: [Parnas, 1972](https://doi.org/10.1145/361598.361623),
[Fowler, Refactoring](https://martinfowler.com/books/refactoring.html),
[Sjøberg et al., 2013](https://doi.org/10.1109/TSE.2012.89), and
[Juergens et al., 2009](https://doi.org/10.1109/ICSE.2009.5070547).

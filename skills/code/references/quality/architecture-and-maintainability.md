# Architecture And Maintainability

Use this leaf when new behavior needs a home: a module, an interface, or a
decision about reuse. Restructuring existing code for its own sake is a
refactoring job.

## Where New Behavior Goes

1. Name the requirement, invariant, or change pressure the structure serves.
2. Put it in the module, contract, or convention that already owns it.
3. Choose the smallest local or native mechanism that meets that pressure.
4. Check callers, data flow, and compatibility for the consequence.

Named patterns and principles are vocabulary for this decision, not targets.

## Heuristics

- Put a consequential decision behind one small interface, and keep its
  representation and policy private when callers don't need them.
- Add a boundary only for a current variation, ownership, compatibility,
  testability, or repeated change. A layer that only forwards calls costs more
  than it gives.
- Reuse the existing rule when new code would copy it. Code that only looks
  similar but can change independently stays separate.
- Use inheritance only when the subtype keeps the base contract; otherwise
  compose or delegate.
- Put a common operation where a caller naturally starts. Add a factory,
  builder, helper, or multi-step protocol only when it carries real
  construction, lifecycle, validation, or compatibility behavior.
- When a non-obvious pattern matters to later maintenance, record its intent
  and the flexibility it buys. Obvious code needs no pattern-name comment.

Example: one policy owns eligibility and price rounding.

```text
Checkout → PricingPolicy.quote(order) → Money
            owns discount rules and price rounding
```

Callers use the returned `Money` and don't copy the discount or rounding rules.

Sources: [Parnas, 1972](https://doi.org/10.1145/361598.361623),
[Liskov and Wing, 1994](https://doi.org/10.1145/197320.197383),
[Juergens et al., 2009](https://doi.org/10.1109/ICSE.2009.5070547),
[Stylos and Myers, 2008](https://doi.org/10.1145/1453101.1453117), and
[ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html).

# Architecture And Maintainability

## Structural Decision

1. Name the current requirement, invariant, risk, or change pressure.
2. Find the module, contract, or repository convention that owns it.
3. Choose the smallest local or native mechanism that addresses that pressure.
4. Inspect callers, data flow, compatibility, and the expected consequence.

Use named patterns and principles as vocabulary for this decision. Do not
implement them for compliance or optimize their count.

## Heuristics

- Put a consequential decision behind one small, coherent interface. Keep its
  representation and policy private when callers do not need them.
- Add a boundary for current variation, ownership, compatibility, testability,
  or repeated change. Keep related behavior together when a new layer would
  only forward calls.
- Consolidate copies when they encode the same rule or create one change
  obligation. Keep independently evolving behavior separate even when its
  syntax looks similar.
- Use inheritance only when the subtype preserves the base contract. Prefer
  composition or delegation when reuse does not require substitutability.
- Put a common reusable operation where a caller naturally starts. Add a
  factory, builder, helper, or multi-step protocol when it carries necessary
  construction, lifecycle, validation, or compatibility behavior.
- Record the local intent and purchased flexibility when a non-obvious pattern
  is important to later maintenance. Do not add pattern-name comments to
  obvious code.
- Consult history when change spread, divergence, or recurring defects matter.
  Use churn and co-change to prioritize inspection and checks, not to condemn
  frequently changed code.

Example—one policy owns eligibility and price rounding:

```text
Checkout -> PricingPolicy.quote(order) -> Money
            owns discount rules and price rounding
```

Callers use the returned `Money`. They do not copy discount tests or price
rounding rules.

These are conditional design heuristics, not proof that more modules, patterns,
or abstraction improve a system.

Sources: [Parnas, 1972](https://doi.org/10.1145/361598.361623),
[Liskov and Wing, 1994](https://doi.org/10.1145/197320.197383),
[Juergens et al., 2009](https://doi.org/10.1109/ICSE.2009.5070547),
[Stylos and Myers, 2008](https://doi.org/10.1145/1453101.1453117), and
[ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html).

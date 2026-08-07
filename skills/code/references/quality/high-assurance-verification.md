# High-Assurance Verification

- Define the property, system boundary, threat or failure model, and trusted
  assumptions before you select a method.
- Express relevant preconditions, postconditions, invariants, state transitions,
  and refinement relations in a form the selected tool can check.
- Select model checking, theorem proving, abstract interpretation, or another
  formal technique only when it matches the property and system model.
- Connect the checked artifact to the exact source, configuration, dependencies,
  compiler, and build that ship. Keep proof and model checks reproducible.
- Test the interfaces and assumptions that remain outside the proof. Use
  independent review for a high-impact assurance claim.
- State the verified property and every material assumption. Do not extend a
  component proof into a system-wide correctness claim.

Example—specify a bounded transfer operation:

```text
pre:       amount > 0 and source.balance >= amount
post:      source.balance' = source.balance - amount
           target.balance' = target.balance + amount
invariant: source.balance' + target.balance' =
           source.balance + target.balance
assumption: both writes commit atomically in the modeled store
```

Prove the implementation against this contract. Test store failures and
transaction behavior because the store assumption remains outside the proof.

Hoare logic establishes compositional reasoning under stated assertions. The
seL4 proof demonstrates strong bounded assurance while listing trusted
hardware, compiler, assembly, boot, and specification assumptions.

Sources: [Hoare, 1969](https://doi.org/10.1145/363235.363259) and
[seL4 formal verification](https://sel4.org/Research/pdfs/sel4-formal-verification-os-kernel.pdf).

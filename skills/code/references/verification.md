# Check Selection And Interpretation

Use the smallest existing repository-owned check that addresses a material
risk. Inspect repository scripts before you state what a generic command runs.
Use the repository package manager, wrapper, and declared tool versions.

Map each material success criterion and preserved behavior to an oracle and a
check level. A missing oracle is a requirements gap; current output is not an
automatic expected result.

When broader validation is in scope, use this order as applicable:

1. Format maintained source.
2. Run owned lint, static analysis, and type checks.
3. Compile or build the affected target.
4. Run focused tests.
5. Run integration or system checks for shared contracts, routing,
   serialization, middleware, migrations, concurrency, or providers.

Create tests or expand test scope only when the user requests tests or the
deliverable requires them. Test observable behavior through the narrowest
credible boundary. Cover the changed success path, material failures, boundary
values, and the specific regression. Stop when another case protects no
distinct risk.

Interpret the actual result. Separate product failures from environment or
tool failures. State the command, relevant scope, and result. A check supports
only the behavior and platform that it exercises. Report a material evidence
gap as blocked when no safe check is available.

Example—evidence stays proportional to the change:

| Risk | Check | Result statement |
|---|---|---|
| Parser rejects an invalid enum | Focused parser test | Invalid value returned the owned validation error |
| Generated client drift | Repository generation check | Generated tree remained unchanged |
| Database ordering across pages | Real-database integration test | Ties used the stable ID and produced no duplicates |

Do not claim broader platform, performance, or compatibility coverage from
these focused checks.

## Repair From Check Feedback

Use compiler, analyzer, test, and runtime failures as evidence in a bounded
repair loop:

```text
contract -> discriminating check -> classify failure -> one evidence-driven edit
         -> rerun the same check -> required broader check -> inspect final diff
```

Preserve the first failure and each material change in evidence. Stop when the
same failure repeats, results oscillate, or the next edit would be speculative.
Do not change a failing test only to accept the implementation. Change its
oracle only when the requested contract changed, and review that contract
change explicitly.

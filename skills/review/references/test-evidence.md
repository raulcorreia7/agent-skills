# Test Evidence Review

Review tests as executable specifications. Trace each material change through
this chain:

```text
requirement or risk -> oracle -> test level -> command -> result -> evidence limit
```

Check these items:

- Confirm that the oracle comes from a requirement, contract, reproduced bug,
  invariant, reference implementation, consumer, or reviewed domain example.
- Confirm that an assertion fails for the relevant wrong behavior.
- Confirm that the test level includes each boundary claimed by the result.
- Flag non-crash checks, self-derived expected values, tautological round trips,
  unreviewed snapshots, and tests of mock calls that replace the claimed risk.
- Inspect generated tests for copied logic, invented requirements, weak error
  checks, excessive mocks, duplicates, and repair-loop accommodation.
- Treat a focused pass as evidence for that selection only. Require broader
  gates when impact mapping is uncertain.
- For a flake change, require the first failure, classified cause, and evidence
  that the fix controls the cause.
- Treat coverage, mutation, counts, pass rates, and agent scores as diagnostic
  evidence, not as correctness claims.
- Report the relevant boundary, platform, schedule, and data limits.

## Example

```text
Claim: the database rejects duplicate external IDs.
Gap: the test mocks the repository and asserts a method call.
Consequence: the test does not exercise the unique constraint or error mapping.
Required evidence: a database integration case with the reviewed persistence contract.
```

## Evidence Base

- [Barr et al., *The Oracle Problem in Software Testing*](https://doi.org/10.1109/TSE.2014.2372785)
- [ISO/IEC/IEEE 29119 series](https://committee.iso.org/sites/jtc1sc7/home/projects/flagship-standards/isoiecieee-29119-series.html)
- [Yang et al., independent tests for overfitting patches](https://doi.org/10.1145/3106237.3106274)

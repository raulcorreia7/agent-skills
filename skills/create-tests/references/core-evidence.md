# Core Test Evidence

## Oracle

Name an independent source for every material expected result. Use a
requirement, public contract, reproduced bug, invariant, reference
implementation, consumer expectation, or reviewed domain example.

Do not derive the expected result from the code under test. Treat a missing
oracle as a requirement gap.

## Test Level

Use the smallest level that can observe the claim:

- Use a unit test for an isolated deterministic rule.
- Use an integration test for a real database, filesystem, framework,
  serializer, queue, or network boundary.
- Use a contract test for compatibility between a consumer and a provider.
- Use a system test for a deployed journey or emergent cross-component result.

A test double can isolate local decisions. It cannot prove the behavior of the
boundary that it replaces.

## Evidence

Record the claim, oracle, cases, command, result, and relevant environment.
State each material boundary that the command did not exercise. Structural
coverage shows reach, not correctness.

## Example

```text
Claim: the API preserves a client-supplied request ID.
Oracle: versioned public API contract.
Level: transport integration test.
Case: send a valid request ID. Assert the response header has the same value.
Check: focused API integration command passes.
Not proved: proxy behavior in the deployed environment.
```

## Evidence Base

- [Barr et al., *The Oracle Problem in Software Testing*](https://doi.org/10.1109/TSE.2014.2372785)
- [ISO/IEC/IEEE 29119 series](https://committee.iso.org/sites/jtc1sc7/home/projects/flagship-standards/isoiecieee-29119-series.html)
- [Inozemtseva and Holmes, coverage and test effectiveness](https://doi.org/10.1145/2568225.2568271)

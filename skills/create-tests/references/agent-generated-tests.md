# Agent-Generated Tests

Treat an agent-generated test as a candidate, not as evidence by itself.

1. Compile and run the test.
2. Check the oracle, assertions, failure message, determinism, and distinct
   risk.
3. Safely confirm that a regression detects the known broken behavior.
4. Add an independent probe for a consequential claim. Use a held-out case,
   reference implementation, property, differential check, or mutation audit.
5. Inspect the final implementation and test diff together.

Stop a repair loop when evidence repeats or oscillates. Preserve the first
failure and each material change in evidence. Do not expose hidden evaluation
tests or their exact feedback to the repair loop.

A second instance of the same model is not automatically an independent oracle.

## Example

```text
candidate ← agent adds tests for a rounding defect and repairs the function
oracle ← published currency-rounding rule
probe ← mutate the boundary comparison; the focused test must fail
stop ← two repairs, same failure → requirement gap
```

## Evidence Base

- [Schäfer et al., TestPilot](https://doi.org/10.1109/TSE.2023.3334955)
- [Yang et al., independent tests for overfitting patches](https://doi.org/10.1145/3106237.3106274)
- [SWE-agent](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html)

# Agent-Generated Tests

An agent-generated test is a candidate, not evidence by itself.

1. Compile and run the test.
2. Check the oracle, assertions, failure message, determinism, and the
   distinct risk it protects.
3. Confirm safely that a regression test detects the known broken behavior.
4. Add an independent probe for a consequential claim: a held-out case,
   reference implementation, property, differential check, or mutation audit.
5. Read the final test diff together with the code it exercises.

Don't expose hidden evaluation tests or their exact feedback to the agent
writing the tests. A second instance of the same model is not an independent
oracle.

## Example

```text
candidate ← agent adds tests for a rounding defect
oracle ← published currency-rounding rule
probe ← mutate the boundary comparison; the focused test must fail
stop ← the mutant survives twice after fixes → requirement gap
```

## Evidence Base

- [Schäfer et al., TestPilot](https://doi.org/10.1109/TSE.2023.3334955)
- [Yang et al., independent tests for overfitting patches](https://doi.org/10.1145/3106237.3106274)
- [SWE-agent](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html)

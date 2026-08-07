# Test Metrics

Use a metric to answer a named diagnostic question. Do not use it as a
correctness certificate or a universal target.

| Metric | Useful question | It does not prove |
| --- | --- | --- |
| Statement or branch coverage | What structure did tests not reach? | The assertions detect wrong behavior |
| Mutation score | Did tests detect selected injected faults? | All real faults are detected |
| Test count | How large is the maintenance inventory? | More confidence |
| Pass rate | What passed in this suite and environment? | No relevant defects exist |
| Flake or retry rate | How reliable is the signal over time? | A rerun invalidates a failure |
| Runtime | Where is feedback expensive? | Slow tests have more value |
| Agent resolve rate | What passed in this exact harness? | General or safe autonomy |

If a metric becomes a gate, add an anti-gaming check. Review assertions for a
coverage gate. Inspect equivalent mutants for a mutation gate. Use fresh
held-out tasks for an agent gate.

## Example

```text
Question: does the generated suite detect boundary-condition faults?
Evidence: branch coverage reaches the boundary, but one focused mutant survives.
Action: strengthen the boundary assertion. Do not raise a universal target.
```

## Evidence Base

- [Inozemtseva and Holmes, coverage and test effectiveness](https://doi.org/10.1145/2568225.2568271)
- [Papadakis et al., mutation testing advances and limits](https://doi.org/10.1016/bs.adcom.2018.03.015)
- [Riddell, Ni, and Cohan, benchmark contamination](https://aclanthology.org/2024.acl-long.761/)

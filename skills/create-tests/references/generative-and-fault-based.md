# Generative And Fault-Based Tests

Select one technique for a named risk. Do not add every technique by default.

| Condition | Technique | Required oracle |
| --- | --- | --- |
| Stable invariant over many valid inputs | Property test | Invariant and valid generator |
| Exact outputs are unavailable, but executions have a known relation | Metamorphic test | Valid relation between executions |
| Independent implementations or modes must agree | Differential test | Defined common input domain |
| Untrusted structured input can crash or violate safety | Fuzz test | Safety properties and valid harness |
| Assertions can pass despite plausible faults | Mutation audit | Reviewed operators and surviving mutants |

Preserve seeds and minimized counterexamples. Use generators that represent the
valid and invalid domains. A fixed seed supplies one repeatable sample. It does
not prove the property.

For mutation results, inspect surviving and equivalent mutants. Do not treat a
mutation score as a correctness score.

## Example

```text
Risk: a decoder corrupts valid encoded values near size boundaries.
Property: decode(encode(value)) equals value for every generated valid value.
Generator: valid values around empty, maximum, and multibyte boundaries.
Evidence: retain the minimized failing value as a regression case.
```

## Evidence Base

- [Claessen and Hughes, QuickCheck](https://doi.org/10.1145/357766.351266)
- [Chen et al., metamorphic testing survey](https://doi.org/10.1145/3143561)
- [Yang et al., differential compiler testing](https://doi.org/10.1145/1993498.1993532)
- [Jia and Harman, mutation testing survey](https://doi.org/10.1109/TSE.2010.62)
- [NIST Secure Software Development Framework, PW.8](https://doi.org/10.6028/NIST.SP.800-218)

# Java Contracts

Repository formatter, nullness model, and parent build conventions take
precedence.

## Types And Execution

- Keep public APIs narrow and use records or sealed hierarchies only when the
  supported release and the domain contract justify them. Do not make API
  shapes depend on storage or framework types.
- Reuse exactly one nullness contract. `Optional` is a return-value contract,
  not a field, parameter, or serialization substitute.
- Use try-with-resources for owned resources. Preserve causes while translating
  exceptions and make shared-state ownership and concurrency rules explicit.
- Keep persistence, framework, and provider details at a boundary. Return
  domain-relevant types to callers.

# C# And .NET Contracts

Repository policy, the pinned SDK in `global.json`, the target-framework
support policy, and the nearest `.editorconfig` take precedence.

## Types And Execution

- Model absence with nullable annotations, not `!`. Model invalid input and
  recoverable outcomes with types when a Boolean or exception loses the caller
  contract. Do not mix competing nullness annotations with nullable reference
  types.
- Keep async I/O async through the call chain, propagate `CancellationToken`,
  and avoid `.Result`, `.Wait()`, and fire-and-forget work outside an owned
  boundary.
- Dispose owned resources with `using` or `await using`. Translate broad
  exceptions only at a boundary that can add actionable context and retain the
  original cause.
- Use `StringComparison` deliberately. Protocol and identifier comparisons
  normally require `Ordinal` or `OrdinalIgnoreCase`.

## Example

```csharp
async Task<Result<Order>> CancelAsync(OrderId id, CancellationToken ct)
{
    var order = await store.FindAsync(id, ct).ConfigureAwait(false); // async all the way
    return order is null ? Result<Order>.NotFound() : Result<Order>.Ok(order);
}
```

```text
absent value → nullable annotation; invalid input → type, not `!` or a Boolean
a.Equals(b, StringComparison.Ordinal) → protocol and identifier comparisons
```

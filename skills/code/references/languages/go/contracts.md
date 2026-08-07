# Go Contracts

Repository package conventions take precedence.

## Types And Contracts

- Write explicit, idiomatic Go. Prefer small concrete types and the standard
  library before frameworks or generic helpers.
- Define a small interface next to its consumer only for a real substitution
  or ownership seam. Return concrete types from implementations when practical.
- Use zero values intentionally. Preserve the observable distinction between a
  nil slice, empty slice, absent value, and missing map entry.
- Keep exported APIs narrow. Avoid package-level mutable state and utility
  dumping grounds.

## Execution And Ownership

- Return errors explicitly. Add useful operation context and use `%w` when a
  caller must retain the cause.
- Put `context.Context` first when request lifetime matters. Do not store it in
  a struct without a strong established reason.
- Make goroutine ownership, shutdown, cancellation, channel closing, and error
  collection explicit. Bound concurrent work. Do not coordinate with sleeps.
- Use `defer` for clear local cleanup. Check close or flush errors when they
  can change the operation result.
- Use synchronization primitives around one explicit invariant.

## Files And Documentation

Follow repository naming. Without a stronger convention, use short lowercase
file names with underscores where useful, such as `payment_service.go`. Use
`_test.go` for tests.

Use `//` for rationale and invariants. Document exported packages and symbols
when linting or caller clarity requires it. Begin an exported declaration
comment with the declaration name.

## Sources

- [Go doc comments](https://go.dev/doc/comment) and
  [Effective Go](https://go.dev/doc/effective_go).

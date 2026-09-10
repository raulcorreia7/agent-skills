# Input, Errors, And Resources

## Input And Guards

- Parse and validate external input at the authoritative boundary. Normalize
  only representations that the domain or protocol defines as equivalent.
- Use native guards for simple preconditions. Reuse an existing schema or
  validation library for structured input. Add a new library only under
  repeated validation pressure.
- Give each guard one reason and one outcome. Combine conditions only when they
  define one rule and have the same result.
- Order guards by prerequisites and observable contracts first. Preserve
  security and error precedence. Consider cost after correctness.
- Choose the outcome from repository and boundary conventions. Distinguish
  programmer defects, invalid external input, domain rejection, absence,
  idempotent no-op, and cancellation.
- Extract validation when the rules have separate ownership, repeat across
  boundaries, or obscure the main path. Do not extract only to reduce guard
  count.

## Errors And Resources

- Handle an error only to recover, translate it to the boundary contract, add
  useful context, or perform cleanup. Preserve the original cause.
- Log an error once at the boundary that owns the operation. Use stable,
  structured fields and exclude secrets and unnecessary personal data.
- Use native scoped cleanup such as `with`, `using`, `defer`, or RAII. Use
  `try`/`finally` when explicit lifecycle cleanup remains necessary.
- Catch only failures this layer can handle. Preserve the primary failure when
  cleanup also fails according to repository convention.
- Retry only a transient failure when the operation is safe to repeat or has an
  idempotency contract. Bound attempts, respect cancellation, and preserve the
  final cause.

Example—translate once at the owning boundary:

```text
request bytes → parse → validate → domain command
parse failure        → 400 InvalidRequest
domain rejection     → 409 OrderAlreadyClosed
dependency timeout   → 504 DependencyTimeout
unexpected failure   → 500 + internal cause record
```

The boundary logs the stable operation and correlation fields. Lower layers
return causes and do not repeat the same log event.

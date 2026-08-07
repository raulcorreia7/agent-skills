# Structured Boundary Core

Treat structured boundary text as a grammar, not an interpolated string.

- Prefer a typed or grammar-aware client, builder, parser, or serializer when
  it expresses the operation clearly and preserves the boundary contract.
- Keep data values separate from syntax through parameter binding,
  serializers, variables, and protocol encoders. Use grammar-aware quoting and
  allowlists for identifiers, paths, operators, functions, headers, or other
  dynamic structure that cannot be bound as data.
- Use a raw or unchecked escape hatch only when the owning boundary requires
  unsupported semantics, exact wire compatibility, measured performance,
  migration, administration, or a protocol-level test.
- Keep explicit source text or manual protocol construction in the owning
  adapter. Define the grammar, version or dialect, encoding, schema, mapping,
  cardinality, limits, transaction or idempotency, timeout, cancellation, and
  error behavior that apply.
- Validate the boundary with the real parser, serializer, service, database
  engine, or protocol conformance test. Test the semantic result, not only the
  constructed text.

Example—keep structure and values separate:

```text
field = allowed_fields[request.sort]
query = query.order_by(field, direction=allowed_directions[request.direction])
query = query.where(customer_id == bind(request.customer_id))
```

The maps select grammar nodes; `bind(...)` supplies data.

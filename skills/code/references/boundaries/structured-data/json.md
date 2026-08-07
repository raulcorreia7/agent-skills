# JSON

- Use the repository serializer and explicit owned types or schemas. Configure
  naming, unknown-member, null, enum, number, date, and duplicate-key behavior
  when defaults can change the contract.
- Bound document bytes, nesting depth, collection sizes, and string lengths at
  untrusted boundaries. Stream only when the format and consumer permit
  incremental validation.
- Preserve numeric precision and distinguish absent, null, empty, and default
  values when the domain does.
- Avoid relaying arbitrary upstream JSON. Parse and map it into an owned
  response contract.
- Verify representative round trips and rejection cases with the actual
  serializer and schema validator used in production.

Example—an owned response distinguishes a missing optional field from a
present nullable field:

```json
{
  "id": "ord_123",
  "totalCents": 1250,
  "cancelledAt": null
}
```

Tests confirm the exact field names, integer range, null behavior, unknown-field
policy, and rejection of duplicate keys when the parser exposes that choice.

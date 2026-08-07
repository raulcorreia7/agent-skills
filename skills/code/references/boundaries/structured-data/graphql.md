# GraphQL

- Prefer generated or typed operations. Put caller values in variables rather
  than constructing operation text.
- Allowlist operation names, fields, directives, fragments, and dynamic
  selection choices exposed by the application contract.
- Bound query depth, aliases, list sizes, pagination, total complexity, response
  bytes, and execution time. Apply authorization to resolved data, not only to
  operation admission.
- Pin or check the schema that generated clients and validators use. Treat
  introspection and persisted-query policy as explicit deployment choices.
- Verify the parsed operation, variable coercion, partial-error behavior, and
  response mapping against the supported server or schema-aware test boundary.

Example—put caller data in variables and keep the operation shape owned:

```graphql
query OrdersByCustomer($customerId: ID!, $first: Int!) {
  orders(customerId: $customerId, first: $first) {
    nodes { id createdAt totalCents }
    pageInfo { endCursor hasNextPage }
  }
}
```

The client caps `$first`; the server applies field authorization and a query
complexity limit.

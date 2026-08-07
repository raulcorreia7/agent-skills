# SQL

- Use the repository's maintained database API, query builder, or ORM for
  supported operations.
- Bind values with parameters. Treat table names, column names, sort
  directions, operators, and clauses as grammar: select them from explicit
  allowlists or construct them with a grammar-aware API.
- Use explicit SQL for unsupported semantics, a measured performance need,
  migrations, or administration. Keep it near its database adapter and make
  the expected rows, columns, types, cardinality, transaction, locking, and
  error behavior explicit.
- Map results into owned types. Handle zero, one, and many rows deliberately.
- Verify meaningful queries against the supported database engine. Include
  transaction, constraint, collation, null, ordering, and concurrency cases
  when they can change behavior.

Example—select the sort expression from an allowlist and bind the values:

```sql
SELECT id, created_at, total_cents
FROM orders
WHERE tenant_id = :tenant_id
ORDER BY created_at DESC, id DESC
LIMIT :page_size;
```

The application owns the fixed `ORDER BY` shape. `tenant_id` and `page_size`
are parameters.

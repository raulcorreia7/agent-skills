# Structured Data And Integrations

Read [core](core.md) for every structured boundary. Then read only the leaves
that match the affected grammar or contract:

- [SQL](sql.md) for relational queries, commands, migrations, or database
  administration.
- [OData](odata.md) for OData query options, metadata, and service requests.
- [HTTP](http.md) for methods, URLs, headers, bodies, status codes, caching, or
  request lifecycle behavior.
- [JSON](json.md) for JSON parsing, serialization, schemas, or mapping.
- [XML](xml.md) for XML parsing, serialization, schemas, namespaces, or
  transformations.
- [GraphQL](graphql.md) for operations, variables, selection sets, schemas, or
  resolver boundaries.
- [other structured languages](other-languages.md) for filters, expressions,
  templates, policies, or another DSL without a dedicated leaf.
- [persistence and schema change](persistence.md) for persistent-store
  transactions or ordering, migrations, deployment overlap, or rollback. Query
  language sorting stays with its language leaf.
- [provider integrations](integrations.md) when provider-specific mapping,
  authentication, pagination, rate limits, compatibility, or drift applies.
- [data representation](representation.md) for non-HTTP paths, time, numbers,
  units, precision, rounding, or genuinely large or unbounded data. Routine
  HTTP URL handling stays with the HTTP leaf.

Several leaves can apply to one boundary. Stop after the common contract and
the selected leaves.

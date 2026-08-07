# OData

- Build queries with a typed client or grammar-aware builder that targets the
  service's supported OData version and metadata.
- Encode literal values. Allowlist field and navigation paths, operators,
  functions, sort keys, expansions, and selectable fields.
- Bound page size, total results, expression complexity, and expansion depth.
  Preserve deterministic ordering across pages.
- Keep the service origin, entity-set path, credentials, and protocol headers
  in configuration. Accept an upstream URL or raw query option only when the
  public contract explicitly owns that capability.
- For an inbound API, expose an owned filter and sort contract. Do not expose
  raw OData query text or enable unrestricted automatic query application.
- Treat metadata as the grammar and type contract. Define authorization and
  field-exposure policy separately; metadata visibility does not grant access.
- Validate the constructed request against pinned metadata and the real
  endpoint or a compatible OData parser. Assert the semantic filter and order
  tree, not only the URL text.

Example—let the typed provider construct the OData grammar:

```csharp
var page = await client.Orders
    .Where(order => order.CustomerId == request.CustomerId)
    .OrderByDescending(order => order.CreatedAt)
    .ThenBy(order => order.Id)
    .Take(request.PageSize)
    .ExecuteAsync(cancellationToken);
```

The endpoint validates `PageSize` against its owned limit and maps the request
model to this expression. It does not accept the caller's `$filter` or
`$orderby` text.

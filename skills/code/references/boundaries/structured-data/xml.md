# XML

- Use a maintained XML parser and serializer with explicit encoding,
  namespaces, schema, entity, DTD, and external-resource behavior.
- Disable external entity and network resolution unless the owned contract
  requires a reviewed, bounded resolver.
- Treat element names, attribute names, namespace URIs, XPath, XSLT, and other
  expressions as grammar. Bind or encode values and allowlist dynamic
  structure.
- Preserve canonicalization, whitespace, mixed-content, and ordering behavior
  only when the consumer contract depends on them.
- Bound document bytes, depth, nodes, expansions, and transform resources.
- Verify against the production parser, schema, and any signature or transform
  implementation that defines compatibility.

Example—bind the namespace in the owned document contract:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<order xmlns="urn:example:orders:v1">
  <id>ord_123</id>
</order>
```

The parser uses the `urn:example:orders:v1` schema, prohibits DTD processing,
and has no external resolver unless the reviewed contract supplies one.

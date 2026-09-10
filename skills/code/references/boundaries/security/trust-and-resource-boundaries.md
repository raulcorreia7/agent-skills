# Trust And Resource Boundaries

- Identify each untrusted source, trust change, principal, protected resource,
  sensitive value, dangerous sink, and resource budget.
- Parse and validate untrusted data at the authoritative server boundary.
  Check syntax, length, range, cardinality, and domain meaning.
- Normalize only forms that the owned contract defines as equivalent. Reject
  ambiguous encodings or conflicting representations.
- Keep values separate from executable grammar. Bind data values and select
  dynamic names, operators, paths, or other structure from explicit
  allowlists. Apply context-specific output encoding at its final sink.
- Bound input and output bytes, item counts, nesting, expansion, processing
  time, memory, and concurrency where an attacker can consume them.
- Minimize privileges and sensitive data. On rejection, prevent partial
  privileged effects and return only information that the caller can receive.
- Apply the applicable [structured-data contract](../structured-data/index.md)
  for the exact protocol, grammar, parser, or serializer.

Example—convert an external request into an owned command:

```text
request → byte limit → owned parser → syntax and domain validation
        → allowlisted operation + bound values → application command
```

The boundary rejects extra structure and oversized collections before it
invokes privileged behavior.

Sources: pinned OWASP [Threat Modeling Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Threat_Modeling_Cheat_Sheet.md),
[Input Validation Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Input_Validation_Cheat_Sheet.md),
and [SQL Injection Prevention Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.md).

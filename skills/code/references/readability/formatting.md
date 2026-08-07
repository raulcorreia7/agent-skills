# Code Formatting

The repository formatter is authority. Use this leaf only when wrapping or
layout still needs judgment and the repository has no sufficient formatter
rule. Treat a numeric line-length setting as a layout constraint, not a reason
to rewrite otherwise clear code.

## Earned Line Breaks

Keep an expression on one line when it is easy to scan. Do not change syntax,
APIs, string construction, or value extraction only to cross a column target.
Do not reflow untouched code for that target. Let the configured formatter own
ordinary wrapping. If an enforced rule still requires a manual break, wrap at a
structural boundary without changing behavior. Without an enforced rule, wrap
only when the resulting structure is easier to read. Preserve an indivisible
line when wrapping creates a worse shape.

When an expression needs work:

1. Introduce a meaningful value when it names a concept, phase, or failure
   point.
2. Otherwise wrap at a structural boundary.
3. Use the formatter's continuation indentation.

Keep short cohesive chains on one line. Split a long chain at a meaningful
checkpoint. Use a vertical chain only for one fluent pipeline when no useful
checkpoint exists.

```text
response = await client.get(endpoint)
payload = await response.json()
customer = customer_schema.parse(payload)

return customer
```

## Stable Shapes

- Keep a complete call or signature on one line when clear. When it must wrap,
  use the formatter's stable multi-line form instead of partial wrapping.
- Keep a short collection on one line. Use one item or property per line for a
  multi-line collection and follow the language trailing-comma convention.
- Avoid manually aligned columns. Let the formatter own indentation and
  spacing.

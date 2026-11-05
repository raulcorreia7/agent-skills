# Code Formatting

A fallback for layout that no formatter or linter decides. When the
repository's formatter runs, it owns wrapping, indentation, and spacing; match
its output and the surrounding code. Treat a line-length setting as a layout
limit, not a reason to rewrite otherwise clear code.

## Earned Line Breaks

Keep an expression on one line when it's easy to scan. Don't change syntax,
APIs, string construction, or value extraction only to get under a column
limit, and don't reflow untouched code for it. When an enforced rule still
needs a manual break, wrap at a structural boundary without changing behavior.
Without one, wrap only when the result is easier to read, and keep an
indivisible line whole when wrapping would make it worse.

When an expression needs work:

1. Introduce a named value when it names a concept, phase, or failure point.
2. Otherwise wrap at a structural boundary.
3. Use the formatter's continuation indentation.

Keep short cohesive chains on one line. Split a long chain at a meaningful
checkpoint. Use a vertical chain only for one fluent pipeline with no useful
checkpoint.

```text
response = await client.get(endpoint)
payload = await response.json()
customer = customer_schema.parse(payload)

return customer
```

## Stable Shapes

- Keep a complete call or signature on one line when clear. When it must wrap,
  use the formatter's stable multi-line form, not partial wrapping.
- Keep a short collection on one line. A multi-line collection gets one item
  or property per line and follows the language's trailing-comma convention.
- Align a column inside one short, stable group where it helps scanning:
  related declarations or assignments, a table of constants, or map entries.
  Separate each group with a blank line and align it on its own.
- Keep diffs small. Don't realign untouched lines, and skip alignment when one
  rename or new entry would realign the whole group.

```text
timeout_ms  = 5_000
retry_limit = 3
backoff     = EXPONENTIAL

log_level = INFO
```

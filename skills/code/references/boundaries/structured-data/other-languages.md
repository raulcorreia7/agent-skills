# Other Structured Languages

Apply this leaf to filters, expressions, templates, policy languages, search
syntax, command fragments, or another DSL without a dedicated contract.

- Identify the grammar and version before construction or evaluation.
- Prefer an AST, typed builder, parser, or restricted interpreter. Keep values
  separate from operators, names, paths, functions, control forms, and code.
- Expose the smallest useful language surface. Allowlist structural choices and
  bound nesting, expression size, evaluation time, memory, and result size.
- Treat escaping as grammar-specific. A quoting rule from another language is
  not a substitute for parsing or binding.
- Verify the parsed tree and evaluator behavior with the real implementation,
  including malformed input, unsupported constructs, and resource limits.

Example—translate an owned filter model into AST nodes:

```json
{
  "operator": "and",
  "operands": [
    { "field": "status", "operator": "eq", "value": "active" },
    { "field": "createdAt", "operator": "gte", "value": "2026-01-01" }
  ]
}
```

The boundary validates each field/operator pair and compiles the value as data;
it does not evaluate caller-supplied expression text.

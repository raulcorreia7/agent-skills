# Troubleshooting

Use the smallest diagnostic that explains an unexpected match or miss:

1. Inspect the parsed pattern with
   `ast-grep run --lang <language> --pattern '<pattern>' --debug-query=ast <path>`.
2. Confirm that each `kind` is a node kind from the selected language's
   Tree-sitter grammar.
3. Add `stopBy: end` when a relational rule must search beyond an immediate
   neighbor.
4. Confirm that a metavariable is the complete content of its syntax node.
5. Reduce a complex rule to one positive matcher, verify it, and add constraints
   one at a time. Use `all` when metavariable-dependent rules need a guaranteed
   evaluation order.

For example, if a function with a nested `await` is missed, make descendant
traversal explicit:

```yaml
kind: function_declaration
has:
  pattern: await $EXPR
  stopBy: end
```

Keep the smallest rule that accounts for the expected match and near miss.

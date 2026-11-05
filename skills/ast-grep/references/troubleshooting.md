# Troubleshooting

Use the smallest diagnostic that explains an unexpected match or miss:

1. Inspect the parsed pattern with `--debug-query=ast` (`cli.md`).
2. Confirm that each `kind` is a node kind from the selected language's
   Tree-sitter grammar.
3. When a relational rule misses a nested target, check its traversal
   (`relational-rules.md` › Traversal).
4. Confirm that a metavariable is the complete content of its syntax node.
5. Reduce a complex rule to one positive matcher, verify it, and add constraints
   one at a time. Use `all` when metavariable-dependent rules need a guaranteed
   evaluation order.

Keep the smallest rule that accounts for the expected match and near miss.

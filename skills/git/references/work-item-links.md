# Work-Item Links

Treat work-item IDs, issue IDs, story IDs, and URLs as traceability metadata,
not commit scopes.

```text
docs(api): add authentication examples

Refs: #1234
```

```text
fix(auth): reject expired tokens

Fixes #1234
```

Use neutral `Refs:` wording for related work. Use closing syntax only when the
change should actually close or resolve the item.

- Put generic URLs in a PR body or commit footer, not a Conventional Commit
  header.
- Preserve any required platform or team title prefix. Keep the remaining title
  readable.

Suggest a better reference when useful. Do not rewrite history without explicit
approval.

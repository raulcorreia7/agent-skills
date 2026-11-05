# Work-Item Links

Work-item, issue, and story IDs and URLs are traceability metadata, not commit
scopes. They go in the commit footer or the PR body, never the header.

```text
docs(api): add authentication examples

Refs: #1234
```

```text
fix(auth): reject expired tokens

Fixes #1234
```

- Use neutral `Refs:` for related work. Use a closing keyword only when the
  change should close or resolve the item.
- Keep any required platform or team title prefix, and keep the rest of the
  title readable.

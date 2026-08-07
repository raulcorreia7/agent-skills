# Python Contracts

Repository configuration, locked development tools, package layout, and
framework conventions take precedence.

## Types And Contracts

- Treat HTTP input, parsed JSON, environment values, files, messages, and
  provider responses as `object` until a parser or guard validates them.
- Prefer typed immutable values, dataclasses, enums, protocols, and explicit
  return types where they express a domain contract. Avoid `Any`, broad casts,
  mutable defaults, and global mutable state.
- Catch a specific exception only where the boundary can recover, translate, or
  add useful context. Preserve the cause with `raise DomainError(...) from exc`.
- Use context managers for owned resources. Keep async I/O async and preserve
  the framework's cancellation contract.

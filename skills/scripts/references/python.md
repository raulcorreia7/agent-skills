# Python Scripts

## Process and Entrypoint Behavior

- Keep import-time behavior free of filesystem, network, process, or environment
  mutation.
- Pass subprocess arguments as a sequence. Handle return codes explicitly. Use
  `shell=True` only when shell syntax is required and all inputs are controlled.
- Return an exit code from `main()` and raise `SystemExit` at the entrypoint:

```python
from collections.abc import Sequence

def main(argv: Sequence[str] | None = None) -> int:
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

## Verification

Use the repository's aggregate check first. For a Ruff-owned repository, a
compact read-only sequence is:

```bash
ruff format --check path/to/script.py
ruff check path/to/script.py
```

Then run the one configured strict type checker and the smallest existing test
that owns the behavior. Do not run multiple type checkers or linters unless the
repository intentionally requires each. Preserve the configured Python target
and rule selection; do not enable preview rules or one-off security selectors.

When the repository uses uv, verify lock consistency without updating it:

```bash
uv lock --check
```

Use the selected package manager's equivalent locked check elsewhere. Run a
configured dependency audit only with required network approval. For a uv
version that supports auditing, keep the lock immutable:

```bash
uv audit --locked
```

Never use automatic audit fixes or dependency upgrades as verification. Do not
create tests or expand test scope unless the user asks.

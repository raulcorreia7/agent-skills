# Python Quality Gates

Copy these settings into `pyproject.toml` and CI. Do not treat this leaf as
agent memory. Repository configuration and locked development tools take precedence. In a
new production package, make `pyproject.toml` the single project-level source
of truth. Set `project.requires-python` to the lowest supported runtime. Make
Ruff and the selected type checker target that version. Do not add Black, isort,
Flake8, Pylint, Bandit, or a second required type checker when Ruff, Pyright,
and the existing test runner already own those concerns.

## Strict Baseline

Use Ruff for formatting, imports, linting, and its stable security rules. Keep
the selected rule set explicit so a tool upgrade does not silently create a new
gate. Leave preview mode disabled. This is a strict, practical starting point,
not an instruction to enable Ruff's unstable `ALL` selector.

```toml
[project]
requires-python = ">=3.11" # Replace with this package's supported minimum.

[tool.ruff]
target-version = "py311" # Match the supported minimum above.
preview = false

[tool.ruff.lint]
select = [
  "E", "F", "I", "N", "UP", "B", "A", "ANN", "ARG", "BLE", "C4",
  "DTZ", "EM", "EXE", "ICN", "ISC", "PERF", "PGH", "PIE", "PT", "PTH",
  "RET", "RSE", "RUF", "S", "SIM", "TID", "TRY",
]
ignore = ["E501"] # The formatter owns line wrapping.

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
line-ending = "lf"
```

Choose one project-wide type-checking gate. Prefer Pyright when its strict mode
fits the repository and editor. Prefer Mypy only when the repository already
uses its plugins or semantics. Do not make both mandatory for ordinary code.

```toml
# pyproject.toml: Pyright option
[tool.pyright]
include = ["src", "tests"]
exclude = ["build", "dist"]
pythonVersion = "3.11" # Match the supported minimum.
typeCheckingMode = "strict"

# pyproject.toml: Mypy alternative (use instead of the Pyright section)
[tool.mypy]
files = ["src", "tests"]
strict = true
warn_unused_configs = true
```

Keep type-checker excludes rare and specific. Fix missing library types with
maintained stubs or a narrow local stub before suppressing a diagnostic. An
unavoidable suppression names the exact rule and records its upstream issue or
compatibility boundary.

For pytest projects, make configuration and marker mistakes fail. Register each
intentional custom marker rather than accepting unknown ones.

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
strict = true
addopts = "-ra"
markers = ["integration: requires a real external integration"]
```

## Sources

- [Ruff configuration](https://docs.astral.sh/ruff/configuration/) and
  [Ruff rule selection](https://docs.astral.sh/ruff/linter/).
- [Pyright configuration](https://github.com/microsoft/pyright/blob/main/docs/configuration.md)
  and [Mypy strict mode](https://mypy.readthedocs.io/en/stable/getting_started.html).
- [pytest strictness](https://docs.pytest.org/en/latest/reference/reference.html)
  and [Python packaging](https://packaging.python.org/en/latest/discussions/setup-py-deprecated/).

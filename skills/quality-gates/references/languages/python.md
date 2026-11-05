# Python Quality Gates

In a new package, make `pyproject.toml` the single source of project
configuration. Set `project.requires-python` to the lowest supported runtime
and make Ruff and the type checker target that version. Ruff, one type
checker, and the test runner cover formatting, imports, linting, and stable
security rules, so leave out Black, isort, Flake8, Pylint, Bandit, and a second
required type checker.

## Strict baseline

Keep the selected Ruff rule set explicit so a tool upgrade does not add a new
gate unannounced. Leave preview mode off and avoid the unstable `ALL`
selector.

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

Choose one project-wide type checker. Prefer Pyright when its strict mode fits
the repository and editor; prefer Mypy only when the repository already relies
on its plugins or semantics.

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
unavoidable suppression names the exact rule and its upstream issue or
compatibility boundary.

For pytest, make configuration and marker mistakes fail, and register each
intentional custom marker.

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
strict = true
addopts = "-ra"
markers = ["integration: requires a real external integration"]
```

## Gate commands

```text
ruff format --check .
ruff check .
pyright                 # or: mypy
pytest
```

Sources: `python` in [sources.yml](../sources.yml).

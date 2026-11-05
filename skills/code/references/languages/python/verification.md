# Python Verification

Run repository scripts first. A minimal gate for a Python package
using the baseline is below.

These run offline:

```text
ruff format --check .
ruff check .
pyright                 # or: mypy
pytest
python -m pip check
```

These fetch build dependencies or vulnerability data; get approval before
running them:

```text
python -m build          # When the project publishes a distribution.
python -m twine check --strict dist/*
pip-audit --locked .     # Audit the committed lock or pyproject resolution.
```

Install from the committed lock file in CI, and run the checks with the
project-managed tool versions. `pip-audit` is a dependency-vulnerability gate.
It is not a substitute for source analysis. Do not use `--fix` in verification.

## Sources

- [pip-audit](https://github.com/pypa/pip-audit).

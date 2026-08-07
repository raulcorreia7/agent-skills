# Python Verification

Run repository scripts first. A minimal high-quality gate for a Python package
using the baseline is:

```text
ruff format --check .
ruff check .
pyright                 # or: mypy
pytest
python -m build          # When the project publishes a distribution.
python -m twine check --strict dist/*
python -m pip check
pip-audit --locked .     # Audit the committed lock or pyproject resolution.
```

Install from the committed lock file in CI, and run the checks with the
project-managed tool versions. `pip-audit` is a dependency-vulnerability gate.
It is not a substitute for source analysis. Do not use `--fix` in verification.

## Sources

- [pip-audit](https://github.com/pypa/pip-audit).

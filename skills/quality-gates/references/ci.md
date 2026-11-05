# CI Gates

A CI gate runs the same commands as the local gate, with the same locked tool
versions, and fails the pipeline when a gate fails. Prefer calling the
repository's task runner (`make check`, `uv run poe check`, `npm run check`)
over repeating each command in YAML, so local runs and CI cannot drift.

## Job shape

- Trigger on pull requests or merge requests and on the default branch.
- Pin each third-party action by release tag, or by full commit SHA when the
  repository pins that way. Read the current tag from the action's releases
  page; that lookup is a network fetch.
- Grant least privilege: `permissions: contents: read` at workflow level, and
  widen it only in the job that needs more.
- Use `pull_request`, not `pull_request_target`, for jobs that run PR code;
  the latter runs with the base repository's secrets.
- Install from the lock file (`uv sync --locked`, `npm ci`, `cargo --locked`,
  `dotnet restore --locked-mode`) and cache the package store keyed on the lock
  file.
- Run checks in check mode (`--check`, `--verify-no-changes`); CI never
  autofixes.
- Leave `continue-on-error` (GitHub) and `allow_failure` (GitLab) off for a
  gate. Adding either is a relaxation.
- When the repository uses pre-commit, run `pre-commit run --all-files` so CI
  checks every file, not only staged ones.

## GitHub Actions

```yaml
# .github/workflows/check.yml
name: check
on:
  pull_request:
  push:
    branches: [main]
permissions:
  contents: read
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5          # pin: tag or full SHA
      - uses: actions/setup-python@v6
        with:
          python-version-file: pyproject.toml
          cache: pip
      - run: python -m pip install -r requirements-dev.lock
      - run: ruff format --check .
      - run: ruff check .
      - run: pyright
      - run: pytest
```

To make the job a required check, branch protection or a ruleset must list it.
That is a repository setting outside the YAML and an approval-gated change.

## GitLab CI

```yaml
# .gitlab-ci.yml
check:
  image: python:3.11-slim                  # pin the image tag the project supports
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
  cache:
    key:
      files: [requirements-dev.lock]
    paths: [.cache/pip]
  variables:
    PIP_CACHE_DIR: $CI_PROJECT_DIR/.cache/pip
  script:
    - python -m pip install -r requirements-dev.lock
    - ruff format --check .
    - ruff check .
    - pyright
    - pytest
```

Merge-request pipelines must succeed before merge only when the project setting
requires it; changing that setting is approval-gated.

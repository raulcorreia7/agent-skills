# Pull Requests

Use the repository PR template and title rules. When neither exists, use a
concise Conventional Commit-style title that could serve as the final squash or
merge commit:

```text
type: subject
type(scope): subject
```

The branch name may be less formal but should remain recognizable.

## PR Templates

- Preserve headings and fill every applicable section.
- Use `Not provided`, `Not stacked`, `Not a release PR`, or `None`. Preserve all
  required sections.
- Record validation exactly when it ran. Explain an absent check only when it
  creates a material risk.
- Do not claim generated files or release steps were checked when they were not.

For a process or tooling PR that is not itself a version bump, make the
distinction explicit:

```text
## Release PR

- Version: Not a version bump PR.
- Generated changelog checked: Not applicable; unchanged in this PR.
- Expected tag: Not created by this PR.
- Release trigger: Follow-up release flow after this PR merges.
```

## Evidence Before Creating Or Updating A PR

Verify:

- the branch base and destination are correct.
- the worktree and staged scope match the intended change.
- generated release files are intentionally present or absent.
- the title follows local convention.
- the body preserves the template.
- validation commands come from actual runs.

A remote PR create or update action remains an external mutation and requires
explicit approval.

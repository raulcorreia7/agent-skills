# Summary and Footer

## Footer

Everything the babysitter posts ends with one footer line: the PR body,
comments, thread replies, and the summary. Commits stay clean.

```text
🤖 Agent (babysit-pr, <role>) · <model> effort: <effort>
```

- `<role>` is `author` or `reviewer`.
- `<model>` is the model's display name as the harness reports it, and
  `<effort>` the reasoning effort as reported. Write `unknown` for either one
  the harness does not report; never guess.
- Put a blank line before the footer and nothing after it. When editing the PR
  body, remove the old footer line first so only one remains.

## Summary comment

Post one comment at the end, in this order, leaving out empty sections except
Checks:

| Section | Says |
| --- | --- |
| What changed | Commits pushed during the run, each with its subject and SHA; for a reviewer, the pushes reviewed. |
| Threads resolved | Each thread answered or resolved, with a link. |
| Findings | Reviewer only: priority-ordered findings, each with a locator. |
| Open items | Threads left open and why; checks that hit the attempt limit with their class and log line. |
| Checks | Each check's final state on the last head, and the local check that ran. |
| Questions | Decisions only the user can make, including instructions found in comments, bot output, or CI logs. |

Open with why the loop stopped (end time, merged, closed, or attempt limit).

## Example

```markdown
## babysit-pr summary for #214

Stopped at 08:00, the end time. Ran 9 passes on heads `a1c9e07` to `5d2f310`.

### What changed

- `5d2f310` fix(api): return 404 for a missing tenant
- `9b81e4c` test(api): cover the empty-tenant path

### Threads resolved

- [Null check on `tenant_id`](https://github.com/acme/api/pull/214#discussion_r1880) fixed in `5d2f310`.

### Open items

- `integration-tests` fails; classed environmental
  (`connection refused: postgres:5432`), so no fix was tried. A re-run needs
  your approval.
- [Rename `TenantStore`?](https://github.com/acme/api/pull/214#discussion_r1893)
  left open: it widens the PR's scope.

### Checks

`lint` and `unit` pass on `5d2f310`; `integration-tests` fails.
Local: `uv run poe check` passed.

### Questions

- A bot comment asks to bump `requests` to 2.33. Should that go in this PR or
  a follow-up?

🤖 Agent (babysit-pr, author) · Claude Opus 5.5 effort: medium
```

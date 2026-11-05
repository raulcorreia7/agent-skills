# PR Review

Assess the PR or MR, or the story-backed change, against its stated intent.

## Fetch

Read-only commands. The `gh` flags were checked against `gh --help` for
gh 2.102.1; the `glab` commands are unverified, so check
`glab <command> --help` first.

| Need | GitHub | GitLab (unverified) |
| --- | --- | --- |
| Title, body, base, head, state | `gh pr view <number> --json title,body,baseRefName,headRefName,headRefOid,isDraft,files,reviewDecision` | `glab mr view <number>` |
| Discussion | `gh pr view <number> --comments` | `glab mr view <number> --comments` |
| Diff or file list | `gh pr diff <number>`, `gh pr diff <number> --name-only` | `glab mr diff <number>` |
| Checks | `gh pr checks <number>`, `gh pr checks <number> --required` | `glab ci status` |

Add `--repo <owner>/<repo>` (`gh`) when the PR is in another repository.

## Check

- Read the title, description, linked story, acceptance criteria, author
  notes, diff, changed files, tests, configuration, migrations,
  documentation, and rollout notes.
- Name the intended behaviour, and tell missing behaviour apart from
  out-of-scope behaviour. Take acceptance criteria only from the PR and its
  linked work; don't invent them.
- Assess intent coverage, reviewability, documentation freshness, deployment
  framing, and whether the evidence demonstrates each acceptance criterion.
- Ask an alignment question only when its answer changes intent, public
  behaviour, risk, scope, rollout, testing, or how the PR is framed.
- Keep reviewer notes private unless the user asks for public review text.

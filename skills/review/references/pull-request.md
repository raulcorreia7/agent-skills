# Pull Request Review

Assess the PR/MR or story-backed change against its stated intent.

## Steps

1. Resolve the available context. Check the title, description, linked story,
   acceptance criteria, author notes, diff, changed files, tests, configuration,
   migrations, documentation, and rollout notes.
2. Identify intended behavior and distinguish missing behavior from
   out-of-scope behavior. Never invent acceptance criteria.
3. Assess intent coverage, reviewability, documentation freshness, deployment
   framing, and whether evidence demonstrates each acceptance criterion.
4. Ask alignment questions only when an answer changes intent, public behavior,
   risk, scope, rollout, testing, or PR framing.
5. Draft concise private reviewer notes and produce public review comments only
   when requested.

## Output

Use this order and omit empty sections:

1. **Verdict:** `approve`, `comment`, `request changes`, or `not reviewable`,
   with a one-sentence rationale. Treat the verdict as a recommendation unless
   the user separately approves the post.
2. **Findings:** `P0`-through-`P3` ordered findings with precise locations,
   evidence, impact, and smallest fixes.
3. **Questions:** Material intent or acceptance decisions and the recommended
   default for each.
4. **Coverage:** Requested outcome, acceptance coverage, documentation
   freshness, and unverified scope.
5. **Checks:** Evidence, commands, and results when they informed the review.
6. **Review text:** Copy-pasteable public comments only when requested.
   Otherwise private reviewer notes.
7. **Residual risk:** Assumptions, unreviewed surfaces, rollout concerns, and
   confidence limits.

When there are no findings, say so explicitly and still report checks and
residual risk.

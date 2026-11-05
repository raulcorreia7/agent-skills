---
name: ast-grep
description: "Finds syntax-aware code structures and authors ast-grep rules. Use when a structural search or ast-grep rule is the primary deliverable and text search cannot reliably express the syntax or AST relationship."
---

# ast-grep

## Job

Write the smallest ast-grep pattern or rule that finds the requested
structure, prove it on a match and a near miss, then run it on the intended
paths. When a correction is a repeatable syntax pattern, propose a scan rule
for the product repository; add it only when an edit is requested.

The lightest path is a direct pattern on existing code. Escalate to a YAML
rule only when a pattern can't express the structure, and to a retained rule
file with tests only when the task keeps the rule.

## Steps

1. Identify the language, target structure, required and excluded cases,
   search paths, and output. Use text search when it expresses the request
   reliably. Otherwise confirm the executable with `ast-grep --version`; when
   it's missing, report the blocked search and ask whether installing it is in
   scope. Complete when text search is chosen, ast-grep answers `--version`,
   or the blocked search is reported.
2. Find at least one expected match and one near miss in supplied or
   repository code. When there isn't one, write a small fixture in the
   system's temporary directory and remove it after testing. Complete when a
   match and a near miss exist on disk.
3. Start with a direct pattern (`references/cli.md` has the commands). When a
   pattern can't express the structure, read `references/scan-rules.md`, then
   each concern that applies:
   - `references/relational-rules.md` for ancestor, descendant, or sibling
     relationships;
   - `references/composite-rules.md` for conjunction, alternatives,
     exclusions, or utility-rule reuse;
   - `references/metavariables.md` for capture equality, unnamed nodes, or
     multi-node captures.

   Read `references/troubleshooting.md` only after an unexpected match or
   miss. Complete when the pattern or rule matches every expected example and
   no near miss.
4. For a rule file the task keeps, add `valid` and `invalid` cases and run
   `ast-grep test` (`references/cli.md`). Complete when the test passes, or
   when no rule file is kept.
5. Scan only the intended paths, scoped with globs and read as compact JSON
   when the result set is large. Complete when the scoped results, the
   expected match, the near miss, and known limits are accounted for.

## Flow

```text
input ← language, structure, include and exclude cases, paths
text search reliable? yes → use it, stop | no → ast-grep --version, or report blocked
examples ← repository code | temp fixture (match + near miss)
loop: pattern | rule → test on examples → refine → until every match and no near miss
rule file kept? yes → ast-grep test | no → continue
scan scoped paths → report matches and limits
stop: scoped results, the match, the near miss, and limits accounted for
```

## Gotchas

- `inside` and `has` stop at the nearest node by default, so a nested target
  is missed. See `references/relational-rules.md` › Traversal for `stopBy`.
- A metavariable embedded in other text, such as `obj.on$EVENT`, is literal
  text, not a capture.
- `--json` needs `=` for its style; `--json compact` reads `compact` as a
  path.

## Guardrails

- Rewriting files (`--update-all`, `--interactive`) happens only for a
  codemod or edit the user asked for. Fixtures in the system's temporary
  directory are fine.
- Infer absence only from a rule tested on a match and a near miss.
- Read `references/sources.yml` only to audit or update the curated upstream
  material, and `references/LICENSE.txt` only for maintenance,
  redistribution, or a license audit.

## Composition

- Use `code` or `refactor` when a validated search leads to requested code
  changes.

## Output

- Search intent and language
- The pattern or rule, and its test result when one was kept
- Commands and scoped paths
- Matches, limits, and follow-up refinements

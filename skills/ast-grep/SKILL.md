---
name: ast-grep
description: "Finds syntax-aware code structures and authors ast-grep rules. Use when a structural search or ast-grep rule is the primary deliverable and text search cannot reliably express the syntax or AST relationship."
---

# ast-grep

## Job

Create the smallest reliable ast-grep pattern or rule for the structural search
request. Verify it on representative code. Then run it against the intended
scope. When a correction is a repeatable syntax pattern, propose a scan rule for
the product repository instead of growing skill prose; add it only when an edit
is requested.

## Steps

1. Identify the language, target structure, required and excluded cases, search
   paths, and desired output. Use text search when it expresses the request
   reliably. Otherwise, confirm the executable with `ast-grep --version`; if it
   is unavailable, report the blocked structural search and ask whether
   installation is in scope. Complete when text search is chosen, ast-grep
   answers `--version`, or the blocked search is reported.
2. Use supplied or repository code when it contains at least one expected
   match and one near miss. Otherwise, build a small fixture in the operating
   system temporary directory with those examples, then remove it after the
   test. Complete when at least one expected match and one near miss exist on
   disk.
3. Start with a direct pattern:
   `ast-grep run --lang <language> --pattern '<pattern>' <path>`. When a direct
   pattern is insufficient and a YAML scan rule is necessary, read
   [scan rules](references/scan-rules.md). Then read each additional rule
   concern that applies:
   - [relational rules](references/relational-rules.md) for ancestor,
     descendant, or sibling relationships;
   - [composite rules](references/composite-rules.md) for conjunction,
     alternatives, exclusions, or utility-rule reuse;
   - [metavariables](references/metavariables.md) for capture equality,
     unnamed nodes, or multi-node captures.

   Prefer `ast-grep scan --inline-rules '<rule-yaml>' <path>` for an ad hoc
   rule; use `ast-grep scan --rule <rule.yml> <path>` only for a rule file the
   task needs to retain. For relational `inside` and `has` rules, use
   `stopBy: end` unless a narrower traversal is intentional. Inspect the parsed
   syntax tree when node kinds or pattern context are uncertain, and read
   [troubleshooting](references/troubleshooting.md) only after a pattern or rule
   produces an unexpected match or miss. Complete when the pattern or rule
   matches every expected example and no near miss.
4. Scan only the intended paths. Complete when the tested rule accounts for the
   expected match, the near miss, the scoped results, and known limitations.

## Flow

```text
target ← language, structure, include/exclude, paths
text search reliable? yes → use it, stop | no → check ast-grep, or report blocked
examples ← repository code or temp fixture (match + near miss)
loop: pattern or rule → test on examples → refine → until match and no near miss
scan intended paths → report matches + limits
stop: scoped results and limitations are accounted for
```

## Guardrails

- Infer absence only from a tested rule with positive and negative examples.
- Keep the result read-only unless the user explicitly requests a codemod or
  edit; fixtures in the operating system temporary directory are allowed.
- Read `references/sources.yml` only to audit or update the curated upstream
  material. Read `references/LICENSE.txt` only for maintenance,
  redistribution, or a license audit.

## Composition

- Use `code` or `refactor` when a validated search leads to requested code
  changes.

## Output

- Search intent and language
- Pattern or rule used
- Commands and scoped paths
- Matches, limitations, and follow-up refinements

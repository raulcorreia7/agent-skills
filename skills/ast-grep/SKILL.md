---
name: ast-grep
description: Finds syntax-aware code structures and authors ast-grep rules. Use when text search cannot reliably express the required syntax or AST relationship.
---

# ast-grep

## Job

Create the smallest reliable ast-grep pattern or rule for the structural search
request. Verify it on representative code. Then run it against the intended
scope. When a correction is a repeatable syntax pattern, commit a scan rule in
the product repository instead of growing skill prose.

## Steps

1. Identify the language, target structure, required and excluded cases, search
   paths, and desired output.
2. Use text search when it expresses the request reliably. Otherwise, confirm
   the executable with `ast-grep --version`. If it is unavailable, report the
   blocked structural search and ask whether installation is in scope.
3. Use supplied or repository code when it contains at least one expected
   match and one near miss. Otherwise, build a small fixture in the operating
   system temporary directory with those examples, then remove it. Prefer an
   inline rule for an ad hoc scan; retain a rule file only when it is needed.
4. Start with a direct pattern:
   `ast-grep run --lang <language> --pattern '<pattern>' <path>`. When a direct
   pattern is insufficient and a YAML scan rule is necessary, read
   [scan rules](references/scan-rules.md). Then read only the additional rule
   concern that applies:
   - [relational rules](references/relational-rules.md) for ancestor,
     descendant, or sibling relationships;
   - [composite rules](references/composite-rules.md) for conjunction,
     alternatives, exclusions, or utility-rule reuse;
   - [metavariables](references/metavariables.md) for capture equality,
     unnamed nodes, or multi-node captures.
   Use `ast-grep scan --inline-rules '<rule-yaml>' <path>` for an ad hoc rule or
   `ast-grep scan --rule <rule.yml> <path>` for a retained rule file.
5. Inspect the parsed syntax tree when node kinds or pattern context are
   uncertain. Read [troubleshooting](references/troubleshooting.md) only after
   a pattern or rule produces an unexpected match or miss.
6. Test the rule against the examples. For relational `inside` and `has` rules,
   use `stopBy: end` unless a narrower traversal is intentional.
7. Scan only the intended paths. Finish when the tested rule accounts for the
   expected match, the near miss, the scoped results, and known limitations.

## Guardrails

- Infer absence only from a tested rule with positive and negative examples.
- Keep the result read-only unless the user explicitly requests a codemod or
  edit.
- Read `references/sources.yml` only to audit or update the curated upstream
  material. Read `references/LICENSE.txt` only for maintenance,
  redistribution, or a license audit.

## Composition

When a validated search leads to requested code changes, compose with `code` or
`refactor` when available. Keep structural search useful on its own when those
skills are absent.

## Output

- Search intent and language
- Pattern or rule used
- Commands and scoped paths
- Matches, limitations, and follow-up refinements

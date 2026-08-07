# Scan Rules

Use a complete configuration mapping with
`ast-grep scan --rule <rule.yml> <path>`:

```yaml
id: no-console-log
language: JavaScript
severity: warning
message: Avoid console.log in production code.
rule:
  pattern: console.log($$$ARGS)
```

For an ad hoc scan, pass the same complete mapping inline:

```text
ast-grep scan --inline-rules '{id: no-console-log, language: JavaScript, rule: {pattern: "console.log($$$ARGS)"}}' <path>
```

The remaining YAML blocks in this reference are nested fragments for the
complete mapping's `rule` key.

## Rule Object

A rule object must have at least one positive matcher, such as `kind` or
`pattern`. A node must satisfy every field in one rule object, which gives an
implicit logical AND. Use an explicit `all` rule when metavariable matching
depends on evaluation order.

## Pattern

A string pattern matches one syntax node and can contain metavariables:

```yaml
pattern: console.log($ARG)
```

Use an object pattern when parsing needs context or the match must select one
part of a larger pattern:

```yaml
pattern:
  context: class { $F }
  selector: field_definition
```

`strictness` controls the matching algorithm. Supported values are `cst`,
`smart`, `ast`, `relaxed`, and `signature`.

```yaml
pattern:
  context: foo($BAR)
  strictness: relaxed
```

## Other Atomic Rules

- `kind` matches a Tree-sitter named node kind, such as `call_expression`.
- `regex` applies a Rust regular expression to the complete text of a node.
- `nthChild` selects a 1-based named-child position. It accepts a number, an
  An+B string such as `2n+1`, or an object with `position`, optional `reverse`,
  and optional `ofRule`.
- `range` selects a character range. Its `start` is inclusive and `end` is
  exclusive; each has 0-based `line` and `column` fields.

Example nested fragments:

```yaml
kind: call_expression
```

```yaml
nthChild:
  position: 1
  reverse: true
```

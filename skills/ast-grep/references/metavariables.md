# Metavariables

Metavariables are pattern placeholders for syntax nodes.

## Named Nodes

`$VAR` captures one named node. Valid forms include `$META`, `$META_VAR`, and
`$_`; lowercase names, numeric names, and kebab-case names are invalid.

Reusing a capture requires equal syntax: `$A == $A` matches `a == a` but not
`a == b`.

## Unnamed Nodes

`$$VAR` captures one unnamed node, such as an operator or punctuation token:

```yaml
kind: binary_expression
has:
  field: operator
  pattern: $$OP
```

## Multiple Nodes

`$$$VAR` captures zero or more nodes non-greedily. For example,
`console.log($$$ARGS)` matches calls with any number of arguments.

## Non-Capturing Variables

A name that starts with an underscore is not captured. Repeated uses can match
different content. For example, `$_FUNC($_FUNC)` matches both `test(a)` and
`testFunc(1 + 1)`.

## Detection Constraints

- Use exact `$A`, `$$B`, or `$$$C` syntax.
- Make the metavariable the complete content of its syntax node.
- Do not embed a metavariable in other text. Patterns such as `obj.on$EVENT`,
  `"Hello $WORLD"`, `a $OP b`, and `$jq` do not create metavariables.

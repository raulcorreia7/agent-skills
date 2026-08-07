# Relational Rules

Relational rules filter a target node by its position relative to other nodes.

## Ancestors And Descendants

`inside` requires the target to be inside a matching ancestor:

```yaml
inside:
  pattern: class $C { $$$ }
  stopBy: end
```

`has` requires the target to have a matching descendant:

```yaml
has:
  pattern: await $EXPR
  stopBy: end
```

`inside` and `has` can use `field` to restrict which sub-node participates in
the relationship.

## Siblings

`precedes` requires a matching node after the target. `follows` requires a
matching node before the target. Both accept `stopBy` but not `field`.

## Traversal

`stopBy` controls traversal:

- `neighbor` is the default and stops when the immediately surrounding node
  does not match.
- `end` searches to the end of the direction: root for `inside`, leaf for
  `has`, and the end of sibling traversal for `precedes` or `follows`.
- A rule object stops when a surrounding node matches that rule, inclusive.

Use `stopBy: end` unless a narrower traversal is intentional.

## Examples

Find functions that contain an await expression:

```yaml
kind: function_declaration
has:
  pattern: await $EXPR
  stopBy: end
```

Find `console.log` calls inside class methods:

```yaml
pattern: console.log($$$)
inside:
  kind: method_definition
  stopBy: end
```

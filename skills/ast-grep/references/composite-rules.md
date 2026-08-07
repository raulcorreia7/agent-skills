# Composite Rules

Use composite rules when one target needs multiple conditions, alternatives,
an exclusion, or a reusable utility rule.

## All

`all` matches only when every nested rule matches. It also guarantees rule
evaluation order when later rules depend on metavariables captured earlier.

```yaml
all:
  - kind: call_expression
  - pattern: console.log($ARG)
```

## Any

`any` matches when at least one nested rule matches:

```yaml
any:
  - pattern: console.log($$$)
  - pattern: console.warn($$$)
  - pattern: console.error($$$)
```

## Not

`not` excludes a target that matches its nested rule:

```yaml
not:
  pattern: console.log($ARG)
```

## Matches

`matches` takes a utility-rule ID and succeeds when that predefined utility
rule matches.

## Combined Example

Find async functions that use `await` but have no `try` and `catch` block:

```yaml
all:
  - kind: function_declaration
  - has:
      pattern: await $EXPR
      stopBy: end
  - not:
      has:
        pattern: try { $$$ } catch ($E) { $$$ }
        stopBy: end
```

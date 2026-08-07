# Directives And Generated Boundaries

Classify a tool-consumed construct before editing it:

1. **Human explanation:** rationale or a constraint ignored by the parser.
2. **Public help:** discoverable command, function, parameter, input, output,
   error, or example documentation.
3. **Tool directive:** parser selection, prerequisite, source mapping,
   suppression, coverage, formatter, type-checker, or generator instruction.
4. **Generated boundary:** ownership, source, regeneration command, or
   do-not-edit notice.
5. **Commented-out behavior:** disabled code or configuration with no active
   contract.

Do not change category accidentally. A directive can affect validation,
generated output, or build behavior.

## Suppressions

- Fix the issue or use a narrow repository-level exception when practical.
- Give an inline suppression its rule and rationale or removal condition.
- Reject blanket disables. Check for stale suppressions when the tool supports
  that check.

Example:

```javascript
// eslint-disable-next-line camelcase -- Provider payload requires this key.
const user_name = payload.user_name;
```

## Generated Files

State only ownership, regeneration location, and overwrite behavior in a
generated header. Do not hand-edit generated content to change its comments.
Maintain the source schema, template, configuration, or generator instead.

Example:

```text
# Generated from api/schema.yaml by tools/generate_client.py; changes are overwritten.
```

Validate a changed directive with its owning documentation, linter, compiler,
formatter, generator, or build tool when available. Report semantics that the
owning tool could not verify.

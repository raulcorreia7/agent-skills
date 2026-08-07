# Code Structure

Treat nearby code as evidence, not as a reason to reproduce accidental
structure. Improve the smallest complete block touched by the behavior change.

## Semantic Paragraphs

Write semantic paragraphs. Keep statements that perform one cohesive operation
together. Add one blank line when code changes purpose, subject, or phase.

Common phases include validation, preparation, core behavior, side effects,
and result construction. Do not add blank lines to a function with one cohesive
phase.

Place one blank line before a terminal `return`, `throw`, `yield`, or equivalent
when statements in the same block prepare that outcome. Keep a short guard
block compact.

```text
first_name = user.first_name.strip()
last_name = user.last_name.strip()

return f"{first_name} {last_name}"
```

## Names And Expressions

- Name values by their domain role or meaning, not only by their type or origin.
  Use the same term for the same concept. Preserve established abbreviations
  such as `ctx`, `err`, and conventional loop indices.
- Prefer fewer negations when an equivalent predicate remains natural. Name
  intermediate predicates when a condition mixes concepts, nested negation, or
  `and` with `or`. Keep one natural rule inline.
- Prefer the clearest conventional form for the local language and repository.
  Keep a compact expression when it performs one obvious, side-effect-free
  operation. Expand control flow when nesting, precedence, short-circuit order,
  mutations, failure points, or mixed responsibilities make behavior hard to
  inspect.
- Introduce intermediate values when their names expose domain meaning or
  separate genuinely difficult logic. Do not add mechanical temporaries only
  to shorten an expression.
- Extract a helper when its name creates a useful higher-level boundary or the
  seam supports real ownership, reuse, or testing. Keep trivial one-use logic
  inline when extraction only adds navigation.
- Keep distinct operations and failure points visible. Avoid nesting retrieval,
  parsing, validation, and side effects in one expression.
- Declare values near their use and in the narrowest useful scope. Group
  related values when they prepare one semantic block.
- Where a language permits omission, prefer explicit body delimiters for
  conditionals and loops unless a clear repository rule requires another form.
  Add other scopes only when they clarify ownership or value lifetime.
- In selection constructs, group alternatives with identical behavior into one
  branch or body. For pure Boolean classification, use an idiomatic membership
  expression when it is clearer and preserves relevant type or exhaustiveness
  checks. Add a branch-local scope only when it limits value lifetime or groups
  non-trivial work. Do not repeat identical bodies or add a scope to every
  trivial branch.
- Reduce nesting when a guard, pattern match, or cohesive extraction reveals a
  clearer main path. Treat depth as a review signal, not a numeric violation.
- In tests, extract a non-trivial actual value before its assertion. Group the
  subject, its meaningful values, and its assertions as one semantic block.

```text
operation_id = create_post.operation_id

assert operation_id == "CreatePost"
```

### Control-Flow Examples

Keep one obvious value choice compact:

```text
status = enabled ? ACTIVE : INACTIVE
```

Expand branches that combine effects or failure points:

```text
if refresh_required:
    refreshed_value = refresh_cache()
    record_refresh(refreshed_value)
    result = refreshed_value
else:
    result = cached_value
```

Use a local scope when one selection branch owns meaningful local work:

```text
select value:
    case KNOWN:
        return mapped

    case LEGACY, ALTERNATE:
        begin local scope
            fallback = build_fallback(value)
            record_fallback(fallback)
            return fallback
        end local scope

    default:
        return failure
```

For pure classification, a membership form can expose the rule directly:

```text
managed_fields = {
    LINE_ID,
    MODIFIED_ON,
    MODIFIED_BY,
    STATUS,
}

return field in managed_fields
```

## Comments

Add a concise comment when it materially helps the next reader understand why.
Explain non-obvious rationale, invariants, constraints, risks, or trade-offs.
Do not narrate visible mechanics or invent a reason.

Place a rationale comment directly above the code it constrains. Keep comments
current when behavior changes. Use the `comments` skill when the comment surface
becomes substantial or primary.

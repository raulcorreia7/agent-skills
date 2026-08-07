# Pipeline And Build Comments

## Pipelines And YAML Configuration

YAML comments are presentation only, never the sole required contract. Comment
non-obvious triggers, conditions, template contracts, ordering, provenance,
promotion, approvals, cache assumptions, platform constraints, or intentional
failure. Prefer clear names over narration. Validate provider schema and
expanded configuration when available.

Example:

```yaml
promote:
  needs: integration
  # Reuse the tested image digest; rebuilding would create a different artifact.
  uses: ./.github/workflows/promote.yml
```

## Build Systems

- In Makefiles, distinguish make comments from recipe text passed to a shell.
  Take care around continuations, variable definitions, functions, and trailing
  whitespace. An apparently harmless inline comment can change a value.
- For other build systems, identify whether a comment is parsed by the build
  language, embedded command language, generator, IDE, or linter before moving
  it.

## Containers

Treat Dockerfile parser directives as configuration. Keep them before other
comments and instructions, and validate them with the intended frontend or
build check. Explain stage boundaries, cache invalidation, platform constraints,
or security trade-offs only when names and instructions are insufficient.

Choose only checks owned by the affected repository and provider. These can
include schema validation, expanded-pipeline validation, build-system dry runs,
and container builds. Report semantics that the owning tool could not verify.

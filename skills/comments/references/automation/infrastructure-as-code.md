# Infrastructure-As-Code Comments

Document policy exceptions, lifecycle ignores, drift ownership, provider
quirks, destructive order, and state assumptions. Document security or cost
trade-offs only when they cannot be encoded or validated.

Never copy live identifiers, secrets, transient plans, or portal state into
comments. Scope and justify linter directives narrowly.

Example:

```hcl
lifecycle {
  # The platform controller owns this tag after deployment.
  ignore_changes = [tags["controller-status"]]
}
```

Use repository-owned formatting, validation, lint, plan, or documentation
checks that can verify the affected comment or directive without mutating live
resources. Report semantics that the owning tool could not verify.

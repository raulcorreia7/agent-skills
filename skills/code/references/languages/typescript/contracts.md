# TypeScript And JavaScript Contracts

Repository scripts, `tsconfig` inheritance, and framework build configuration
take precedence.

## Types And Contracts

- Treat requests, forms, storage, environment values, messages, parsed JSON,
  caught errors, and provider responses as `unknown`. Use a parser or type
  guard to validate them. Do not hide the boundary with `as` or `!`.
- Prefer discriminated unions, readonly data, named options, and exhaustive
  switches to `any`, Boolean parameter lists, and unchecked index access.
- Keep exports narrow. Avoid new barrel files and circular imports. Use
  `import type` for type-only dependencies.
- Await owned work and propagate cancellation and rejection behavior through
  the existing framework contract. Do not leave promises unobserved.

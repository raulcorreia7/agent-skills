# Rust Contracts

Repository toolchain, feature policy, and crate layout take precedence.

## Types And Contracts

- Use types and exhaustive matching to make invalid states difficult to
  represent.
- Use `Option` for meaningful absence and `Result` for recoverable failure.
  Preserve source errors and add context at the owning boundary.
- Keep public APIs narrow and semver-aware. Prefer explicit conversions over
  clever lifetime or trait machinery.
- Do not clone only to silence the borrow checker. Make ownership transfer
  visible.
- Use traits for a real capability seam or generic contract, not for one
  private implementation without substitution pressure.

## Execution And Ownership

- Use RAII for owned resources. Keep spawned task ownership, cancellation, and
  join behavior explicit.
- Avoid panics in library code unless the contract defines an internal
  invariant or unrecoverable state.
- Use macros only when functions, types, or derives cannot express the intent
  clearly.
- Keep `unsafe` narrow. State and enforce the invariant that makes each unsafe
  operation sound.

## Files And Documentation

Follow repository naming. Without a stronger convention, use `snake_case.rs`,
such as `payment_service.rs`.

Use `//` for implementation rationale, `///` for public items, and `//!` for
module or crate contracts. Add `# Errors`, `# Panics`, `# Safety`, and examples
when those caller contracts apply.

## Sources

- [rustdoc guidance](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
  and [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/).

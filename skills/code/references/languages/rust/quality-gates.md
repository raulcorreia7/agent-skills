# Rust Quality Gates

Repository toolchain, feature policy, crate layout, and CI commands take
precedence. Keep formatter, lint, and dependency policy in version control. Do
not depend on a developer's global Cargo or rustup configuration.

## Toolchain And Configuration

Commit a root `rust-toolchain.toml` that selects the repository-approved stable
release and required components. An explicit `cargo +toolchain` or
`RUSTUP_TOOLCHAIN` can override it. Use `rustup show` to confirm the active
toolchain. Pin the release in an actual repository when byte-for-byte
reproducibility matters. The placeholder below deliberately avoids inventing a
version for another project.

```toml
# rust-toolchain.toml
[toolchain]
channel = "<approved-stable-release>"
components = ["clippy", "rustfmt"]
profile = "minimal"
```

Set each package's `rust-version` to the minimum supported Rust version (MSRV)
and test it separately when the project promises MSRV support. Cargo discovers
configuration from the current directory upward. When run from a workspace it
does not read `.cargo/config.toml` files inside member crates. Put shared Cargo
configuration at the workspace root.

For workspaces, own durable compiler and Clippy levels at the root, then opt
each member in. `workspace.lints` requires a toolchain that supports it.

```toml
# Cargo.toml at workspace root
[workspace.lints.rust]
warnings = "deny"
future_incompatible = "deny"
rust_2018_idioms = "deny"
unsafe_code = "forbid"

[workspace.lints.clippy]
all = "deny"
pedantic = "deny"
nursery = "deny"
cargo = "deny"

# crates/example/Cargo.toml
[lints]
workspace = true
```

`unsafe_code = "forbid"` is the strict default. If the product genuinely
requires `unsafe`, make that exception at the workspace policy boundary, keep
the unsafe operation small, and document the invariant next to it. Do not add
blanket `allow` attributes. Use a narrow `#[expect(..., reason = "...")]`
only when the exception is intentional and reviewable. Do not enable Clippy's
`restriction` group wholesale: its lints are domain-specific rather than a
general production baseline.

Use `cargo fmt --all`. Avoid nightly-only rustfmt settings and alternative
formatters. Commit `Cargo.lock` for applications and workspaces unless a
deliberate published-library policy says otherwise. CI must use `--locked`.

## Dependencies And Security

Use one dependency-policy tool rather than overlapping advisory scanners.
`cargo-deny` checks advisories, duplicate or banned crates, licenses, and
sources in one pass. Commit `deny.toml`. Provision the tool through the
repository's CI bootstrap instead of an unpinned install command.

```toml
# deny.toml — begin with policy that is true for this repository.
[advisories]
yanked = "deny"
unmaintained = "all"
unsound = "all"
unused-ignored-advisory = "deny"

[bans]
wildcards = "deny"
multiple-versions = "deny"
multiple-versions-include-dev = true

[sources]
unknown-registry = "deny"
unknown-git = "deny"
required-git-spec = "rev"

[licenses]
include-dev = true
# Add only the SPDX identifiers that the repository's legal policy approves.
allow = ["Apache-2.0", "MIT"]
unused-allowed-license = "deny"
```

Treat every dependency, license, source, advisory ignore, and duplicate-version
exception as reviewed policy. An exception needs a reason, owner, and removal
condition. Do not weaken global checks to admit one dependency.

## Sources

- [rustup overrides](https://rust-lang.github.io/rustup/overrides.html) and
  [Cargo configuration](https://doc.rust-lang.org/cargo/reference/config.html)
  — toolchain and configuration precedence.
- [Cargo workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html),
  [lint levels](https://doc.rust-lang.org/rustc/lints/levels.html), and
  [Clippy lints](https://rust-lang.github.io/rust-clippy/master/index.html) —
  workspace lint ownership and strict linting.
- [cargo-deny checks](https://embarkstudios.github.io/cargo-deny/checks/),
  [advisory policy](https://embarkstudios.github.io/cargo-deny/checks/advisories/cfg.html),
  [dependency policy](https://embarkstudios.github.io/cargo-deny/checks/bans/cfg.html),
  [license policy](https://embarkstudios.github.io/cargo-deny/checks/licenses/cfg.html), and
  [source policy](https://embarkstudios.github.io/cargo-deny/checks/sources/cfg.html).

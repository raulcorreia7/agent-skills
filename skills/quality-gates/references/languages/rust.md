# Rust Quality Gates

Keep formatter, lint, and dependency policy in version control rather than in a
developer's global Cargo or rustup configuration.

## Toolchain and configuration

Commit a root `rust-toolchain.toml` that selects the approved stable release
and the required components. `cargo +toolchain` or `RUSTUP_TOOLCHAIN` can
override it; `rustup show` confirms the active toolchain. Replace the
placeholder with a real release; do not invent one for another project.

```toml
# rust-toolchain.toml
[toolchain]
channel = "<approved-stable-release>"
components = ["clippy", "rustfmt"]
profile = "minimal"
```

Set each package's `rust-version` to the minimum supported Rust version (MSRV)
and test it separately when the project promises MSRV support. Cargo reads
configuration from the current directory upward, and from a workspace it skips
`.cargo/config.toml` files inside member crates, so put shared Cargo
configuration at the workspace root.

For workspaces, set compiler and Clippy levels at the root and opt each member
in. `workspace.lints` needs a toolchain that supports it.

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

`unsafe_code = "forbid"` is the strict default. When the product needs
`unsafe`, make the exception at the workspace policy boundary, keep the unsafe
operation small, and document its invariant next to it. Prefer a narrow
`#[expect(..., reason = "...")]` to a blanket `allow`. Leave Clippy's
`restriction` group off as a whole: its lints are domain-specific.

Use `cargo fmt --all` with stable rustfmt settings and no alternative
formatter. Commit `Cargo.lock` for applications and workspaces unless a
published-library policy says otherwise, and use `--locked` in CI.

## Dependencies and security

Use one dependency-policy tool. `cargo-deny` checks advisories, duplicate or
banned crates, licenses, and sources in one pass. Commit `deny.toml` and
provision the tool through the CI bootstrap at a pinned version.

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

Each dependency, license, source, advisory ignore, or duplicate-version
exception needs a reason, an owner, and a removal condition. Admit one
dependency with a scoped exception, not by weakening a global check.

## Gate commands

```text
cargo fmt --all -- --check
cargo clippy --workspace --all-targets --all-features --locked
cargo test --workspace --all-targets --all-features --locked
cargo deny check          # fetches advisory data; approval-gated
```

Use `--all-features` only when features are composable; otherwise list each
supported feature combination in the CI matrix.

Sources: `rust` in [sources.yml](../sources.yml).

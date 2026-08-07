# Rust Verification

Run focused tests while iterating. Before merge, run this sequence or the
repository equivalent from the workspace root:

```text
cargo fmt --all -- --check
cargo clippy --workspace --all-targets --all-features --locked
cargo build --workspace --all-targets --all-features --locked
cargo test --workspace --all-targets --all-features --locked
cargo test --workspace --doc --all-features --locked
cargo deny check
```

`--all-features` is correct only when the feature set is intentionally
composable. Otherwise, run the same build, Clippy, and test commands for each
supported feature combination in CI. Add target triples to that matrix when
conditional compilation changes code or dependencies.

## Sources

- [cargo fmt](https://doc.rust-lang.org/cargo/commands/cargo-fmt.html),
  [cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html), and
  [lockfile guidance](https://doc.rust-lang.org/cargo/guide/cargo-toml-vs-cargo-lock.html).

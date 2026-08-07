# Go Quality Gates

Repository policy, the Go version, and package conventions take precedence.
Keep the toolchain and
analysis policy in the repository. Do not make an editor or developer-machine
setting the source of truth.

## Toolchain And Configuration

`go.mod` owns the module's minimum Go version. Its `toolchain` directive can
suggest a newer toolchain when the module is the main module. It is not a
substitute for the required `go` version. Keep both aligned with the supported
release policy and let CI use that policy, not whichever Go happens to be on a
developer's `PATH`.

```text
# go.mod — values are the repository's approved releases
go <minimum-supported-release>
toolchain go<CI-release> # only when it selects a newer toolchain
```

`go.work` is a developer workspace, not a module contract. A checked-in
workspace can make CI test different replacements from downstream consumers.
For module CI, set `GOWORK=off`. Use a workspace deliberately only when the
repository's build owns all listed modules.

`gofmt` has no project configuration: use it without a competing formatter.
Put a root `staticcheck.conf` under version control and let deeper files make
only documented, package-specific changes. Staticcheck merges configurations
down the package tree, with the deepest value taking precedence.

```toml
# staticcheck.conf
# Enable the style checks that Staticcheck omits by default as well.
checks = ["all"]
```

Pin third-party analysis tools in the repository's CI/tool bootstrap rather
than installing `@latest` during a reproducible build. Do not add an aggregate
linter that duplicates `go vet` and Staticcheck.

## Dependencies And Security

`go.mod` and `go.sum` are the dependency contract. Keep both tidy, commit their
intentional changes, and avoid broad `replace` directives in released modules.
Use the default checksum database for public modules. Scope `GOPRIVATE` only to
actual private module paths so private names and content are not sent to public
services.

`govulncheck` is build-configuration-sensitive. Run it for each supported
target or build-tag configuration that changes reachable code.

## Sources

- [Go Modules Reference](https://go.dev/ref/mod) — `go` and `toolchain`
  directives, workspace behavior, tidy, and module verification.
- [go vet](https://pkg.go.dev/cmd/vet) and
  [govulncheck](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck) — built-in
  static analysis and reachability-aware vulnerability analysis.
- [Staticcheck configuration](https://staticcheck.dev/docs/configuration/) and
  [check options](https://staticcheck.dev/docs/configuration/options/) — config
  inheritance and the full check set.

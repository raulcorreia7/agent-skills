# Go Quality Gates

Keep the toolchain and analysis policy in the repository, not in editor or
developer-machine settings.

## Toolchain and configuration

`go.mod` owns the module's minimum Go version. Its `toolchain` directive can
suggest a newer toolchain when the module is the main module; it does not
replace the required `go` version. Align both with the supported release
policy and let CI use that policy, not whichever Go is on a developer's
`PATH`.

```text
# go.mod — values are the repository's approved releases
go <minimum-supported-release>
toolchain go<CI-release> # only when it selects a newer toolchain
```

`go.work` is a developer workspace, not a module contract: a checked-in
workspace can make CI test different replacements from downstream consumers.
For module CI, set `GOWORK=off`. Use a workspace in CI only when the
repository's build owns all listed modules.

`gofmt` has no configuration; use it without a competing formatter. Commit a
root `staticcheck.conf` and let deeper files make only documented,
package-specific changes. Staticcheck merges configurations down the package
tree, and the deepest value wins.

```toml
# staticcheck.conf
# Also enable the style checks that Staticcheck omits by default.
checks = ["all"]
```

Pin third-party analysis tools in the repository's CI or tool bootstrap rather
than installing `@latest` during a build. Skip aggregate linters that
duplicate `go vet` and Staticcheck.

## Dependencies and security

`go.mod` and `go.sum` are the dependency contract. Keep both tidy and avoid
broad `replace` directives in released modules. Use the default checksum
database for public modules, and scope `GOPRIVATE` to the actual private module
paths so private names are not sent to public services.

`govulncheck` depends on build configuration. Run it for each supported target
or build-tag configuration that changes reachable code. It fetches
vulnerability data, so it is approval-gated.

## Gate commands

```text
test -z "$(gofmt -l .)"
go vet ./...
staticcheck ./...
go test -race -shuffle=on -count=1 ./...
```

Sources: `go` in [sources.yml](../sources.yml).

# Go Verification

Run focused tests while iterating. Before merge, run the repository commands
or this equivalent sequence from each module root:

```text
gofmt -d <changed-go-files>  # expect no output
go vet ./...
staticcheck ./...
go build ./...
go test -race -shuffle=on -count=1 ./...
go mod tidy -diff
go mod verify
govulncheck ./...
```

Run the race detector on every supported platform where it is available. Keep
test-only build tags and platform-specific packages in the verification matrix.
`./...` alone does not prove every build-tag combination.

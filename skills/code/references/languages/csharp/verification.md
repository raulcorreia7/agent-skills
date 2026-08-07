# C# And .NET Verification

Run the repository's wrapper or CI target if it exists. Otherwise, from the
solution root, use this minimal sequence. Replace `solution.sln` as needed.

```text
dotnet restore solution.sln --locked-mode
dotnet format solution.sln --verify-no-changes --no-restore
dotnet build solution.sln --no-restore
dotnet test solution.sln --no-build
dotnet package list solution.sln --vulnerable --include-transitive --no-restore
```

Use the CLI spelling provided by the pinned SDK (`dotnet list package` on older
SDKs). Do not use `--no-build` if the selected test target builds generated
sources that the preceding build does not cover.

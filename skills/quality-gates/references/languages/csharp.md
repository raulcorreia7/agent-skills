# C# and .NET Quality Gates

The pinned SDK in `global.json`, the target-framework support policy, and the
nearest `.editorconfig` set the frame. Extend the root `Directory.Build.props`
or the existing shared build configuration, and keep one analyzer set, one
formatter, and one nullable convention. For a legacy non-SDK project, use its
established analyzer package and build integration instead of these
properties.

## Strict baseline

Keep nullable contracts accurate, enable the SDK analyzers at their complete
non-preview rule set, and treat every warning as an error. Suppress a single
diagnostic only with a narrow justification and a removal path; avoid
project-wide warning exclusions.

```xml
<!-- Directory.Build.props, or the repository's existing shared props file -->
<Project>
  <PropertyGroup>
    <Nullable>enable</Nullable>
    <EnableNETAnalyzers>true</EnableNETAnalyzers>
    <AnalysisLevel>latest-all</AnalysisLevel>
    <EnforceCodeStyleInBuild>true</EnforceCodeStyleInBuild>
    <TreatWarningsAsErrors>true</TreatWarningsAsErrors>

    <!-- Applications: commit the lock files and require them in CI. -->
    <RestorePackagesWithLockFile>true</RestorePackagesWithLockFile>
    <NuGetAudit>true</NuGetAudit>
    <NuGetAuditMode>all</NuGetAuditMode>
  </PropertyGroup>
</Project>
```

`latest-all` enables the SDK's `All` rule set, not only the recommended subset.
A few legacy rules stay opt-in by design; enable one only when its signal fits
the repository. Make explicit requirements unambiguous in `.editorconfig`, for
example security severity:

```ini
[*.cs]
dotnet_diagnostic.category-Security.severity = error
```

Prefer the SDK analyzers to overlapping general-purpose analyzer packages. Add
a specialist analyzer only for a demonstrated gap, such as a framework-specific
contract, and make it build-breaking. `dotnet format` is the one formatter; it
reads `.editorconfig`, including code-style diagnostics.

## Compatibility and supply chain

- Raise the target framework, language version, or SDK through the support
  policy, never only to enable a rule; then re-check analyzer diagnostics.
- Commit `packages.lock.json` for deployable applications. Libraries may omit
  lock files because the consuming application's graph is authoritative. Use
  locked restore in CI.
- Use repository-controlled NuGet sources. When private and public sources are
  mixed, map package ID patterns to their source so an internal ID cannot
  resolve from the wrong feed.
- Keep NuGet audit on. The repository risk policy sets the audit level and the
  failure threshold; record an exception as a time-bounded risk decision.

## Gate commands

```text
dotnet restore solution.sln --locked-mode   # reaches package feeds; approval-gated
dotnet format solution.sln --verify-no-changes --no-restore
dotnet build solution.sln --no-restore
dotnet test solution.sln --no-build
```

Sources: `csharp` in [sources.yml](../sources.yml).

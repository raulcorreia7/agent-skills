# C# And .NET Quality Gates

Repository policy, the pinned SDK in `global.json`, the target-framework
support policy, and the nearest `.editorconfig` take precedence. Extend the
root `Directory.Build.props` or existing shared build configuration. Do not add
a second analyzer, formatter, or nullable convention to one project. For a
legacy non-SDK project, use its established analyzer package and build
integration instead of copying these properties.

## Strict Baseline

Keep nullable contracts accurate and enable the SDK analyzers at their complete,
non-preview rule set. Treat every warning as a build failure. Suppress an
individual diagnostic only with a narrow justification and a removal path.
Never use a project-wide warning exclusion.

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

`latest-all` is deliberately strict: it enables the SDK's `All` rule set, not
only the recommended subset. A small set of legacy rules remains opt-in by
design. Enable one individually only when its signal fits the repository. This
does not replace explicit requirements. For example, make security rule
severity unambiguous in the repository's `.editorconfig`:

```ini
[*.cs]
dotnet_diagnostic.category-Security.severity = error
```

Prefer this SDK analyzer set over overlapping general-purpose analyzer
packages. Add a specialist analyzer only for a demonstrated gap (for example,
a framework-specific contract) and make it build-breaking. `dotnet format` is
the one formatter: it reads `.editorconfig`, including code-style diagnostics.

## Compatibility And Supply Chain

- Do not increase the target framework, language version, or SDK solely to
  enable a rule. Upgrade them through the repository's support policy, then
  re-evaluate analyzer diagnostics.
- Commit `packages.lock.json` for deployable applications. Libraries may omit
  lock files because a consuming application's resolved graph is authoritative.
  In CI, use locked restore. Dependency changes must intentionally update the
  lock file.
- Use repository-controlled NuGet sources. When private and public sources are
  mixed, map package ID patterns to their intended source so an internal ID
  cannot resolve from an unintended feed.
- Keep NuGet audit enabled. Let the repository risk policy select the audit
  level and failure threshold. Record an exception as an explicit,
  time-bounded risk decision. Audit source availability is part of the build
  contract.

## Sources

- [Code analysis overview](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/overview),
  [analyzer configuration and precedence](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/configuration-files),
  [analyzer rule categories](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/categories),
  and [MSBuild SDK properties](https://learn.microsoft.com/en-us/dotnet/core/project-sdk/msbuild-props).
- [dotnet format](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-format),
  [NuGet audit](https://learn.microsoft.com/en-us/nuget/concepts/auditing-packages),
  [lock files](https://learn.microsoft.com/en-us/nuget/consume-packages/package-references-in-project-files),
  and [Package Source Mapping](https://learn.microsoft.com/en-us/nuget/consume-packages/package-source-mapping).

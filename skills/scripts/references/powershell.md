# PowerShell Scripts

## Fragile Behavior

- Use comment-based help for public scripts and advanced functions.
- Use `[CmdletBinding()]`, typed parameters, validation attributes, and approved
  verbs for exported functions.
- Use `SupportsShouldProcess` with `-WhatIf` and `-Confirm` for state changes.
- Emit structured objects on the success stream. Use verbose, information,
  warning, and error streams for diagnostics.
- Make non-terminating errors fail when required with `$ErrorActionPreference =
  'Stop'` or `-ErrorAction Stop`. These settings do not convert a native
  process failure into a PowerShell error. Check `$LASTEXITCODE` explicitly.
- Prefer splatting and path APIs over long calls, backtick continuation, or
  string-built paths.

## Shape

```powershell
[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string] $Path
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Main {
    if ($PSCmdlet.ShouldProcess($Path, 'Update')) {
        # Execute the validated state change.
    }
}

Main
```

## Verification

Use repository settings and tasks first. Otherwise run all default
PSScriptAnalyzer rules and make findings fail the check:

```powershell
Invoke-ScriptAnalyzer -Path .\scripts\Task.ps1 -EnableExit
```

Pass `-Settings` when the repository owns a PSScriptAnalyzer settings file. Run
its formatter in check mode when configured and one focused Pester test when an
existing suite owns the behavior. For state changes, exercise `-WhatIf`; for
native commands, exercise nonzero `$LASTEXITCODE` handling. Validate a module
manifest with `Test-ModuleManifest` when the script is distributed as a module.

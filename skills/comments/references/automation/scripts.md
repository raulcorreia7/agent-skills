# Script Comments

Prefer CLI help, validation, and structured inputs for user-facing behavior.
Comment only automation details whose order, environment, lifecycle, or parsing
is not clear from the code.

## Shell And Bash

- Document sourced-library public functions only when names and parameters do
  not establish their contract.
- Explain non-obvious splitting, globbing, subshells, traps, cleanup,
  privileges, retries, or non-portable behavior.
- Keep shebangs and ShellCheck directives in tool-defined positions. Scope and
  justify suppressions narrowly.
- Do not narrate commands or preserve dead alternatives as comments.

Example:

```sh
#!/usr/bin/env bash
set -euo pipefail

# Preserve pipeline failures when the final command succeeds.
generate_report | publish_report
```

Use the interpreter from the shebang for a parse check, such as
`bash -n <script>`. Use the repository formatter, such as `shfmt -d <script>`,
and ShellCheck when they are authoritative and available.

## PowerShell

- Use comment-based help for reusable or exported commands that need
  `Get-Help`. Keep it aligned with the command contract.
- Preserve placement rules for help, signatures, `#Requires`, regions, and
  other special comments.
- Explain non-obvious binding, remoting, scope, preferences, error behavior,
  platform differences, or cleanup.

Example:

```powershell
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

<#
.SYNOPSIS
Gets cached build metadata.
#>
function Get-BuildMetadata { }
```

Use the repository's PowerShell formatter when one is configured. Parse with
`System.Management.Automation.Language.Parser` and fail on returned parse
errors. Run `Invoke-ScriptAnalyzer -Path <script>` when PSScriptAnalyzer is an
owned check.

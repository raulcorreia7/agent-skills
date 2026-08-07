# Batch Scripts

Prefer PowerShell for robust Windows automation.

## Fragile Behavior

- Start with `@echo off` and `setlocal EnableExtensions DisableDelayedExpansion`.
- Enable delayed expansion only in the smallest scope that requires it.
- Quote paths and arguments such as `"%~1"` and `"%TARGET%"`. Expansion occurs
  before a parenthesized block runs; delayed expansion uses `!NAME!` but can
  corrupt input that contains `!`.
- Check `%ERRORLEVEL%` or use `if errorlevel 1` after fallible commands.
- Keep labels small and end them with explicit `exit /b <code>`.
- Hand complex parsing, arrays, and data shaping to PowerShell, Python, or Node.

## Shape

```bat
@echo off
setlocal EnableExtensions DisableDelayedExpansion

call :main %*
exit /b %ERRORLEVEL%

:main
if "%~1"=="" (
  echo Usage: %~nx0 check^|render 1>&2
  exit /b 2
)
exit /b 0
```

## Verification

Run the repository's existing batch formatter or analyzer when present; there
is no portable default worth adding for one script. Exercise help, invalid
usage, and exit propagation under the oldest supported `cmd.exe` environment:

```bat
rem Expect 0, then the command's documented invalid-usage code.
cmd.exe /d /c "scripts\task.cmd --help"
cmd.exe /d /c "scripts\task.cmd --invalid"
```

Run the smallest existing behavior test after these interface checks.

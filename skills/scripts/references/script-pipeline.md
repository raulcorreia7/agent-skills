# Script Pipeline

Use this pattern when automation has distinct discovery, planning, execution,
and verification stages that need separate review or testing. A small wrapper
does not need this pattern.

## Default Stages

```text
parse_args
validate_args
load_config
discover_inputs
plan_changes
preview_changes
execute_changes
verify_result
render_output
cleanup
```

Combine or omit stages that do not improve the contract. Preserve the ordering
invariants: cheap validation before discovery, planning before writes, and
verification before success output.

## Stage Contract

- Accept explicit input and return a structured result where the language
  supports it.
- Keep discovery and planning read-only.
- Isolate destructive stages and validate their target again at the mutation
  boundary.
- Keep rendering outside business logic and diagnostics outside result data.
- Make cleanup safe after partial failure and retries.
- Keep planning independently observable from execution.

## Orchestration Shapes

```bash
main() {
  parse_args "$@"
  validate_args
  discover_inputs
  plan_changes
  preview_or_execute
  verify_result
}

main "$@"
```

```powershell
function Main {
    Get-Input | Test-Input | New-Plan | Invoke-Plan | Test-Result
}

Main
```

```ts
async function main(): Promise<void> {
  const input = parseInput(process.argv)
  const plan = await buildPlan(await discover(validate(input)))
  const result = input.dryRun ? plan : await execute(plan)
  render(await verify(result))
}
```

## Verification

Verify the earliest stage that can prove each contract:

| Contract | Smallest useful check |
|---|---|
| Parsing and validation | Invalid and boundary inputs; no discovery or writes |
| Discovery and planning | Fixed fixture; stable, read-only plan |
| Preview | Same plan as execution; no mutation |
| Execution | Disposable target; expected writes only |
| Verification and cleanup | Partial failure; actionable error and safe cleanup |

Run language-level formatting, static analysis, strict typing, and dependency
checks through the selected implementation guide. Do not make an end-to-end
side-effect test the only evidence for a stage that has a read-only seam.

## Smells

- The abstraction is longer than the work.
- Every stage mutates one shared object.
- Errors are unstructured strings with no failing stage.
- Validation occurs after writes or rendering occurs before work completes.
- The only test path executes the whole workflow and its side effects.

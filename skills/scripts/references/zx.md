# zx Scripts

## Decision

Use `zx` when command orchestration, package-manager tasks, filesystem work, or
cross-platform shell selection dominates. Keep plain Node or TypeScript when
application logic, data transformation, or API integration dominates. Keep
Bash or PowerShell for small, conventional platform-local glue.

## Project Fit

- Prefer the repository's existing TypeScript runner and module convention.
  Use `.mts` only when ESM mode must be explicit. Use `.mjs` when TypeScript
  setup lacks justification.
- Use `zx@lite` only when the script intentionally avoids the full package's
  filesystem, glob, prompt, YAML, dotenv, and temporary-file helpers.
- Preserve the repository's strict TypeScript settings. For a new TypeScript
  script configuration, enable `strict` and use `noEmit` when another runner
  owns execution:

```json
{
  "compilerOptions": {
    "strict": true,
    "noEmit": true
  }
}
```

## Command Safety

- Pass dynamic arguments through `${...}` and arrays so `zx` quotes values. Do
  not assemble one raw command string or add shell quotes around substitutions.
- Use `glob()` for intentional dynamic glob expansion and `os.homedir()` for
  home paths.
- Set `preferLocal: true` for project-local binaries.
- Choose the shell explicitly when behavior depends on Bash, Windows PowerShell,
  or `pwsh`.

```ts
const files = await glob(["docs/**/*.md", "wiki/**/*.md"])
const flags = ["--config", ".markdownlint.json"]

await $({ preferLocal: true })`markdownlint ${flags} ${files}`
```

## Runtime

- Bound commands that can hang with a timeout or `AbortController`.
- Use `nothrow` only when non-zero status is expected and handled.
- Consume output explicitly with `.json<T>()`, `.lines()`, `.text()`, or
  `.buffer()`.
- Set `process.exitCode` after asynchronous work. Avoid a `process.exit()` call
  before output can flush.

## Verification

Use the repository's package manager and aggregate task first. For an npm-based
repository that owns these scripts, a production check sequence is:

```bash
npm run format:check
npm run lint
npm run typecheck
npm test -- task
```

Keep one formatter, one linter, and the configured strict type checker. Do not
replace project scripts with direct tool invocations or enable unstable rules
for one file. Run the selected package manager's lock validation. With network
approval, an npm-owned repository can run its read-only dependency audit:

```bash
npm audit
```

Do not run automatic audit fixes or upgrades. Do not create tests or expand
test scope unless the user asks.

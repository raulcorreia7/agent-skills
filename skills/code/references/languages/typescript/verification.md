# TypeScript And JavaScript Verification

Use the repository scripts, which must call the local tools. With npm, a
minimal CI-quality sequence is below.

These reach the registry; get approval before running them:

```text
npm ci
npm audit
```

These run offline once dependencies are installed:

```text
npm exec prettier -- --check .
npm exec eslint -- . --max-warnings 0
npm exec tsc -- --project tsconfig.verify.json
npm test
npm run build
```

For pnpm or Yarn, use the lockfile-enforcing install command and the matching
local-execution command. Commit exactly one lock file. `npm audit` reports
dependency vulnerabilities. Let the repository risk policy select the audit
failure threshold. Review and update the lock file deliberately instead of
running an automatic fix in CI.

## Sources

- [npm audit](https://docs.npmjs.com/cli/v11/commands/npm-audit/).

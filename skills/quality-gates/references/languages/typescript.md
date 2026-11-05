# TypeScript and JavaScript Quality Gates

Run the locked TypeScript, ESLint, and Prettier through the repository's
package manager. Keep one formatter and one linter.

## Strict baseline

Put stable, high-signal compiler checks in the checked `tsconfig`. Module,
target, JSX, lib, paths, and emit settings belong to the runtime or framework,
so extend them instead of copying this fragment over them. Use a no-emit
verification config when the application build emits files.

```jsonc
// tsconfig.verify.json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "noEmit": true,
    "strict": true,
    "exactOptionalPropertyTypes": true,
    "noUncheckedIndexedAccess": true,
    "noPropertyAccessFromIndexSignature": true,
    "noImplicitOverride": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "allowUnreachableCode": false,
    "allowUnusedLabels": false,
    "forceConsistentCasingInFileNames": true,
    "isolatedModules": true,
    "verbatimModuleSyntax": true,
    "skipLibCheck": false
  },
  "include": ["src", "tests"]
}
```

For JavaScript source in the checked program, add these options to the owning
config and state its contracts in JSDoc:

```json
{ "compilerOptions": { "allowJs": true, "checkJs": true } }
```

Use type-aware ESLint with the stable `recommendedTypeChecked` and
`stylisticTypeChecked` configurations. The contents of `strictTypeChecked` and
`all` are not semver-stable, so add stable strict rules one by one instead.

```js
// eslint.config.mjs
import js from "@eslint/js";
import tseslint from "typescript-eslint";

export default tseslint.config(
  { ignores: ["dist/**", "coverage/**", "node_modules/**"] },
  js.configs.recommended,
  tseslint.configs.recommendedTypeChecked,
  tseslint.configs.stylisticTypeChecked,
  {
    languageOptions: {
      parserOptions: { projectService: true, tsconfigRootDir: import.meta.dirname },
    },
    rules: {
      "@typescript-eslint/consistent-type-imports": "error",
      "@typescript-eslint/no-floating-promises": "error",
      "@typescript-eslint/no-misused-promises": "error",
      "@typescript-eslint/no-unnecessary-condition": "error",
      "@typescript-eslint/no-unnecessary-type-assertion": "error",
      "@typescript-eslint/only-throw-error": "error",
      "@typescript-eslint/strict-boolean-expressions": "error"
    }
  }
);
```

Prettier owns whitespace and layout; leave ESLint formatting rules off. Keep
its options in a checked file so editors and CI agree.

```json
// .prettierrc.json
{ "semi": true, "singleQuote": false, "trailingComma": "all" }
```

## Gate commands

```text
npm exec prettier -- --check .
npm exec eslint -- . --max-warnings 0
npm exec tsc -- --project tsconfig.verify.json
npm test
```

For pnpm or Yarn, use the matching local-execution command.

Sources: `typescript` in [sources.yml](../sources.yml).

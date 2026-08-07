# TypeScript And JavaScript Quality Gates

Repository scripts, the lock file, `packageManager`, `tsconfig` inheritance,
and framework build configuration take precedence. Use the locally locked
TypeScript, ESLint, and Prettier through the repository's package manager. Do
not replace its package manager or add overlapping formatters and linters.

## Strict Baseline

Put stable, high-signal compiler checks in the checked `tsconfig`. Keep module,
target, JSX, lib, paths, and emit settings owned by the runtime or framework.
do not copy this fragment over them. Use a no-emit verification config when the
application build emits files.

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

For JavaScript source that is part of the checked program, add these two
options to the owning config and use JSDoc to state its contracts:

```json
{ "compilerOptions": { "allowJs": true, "checkJs": true } }
```

Use type-aware ESLint with the stable `recommendedTypeChecked` and
`stylisticTypeChecked` configurations. Do not use `strictTypeChecked` or `all`
as a default gate: their rule contents are explicitly not semver-stable. Add
stable, high-value strict rules explicitly instead.

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

Use Prettier for whitespace and syntax layout, not ESLint formatting rules.
Keep its options in a checked configuration file so editors and CI agree.

```json
// .prettierrc.json
{ "semi": true, "singleQuote": false, "trailingComma": "all" }
```

## Sources

- [TypeScript strict mode](https://www.typescriptlang.org/tsconfig/strict),
  [TypeScript compiler options](https://www.typescriptlang.org/tsconfig/),
  [noUncheckedIndexedAccess](https://www.typescriptlang.org/tsconfig/noUncheckedIndexedAccess.html),
  [exactOptionalPropertyTypes](https://www.typescriptlang.org/tsconfig/exactOptionalPropertyTypes.html), and
  [skipLibCheck](https://www.typescriptlang.org/tsconfig/skipLibCheck.html).
- [typescript-eslint configurations](https://typescript-eslint.io/users/configs/),
  [typescript-eslint project service](https://typescript-eslint.io/packages/parser/), and
  [Prettier CLI](https://prettier.io/docs/cli.html).

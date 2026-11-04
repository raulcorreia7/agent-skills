# Change Review

Review significant risk and return evidence-backed findings.

## Steps

1. Review the diff first. Follow callers, schemas, configuration, migrations,
   tests, scripts, generated artifacts, and documentation only far enough to
   verify impact.
2. Check behavior, failure paths, data safety, authorization, compatibility,
   rollout, maintainability, and meaningful missing confidence. Treat style as
   a finding only when it creates real risk.
3. Use repository-native validation and CI commands as the checks, and leave
   test scope unchanged.
4. Stop when evidence is proportionate to risk or further validation needs new
   authority, infrastructure, live access, or test creation.

## Output

Use this order and omit empty sections:

1. **Verdict:** `pass`, `findings`, or `not reviewable`.
2. **Findings:** Severity-ordered (`P0` through `P3`), each with a concise
   title, precise location, impact, evidence, and smallest safe fix.
3. **Questions:** Only questions whose answers change correctness or
   risk.
4. **Checks:** Exact commands, results, and failure classification when checks
   ran.
5. **Residual risk:** Assumptions, unreviewed surfaces, and confidence limits.

When there are no findings, say so explicitly. Do not bury findings in a
summary or mix optional suggestions with correctness findings.

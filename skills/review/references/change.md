# Change Review

Review material risk and return evidence-backed findings.

## Steps

1. Review the diff first. Follow callers, schemas, configuration, migrations,
   tests, scripts, generated artifacts, and documentation only far enough to
   verify impact.
2. Check behavior, failure paths, data safety, authorization, compatibility,
   rollout, maintainability, and meaningful missing confidence. Treat style as
   a finding only when it creates material risk. Treat pattern, principle,
   smell, or metric conformance as neither proof nor a defect without a concrete
   consequence.
3. Inspect repository-native validation and CI commands only when they can
   resolve a material review question. Run a small safe existing check when it
   is useful. Do not expand test scope.
4. Classify failures as change-caused, pre-existing, environmental, or
   inconclusive. Verify suspected findings and distinguish defects,
   suggestions, questions, and uncertainty.
5. Stop when evidence is proportionate to risk or further validation needs new
   authority, infrastructure, live access, or test creation.

## Output

Use this order and omit empty sections:

1. **Verdict:** Pass, findings present, or not reviewable.
2. **Findings:** Severity-ordered (`P0` through `P3`), each with a concise
   title, precise location, impact, evidence, and smallest safe fix.
3. **Questions:** Only questions whose answers materially change correctness or
   risk.
4. **Checks:** Exact commands, results, and failure classification when checks
   ran.
5. **Residual risk:** Assumptions, unreviewed surfaces, and confidence limits.

When there are no findings, say so explicitly. Do not bury findings in a
summary or mix optional suggestions with correctness findings.

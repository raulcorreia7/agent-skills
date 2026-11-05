# Adversarial Reviewer Contracts

All roles assess the full scope and criteria, within the role limits in
`SKILL.md` (Guardrails).

## Report Shape

Return:

1. **Verdict:** `pass`, `findings`, or `not reviewable`.
2. **Findings:** Use a composed specialist's priority vocabulary; otherwise
   order `Critical`, `High`, `Medium`, or `Low`. Give each a precise locator,
   affected criterion, evidence, consequence, verification or falsification
   attempt, confidence, and smallest safe direction.
3. **Evidence:** Inspected local evidence and exact commands and results.
4. **Coverage:** Reviewed and unreviewed scope.
5. **Residual uncertainty:** Assumptions, evidence limits, and unresolved
   questions.

Return conclusions, not hidden reasoning. `SKILL.md` step 4 defines an unusable
report.

## Example Finding

**High — Retry can duplicate a completed operation.** At `worker.py:84`, a
timeout retries a write without an idempotency key, violating the stated
at-most-once criterion. The reviewer found no stored operation identifier or
upstream deduplication guard. A duplicate write is observable after an
ambiguous timeout. Confidence: high. Smallest direction: persist and reuse an
operation key at the write boundary.

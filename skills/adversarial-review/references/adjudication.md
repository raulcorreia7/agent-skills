# Evidence Adjudication

Normalize a composed `review` report as `P0` = `Critical`, `P1` = `High`,
`P2` = `Medium`, and `P3` = `Low`. Preserve the specialist label beside the
normalized label so composition is lossless.

Report order, length, tone, stated confidence, agreement, repetition, reviewer
identity, and model identity are not evidence.

## Example

A composed `review` finding labelled `P1` appears in the normalized synthesis
as `High (review: P1)`. Confirm it when the cited retry path and violated
at-most-once criterion are present in the artifact. Reject it when both reports
repeat the claim but the cited boundary already supplies and persists an
idempotency key; agreement does not override the disconfirming evidence.

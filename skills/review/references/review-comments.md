# Public Review Comments

## Comment Quality

- Comment on code, not the author.
- Explain why it matters.
- Offer the smallest practical fix.
- Mark optional ideas as non-blocking.
- Prefer clearer code over review-thread explanations.

## Labels

- `blocking`: must fix before merge.
- `question`: answer may change the review.
- `suggestion`: non-blocking improvement.
- `nit`: optional polish.
- `note`: useful context, no action required.

## Example

`blocking` — `worker.py:84` retries the write after an ambiguous timeout
without reusing an operation key. The first attempt can complete before the
retry, producing a duplicate write. Persist one key at the write boundary and
reuse it for every retry.

# Persistence And Schema Change

- Make transaction, isolation, consistency, and ordering contracts explicit.
  Add deterministic tie-breakers when callers or pagination depend on order.
- Design schema changes for deployment overlap and rollback. Use
  expand-and-contract when old and new versions can run together.
- Define ownership and compatibility for stored encodings, defaults, nulls,
  constraints, indexes, backfills, and generated values.
- Bound migrations and backfills by time, lock impact, batch size, retry,
  checkpoint, and recovery behavior.
- Check engine-specific DDL transaction support, lock acquisition, online or
  concurrent index behavior, and statement or lock timeouts when they can
  affect availability.
- Verify forward and rollback paths with production-compatible storage and
  representative existing data when the risk warrants it.

Example—expand and contract a renamed field:

1. Add nullable `display_name` while readers still use `name`.
2. Deploy dual-write code and backfill in bounded batches.
3. Switch reads after compatibility and data checks pass.
4. Stop the old write after the rollback window.
5. Remove `name` in a later migration.

Each phase has a rollback action and a check for mixed-version operation.

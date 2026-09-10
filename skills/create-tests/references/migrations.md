# Migration Tests

Apply the actual versioned migration to representative data from each supported
predecessor. Verify counts, keys, nullability, semantic invariants, and
application reads and writes.

When deployments overlap, test each supported application and schema pairing.
Exercise realistic volume, locks, interruption, retry, and the declared
recovery path when these risks matter.

Do not assume that rollback is safe for a destructive data transformation.

## Example

```text
claim ← a renamed account stays readable during a rolling deployment
oracle ← compatibility contract + migration invariant
cases ← old reader + transition schema | new writer + old reader
data ← representative pre-migration rows keep keys, counts, field values
not proved ← peak-volume lock duration → load rehearsal
```

## Evidence Base

- [Grolinger and Capretz, database schema evolution](https://doi.org/10.1016/j.infsof.2010.10.002)
- [Sadalage and Fowler, evolutionary database design](https://martinfowler.com/articles/evodb.html)

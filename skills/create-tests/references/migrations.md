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
Claim: a renamed account remains readable during a rolling deployment.
Oracle: compatibility contract and migration invariant.
Cases: old reader plus transition schema. New writer plus old reader.
Data: representative pre-migration rows preserve keys, counts, and field values.
Not proved: peak-volume lock duration. Run a load rehearsal.
```

## Evidence Base

- [Grolinger and Capretz, database schema evolution](https://doi.org/10.1016/j.infsof.2010.10.002)
- [Sadalage and Fowler, evolutionary database design](https://martinfowler.com/articles/evodb.html)

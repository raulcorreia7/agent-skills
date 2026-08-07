# Discovery

## Order

1. Read local guidance, existing docs, repositories, manifests, configuration,
   pipeline definitions, and IaC when present.
2. Build initial source and element records from explicit seeds.
3. For each confirmed and authorized provider, select an available read-only
   adapter or tool. Keep each request bounded to one scope and evidence shape.
   If no suitable tool is available, use repository and supplied evidence,
   mark live coverage `unavailable` or `partial`, and record the missing check.
4. Trace material relationships outward until you reach the declared boundary
   or no new material dependency appears.
5. Record unavailable providers, denied scopes, unsupported tools, and stale
   observations in coverage. Keep access within scope.

Do not select a provider-specific adapter before the provider and scope are
confirmed. Keep provider requests separate when that reduces noise. The parent
reconciles all results. A discovery agent never writes project files or changes
external state. Do not substitute remembered platform facts for unavailable
live discovery.

## Example request

> Inspect the authorized provider scope for workloads and material dependencies
> of the seeded API. Return canonical resource IDs, directional relationships,
> review locators, observation time, and coverage limits. Make no changes and
> do not return secret values.

# Audit Domains

Read the section for each selected domain mode; `full` reads all seven.

## project

- Confirm purpose, supported users, owners, entrypoints, interfaces, build and
  run paths, repository boundaries, and generated artifacts.
- Compare manifests, lockfiles, CI, examples, setup instructions, ownership
  files, and recent activity for contradictions or stale signals.
- Inspect repository hygiene, ignored state, archived paths, temporary files,
  duplicated guidance, and undocumented ownership boundaries.
- Treat age as a freshness signal, not proof that material is stale.

## tests

- Map unit, integration, contract, end-to-end, migration, and smoke coverage to
  important behaviour and failure modes.
- Inspect CI selection, retries, quarantine, timing, concurrency, fixture
  ownership, isolation, cleanup, and nondeterministic inputs.
- Separate missing behavioural confidence from a low aggregate coverage number.

## dependencies

- Inspect direct and transitive ownership, lock state, update pressure,
  provenance, licenses, advisories, support status, and unnecessary weight.
- Check that the repository actually uses a dependency before recommending a
  change to it.
- A newer or more popular package is not by itself a reason to replace one.

## security

- Inspect authentication and authorization boundaries, secrets, untrusted
  inputs, injection paths, outbound requests, logs, errors, data retention,
  encryption, abuse paths, and sensitive-data handling.
- Separate exploitability evidence from theoretical weakness, and record
  access or threat-model limits.

## delivery

- Trace build, test, artifact, environment promotion, migration, deployment,
  verification, rollback, and recovery paths.
- Inspect trigger scope, delivery credentials, approvals, concurrency, caches,
  artifact provenance, and generated-file contracts.
- Check that stateful and irreversible delivery operations have explicit
  safety gates.

## infra

- Map infrastructure-as-code ownership, resources, environments,
  configuration, policy, and state boundaries.
- Inspect infrastructure credentials, environment differences, drift signals,
  generated-file contracts, and recovery paths.
- Check that stateful and irreversible infrastructure operations have
  explicit safety gates.

## operations

- Map service objectives, dependencies, failure domains, health signals,
  telemetry, alert ownership, dashboards, runbooks, incidents, capacity,
  retention, and recovery evidence.
- Check whether alerts are actionable and whether operators can correlate a
  symptom with deployment and dependency state.
- Treat cost and performance recommendations as hypotheses until baselined.

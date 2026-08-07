# Live And External Audit Boundaries

Read-only intent does not itself authorize access to production, tenant,
customer, repository-hosting, or other external systems.

Before an external system query:

1. Confirm that the user's request places the system and scope in bounds.
2. Use the least-privilege connector or reviewed tool available.
3. Prefer metadata and narrow queries over content or bulk export.
4. Do not retrieve secrets, credentials, customer data, build logs, artifacts,
   or environment values unless separately required and authorized.
5. Separate live observations from repository declarations and inference.
6. Report unavailable providers and missing coverage. Keep access within scope.

For cloud comparison, record the approved source and scope, the allowed
identifiers, state, and timestamps observed, and the owned declaration each
observation is compared with. Report unmatched declarations and unavailable
evidence separately from supported drift claims.

Never create, update, delete, deploy, publish, run jobs, assign access, change
settings, or trigger side effects during an audit. A compliance assessment or
production security test requires a separately defined authority and method.

# Live And External Systems

Read-only intent doesn't authorize access. Production, tenant, customer,
repository-hosting, and other external systems each need the user's approval
of the system and scope before the first query.

Before and during an approved query:

1. Use the least-privileged connector or reviewed tool available.
2. Prefer metadata and narrow queries over content or bulk export.
3. Leave out secrets, credentials, customer data, build logs, artifacts, and
   environment values unless the user separately approves them.
4. Label each live observation apart from repository declarations and
   inference.

For a cloud comparison, record the approved source and scope, the identifiers,
state, and timestamps observed, and the owned declaration each observation is
compared with. Report unmatched declarations and unavailable providers apart
from supported drift claims.

An audit never creates, updates, deletes, deploys, publishes, runs jobs,
assigns access, changes settings, or triggers side effects. A compliance
assessment or production security test needs its own authority and method.

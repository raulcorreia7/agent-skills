# Change Review

Review the diff for significant risk.

- Read the diff first. Follow callers, schemas, configuration, migrations,
  tests, scripts, generated artifacts, and documentation only as far as you
  need to verify impact.
- Check behaviour, failure paths, data safety, authorization, compatibility,
  rollout, maintainability, and missing confidence that matters. Style is a
  finding only when it creates real risk.
- Use the repository's own validation and CI commands as the checks, and
  leave test scope unchanged.
- Stop when the evidence is proportionate to the risk, or when more
  validation needs new authority, infrastructure, live access, or new tests.

# Architecture Review

Assess the design against its stated outcomes and constraints. Redesign is
outside the default review.

## Checklist

- [ ] The artifact, intended outcomes, scope, constraints, users, and
  available evidence are named. Missing requirements are reported as
  questions, not invented.
- [ ] Boundaries, dependencies, data ownership, data flow, trust boundaries,
  failure domains, and deployment shape are mapped. Operational ownership is
  mapped only as far as the review needs.
- [ ] Each quality attribute that affects the system is assessed:
  correctness, simplicity, evolvability, reliability, security, privacy,
  performance, cost, observability, testability, operability, and migration
  safety.
- [ ] Each named pattern, principle, smell, metric, reference architecture, or
  piece of repository history is treated as a lead to investigate, not as
  proof of quality or a defect.
- [ ] Claims are checked against current code, configuration, diagrams,
  documentation, or approved live evidence where practical.
- [ ] Defects, significant risks, open decisions, and optional improvements
  are kept apart, and each significant finding has the smallest change that
  addresses it.
- [ ] Style preferences appear only when they create a real risk.

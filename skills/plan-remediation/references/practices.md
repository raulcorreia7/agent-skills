# Plan remediation practices

## Evidence map

- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final):
  evidence preservation, containment, eradication, trusted recovery, monitoring,
  and improvement.
- [CISA Federal Incident and Vulnerability Response
  Playbooks](https://www.cisa.gov/resources-tools/resources/federal-government-cybersecurity-incident-and-vulnerability-response-playbooks):
  federal response-playbook rationale.
- [NIST SP 800-40 Rev. 4](https://csrc.nist.gov/pubs/sp/800/40/r4/final):
  vulnerability-remediation lifecycle rationale.
- [NIST SP 800-218 SSDF](https://csrc.nist.gov/pubs/sp/800/218/final):
  root-cause analysis, similar-instance search, risk-based executable checks, CI
  evidence, and recurrence reduction.
- [NIST SP 800-128](https://csrc.nist.gov/pubs/sp/800/128/upd1/final):
  security-focused configuration baselines, controlled changes, monitoring, and
  infrastructure risk reduction.
- [OWASP Secrets Management Cheat
  Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html):
  revocation, rotation, blast-radius review, and audit evidence.
- [Rachatasumrit and Kim, ICSM
  2012](https://doi.org/10.1109/ICSM.2012.6405293) for regression-test and
  refactoring interaction; [Kanewala and Bieman,
  2014](https://doi.org/10.1016/j.infsof.2014.05.006) for oracle limits; and
  [Riaz, Mendes, and Tempero,
  2009](https://doi.org/10.1109/ESEM.2009.5314233) for maintainability-metric
  limits.
- [ISO/IEC/IEEE 15289:2019](https://www.iso.org/standard/74909.html) and
  [ISO/IEC/IEEE 26511:2018](https://www.iso.org/standard/70879.html) for
  documentation ownership, review, publication, and lifecycle maintenance.
  Label implementation inferences; do not reproduce paywalled standard text.

## Codebase example

- **Leakage, `Critical`:** Contain exposure and revoke affected credentials;
  correct the trust boundary with regression evidence; prevent recurrence with
  least privilege, secret scanning, monitoring, and owned control review.
- **No tests around risky behavior, `High`:** Add behavior-focused
  characterization or regression tests; correct the root cause and refactor
  only behind passing evidence; prevent recurrence with risk-selected CI checks
  and test ownership, not arbitrary coverage.
- **Hard dependencies, `Medium`:** Record the failing boundary and protect
  current behavior; introduce the smallest justified seam; add contract tests
  and dependency-lifecycle ownership when evidence supports them.
- **Missing or stale docs, `Medium`:** Add minimum accurate operational or
  interface guidance with an owner; correct current documentation; use
  change-triggered freshness review and lifecycle ownership.

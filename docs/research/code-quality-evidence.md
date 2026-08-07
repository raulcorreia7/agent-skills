# Evidence for High-Quality Code Practices

**Decision:** Define code quality as demonstrated fitness for the software's
contract and risk, not conformance to a universal style or numeric score. Require
observable behavior, explicit boundaries and invariants, focused verification,
security and failure handling, understandable ownership, and evidence from the
real workload. Treat coverage, complexity, defect, review, and delivery measures
as diagnostic proxies rather than quality targets.

This report was reviewed on 2026-08-06. It supports the current `code` skill.
It is not a runtime rules file or a systematic literature review.

## Evidence method

The review prioritizes original peer-reviewed studies and systematic reviews,
formal and industry standards, official specifications and documentation, OWASP
guidance, and first-party engineering accounts. Search results and secondary
summaries were discovery inputs only. Each material claim below links to the
source that owns it.

The security pass reviewed the user-supplied
[OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) on 2026-08-06
and cross-checked the rendered guidance against the canonical working sources at
[`OWASP/CheatSheetSeries` commit
`da4c967e9de854727f72bb2748dd98f76c888b06`](https://github.com/OWASP/CheatSheetSeries/tree/da4c967e9de854727f72bb2748dd98f76c888b06).
The series is a living consensus resource. The pinned revision makes this
review reproducible. Recheck the current rendered version before changing
security policy.

Evidence labels mean:

- **Formal:** a definition, proof framework, or analytical result. It establishes
  logical properties under stated assumptions, not field effectiveness.
- **Empirical-causal:** a controlled intervention or experiment supports a causal
  inference within its setting.
- **Empirical-association:** observational or correlational evidence; confounding
  and transfer limits remain.
- **Synthesis:** a systematic review or meta-analysis whose reliability depends
  on the included studies and review method.
- **Standard/consensus:** a normative requirement or expert consensus. It is an
  authoritative contract, not causal evidence that adoption alone improves an
  outcome.
- **Expert/first-party:** an authoritative design argument or operational account.
  It should be adapted and tested in the target system.

## Compact claim-to-source map

| Area | Supported claim | Evidence and boundary |
| --- | --- | --- |
| Quality model | Product quality is multidimensional; requirements and evaluation should select the characteristics that matter to the product and stakeholders. | **Standard:** [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) defines a nine-characteristic product quality model. It is a reference model, not a single score or proof of quality. |
| Correctness contracts | Preconditions, postconditions, invariants, and compositional reasoning can specify and prove program properties; machine-checked refinement can provide unusually strong assurance for a bounded critical component. | **Formal:** [Hoare, 1969](https://doi.org/10.1145/363235.363259) establishes an axiomatic basis. The [seL4 kernel verification](https://sel4.org/Research/pdfs/sel4-formal-verification-os-kernel.pdf) proves that its C implementation refines its abstract specification while explicitly assuming correct hardware, compiler, assembly, boot code, and specification. Neither source shows that full verification is cost-effective for every program. |
| Verification | Broadly applicable developer verification includes automated functional and structural tests, historical regression cases, static analysis, secret detection, fuzzing, and dependency review, selected by risk. | **Standard/consensus:** [NISTIR 8397](https://doi.org/10.6028/NIST.IR.8397) gives minimum verification guidance and explicitly says it does not cover the totality of verification. |
| Test-first development | TDD often reports quality benefits, but productivity and effect sizes vary materially by context and study. | **Synthesis:** a [2016 systematic review](https://doi.org/10.1016/j.infsof.2016.02.004) found predominantly positive quality results but lower productivity in industrial settings; a [2025 tertiary study](https://doi.org/10.1016/j.infsof.2025.107762) found limited overlap among TDD reviews and warns that their conclusions depend on study selection. This supports verification, not a universal TDD mandate. |
| Coverage | Structural coverage can locate unexecuted code, but high coverage is not strong evidence of fault detection or fewer production defects. | **Empirical-association:** Inozemtseva and Holmes generated 31,000 suites for five Java systems and found only low-to-moderate correlation after controlling for suite size; stronger criteria did not add insight ([ICSE 2014](https://doi.org/10.1145/2568225.2568271)). A later study of 100 open-source Java projects found insignificant project-level and no file-level correlation with post-release bugs ([Kochhar et al., 2017](https://www.microsoft.com/en-us/research/publication/code-coverage-and-post-release-defects-a-large-scale-study-on-open-source-projects/)). Both are context-bound associations, not causal trials. |
| Mutation testing | Selective mutation testing can expose concrete test-suite holes and is more behavior-sensitive than raw coverage, but its score is still a proxy. | **Empirical-association:** a Google study of 15 million mutants found that developers added tests in response and that surviving mutants were coupled with historical real faults. [Petrović et al., ICSE 2021](https://research.google/pubs/long-term-effects-of-mutation-testing/) The retrospective, Google-specific study does not prove a transferable reduction in production defects. |
| Modularity | Decompose around design decisions likely to change and hide each decision behind an interface; decomposition by processing steps can spread change knowledge. | **Expert/canonical comparative design:** [Parnas, 1972](https://doi.org/10.1145/361598.361623) compares two designs and argues for information hiding to improve flexibility and comprehensibility. It also notes possible efficiency tradeoffs under a conventional implementation. |
| Complexity | Complexity measures can correlate with failures within a project, but no metric set is a universal defect predictor. | **Empirical-association:** a study of five Microsoft systems found correlations and project-specific predictive models, while explicitly finding no universally best metric set. [Nagappan, Ball, and Zeller, ICSE 2006](https://doi.org/10.1145/1134285.1134349) McCabe's original measure is a graph property, not a universal maintainability threshold. [McCabe, 1976](https://doi.org/10.1109/TSE.1976.233837) |
| Readability | Human readability judgments have measurable regularities, but automated readability remains a learned proxy tied to annotators, languages, and features. | **Empirical-association:** Buse and Weimer derived a metric from 120 annotators and reported associations with change and defect measures. [IEEE TSE 2010](https://doi.org/10.1109/TSE.2009.70) This does not establish one style for all code or readers. |
| Secure development | Security work belongs throughout design, implementation, verification, release, and vulnerability response, with protected environments and provenance. | **Standard/consensus:** [NIST SP 800-218 SSDF 1.1](https://doi.org/10.6028/NIST.SP.800-218) supplies a risk-based practice vocabulary intended for integration into an SDLC, not a one-size-fits-all checklist. [OWASP ASVS 5.0](https://owasp.org/www-project-application-security-verification-standard/) supplies application-security verification requirements. |
| Memory safety | For new security-sensitive native components, a memory-safe language can remove major vulnerability classes; existing unsafe-language code needs layered prevention and mitigation. | **Empirical-association/first-party:** Chromium attributes about 70% of 912 high or critical security bugs since 2015 to memory unsafety and describes safer languages among its mitigations. [Chromium memory-safety analysis](https://www.chromium.org/Home/chromium-security/memory-safety/) This is one large C/C++ system and does not cover logic, authorization, or design flaws. |
| Trust and input boundaries | Model data flows and trust boundaries. Validate untrusted input for syntactic and domain correctness at an authoritative boundary; keep commands and data structurally separate. | **Consensus:** [OWASP threat modeling](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html), [input validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html), and [SQL injection prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html). Validation is not a substitute for context-appropriate encoding, parameterization, or authorization. |
| Authorization | Enforce authorization on every request, least privilege, and deny by default. | **Consensus:** the [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) states these controls and calls for unit and integration tests. It does not select the application's policy model. |
| Concurrency | Concurrent behavior needs an explicit correctness condition. Linearizability makes each completed operation appear to take effect atomically between invocation and response, preserving real-time ordering. | **Formal:** [Herlihy and Wing, 1990](https://doi.org/10.1145/78969.78972) defines linearizability and proof methods. Linearizability is deliberately strong and is not required by every concurrent or distributed system. |
| Persistent data | Put durable invariants in the authoritative store where possible, and choose transaction isolation from the anomalies the contract must exclude. | **Specification/first-party:** PostgreSQL documents enforced [constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) and how [isolation levels](https://www.postgresql.org/docs/current/transaction-iso.html) admit different anomalies. Gray and Reuter provide the canonical transaction, concurrency-control, and recovery treatment in [*Transaction Processing*](https://books.google.com/books?id=VFKbCgAAQBAJ). Product-specific semantics still govern. |
| Retries and partial failure | Retry only failures expected to be transient; bound attempts, use timeouts and backoff with jitter, and make side-effecting operations idempotent or deduplicated. | **Empirical-causal within a simulation:** Amazon's [backoff-and-jitter simulator](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) shows reduced contention and client work under its model. **Expert/first-party:** [Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) and [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) describe production failure modes. Exact policy remains workload-specific. |
| Performance | Measure representative end-to-end workloads and distributions before optimizing. Speedup is limited by the fraction actually improved, and fan-out makes tail latency increasingly important. | **Formal/analytical:** [Amdahl, 1967](https://doi.org/10.1145/1465482.1465560). **Expert/peer-reviewed systems account:** [Dean and Barroso, 2013](https://doi.org/10.1145/2408776.2408794). Neither supplies a transferable latency target. |
| Dependencies and supply chain | Add a dependency only for a justified capability; evaluate authenticity, maintenance, security response, API compatibility, license, transitive impact, and update path. Preserve inventory and verifiable build provenance. | **Consensus:** [OpenSSF dependency evaluation](https://best.openssf.org/Concise-Guide-for-Evaluating-Open-Source-Software.html), [NIST SSDF](https://doi.org/10.6028/NIST.SP.800-218), [CISA 2025 SBOM minimum elements](https://www.cisa.gov/sites/default/files/2025-08/2025_CISA_SBOM_Minimum_Elements.pdf), and [SLSA 1.2](https://slsa.dev/spec/v1.2/). An SBOM, score, signature, or attestation improves visibility or integrity evidence; none proves absence of vulnerable or malicious behavior. |
| Accessibility | Code-owned web interfaces must preserve perceivability, keyboard operation, visible and sensible focus, programmatic name/role/value, status communication, and error assistance. | **Standard:** [WCAG 2.2](https://www.w3.org/TR/WCAG22/) defines testable conformance criteria. Conformance is page/process-wide; passing an automated scanner alone is not a conformance claim. |
| Observability | Instrument user-visible outcomes and causal diagnostic context; use consistent semantic fields, correlate interactions, and exclude or protect sensitive data. Alert on actionable symptoms, not every internal event. | **Specification/consensus:** [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/general/) standardize telemetry names. The [Google SRE monitoring chapter](https://sre.google/sre-book/monitoring-distributed-systems/) distinguishes symptoms from causes and describes latency, traffic, errors, and saturation. The [OWASP logging guide](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) covers event content, sanitization, secrets, integrity, and failure testing. |
| Review | Review is useful for defect discovery, design discussion, and knowledge transfer, but review counts and participation measures are not established causal quality measures. Keep unrelated concepts in separate review units when practical. | **Empirical, mixed:** McIntosh et al. reported associations between review coverage/participation and post-release defects in three projects ([MSR 2014](https://doi.org/10.1145/2597073.2597076)); a reproduction and Chrome replication found unstable effects and models without review predictors performed as well or better ([Krutauz et al.](https://arxiv.org/abs/2005.09217)). A controlled experiment with 28 professional and graduate developers found that decomposition reduced wrongly reported issues but did not increase defects found or understanding of the rationale ([di Biase et al., 2019](https://doi.org/10.7717/peerj-cs.193)). Rigby and Bird observed convergent lightweight practices and knowledge diffusion across projects ([FSE 2013](https://doi.org/10.1145/2491411.2491444)). |
| Measurement | When a proxy becomes a control target, people can optimize the proxy and distort the underlying work. | **Theory and qualitative evidence:** Campbell described corruption pressure on quantitative indicators in [*Assessing the Impact of Planned Social Change*](https://eric.ed.gov/?id=ED303512); Strathern analyzed audit systems that take on a life of their own ([1997](https://doi.org/10.1017/S1062798700002660)); Austin develops software-relevant measurement-dysfunction models in [*Measuring and Managing Performance in Organizations*](https://books.google.com/books?id=PTymPRAsE-sC). These support safeguards, not abandonment of measurement. |

## OWASP Cheat Sheet Series synthesis

These are the cross-cutting controls that belong in a general code-quality
workflow. Product-, framework-, and language-specific details remain in the
linked sheet; this report does not reproduce their full checklists.

| Boundary | High-yield directive | Pinned canonical source |
| --- | --- | --- |
| Input and injection | Validate untrusted data on the server for expected syntax, length, range, and domain meaning. Prefer positive validation for constrained fields, then use context-specific structured APIs or encoding. For SQL, bind values with parameterized queries; validation alone does not separate code from data. | [Input validation](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Input_Validation_Cheat_Sheet.md), [SQL injection prevention](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.md) |
| Authentication and sessions | Use a maintained identity/session implementation instead of custom cryptography or token formats. Protect credential comparison and recovery, require stronger or repeated authentication for sensitive actions, renew the session identifier after privilege changes, use restrictive cookie attributes, enforce server-side idle/absolute expiry, and invalidate on logout or compromise. | [Authentication](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Authentication_Cheat_Sheet.md), [session management](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Session_Management_Cheat_Sheet.md) |
| Secrets | Keep secrets out of source, ordinary configuration, build output, errors, and logs. Use a purpose-built store and scoped workload identity where available. Own creation, distribution, least privilege, rotation, revocation, expiry, detection, auditing, and exposure response as one lifecycle. | [Secrets management](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Secrets_Management_Cheat_Sheet.md) |
| Security logging | Define risk-based security events and stable fields during design. Record enough when/where/who/what/result context for investigation; sanitize untrusted fields, omit or mask secrets and sensitive data, protect integrity and access, bound resource use, and test logging loss and failure. | [Logging](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Logging_Cheat_Sheet.md) |
| Outbound requests and SSRF | Avoid accepting a complete user-controlled URL when the destination can be selected by identifier. Otherwise allow only the required schemes and destinations, disable redirect following, resolve and validate all destination addresses, and enforce the same egress boundary at the network layer. Reject local, private, link-local, and metadata destinations as the contract requires; account for alternate encodings, IPv4/IPv6, and DNS rebinding. | [SSRF prevention](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.md) |
| File handling | Treat the filename, extension, media type, and content as untrusted. Allow only business-required formats; validate type and signature with maintained parsers, generate storage names, enforce size/count/decompression limits, store outside executable or public paths, authorize access, and scan or transform content when risk warrants it. | [File upload](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/File_Upload_Cheat_Sheet.md) |
| Deserialization | Do not deserialize untrusted native object graphs. Prefer a simple data format with a strict schema and bounded parser. Where legacy object serialization is unavoidable, authenticate the data, allow only expected types, remove gadget-capable dependencies, limit resources, and isolate the operation. | [Deserialization](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Deserialization_Cheat_Sheet.md) |
| Vulnerable dependencies | Inventory direct and transitive components and monitor several reliable disclosure sources where proportionate. For each finding, determine where the component is used, the vulnerable behavior, and the applicable technical risk. Prefer a tested supported upgrade or removal; otherwise validate and track a narrow mitigation, or escalate explicit risk acceptance to the accountable risk owner. | [Vulnerable dependency management](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.md) |

## High-yield directives for an agent skill

The following are conservative design inferences from the evidence above. They
are intentionally conditional on the repository, language, risk, and requested
behavior.

1. **Define observable success before editing.** State required behavior,
   compatibility, invariants, failure behavior, and relevant non-functional
   constraints. Resolve material ambiguity before choosing an implementation.
2. **Inspect the behavior owner and its contracts.** Read the smallest relevant
   call path, data model, tests, interfaces, and local conventions. Preserve
   public behavior and data shape unless change is approved.
3. **Keep one owner for each decision and invariant.** Hide volatile design
   choices behind a small coherent interface. Place validation and durable
   invariants at the authoritative boundary. Avoid parallel sources of truth.
4. **Add structure only for current pressure.** Extract a module or abstraction
   when it hides a real decision, removes real repetition, creates a needed test
   seam, or establishes clear ownership. Do not abstract for hypothetical reuse.
5. **Make the common path easy to read.** Prefer direct control flow, precise
   domain names, explicit units and states, and standard language constructs.
   Use comments for rationale, constraints, and non-obvious consequences rather
   than narrating syntax.
6. **Treat complexity measures as investigation prompts.** Simplify tangled
   branches, excessive state, implicit coupling, and distant effects when direct
   inspection shows comprehension or change risk. Do not refactor solely to meet
   a numeric threshold.
7. **Verify behavior at the cheapest faithful level.** Test normal, boundary,
   invalid, and failure cases that can falsify the contract. Add a regression test
   for a fixed defect when it is stable and proportionate. Use integration,
   property, fuzz, race, load, or formal checks where the failure class warrants
   them. Coverage may reveal gaps; it does not certify the suite.
8. **Design from trust boundaries.** Validate untrusted input for syntax and
   domain meaning before use. Use typed or parameterized APIs that separate code
   from data. Authorize every operation and object; deny by default and grant the
   minimum capability. Keep secrets out of source, errors, and telemetry. Prefer
   a memory-safe language for new security-sensitive native code when ecosystem,
   interoperability, and performance constraints permit it.
9. **Constrain dangerous interpreters and I/O.** Use maintained authentication
   and session facilities with renewal and server-side invalidation. Constrain
   outbound destinations and egress, treat files as hostile content, and avoid
   native deserialization of untrusted objects. Give every accepted format,
   scheme, size, destination, and resource use an explicit business reason.
10. **Specify concurrent and durable state transitions.** Identify ownership,
   atomicity, ordering, consistency, and cancellation requirements. Use native
   synchronization, transactions, uniqueness, referential integrity, and
   idempotency mechanisms instead of check-then-act conventions that race.
11. **Bound failure handling.** Give remote and blocking work deadlines. Retry
    only classified transient failures, with a budget and jittered backoff; make
    repeated side effects safe. Preserve the primary error, release resources,
    and test partial failure and cleanup.
12. **Measure performance before and after.** Use a representative workload,
    environment, input distribution, warmup, and repeated samples. Measure the
    user-relevant end-to-end outcome, including tail latency, throughput, memory,
    and cost as applicable. Optimize the demonstrated bottleneck and retain a
    regression check when the requirement is durable.
13. **Justify every dependency.** Prefer a suitable standard-library or existing
    component, but do not reimplement mature security-sensitive functionality to
    reduce a dependency count. For a new dependency, verify the exact version,
    official source and documentation, maintenance and security response,
    license, compatibility, transitive footprint, safe defaults, and update path.
    Use lockfiles, inventories, integrity/provenance checks, and vulnerability
    monitoring supported by the ecosystem.
14. **Preserve accessibility in code-owned interfaces.** Prefer native semantic
    controls. Verify keyboard-only operation, focus order and visibility,
    programmatic names and state, errors and status messages, text alternatives,
    contrast, zoom/reflow, and pointer alternatives that apply to the change.
    Combine automated checks with keyboard and representative assistive-technology
    checks for material interactions.
15. **Build actionable observability into the behavior.** Emit structured,
    stable events around user-visible outcomes and important state transitions;
    include correlation, result, latency, and reason where useful. Bound
    cardinality and volume, sanitize untrusted fields, exclude sensitive data,
    and ensure telemetry failure cannot break the main operation.
16. **Review the final diff against the contract and risk.** Check correctness,
    data migration and compatibility, trust boundaries, concurrency, failure
    paths, accessibility, observability, and relevant tests. Remove abandoned
    hypotheses and unrelated changes. Use independent specialist review for
    high-impact security, safety, privacy, or data-integrity changes.

## Metric and Goodhart warnings

Use metrics to answer a named question, establish a baseline, find a hotspot, or
detect a regression. Keep the underlying outcome and sampling method visible.
Prefer several independent dimensions and qualitative inspection over one
composite score. The [SPACE framework](https://www.microsoft.com/en-us/research/publication/the-space-of-developer-productivity-theres-more-to-it-than-you-think/)
likewise argues that developer productivity cannot be represented by one
activity measure or dimension; it is an expert measurement framework, not a
causal validation of any metric.

| Proxy | Legitimate use | Misuse to avoid |
| --- | --- | --- |
| Line/branch coverage | Locate code a suite did not execute; compare a focused change with its tests. | A universal percentage target, individual ranking, or a claim that covered behavior is asserted correctly. |
| Mutation score | Probe whether tests distinguish selected synthetic changes; use surviving mutants as concrete review prompts ([Petrović et al.](https://research.google/pubs/long-term-effects-of-mutation-testing/)). | Proof of real-fault detection; ignoring equivalent, trivial, or unrepresentative mutants. |
| Cyclomatic/cognitive complexity | Find control-flow hotspots for inspection within one codebase and tool definition. | Cross-language or cross-project ranking; mandatory refactors based on one cutoff. |
| LOC, churn, file count, or diff size | Estimate review surface and identify unexpectedly broad changes. | Productivity, quality, or minimality targets. Generated code and necessary migrations make counts especially misleading. |
| Defect or vulnerability count | Track discovered classes, severity, recurrence, exposure, and remediation. | Rewarding low discovery, comparing teams with different reporting/testing, or treating absence of reports as absence of defects. |
| Test count/pass rate | Detect regression and failed checks. | Treating many trivial tests or green incomplete suites as assurance. |
| Static-analysis findings | Triage concrete rules with location and confidence; watch recurrence. | Maximizing closure count, equating tool silence with security, or ignoring false negatives and rule coverage. |
| Review count, comments, reviewers, or duration | Inspect workflow load, latency, and anomalous cases. | Reviewer or author performance scores, mandatory comment quotas, or causal claims about product quality. |
| Dependency count, age, popularity, score, SBOM, or signature | Inventory, prioritize investigation, verify identity/provenance, and plan updates. | Automatic trust or rejection. A signed, popular, recent, or high-scoring component can still be unsuitable or vulnerable. |
| Latency/throughput averages | Trend a stable workload and detect gross shifts. | Ignoring workload changes, error responses, resource cost, or the distribution and tail. |
| Delivery frequency or lead time | Understand system-level flow for a stable product context alongside stability and reliability outcomes, as in [DORA's paired throughput/stability model](https://cloud.google.com/resources/state-of-devops). | Individual/team quotas, universal benchmark classes, causal claims from survey associations, or a substitute for value, security, and change risk. |

Practical safeguards follow Campbell, Strathern, and Austin: keep measures
informational where possible; never rank individuals from code proxies; pair a
leading proxy with outcome and harm measures; publish definitions and known blind
spots; audit samples manually; rotate or retire measures that are being gamed;
and revisit a threshold when the technology, workload, or incentive changes.
Compliance thresholds are legitimate when the governing standard and risk call
for them, but the threshold is then a contract boundary, not a complete quality
model.

## Conflicts and uncertainty

- **Modularity versus cost:** information hiding can localize change and improve
  comprehension, while an extra boundary can add allocation, indirection,
  serialization, or deployment cost. Preserve the seam when it owns a real
  decision; optimize its implementation only after measurement.
- **Abstraction versus directness:** deduplication can centralize a contract, but
  premature generalization couples cases that may evolve differently. Repeated
  syntax alone is not sufficient evidence for a shared concept.
- **TDD versus flexible verification:** reviews report contextual quality gains
  and mixed productivity. Require a falsifiable check and regression protection;
  do not require test-first ordering when another verification technique better
  fits exploratory, UI, data, or legacy work.
- **Coverage versus assurance:** low coverage can expose a clear gap. High
  coverage does not establish assertions, oracle quality, concurrency coverage,
  representative inputs, or fault detection.
- **Review benefits versus review metrics:** review supports discussion and
  knowledge flow, but the observed relationship between review measures and
  post-release defects is unstable. Keep review evidence-focused and do not
  optimize participation counts.
- **Reuse versus supply-chain surface:** each dependency adds attack,
  compatibility, and maintenance exposure; reimplementing mature functionality
  also creates defect and security risk. Decide from capability criticality,
  implementation difficulty, and the candidate's evidence—not dependency count.
- **Retries versus overload and duplicate effects:** a retry can recover a
  transient failure or intensify an outage. Deadlines, budgets, jitter,
  idempotency, and load shedding are part of the same decision.
- **Consistency versus availability and latency:** linearizability and serializable
  transactions simplify reasoning but can cost coordination and availability.
  Weaker guarantees are valid only when the user-visible contract defines and
  tolerates their anomalies.
- **Observability versus privacy, cost, and reliability:** more telemetry can
  expose secrets, create cardinality and storage cost, or fail the request path.
  Instrument the questions operators must answer and test degraded telemetry.
- **Readability is reader- and context-dependent:** formatter output and learned
  scores cannot decide whether domain concepts, state transitions, or ownership
  are understandable. Representative human review remains decisive.

## Evidence limits

Software engineering evidence is unusually context-sensitive: language,
toolchain, team, system age, criticality, workload, and measurement choices all
affect results. Much of the field evidence is observational, and several famous
practices rest on formal reasoning or expert consensus rather than controlled
field trials. Standards define defensible requirements but do not show that a
team implemented them correctly. No reviewed source supports universal limits on
function length, file size, complexity, coverage, dependency count, reviewer
count, or change size.

The safest transferable principle is an evidence loop: define the system-specific
contract and risk, make the smallest coherent change, and run the most faithful
affordable check that could falsify success. Preserve explicit residual risk when
the check cannot cover the important failure mode.

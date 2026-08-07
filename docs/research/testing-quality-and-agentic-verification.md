# Testing Quality and Agentic Verification

**Decision:** Treat every test as evidence for a named behavioral claim, not as
a correctness certificate. Prefer the cheapest test that can observe the real
risk, but cross real boundaries when the claim depends on them. Strengthen
important suites with independent oracles and fault-revealing techniques. Let
agents generate and run tests, but do not let the same repair loop silently
rewrite both the implementation and its oracle until they agree.

This targeted review was completed on 2026-08-06 for the repository's
`create-tests`, `code`, and `review` skills. It is not a systematic literature
review. It prioritizes peer-reviewed primary studies, systematic reviews,
standards, and first-party guidance. Agentic software engineering changes
quickly, so model- and benchmark-specific results are not universal effect
sizes.

## Evidence method

Claims were included when they could change a reusable testing directive. A
**strong-evidence** directive has support from a peer-reviewed experiment,
survey, or normative standard that directly studies the mechanism. An
**expert-practice** directive is a conservative design inference from those
sources or authoritative practitioner guidance; it is useful but not proven to
be the uniquely best workflow.

The important distinction is between three questions:

1. **Reach:** Did execution reach the relevant code, state, or boundary?
2. **Oracle:** Would the assertion distinguish correct from incorrect behavior?
3. **Environment:** Did the test exercise the platform, dependency, schedule,
   data shape, and configuration relevant to the claim?

A passing result supports only the intersection of those three answers.

## Strong evidence: claim-to-source map

| Claim | What it supports | Boundary and source |
| --- | --- | --- |
| A test needs a meaningful oracle, not only generated inputs or execution. | State the expected behavior independently of the current implementation. Review assertions as carefully as production code. | The oracle problem is a recognized bottleneck in test automation; specifications, contracts, models, metamorphic relations, and human judgment are different oracle sources. [Barr et al., IEEE TSE 2015](https://doi.org/10.1109/TSE.2014.2372785) |
| Structural coverage is useful for finding unexercised code but is not a sufficient quality or correctness measure. | Use coverage diagnostically; do not prescribe one universal percentage or infer fault detection from it. | After controlling for suite size, coverage had low-to-moderate correlation with mutation effectiveness in 31,000 suites across five Java programs. A separate study of 100 Java projects found insignificant project-level and no file-level correlation with post-release defects. [Inozemtseva and Holmes, ICSE 2014](https://doi.org/10.1145/2568225.2568271), [Kochhar et al., IEEE Transactions on Reliability 2017](https://www.microsoft.com/en-us/research/publication/code-coverage-and-post-release-defects-a-large-scale-study-on-open-source-projects/) |
| Mutation testing evaluates whether a suite detects selected injected faults and can expose weak assertions that coverage misses. | Use focused mutation analysis for high-risk logic or to audit generated tests. Inspect surviving and equivalent mutants; do not treat the score as correctness. | Mutation testing is a mature fault-based adequacy technique, but cost, operator selection, equivalent mutants, and experimental validity remain material. [Jia and Harman, IEEE TSE 2011](https://doi.org/10.1109/TSE.2010.62), [Papadakis et al., *Advances in Computers* 2019](https://doi.org/10.1016/bs.adcom.2018.03.015) |
| Property-based testing can search a much larger input space than a few examples when a stable invariant and valid generator exist. | Add properties for algebraic rules, state machines, round trips, parsing, and boundary-rich domains; retain minimized counterexamples as regressions. | QuickCheck introduced executable properties, generated inputs, custom generators, and case-study evidence, while also documenting pitfalls. The result is technique evidence, not a guarantee that random samples prove a property. [Claessen and Hughes, ICFP 2000](https://doi.org/10.1145/357766.351266) |
| Metamorphic testing helps when exact outputs are expensive or unavailable but relations between executions are known. | Test relations such as permutation invariance, monotonicity, round trips, scale transformations, and semantics-preserving rewrites. | The research survey finds broad application and identifies relation discovery and validation as central challenges. A wrong metamorphic relation is a wrong oracle. [Chen et al., ACM Computing Surveys 2018](https://doi.org/10.1145/3143561) |
| Differential testing can reveal discrepancies without manually specifying every output when independent implementations or modes should agree. | Compare parsers, compilers, protocols, old/new implementations, or optimized/reference paths on defined common inputs. | Csmith's randomized differential testing found more than 325 previously unknown compiler bugs. Results depend on avoiding undefined behavior and on sufficiently independent implementations; shared defects can agree. [Yang et al., PLDI 2011](https://doi.org/10.1145/1993498.1993532) |
| Flaky tests destroy the deterministic interpretation of regression results and have multiple root causes. | Treat nondeterminism as a defect to diagnose. Record seeds, order, timing, schedule, environment, and repeated outcomes; fix isolation or product races rather than normalizing reruns. | The first broad empirical study analyzed 201 likely flake-fixing commits in 51 projects and classified causes and fixes. It does not establish a universal rerun count or quarantine policy. [Luo et al., FSE 2014](https://doi.org/10.1145/2635868.2635920) |
| Regression selection and prioritization trade feedback time against fault-detection opportunity. | A focused test is an early signal, not the final gate. Use conservative impact mapping and fall back to broader suites when the mapping or change boundary is uncertain. | The systematic survey distinguishes minimization, selection, and prioritization and documents their objectives and trade-offs. Safe selection algorithms preserve all tests that may expose a fault under explicit assumptions. [Yoo and Harman, STVR 2012](https://doi.org/10.1002/stv.430), [Rothermel and Harrold, ACM TOSEM 1997](https://doi.org/10.1145/248233.248262) |
| Repeating an ordinary concurrency test samples schedules poorly; controlled schedule exploration makes failures reproducible. | For shared-state or asynchronous behavior, add schedule control/model checking where supported, plus invariants around ordering, cancellation, retries, and idempotency. | CHESS controlled thread scheduling, systematically explored interleavings, and reproduced failures in several substantial systems. Its platform and bounded search do not prove all schedules safe. [Musuvathi et al., OSDI 2008](https://www.usenix.org/event/osdi08/tech/full_papers/musuvathi/musuvathi_html/index.html) |
| Security verification needs risk-selected techniques beyond ordinary functional tests. | Test security requirements and regressions; add static/dynamic analysis, fuzzing, and high-risk penetration testing where applicable. | NIST SSDF PW.8 calls for scoped executable-code testing, security-feature tests, dynamic testing, regression tests for reported vulnerabilities, production-relevant stacks, fuzzing, and risk-based penetration testing. OWASP ASVS provides versioned, testable web-application requirements. [NIST SP 800-218](https://doi.org/10.6028/NIST.SP.800-218), [OWASP ASVS 5.0](https://owasp.org/www-project-application-security-verification-standard/) |
| Test levels answer different questions; isolated tests cannot demonstrate real integration or system behavior. | Select unit, integration, contract, and system tests by the claim and boundary, not by a fixed quota. | ISO/IEC/IEEE 29119 defines common concepts, processes, documentation, and test-design techniques; SWEBOK v4 distinguishes testing levels and objectives. These sources standardize the vocabulary but do not prove a universal “pyramid” ratio. [ISO/IEC/IEEE 29119 series](https://committee.iso.org/sites/jtc1sc7/home/projects/flagship-standards/isoiecieee-29119-series.html), [SWEBOK v4, chapter 5](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf) |
| LLMs can generate executable tests and improve structural coverage, but the demonstrated gains are system- and benchmark-specific. | Use LLM generation as a candidate-production mechanism, then validate compilation, execution, oracle quality, distinct risk, and fault revelation. | TestPilot evaluated 1,684 API functions in 25 npm packages and reported median 70.2% statement and 52.8% branch coverage; it also re-prompted failed tests with error feedback. CODAMOSA improved search-based coverage on many of 486 Python benchmarks by querying an LLM after search plateaued. Neither result establishes semantic correctness of generated assertions. [Schäfer et al., IEEE TSE 2024](https://doi.org/10.1109/TSE.2023.3334955), [Lemieux et al., ICSE 2023](https://doi.org/10.1109/ICSE48619.2023.00085) |
| Execution feedback makes agent correction more grounded, but a passing repository suite can accept an overfit patch. | Preserve independent behavioral checks, inspect the final diff, and distinguish “plausible under visible tests” from “correct.” | SWE-agent shows that concise environment feedback and a purpose-built interface help agents act on code. Program-repair research documents test-suite overfitting and shows that independent generated tests can filter many overfit patches. [SWE-agent, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html), [Yang et al., FSE 2017](https://doi.org/10.1145/3106237.3106274) |
| Agent evaluation is vulnerable when tasks, solutions, tests, or feedback leak into training or adaptation. | Keep evaluation tests inaccessible during the run, separate development from final evaluation, record model/tool versions, and prefer fresh or time-sliced tasks. | Riddell et al. found substantial benchmark/training-corpus overlap and significantly better model performance on contaminated subsets. LiveCodeBench uses continuously collected, time-segmented problems and demonstrates contamination, overfitting, and saturation in traditional code benchmarks. [Riddell, Ni, and Cohan, ACL 2024](https://aclanthology.org/2024.acl-long.761/), [Jain et al., ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/94074dd5a072d28ff75a76dabed43767-Abstract-Conference.html) |

## Expert practice: the smallest defensible testing portfolio

These are conservative inferences, not empirically fixed ratios.

| Risk or claim | First useful evidence | Add when the named boundary matters |
| --- | --- | --- |
| Pure deterministic rule | Example-based unit test | Property tests; focused mutation audit |
| Parser, serializer, or transformation | Round-trip and invalid-input tests | Differential or metamorphic checks; corpus/fuzz tests |
| Database, filesystem, queue, network, framework wiring | Narrow integration test with the real implementation | Contract test for provider/consumer compatibility; system smoke test |
| Public API or event schema | Consumer and provider contract examples | Version-skew and compatibility tests; one real transport path |
| Cross-service user outcome | Component-level tests for local decisions | A small number of system journeys for wiring, deployment, and emergent behavior |
| Bug fix | Focused regression that fails on the known broken behavior when safe | Neighboring boundary/property cases when the root cause is broader |
| Shared state or asynchronous work | Deterministic state-machine assertions | Controlled schedules, race/sanitizer tooling, cancellation and retry cases |
| Schema or data migration | Apply migration to representative prior states and verify invariants | Old/new application compatibility, realistic volume/locks, interruption and recovery rehearsal |
| Security boundary | Requirement-based positive and negative tests | Static/dynamic analysis, fuzzing, dependency/configuration checks, penetration testing |
| Agent-generated implementation | Repository tests and static checks | Independent held-out or newly authored oracle; mutation/property/differential probe |

The common safe action is to start narrow for fast diagnostic feedback and
broaden only where the claim crosses a boundary. A universal mandate such as
“all tests are unit tests,” “always use end-to-end tests,” or “70/20/10” has no
support in the reviewed evidence.

### Migration practice

Migration tests need state, compatibility, and operational assertions, not
only “the migration command exited zero.” Apply the actual versioned migration
from each supported predecessor to representative data; verify row counts,
keys, nullability, semantic invariants, and application reads/writes. Where
deployments overlap, exercise old application/new schema and new
application/transition schema. Rehearse interruption, retry, and the declared
recovery path; rollback is not safe or available for every data transformation.

This is expert practice supported by an exploratory database-evolution study
and Fowler's original evolutionary-database guidance. The study used a simple
schema and therefore does not establish a general effect size. Fowler recommends
version-controlled migration scripts, the same scripts through environments,
application tests after migration, small changes, and transition phases for
compatibility. [Grolinger and Capretz, Information and Software Technology 2011](https://doi.org/10.1016/j.infsof.2010.10.002),
[Sadalage and Fowler, “Evolutionary Database Design”](https://martinfowler.com/articles/evodb.html)

### Flake triage practice

A rerun is diagnostic evidence, not a pass. On a nondeterministic failure:

1. Preserve the first failure, logs, seed, test order, shard, worker count,
   platform, dependency versions, time zone, and timing/schedule clues.
2. Re-run under controlled variants to classify test isolation, order/state
   pollution, time/randomness, resource limits, external dependency, or a real
   product race.
3. Fix the root cause and verify repeated deterministic outcomes. If immediate
   quarantine is necessary to restore signal, record an owner, reason, issue,
   expiry/removal condition, and a separate non-blocking execution lane.
4. Do not make an automatic rerun overwrite the original failing status or let
   an agent label a test flaky from one failure and one pass.

Quarantine mechanics and record shape are expert practice. The evidence strongly
supports treating flakiness as a reliability problem, but it does not establish
one rerun count, duration, or organization-wide policy.

## Directives for `create-tests`

Retain its current focus on the smallest stable observable-boundary test,
distinct risks, deterministic isolation, focused execution, and safe
fail-before-fix validation. Add or clarify:

1. **Name the oracle source.** For every material assertion, identify the
   requirement, public contract, bug reproduction, invariant, reference
   implementation, consumer expectation, or reviewed domain example. Existing
   output is not automatically expected output.
2. **Match the level to the claim.** A mock-based unit test cannot prove wire
   format, database semantics, framework wiring, provider compatibility, or a
   deployed journey. Use the narrowest real boundary that can observe the risk.
3. **Select a strengthening technique deliberately.** Use property testing for
   generative invariants, metamorphic testing for relations without exact
   outputs, differential testing for independent equivalents, mutation testing
   to audit assertions, and fuzzing for untrusted structured inputs. Do not
   require all techniques on every change.
4. **Validate generated tests independently.** Compile and run them; inspect
   assertion meaning, failure messages, determinism, and duplication; make a
   regression fail against the known broken state when safe; for high-risk
   generated suites, add a mutation or held-out behavioral probe.
5. **Preserve randomness as evidence.** Use reproducible seeds, valid generators,
   shrinking/minimization, and retained counterexamples. A fixed seed alone
   turns a property test into one repeatable sample.
6. **Handle flakiness explicitly.** Never weaken assertions, add sleeps, broaden
   timeouts, or normalize reruns without evidence that this addresses the root
   cause. Report quarantine and residual signal loss.
7. **Report evidence limits.** State what the focused command exercised and the
   material boundaries, platforms, schedules, data states, or full-suite gates
   it did not exercise. Coverage is reach evidence, not proof.

### Compact risk-and-case example

```text
Claim: a renamed account remains readable throughout a rolling deployment.
Oracle: public compatibility contract and migration invariant.
Cases:
- old reader + transition schema -> same account fields
- new writer + transition schema -> old reader can still read
- representative pre-migration data -> migrated keys/counts preserved
Checks: focused migration/compatibility suite, then service integration suite
Not proved: production lock duration at peak volume; requires a load rehearsal
```

## Directives for `code`

Retain the current evidence ordering and its warning that a check supports only
the behavior and platform it exercises. Add or clarify:

- Before implementation, map each success criterion and material preserved
  behavior to an oracle and a verification level. An unavailable oracle is a
  requirements gap, not an invitation to assert the current output.
- Run the fastest discriminating check after a coherent edit. After focused
  success, run the repository-prescribed broader gate when shared contracts,
  generated artifacts, migrations, concurrency, security, or cross-component
  behavior changed.
- An agent may use compiler, lint, test, and runtime feedback to repair its
  patch. It must not edit a failing test merely to accept the patch unless the
  requested contract changed; that change requires explicit review of the new
  oracle.
- For a regression, safe fail-before-fix validation shows that the new test is
  sensitive to the known defect. It does not mandate universal TDD and does not
  prove neighboring behavior. Meta-analyses report context-dependent quality
  benefits and no universal productivity benefit. [Rafique and Mišić, IEEE TSE
  2013](https://doi.org/10.1109/TSE.2012.28)
- Stop repair loops that repeat the same failure or oscillate. Preserve the
  first failure and changed evidence, diagnose before another edit, and report
  the unresolved boundary rather than accumulating speculative changes.
- Before handoff, inspect the final diff and test diff together. Remove tests
  that merely restate implementation mechanics, duplicate existing evidence,
  or pass whether the intended fault is present or absent.

## Directives for `review`

Review tests as executable specifications, not as an automatic positive signal.
For each material change:

1. Trace requirement or risk -> oracle -> test level -> executed command ->
   result. Missing links are evidence gaps, not necessarily defects.
2. Check that assertions can fail for the relevant wrong behavior. Flag tests
   that only assert non-crash, mock calls, snapshots without a reviewed
   contract, self-derived expected values, or tautological round trips.
3. Inspect whether test doubles omit the boundary being claimed. Require a real
   integration, provider contract, or system case only when that boundary is
   material.
4. For generated tests, look for copied implementation logic, hallucinated
   requirements, weak exception assertions, over-mocking, duplicate coverage,
   and repair-loop accommodation. Seek an independent oracle for consequential
   claims.
5. For test selection, verify impact-map assumptions and that uncertain shared
   changes fall back to broader gates. “Focused tests pass” is not evidence that
   the full prescribed suite ran.
6. For flake changes, require the original failure evidence, classified cause,
   and proof that the fix controls the cause. Treat sleeps, retries, timeout
   inflation, and silent quarantine as suspect masking.
7. For migrations, review predecessor states, compatibility window, data
   invariants, volume/locking, interruption, retry, recovery, and staged
   observability. For concurrency, review schedules, cancellation, idempotency,
   ordering, and race-tool evidence. For security, trace tests to versioned
   requirements and trust boundaries.
8. Report passing checks precisely and retain residual risk. Do not convert
   coverage, mutation score, test count, or an agent benchmark score into a
   correctness claim.

## Bounded agent verification loop

Use this loop when an agent generates tests or repairs code from test feedback:

```text
contract / risk
  -> independent oracle and selected test level
  -> candidate test or patch
  -> execute the narrowest discriminating check
  -> classify product, test, environment, or specification failure
  -> make one evidence-driven correction
  -> re-run the same check
  -> run required broader and independent checks
  -> inspect final implementation and tests together
```

Operational guardrails:

- Keep a bounded attempt budget or stop on repeated/oscillating evidence. The
  exact number is workload-specific; the semantic stop condition matters more.
- Record command, environment, seed, first failure, subsequent evidence, and
  files changed. Do not present only the final green run.
- Separate the candidate-producing context from decisive held-out evaluation.
  Do not reveal hidden tests or their exact feedback to the repair loop.
- When one agent creates both implementation and tests, obtain independence
  from a specification, preexisting tests, a human-reviewed oracle, mutation,
  a reference implementation, or a separately held-out evaluator. A second
  instance of the same model is not automatically an independent oracle.
- In evaluations, freeze model, prompt, tools, budget, repository commit,
  dependencies, and hardware-relevant settings; report repeated-run variance,
  invalid tasks, and pass criteria. Prefer fresh time-sliced tasks and keep
  evaluation data out of training and prompt optimization.

## Metrics that help without becoming targets

| Metric | Useful interpretation | Invalid inference |
| --- | --- | --- |
| Statement/branch coverage | Code not reached; change in exercised structure | High percentage means the behavior is correct |
| Mutation score | Sensitivity to the selected mutation operators | All real faults would be detected |
| Test count | Inventory and maintenance signal | More tests mean more confidence |
| Pass rate | Outcome under this suite and environment | No relevant defects exist |
| Flake/retry rate | Signal reliability and nondeterminism trend | A rerun pass invalidates the first failure |
| Runtime | Feedback cost and gate placement input | Slow tests are inherently more valuable |
| Agent resolve rate | Outcome on the exact benchmark and harness | General software-engineering ability or safe autonomy |

Use metrics in a balanced risk-and-case review. If a metric becomes a gate,
pair it with protections against gaming: assertion review for coverage,
equivalent-mutant handling for mutation, and fresh held-out tasks for agents.

## Anti-patterns

- Assert the implementation's output against a copy of the same implementation.
- Ask an LLM for both the requirement and the test oracle when an authoritative
  contract exists elsewhere.
- Accept generated tests because they compile, pass, or raise coverage.
- Let an agent change production code and failing tests repeatedly without
  preserving which contract changed.
- Mock the database, serializer, transport, framework, or provider and claim
  that its real integration works.
- Duplicate the same happy path at every test level while leaving failure,
  compatibility, security, data, and concurrency risks untested.
- Set an organization-wide coverage percentage, mutation score, unit/system
  ratio, or rerun count as a proxy for adequacy.
- Delete, skip, quarantine, retry, sleep, or inflate timeouts until a flaky gate
  turns green.
- Run only selected tests after changes to shared schemas, configuration,
  generated code, dependency versions, or broad runtime behavior when impact
  analysis is uncertain.
- Treat random stress repetition as systematic concurrency coverage.
- Test a migration only from an empty database or only at the final schema.
- Put visible evaluation tests in the agent's repair context, tune on the test
  set, or compare agents using different budgets, tools, commits, or invalid-task
  filtering.

## Conflicts, uncertainty, and limits

- **Test distribution:** Standards define levels, not an optimal ratio. The
  popular test pyramid is useful expert guidance, not a validated universal
  law. Architecture, failure cost, boundary ownership, runtime, and observability
  should determine the portfolio.
- **Mutation:** Stronger than raw reach for auditing assertions, but operator
  representativeness, equivalent mutants, runtime cost, and weak-mutant bias
  limit comparisons. Use it as another probe, not the final oracle.
- **Property, metamorphic, and differential testing:** These techniques move
  oracle work into properties, relations, generators, or comparison systems.
  They do not remove it. Shared defects, invalid domains, and false relations
  can yield confident false negatives or positives.
- **Flake handling:** Root causes are well documented; ideal quarantine and
  rerun policies remain context-dependent. A flaky test can also expose a real
  race or resource defect in the product.
- **LLM-generated tests:** Peer-reviewed studies show promising execution and
  coverage outcomes on specific languages and packages. Evidence for durable
  maintainability, oracle correctness, real-bug detection, and performance
  across current models is less mature and changes rapidly.
- **Repair loops:** Execution feedback is more grounded than unaided
  self-critique, but visible-suite success encourages overfitting. No static
  prompt rule makes a test suite complete; independent and held-out evidence is
  still necessary.
- **Agent benchmarks:** Measured corpus overlap and performance inflation make
  contamination a demonstrated risk, while fresh time splits reduce but do not
  remove indirect leakage, benchmark-specific tuning, harness defects, or task
  invalidity. Report benchmark-local results and preserve evaluation provenance.
- **Security and migrations:** The reviewed standards and practitioner guidance
  define strong process expectations, but exact techniques depend on threat
  model, platform, data criticality, rollout, and recovery constraints. These
  require specialist review when consequential.

## Repository recommendation

Keep `create-tests` as the owner of test design and generated-test validation,
`code` as the owner of evidence-driven implementation checks and bounded repair,
and `review` as the independent evaluator of oracle quality and missing risk
boundaries. Do not duplicate the literature or technique catalog into all three
skills. Put the compact oracle/level/limits contract in `create-tests`, point
`code` to it when tests are material, and give `review` a concise test-evidence
checklist.

The release criterion for these skill changes is not instruction count. It is
whether representative cases cause the agent to select a valid oracle, choose
the smallest level that observes the risk, preserve independent evaluation,
handle flakiness without masking, and describe precisely what the executed
checks do and do not support.

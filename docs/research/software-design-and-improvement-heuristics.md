# Software Design and Improvement Heuristics

**Decision:** Use a small set of conditional design heuristics, not a pattern
catalog, smell-removal checklist, or universal scoring system. Solve the current
requirement, hide consequential decisions behind coherent interfaces,
generalize only for a known seam or repeated change pressure, and improve code
in small reviewable steps. Treat patterns, smells, duplication, coupling,
cohesion, and change history as prompts to inspect a concrete risk. Follow the
owning ecosystem and repository contracts. Treat a public interface change as a
compatibility decision, not a local cleanup.

This synthesis was completed on 2026-08-07 for maintainers of the repository's
agent code-writing skill.

## Research frame

- **Question:** Which portable heuristics should guide ordinary software design,
  improvement, pattern selection, API consistency, and avoidance of
  overengineering?
- **Audience:** Maintainers who need useful defaults without turning an agent
  into a pattern applier, style enforcer, or speculative framework builder.
- **As-of date:** 2026-08-07.
- **Source boundary:** Peer-reviewed systematic reviews, controlled experiments,
  repository and industrial studies, foundational papers and original authors,
  plus first-party operational guidance from Google, Microsoft, Rust, and
  Abseil. The sources were selected to clarify contracts, observed effects, and
  trade-offs; this is not an exhaustive systematic review.
- **Exclusions:** Control-flow syntax, formatting, naming, comments, and
  expression-level readability are in [Readable Control
  Flow](readable-control-flow-and-code-style.md). General quality models,
  complexity and coverage, security, performance, and dependency evidence are
  in [Evidence for High-Quality Code Practices](code-quality-evidence.md).
  This report uses only the human and structural studies needed to evaluate
  modularity, patterns, refactoring, duplication, and API shape. Verification
  depth and test selection are in
  [Testing Quality and Agentic Verification](testing-quality-and-agentic-verification.md).
  This report does not re-evaluate those evidence bases.
- **Evidence standard:** A source can establish its own design argument,
  specification, or operational policy. It cannot by itself establish that the
  advice causes better outcomes in every language, team, or system.

Evidence labels used below:

- **Foundational:** an original scholarly design argument or comparison.
- **Formal:** a proof, semantics, type system, or static analysis establishes a
  property under stated assumptions; it does not by itself establish a human or
  maintenance outcome.
- **Controlled:** an experiment can support a causal inference for its studied
  task and population, not an unrestricted language-independent rule.
- **Empirical-association:** an observational or repository study reports an
  association; it does not establish that changing the measured property causes
  the outcome.
- **Synthesis:** a systematic review aggregates a bounded, heterogeneous
  literature and inherits the limitations of its primary studies.
- **Original-author:** guidance from an author associated with the named idea.
- **First-party practice:** an organization or ecosystem documents how it
  designs or reviews its own software.
- **Inference:** a proposed portable rule synthesized from the sources.

## Findings

### Put boundaries around knowledge that is likely to change

Parnas compared two decompositions of the same system and argued that modules
should hide design decisions, not merely mirror processing steps. His paper
reports expected benefits for independent development, comprehensibility, and
change, while also acknowledging that the information-hiding decomposition can
be less efficient under conventional subroutine implementation. This is a
foundational comparative argument, not a modern controlled field study.
[Parnas, *Communications of the ACM*, 1 December
1972](https://doi.org/10.1145/361598.361623)

Ousterhout's “deep module” formulation expresses the related goal as a large
amount of useful behavior behind a small interface. His course material also
recommends comparing more than one design for important interfaces. These are
original-author teaching principles, not measured universal effects.
[Designing Abstractions, Stanford](https://web.stanford.edu/~ouster/CS349W/lectures/abstraction.html),
[Ousterhout's book page, updated 16 November
2021](https://web.stanford.edu/~ouster/cgi-bin/book.php)

**Inference:** Add a boundary when it hides a real decision, invariant,
dependency, or source of change. Judge a module by how much complexity callers
avoid, not by file count, method count, or conformance to a preferred shape.
For consequential interfaces, compare at least two plausible designs before
committing to one.

### Reconcile useful generality with YAGNI

Ousterhout distinguishes reusable building blocks, which benefit from clean
and orthogonal generality, from one-use modules, which should remain specific;
his course notes recommend specialization when uncertain and generalization
when reuse appears. Fowler's YAGNI essay rejects capability and abstraction
built only for a presumed future requirement, especially when it makes current
code harder to understand. Fowler also states that YAGNI is not a reason to
neglect code health: refactoring and changeability enable incremental design.
[Ousterhout, Managing Modularity](https://web.stanford.edu/~ouster/cgi-bin/cs190-spring15/lecture.php?topic=complexity),
[Fowler, “Yagni,” 26 May 2015](https://martinfowler.com/bliki/Yagni.html)

**Inference:** Generalize for an already shared responsibility, stable public
contract, repeated change, or required test/ownership seam. Keep a one-use
implementation specific when the only benefit is hypothetical flexibility.
This resolves the apparent conflict: deep design reduces the complexity of a
needed capability; YAGNI rejects extra capability and speculative variation.

### Use named principles as questions, not as a scorecard

SOLID is a useful vocabulary for discussing responsibility, extension,
substitutability, interface size, and dependency direction. Its original
sources are design arguments, not a validated bundle whose adoption generally
reduces defects or maintenance effort. A 2024 experiment with 100 data
scientists reported moderate perceived-understanding effects for SOLID-oriented
machine-learning code, but it changed several structural properties together
and did not measure modification correctness, elapsed maintenance time, or
long-term evolution. No broad, high-quality systematic review validating the
whole bundle was located. [Martin, “Design Principles and Design Patterns,”
2000](https://objectmentor.com/resources/articles/Principles_and_Patterns.pdf),
[Cabral et al., CAIN 2024](https://doi.org/10.1145/3644815.3644957)

One principle does have a formal correctness core: behavioral subtyping
requires properties proved about a supertype to remain true for its subtypes;
matching method signatures alone is insufficient. Controlled inheritance
experiments remain task-dependent: flat designs were easier in some maintenance
tasks, inheritance helped another, and another result was null. [Liskov and
Wing, ACM TOPLAS 1994](https://doi.org/10.1145/197320.197383), [Harrison,
Counsell, and Nithi, JSS
2000](https://doi.org/10.1016/S0164-1212(99)00144-2), [Freeman and Schach, JSS
2005](https://doi.org/10.1016/j.jss.2004.05.010)

**Finding:** Use SOLID and similar catalogs to ask whether ownership,
substitutability, interface burden, or dependency direction is wrong. Do not
optimize a principle count. Use inheritance only for a genuine substitutable
relationship whose behavior and invariants clients can rely on; otherwise
prefer composition or delegation. “Composition over inheritance” remains a
soft design preference, not a ban or a numeric inheritance-depth limit.

### A design pattern is a candidate explanation, not a requirement

The original design-pattern paper presents patterns as a way to identify,
name, and abstract recurring themes in object-oriented design, including their
intent, collaborations, and responsibilities. It records design experience and
supplies vocabulary; it does not show that applying more patterns improves a
system or that its object-oriented forms transfer unchanged to every language.
[Gamma, Helm, Johnson, and Vlissides, ECOOP 1993, pp.
406–431](https://doi.org/10.1007/3-540-47910-4_21)

**Inference:** Name or introduce a pattern only after identifying the recurring
problem, context, forces, and consequences it explains. Prefer a native
language or framework facility when it already solves the problem. Reject a
pattern when it adds participants, indirection, or extension points without
current pressure.

The empirical literature makes that inference more important. A 2012
systematic review screened 611 candidates and retained 10 papers containing 11
formal experiments, plus seven experience reports. It found some evidence that
GoF patterns provide a maintenance framework, but also qualitative evidence
that they did not necessarily help novices learn design. A later review of 50
primary studies found contradictory, difficult-to-compare results across
patterns and quality attributes; pattern documentation, class size, and
scattering materially affected the observations. [Zhang and Budgen, IEEE TSE
2012](https://doi.org/10.1109/TSE.2011.79), [Wedyan and Abufakher, IET Software
2020](https://doi.org/10.1049/iet-sen.2018.5446)

A controlled experiment with 29 professional C++ developers illustrates the
boundary. Pattern-based solutions were faster or safer for some maintenance
tasks, slower for others, and neutral or inconclusive elsewhere. For one
Observer task, the patterned version was 151% slower before pattern training;
for a change that matched Observer's extension point, it was 29% faster. A
family of four experiments with 88 professionals and students found that
documenting pattern instances improved comprehension correctness for readers
with adequate experience. [Prechelt et al., IEEE TSE
2001](https://doi.org/10.1109/32.988711), [Scanniello et al., ACM TOSEM
2015](https://doi.org/10.1145/2699696)

**Finding:** Pattern names are useful vocabulary when they explain a real
mechanism and expected change. Pattern presence or count is not a quality
measure. When a non-obvious pattern matters to maintenance, record its local
intent and the flexibility it purchases.

### Keep functional design practices opt-in

Functional techniques provide transferable mechanisms, but their evidence is
not a warrant for making an application “functional” by default. A 2023
systematic review of functional-programming-oriented software design retained
only 14 primary studies from 2012–2022 and described the area as little
explored. Much of the stronger literature establishes language semantics,
static guarantees, or worked design arguments rather than comparative
maintenance outcomes. [Camarillo-Villa et al., CONISOFT
2023](https://doi.org/10.1109/CONISOFT58849.2023.00015)

Pure computation and explicit effects have a formal reasoning basis. Moggi's
computational lambda calculus distinguishes value-producing functions from
computations such as state, exceptions, and nondeterminism so program
equivalence can account for those behaviors. Lucassen and Gifford's effect
system statically computes a conservative approximation of the side effects an
expression can have. These papers establish semantic and analysis properties;
they do not measure everyday readability, debugging time, or long-term
maintainability. [Moggi, *Information and Computation*
1991](https://doi.org/10.1016/0890-5401(91)90052-4), [Lucassen and Gifford,
POPL 1988](https://doi.org/10.1145/73560.73564)

“Functional core, imperative shell” is a practitioner decomposition that puts
deterministic decisions over values in a core and I/O, storage, and other
effects in a surrounding shell. Its original worked example reports easier
isolated testing and fewer conditionals in the shell; it is not a controlled
comparison or a universal architecture. [Bernhardt, *Functional Core,
Imperative Shell*, 12 July
2012](https://www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-shell)

Immutability has similarly bounded evidence. In a controlled study with 20
Java programmers, participants using a tool that enforced transitive class
immutability generally completed the studied tasks without the mutation errors
made by every participant relying on Java's `final`; the authors also applied
the tool to two existing components. The paper explicitly states that it did
not establish when designing components to be immutable is beneficial, and
notes limits including simple tasks, a narrow participant population, delayed
initialization, circular structures, and external effects. [Coblenz et al.,
ICSE 2017](https://doi.org/10.1109/ICSE.2017.52)

Closed data variants and exhaustive matching can make missing cases visible to
a supporting compiler. Maranget formally defines useless and non-exhaustive
pattern clauses and supplies an algorithm implemented for OCaml and applicable
to Haskell. This is a compiler-analysis result, not evidence that every domain
has a closed state space. Turner's total-functional-programming discipline
likewise gives strong termination and error-freedom properties, but deliberately
restricts expressiveness and reports that some algorithms become inconvenient.
[Maranget, *Journal of Functional Programming*
2007](https://doi.org/10.1017/S0956796807006223), [Turner, *Journal of
Universal Computer Science*
2004](https://doi.org/10.3217/jucs-010-07-0751)

Higher-order functions, composition, folds, and pipelines can encode recurring
transformation structure directly. Hughes argues through worked examples that
higher-order functions and lazy evaluation provide modular “glue”; Gibbons
shows that some object-oriented patterns can instead become typed, reusable
higher-order library abstractions. These are design and expressiveness
arguments, not demonstrations that dense chains, point-free expressions, or a
functional-pattern catalog improve comprehension. [Hughes, *The Computer
Journal* 1989](https://doi.org/10.1093/comjnl/32.2.98), [Gibbons, WGP
2006](https://doi.org/10.1145/1159861.1159863)

**Finding:** Consult functional techniques only when the user requests them,
the repository already establishes them, or a concrete design proposal makes
their trade-off relevant. Then prefer immutable values for a demonstrated
aliasing or state risk, expose consequential effects at a clear boundary,
model genuinely closed alternatives so supported exhaustiveness checks can
help, and return absence or failure explicitly when it belongs to the
contract. Use composition or pipelines only while their stages and control flow
remain obvious. Do not impose application-wide purity, immutability, totality,
effect abstractions, or a functional pattern catalog. Keep necessary mutation
and effects close to their owner, and prefer direct code when a functional
abstraction adds unfamiliar jargon, hidden control flow, or debugging
indirection for the maintainers who own the code.

### Extract coherent concepts, not merely shorter functions

Direct human studies do not support a universal small-function rule. In a 2024
experiment, decomposing two Java operations helped some comprehension measures
for one operation, hurt them for the other, and did not reliably reduce reading
time. A separate experiment found that extracting Java methods helped novices
substantially on difficult tasks but added navigation cost and hurt them on
simple tasks. [Tempero et al., ICPC
2024](https://doi.org/10.1145/3643916.3644432), [da Costa et al., JSS
2026](https://doi.org/10.1016/j.jss.2026.112825)

**Finding:** Extract a helper or module when its name creates a coherent domain
concept, it hides knowledge, or it supports real reuse, ownership, testing, or
change. Do not extract solely to meet a length target. Avoid pass-through layers
that make readers traverse more units without hiding useful complexity.

### Assess cohesion and coupling together

A small controlled maintenance experiment found no significant main effect for
coupling or cohesion alone, but did find a significant interaction between
them. In a longitudinal study of 233 releases from 10 systems, automated
remodularization could improve the selected structural fitness measures, but it
changed more than 57% of system structure on average; developers' actual changes
avoided that disruption. [Darcy et al., IEEE TSE
2005](https://doi.org/10.1109/TSE.2005.130), [Paixao et al., IEEE Transactions
on Evolutionary Computation
2018](https://doi.org/10.1109/TEVC.2017.2691281)

Coupling measures have identified fault-prone classes within individual
systems, including after size control, while specific cohesion measures have
failed in the same studies. The metric definitions, languages, systems, and
outcomes differ, so the result supports local investigation rather than a
portable threshold. [Basili, Briand, and Melo, IEEE TSE
1996](https://doi.org/10.1109/32.544352), [El Emam et al., NRC validation
study](https://nrc-publications.canada.ca/eng/view/object/?id=94d7b739-8ff0-4eb0-872f-22e02cf34767)

**Finding:** Keep responsibilities that change together near each other and
avoid dependencies that make a change spread. Inspect both sides of that
trade-off and the compatibility cost of moving code. Use coupling or cohesion
scores to locate a question, not to decide the design.

### Treat duplication as a synchronization risk, not an automatic violation

Clone evidence is deliberately mixed. A case study of five commercial and
open-source systems found 107 confirmed faults among inconsistent clone groups.
A release-level replication found that only 1.02% to 4.00% of clone genealogies
introduced defects in three open-source systems. A later study of five
open-source and three industrial systems classified 61.0% to 84.7% of clones as
not harmful under its consistent-maintenance-overhead criterion. These studies
use different histories, granularities, and definitions of harm. [Juergens et
al., ICSE 2009](https://doi.org/10.1109/ICSE.2009.5070547), [Bettenburg et al.,
Science of Computer Programming
2012](https://doi.org/10.1016/j.scico.2010.11.010), [Hu et al., SANER
2021](https://doi.org/10.1109/SANER50967.2021.00029)

A replicated developer study gives the mechanism a human interpretation:
participants completed fewer repairs when a bug was cloned, while being shown
the clone locations improved complete repairs. [Chatterji et al., WCRE
2013](https://doi.org/10.1109/WCRE.2013.6671286)

**Finding:** Consolidate copies when they encode the same rule or create one
change obligation that must stay synchronized. Tolerate or explicitly track
intentional copies when they have independent lifecycles or when a shared
abstraction would create the tighter dependency. Repeated syntax alone does not
establish a shared concept.

### A smell identifies a question, not a required refactoring

In a field experiment with six professional developers maintaining four
functionally equivalent Java systems, none of 12 smells significantly increased
effort after adjustment for file size and number of changes. Those two controls
explained nearly all modeled effort. A three-system repository study likewise
found small, smell-specific effects that sometimes reversed direction across
systems. [Sjøberg et al., IEEE TSE
2013](https://doi.org/10.1109/TSE.2012.89), [Hall et al., ACM TOSEM
2014](https://doi.org/10.1145/2629648)

A systematic review of 76 refactoring studies found much stronger evidence for
changes in internal metrics than for external outcomes such as maintainability
or reliability. Only 10 of the 76 studies statistically tested metric changes,
and different refactorings sometimes moved quality attributes in opposite
directions. A 25-project longitudinal study found that 95.1% of detected
refactorings neither removed nor introduced a detected smell. [Al Dallal and
Abdin, IEEE TSE 2018](https://doi.org/10.1109/TSE.2017.2658573), [Cedrim et
al., SBES 2016](https://doi.org/10.1145/2973839.2973848)

**Finding:** Require a concrete objective before refactoring: localize a rule,
make an expected change safer, improve a test seam, remove a demonstrated
confusion, or correct an actual compatibility or fault risk. Verify that
objective afterward. A lower smell count or internal metric proves only that
the selected detector or metric changed.

### Use history to prioritize attention, not to punish change

Change history often predicts faults better than static structure within one
project. A study of a large long-lived system found that recent and large
changes predicted future fault incidence better than code length or static
complexity. A Windows Server study found relative churn useful within that
product, while absolute churn was a poor predictor. Mining co-change histories
has also produced useful change-location suggestions in eight open-source
projects. [Graves et al., IEEE TSE
2000](https://doi.org/10.1109/32.859533), [Nagappan and Ball, ICSE
2005](https://doi.org/10.1145/1062455.1062514), [Zimmermann et al., IEEE TSE
2005](https://doi.org/10.1109/TSE.2005.72)

**Finding:** Give recently changed, widely changed, or historically co-changing
code proportionate review and verification. Do not treat churn as misconduct or
technical debt: necessary fixes, migrations, and risk reduction also create
churn, and the studies are predictive rather than causal.

### Make the common interface path discoverable

In a counterbalanced study with 10 Java programmers, placing or referencing an
operation on the class that programmers naturally explored reduced
object-combination time by factors between 2.4 and 11.2 across three tasks.
Another 12-person study found that all participants first tried constructors;
factory-only construction cost more time and produced more failures in two
construction tasks, although a debugging task did not show that disadvantage.
[Stylos and Myers, ESEC/FSE
2008](https://doi.org/10.1145/1453101.1453117), [Ellis et al., ICSE
2007](https://doi.org/10.1109/ICSE.2007.85)

**Finding:** Expose a direct common-case operation from the type, module, or
namespace where a user naturally starts. Require a helper, builder, factory, or
multi-step protocol when it carries necessary construction, lifecycle,
validation, or compatibility semantics, not merely because the pattern exists.

### Improve continuously in small, behavior-aware steps

Fowler defines refactoring as restructuring through small transformations that
preserve observable behavior; the second edition of his book is dated 2018.
Google's canonical code-review policy favors approval once a change definitely
improves overall code health, even if it is not perfect, and says technical
facts and data outrank personal preference. Google also advises separating a
major style-only change from a functional change because combination obscures
review and complicates merges and rollbacks. These are an original-author
method and a first-party operating policy, not causal estimates.
[Fowler, *Refactoring*, second edition,
2018](https://martinfowler.com/books/refactoring.html),
[Google code-review standard](https://google.github.io/eng-practices/review/reviewer/standard.html),
[Google review checklist](https://google.github.io/eng-practices/review/reviewer/looking-for.html)

**Inference:** Prefer the smallest coherent improvement that preserves the
approved contract and can be reviewed and verified. Do not require unrelated
perfection. Keep mechanical style churn separate when practical, and explain
substantive design requests with a contract, risk, or engineering principle.

### Consistency reduces surprise, but local style is not a universal design law

The Rust API Guidelines describe themselves as recommendations based largely on
the library team's standard-library and ecosystem experience. They explicitly
say they are not a mandate and vary in firmness; their checklist emphasizes
predictability, naming, flexibility, type safety, dependability, and
future-proofing. Microsoft's .NET Framework Design Guidelines similarly seek a
consistent, easy-to-use programming model, distinguish `DO`, `CONSIDER`,
`AVOID`, and `DO NOT`, and acknowledge that good design can require a
violation. These are ecosystem-specific first-party practices.
[Rust API Guidelines](https://rust-lang.github.io/api-guidelines/),
[Rust API checklist](https://rust-lang.github.io/api-guidelines/checklist.html),
[Microsoft Framework Design
Guidelines](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/)

Google's review standard makes its style guide authoritative for Google code,
treats unspecified style as preference, and falls back to existing-code
consistency only when that does not worsen code health. It also says software
design is almost never merely a style question.
[Google code-review standard](https://google.github.io/eng-practices/review/reviewer/standard.html)

**Inference:** Follow checked-in formatters, analyzers, language conventions,
public API idioms, and nearby code unless a correctness, compatibility, or
maintainability reason justifies divergence. Keep repository conventions
authoritative for style; do not use “consistency” to preserve a demonstrably
harmful design.

### Public interfaces turn cleanup into compatibility work

Abseil states that it generally avoids backward-incompatible C++ API changes
and that, at its scale, every change is potentially breaking for some user. It
defines the surface to which that policy applies and distinguishes public APIs
from implementation details. Microsoft classifies library changes by source,
binary, and behavioral compatibility and notes that some otherwise desirable
changes require judgment. Both are first-party policies within their own
ecosystems, not universal laws.
[Abseil Compatibility Guidelines](https://abseil.io/about/compatibility),
[.NET library change rules](https://learn.microsoft.com/en-us/dotnet/core/compatibility/library-change-rules)

**Inference:** Before changing a public interface, identify its consumers and
documented behavior, then assess source, binary, data, and behavioral
compatibility as applicable. Preserve the interface by default. If a breaking
change is approved, provide a proportionate migration path instead of disguising
it as an internal refactor.

## Compact evidence map

| Proposed heuristic | Support state | Source status and applicability limit |
| --- | --- | --- |
| Hide consequential decisions behind coherent interfaces. | Supported as a design principle; outcome size is not quantified. | **Foundational/original-author:** Parnas 1972 and Ousterhout course material. Examples are mostly modular and object-oriented designs. |
| Generalize only for known pressure or a stable reusable seam. | Supported as a reconciliation of two expert arguments. | **Original-author:** Ousterhout and Fowler. The exact threshold remains project-specific. |
| Treat SOLID and similar catalogs as questions, not compliance scores. | Candidate review vocabulary; the bundle lacks broad effectiveness evidence. | **Original-author/controlled:** one narrow ML-code experiment changed several properties together. Formal behavioral-subtyping evidence applies to correctness, not general maintainability. |
| Match a pattern to its recurring problem and consequences; do not pattern-match by name alone. | Supported in specific maintenance contexts, with positive, negative, and null findings. | **Synthesis/controlled:** GoF evidence is small, heterogeneous, object-oriented, task-dependent, and sensitive to reader experience. |
| Apply functional techniques only when requested, established locally, or justified by a concrete proposal. | Supported for specific semantic guarantees; general maintenance benefit remains unresolved. | **Formal/controlled/original-author:** effect, exhaustiveness, and totality results establish bounded properties; one small immutability study supports compiler enforcement for its tasks; architectural and composition claims are design arguments. |
| Extract only around a coherent concept or real seam. | Directly supported as a conditional rule; no universal small-function benefit. | **Controlled:** two small Java studies with students or novices reported task-dependent benefits and navigation costs. |
| Assess cohesion and coupling together; use their metrics for investigation. | Corroborated hotspot heuristic, not a quality gate. | **Controlled/empirical-association:** measures and effects vary by system; mechanical optimization can require disruptive restructuring. |
| Consolidate copies when they share one change obligation. | Supported as a synchronization-risk heuristic; blanket DRY is contradicted. | **Controlled/empirical-association:** inconsistent clones can cause missed fixes, while several field studies find most clones non-harmful under their measures. |
| Refactor for a concrete observed objective, not to remove a smell or lower a score. | Strong caution; external outcome benefits remain unresolved. | **Synthesis/controlled/empirical-association:** smell effects are small and contextual; most refactoring studies measure internal proxies. |
| Use churn and co-change to prioritize review and tests. | Supported within studied projects as a predictive signal. | **Empirical-association:** history can reveal risk and hidden dependencies but does not show that change causes poor quality. |
| Put the common API operation where users naturally look. | Supported for discoverability in bounded API tasks. | **Controlled:** small Java experiments; the exact interface form does not transfer literally to every paradigm. |
| Make small, reviewable, behavior-aware improvements instead of demanding perfection. | Supported as method and operating policy. | **Original-author/first-party:** Fowler and Google. Neither supplies a transferable effect size. |
| Let repository and ecosystem contracts own style and API idiom. | Supported as operational practice, not universal superiority. | **First-party:** Google, Rust, and Microsoft. Each guide is scoped to its ecosystem. |
| Treat public API changes as compatibility decisions. | Strong operational support within two large ecosystems. | **First-party:** Abseil C++ and .NET; consumer reach and compatibility dimensions differ elsewhere. |

## Conflicts and limits

- **Specific now versus reusable later:** YAGNI can be misread as hostility to
  design; “general-purpose” can be misread as permission for speculative
  extension points. The practical boundary is evidence of a current shared
  responsibility, stable seam, or repeated change.
- **Local consistency versus improvement:** Consistency makes code predictable,
  but copying a problematic local design can deepen it. A divergence needs a
  concrete reason and should usually stay within the requested change.
- **Behavior preservation versus intentional correction:** A refactor preserves
  behavior. A bug fix, migration, or contract change does not become a refactor
  merely because it also restructures code; compatibility and verification must
  address the intended behavior change explicitly.
- **Compatibility versus progress:** Abseil and .NET both permit some justified
  breaks. “Never break anything” and “all observable behavior is contractual”
  are too strong as portable rules without a defined public surface and support
  policy.
- **Patterns versus language facilities:** The GoF source captures
  object-oriented experience from its period. Modern type systems, standard
  libraries, frameworks, and functional constructs can make a named pattern
  unnecessary or materially change its implementation.
- **Semantic guarantees versus application defaults:** Effect systems,
  immutability checkers, exhaustive matches, and total languages establish
  different guarantees under different assumptions. None shows that an entire
  application should maximize purity, immutability, explicit variants, or
  higher-order composition. Open extension points, lifecycle state, I/O,
  performance, and ecosystem conventions can justify a different design.
- **Composition versus transparency:** A named pipeline can expose data flow;
  a dense or point-free chain can hide intermediate values, failure paths, and
  debugging locations. The literature inspected does not establish a portable
  complexity threshold for that trade-off.
- **Metrics versus outcomes:** Size, complexity, smell, coupling, cohesion,
  churn, clone, and maintainability scores can locate an investigation target.
  Their definitions and confounders differ, and improving the score does not
  establish improved comprehension, maintenance time, defects, or user value.
- **Evidence strength:** Controlled studies are usually small and use bounded
  Java or C++ tasks; repository studies are observational; reviews aggregate
  heterogeneous definitions and proxies. Foundational and first-party sources
  establish decision frames and operational contracts. None provides
  language-independent causal proof for a universal shape or numeric limit.

## Proposed next steps

1. If maintainers choose to update the code-writing contract, add a short,
   language-independent design screen:
   - What current requirement, invariant, or change pressure justifies this
     structure?
   - Which module, contract, or repository convention already owns it?
   - Does an abstraction hide real complexity, or add hypothetical flexibility
     and navigation?
   - If a pattern is proposed, do its problem, context, and consequences match?
   - If a functional technique is requested, established locally, or proposed,
     which concrete effect, mutation, state-space, failure, or transformation
     problem does it solve without obscuring the common path?
   - If code is duplicated, does it represent one synchronized rule or
     intentionally independent behavior?
   - If a smell or metric motivates work, what concrete harm is present and what
     outcome will verify improvement?
   - Which recent or historically co-changing code needs extra review or tests?
   - Can a user discover the common API operation from the natural entry point?
   - Is any public or persisted behavior changing, and who can depend on it?
   - What is the smallest coherent, reviewable, verifiable change?
2. Keep these as soft defaults. Promote an item to a hard rule only when an
   applicable language specification, public compatibility contract, security
   boundary, formatter, analyzer, or repository policy owns it.
3. Do not add universal limits for function size, abstraction depth,
   inheritance depth, coupling, cohesion, clone percentage, smell count, churn,
   Maintainability Index, or pattern use. The evidence does not justify those
   gates.
4. If stronger policy is contemplated, first define the external outcome and
   commission a targeted review or repository-specific study. The next useful
   evidence would measure maintenance correctness, time, defects, or change
   spread—not another internal score.

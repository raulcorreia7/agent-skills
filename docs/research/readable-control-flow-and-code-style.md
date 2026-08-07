# Readable Control Flow Across Programming Languages

**Decision:** Use a soft, language-independent rule based on semantic clarity,
not physical line count or one preferred syntax. Prefer control flow that makes
decisions, evaluation order, outcomes, and side effects easy to inspect. Keep a
compact expression when it communicates one obvious operation. Expand it when
nesting, unfamiliar syntax, precedence, side effects, or mixed responsibilities
hide what happens. Use blocks where they make ownership or scope explicit, but
do not add language-specific delimiters without a semantic or local-style reason.

The available evidence does not support adding a local scope to every selection
branch, banning all conditional expressions, or mechanically expanding every
one-line expression. These choices depend on semantics, local conventions, and
the amount of behavior a reader must hold at once.

C# switch sections were the motivating case. Their language and tooling
evidence remains below as a bounded case study, not as a C#-specific runtime
rule or a basis for generalizing C# syntax to other languages.

This research synthesis was completed on 2026-08-07 for maintainers of the
repository's agent code-writing skill.

## Research frame

- **Question:** What should an agent code-writing contract say, across
  programming languages, about scoped blocks, one-line control flow,
  conditional expressions, nesting, explicit branches, readability,
  complexity, and debuggability?
- **Audience:** Maintainers who need portable defaults without overriding a
  language's semantics or a repository's established style.
- **As-of date:** 2026-08-07.
- **Source boundary:** Peer-reviewed human-comprehension experiments and
  systematic reviews across C, C++, Java, JavaScript, and Python; foundational
  and empirical complexity research; and selected language specifications,
  analyzers, debugger documentation, and first-party style guides used to bound
  syntax- and tool-specific claims.
- **Material exclusions:** The review is not an exhaustive systematic review.
  It excludes opinion posts as effectiveness evidence, generated-code
  aesthetics, runtime-performance claims, and language constructs for which no
  directly relevant study was found. It does not assume that tracing accuracy,
  reading time, perceived readability, bug finding, maintenance effort, and
  defect history measure the same outcome.
- **Sufficient evidence:** Syntax and tooling claims need their owning
  specification or product documentation. Effectiveness claims need a directly
  relevant empirical study and are qualified by task, language, and population.
  A general default needs corroboration or must remain a labelled inference. No
  source count, style-guide agreement, or metric value is treated as causal
  evidence.

Source labels used below:

- **Normative:** a language standard or specification defines valid syntax and
  semantics.
- **Tool contract:** official documentation defines a configurable analyzer,
  metric, formatter, or debugger behavior.
- **First-party practice:** a project or documentation team states the style it
  uses. This establishes that team's convention, not universal effectiveness.
- **Inference:** a proposed agent rule derived from the sources. It is not a
  source-reported finding.

## Bottom line

The strongest defensible default is “use the clearest conventional form for the
local context,” with concrete warning signs rather than a syntax ban:

- Preserve compact code when it expresses one familiar, pure operation.
- Use identifiers that communicate domain role or value meaning. Preserve short
  established idioms and do not optimize names for length alone.
- Expand code when a reader must mentally untangle nested choices, precedence,
  short-circuit order, mutations, failure points, or multiple responsibilities.
- Introduce intermediate values when their names expose domain meaning. Do not
  add meaningless temporaries merely to shorten an expression.
- Prefer fewer negations in compound Boolean logic when the equivalent form is
  equally natural. Do not ban negative predicates.
- Extract a helper only when its name creates a useful semantic boundary or the
  extraction supports real ownership, reuse, or testing.
- Reduce unnecessary nesting when the flatter form preserves obvious semantics.
- Keep optional delimiters around embedded control-flow bodies when the language
  and repository convention support them. Add a branch-local scope when it
  limits value lifetime or groups non-trivial work, not to every trivial branch.
- Group selection alternatives with identical behavior. For pure Boolean
  classification, consider a clear idiomatic membership form when it preserves
  relevant type or exhaustiveness checks.
- Use complexity scores to find review and testing hotspots. Do not use a score,
  brace count, nesting depth, or line length as a universal quality gate.

## Cross-language empirical findings

### Ternaries and explicit branches have mixed, context-dependent results

The best-known controlled result favoring an explicit branch is Gopstein et
al.'s C/C++ tracing experiment with 73 mostly student programmers. For its
specific conditional-operator snippet, participants answered 110 of 145 trials
correctly with the ternary and 143 of 145 with the clarified `if`; the reported
effect was significant (phi 0.36, p = 1.74e-05). The treatment was one compact,
state-updating form, not a test of every pure two-value ternary. [Gopstein et
al., ESEC/FSE 2017](https://doi.org/10.1145/3106237.3106264)

A Java replication with 132 novices pointed in the same direction but did not
find a statistically significant correctness result for the conditional
operator; its confidence interval was very wide. Participants still perceived
the ternary as more confusing. A JavaScript replication involving 210
developers also found a directional but non-significant result after correction
for multiple comparisons. [Langhout and Aniche, ICPC
2021](https://doi.org/10.1109/ICPC52881.2021.00012), [Torres et al., JSS
2023](https://doi.org/10.1016/j.jss.2023.111731)

A small Python eye-tracking experiment favored a multiline branch over its
one-line conditional expression for several tracing and gaze outcomes, but not
all outcomes. Conversely, a field survey found conditional operators in 98% of
50 C projects and only 8.25% of 97 experienced respondents rated them
negatively. Prevalence and opinion do not prove comprehension, but they weaken a
claim that the construct is inherently unreadable. [da Costa et al., EMSE
2023](https://doi.org/10.1007/s10664-023-10311-0), [Medeiros et al., EMSE
2019](https://doi.org/10.1007/s10664-018-9666-x)

**Finding:** Do not ban ternaries. Permit a familiar, pure choice between two
obvious values. Expand nested, side-effecting, precedence-heavy, or otherwise
non-obvious conditional expressions. No verified study in this review isolated
nested ternaries, so that boundary is a conservative inference rather than a
measured universal cutoff.

### Physical line count is a poor proxy for semantic density

The same Python eye-tracking study provides a useful counterexample to “more
lines are easier”: a one-line multiple assignment took less time in its local
area of interest and produced fewer local regressions than the split form. In a
Java study of 231 novices, direct Boolean returns and explicit `if` branches had
almost identical comprehension results; across seven style patterns, the
authors found no overall accuracy or time difference between the designated
expert and novice forms. [da Costa et al., EMSE
2023](https://doi.org/10.1007/s10664-023-10311-0), [Wiese, Rafferty, and Fox,
ICSE-SEET 2019](https://doi.org/10.1109/ICSE-SEET.2019.00017)

The 2023 formatting systematic review found sparse, old, and often conflicting
evidence across formatting elements. Even “one statement per line” results did
not establish that every expression should be expanded; a statement and a
physical line are different units. [Oliveira et al., JSS
2023](https://doi.org/10.1016/j.jss.2023.111728)

**Finding:** Avoid “one-liner” as the policy's main test. Review semantic density:
how many decisions, effects, failure points, concepts, and precedence rules the
reader must hold at once. Let the language formatter own ordinary wrapping.

### Named intermediate values help selectively

In an experiment with 113 participants and six mathematical Python functions,
meaningfully named intermediate values produced a corrected-for-multiplicity
benefit over one compound expression only for the hardest function. Meaningless
temporaries reduced accuracy in two cases, and no time comparison survived the
correction. [Cates, Yunik, and Feitelson, ICPC
2021](https://doi.org/10.1109/ICPC52881.2021.00020)

**Finding:** Extract a value when its name reveals a domain concept, separates a
real failure or effect, or decomposes genuinely difficult logic. Decomposition
without meaning can add indirection and should not be mandatory.

### Less nesting often improves speed and preference, but not reliably accuracy

An online experiment with 275 participants found that less-nested Java methods
were rated more readable and read faster; the correctness effect was very small
and borderline. A 2024 eye-tracking replication with 46 participants again
found faster reading and higher confidence, while bug-finding accuracy was 5.4%
lower and not significantly different. [Johnson et al., ICSME
2019](https://doi.org/10.1109/ICSME.2019.00085), [Park et al., EMSE
2024](https://doi.org/10.1007/s10664-024-10532-x)

Other studies show why the rule must remain conditional. A 1986 experiment with
148 students reported no average comprehension difference between nested and
unnested versions. A later experiment with 220 professionals found that nesting
topology and predicate semantics mattered: nested simple conditions were not
reliably worse than one compound predicate, while balanced-tree-like nesting
was harder in some comparisons. [Harrison and Cook, JSS
1986](https://doi.org/10.1016/0164-1212(86)90003-8), [Ajami, Woodbridge, and
Feitelson, EMSE 2019](https://doi.org/10.1007/s10664-018-9628-3)

**Finding:** Reduce unnecessary nesting when a guard, pattern, lookup, or
cohesive extraction makes the main path clearer without obscuring evaluation
order. No universal nesting-depth threshold is supported, and the reviewed
studies did not isolate guard clauses or early returns as a general remedy.

### Optional delimiters have the most consistent direct style evidence

In the C/C++ tracing experiment, omitted braces produced more errors. The Java
replication found 19 correct and 13 wrong outcomes without braces versus 27 and
4 with braces (odds ratio 4.62, 95% CI [1.30, 16.36]); 93.3% of respondents also
perceived omission as more confusing. The 2023 formatting review found these
modern results alongside older null findings. [Gopstein et al., ESEC/FSE
2017](https://doi.org/10.1145/3106237.3106264), [Langhout and Aniche, ICPC
2021](https://doi.org/10.1109/ICPC52881.2021.00012), [Oliveira et al., JSS
2023](https://doi.org/10.1016/j.jss.2023.111728)

The tested risk was an embedded body's misleading visual ownership. It does not
show that an extra nested block improves every switch section, match arm, or
equivalent construct. Some languages make delimiters mandatory, some use
indentation, and some expression-oriented forms have no analogous block.

**Finding:** A portable rule should prefer explicit ownership of conditional
and loop bodies, then defer to language syntax and repository style. It should
not generalize that result into “put braces around every possible body.”

## Additional portable heuristics

These candidates extend beyond layout and conditional syntax. Their evidence is
still context-bound, so each remains a soft default.

| Heuristic | Evidence | Portable conclusion |
| --- | --- | --- |
| Use meaningful identifier words | In a within-subject experiment, 72 professional C# developers located semantic defects 19% faster with full-word identifiers than with abbreviations or letters. Other studies found no general advantage for full words over abbreviations, and misleading long names can erase the benefit. [Hofmeister, Siegmund, and Holt, EMSE 2019](https://doi.org/10.1007/s10664-018-9621-x), [Scanniello et al., TOSEM 2017](https://doi.org/10.1145/3104029), [Avidan and Feitelson, ICPC 2017](https://doi.org/10.1109/ICPC.2017.27) | Name by domain role and value meaning, not by a length target. Avoid unexplained letters and abbreviations outside narrow established idioms. |
| Follow the repository's naming and formatting system | The formatting review retained only 15 human studies from 4,914 records and found positive, null, and conflicting results, including disagreement between camel case and snake case. Google, PEP 8, and Effective Go converge operationally on consistent project style and formatter ownership. [Oliveira et al., JSS 2023](https://doi.org/10.1016/j.jss.2023.111728), [Google style-guide scope](https://google.github.io/styleguide/), [PEP 8](https://peps.python.org/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds), [Effective Go](https://go.dev/doc/effective_go#formatting) | Do not invent universal casing, spacing, or wrapping rules. Follow checked-in configuration and avoid unrelated style churn. |
| Comment non-obvious intent and keep comments synchronized | In an eye-tracking experiment with 20 students and 12 Java snippets, comments changed comprehension performance by between a 30% decrease and a 34% increase depending on the snippet. A study of 277 participants, about 81% professionals, found comments less useful than expected in small tasks and identifiers often more useful. [Abdelsalam et al., EMSE 2026](https://doi.org/10.1007/s10664-025-10721-2), [Nielebock et al., EMSE 2019](https://doi.org/10.1007/s10664-018-9664-z) | Comment intent, constraints, invariants, trade-offs, or API behavior that code cannot express. Do not narrate every operation or enforce comment quotas. Update or remove comments with behavior changes. |
| Prefer fewer negations when equivalent formulations are equally natural | In a 2026 experiment with 362 participants, each added negation cost about 2.6 seconds in fitted models; multiple negations also increased errors. A study of 220 professionals found that some, but not all, negations made predicates harder. [Baron and Feitelson, EMSE 2026](https://doi.org/10.1007/s10664-026-10818-2), [Ajami, Woodbridge, and Feitelson, EMSE 2019](https://doi.org/10.1007/s10664-018-9628-3) | Prefer a direct formulation for compound or double-negated logic when it preserves natural domain language. Do not ban ordinary negative predicates such as `isEmpty`. |
| Extract helpers only for a useful semantic boundary | In an eye-tracking study with 32 Java novices, extraction reduced time by up to 78.8% on harder tasks but increased it by up to 166.9% on simpler tasks; navigation between call sites and helper bodies remained a cost. [da Costa et al., JSS 2026](https://doi.org/10.1016/j.jss.2026.112825) | Extract when the helper name lets callers reason at a higher level or when reuse, testing, or ownership justifies the seam. Keep trivial one-use logic inline when extraction only adds navigation. |
| Keep conditional effects and mutation explicit | C/C++ and Java tracing experiments found large error effects for patterns such as assignment as a value, short-circuit logic used as control flow, and embedded post-increment, although not every tested pattern replicated. [Gopstein et al., ESEC/FSE 2017](https://doi.org/10.1145/3106237.3106264), [Langhout and Aniche, ICPC 2021](https://doi.org/10.1109/ICPC52881.2021.00012) | Use explicit statements when expression syntax hides whether or when mutation, I/O, or another effect executes. Do not ban ordinary explicit mutation or established idioms. |
| Group selection alternatives with identical behavior | Rust Clippy's first-party `match_same_arms` lint treats identical match bodies as a possible copy error and recommends an or-pattern when the behavior is intentionally shared because it exposes intent. This is operational, language-specific guidance, not a controlled readability study. [Rust Clippy lint documentation](https://rust-lang.github.io/rust-clippy/beta/index.html#match_same_arms) | Group alternatives that intentionally share one outcome. For pure Boolean classification, consider an idiomatic membership form when it is clearer and preserves relevant type or exhaustiveness checks. |

The company and language guides above establish mature operational practice,
not causal effectiveness. The experiments remain limited by language, task,
snippet size, and participant population.

## Motivating C# case study

### Case blocks are legal but optional

The C# grammar defines a switch section as one or more labels followed by a
statement list. A block is itself a statement, and a variable declared in a
block has that block as its scope. In contrast, a local declared directly in a
switch section belongs to the enclosing switch block's declaration space and
has switch-block scope. Adding `{ ... }` after a label can therefore isolate
locals and permit independent names in separate sections. The grammar does not
require that extra block. [ECMA-334:2023, §§13.3 and
13.8.3](https://ecma-international.org/wp-content/uploads/ECMA-334_7th_edition_december_2023.pdf),
[current C# specification, §§7.3 and
7.7](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/basic-concepts),
[current C# specification,
§13.8.3](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/statements#1383-the-switch-statement)

C# prevents implicit fall-through from a nonempty switch section. A reachable
section endpoint is a compile-time error. Multiple consecutive labels can
belong to one switch section, and `return`, `throw`, `break`, or an explicit
`goto case` can terminate or transfer control. Extra section blocks are not the
mechanism that prevents fall-through. [ECMA-334:2023,
§13.8.3](https://ecma-international.org/wp-content/uploads/ECMA-334_7th_edition_december_2023.pdf),
[current C# specification,
§13.8.3](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/statements#1383-the-switch-statement)

**Case-study implication:** Requiring a block for every `case` is a style
preference. A block has semantic value when it intentionally owns local
declarations. Consecutive labels that share one outcome can share one section
and, when useful, one block.

### C# tooling treats braces and same-line bodies as configurable style

Roslyn rule IDE0011 exposes `csharp_prefer_braces = true`, `false`, or
`when_multiline`; its documented default is `true`. Its examples concern
embedded control-flow bodies such as `if`. The page does not document a mode
that inserts a distinct block around every switch section. [IDE0011, updated
2023-07-25](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/style-rules/ide0011)

IDE2001 can require embedded statements for constructs such as `if`, `while`,
and `for` to start on their own line. The option is experimental, and its
documented default permits the same-line form. This is configurable tooling
behavior, not evidence that either layout reduces defects. [IDE2001, updated
2025-08-21](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/style-rules/ide2001)

The .NET style-rule inventory documents switch completeness and case
indentation options, but this review found no built-in option for wrapping every
switch section in a block. This is a bounded negative finding, not proof that no
third-party analyzer implements it. [.NET code-style rule inventory, updated
2026-07-09](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/style-rules/),
[code-style options](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/code-style-rule-options)

**Case-study implication:** Do not describe per-case blocks as standard C#
analyzer behavior. Repository configuration remains authoritative.

### First-party C# guides differ on exact brace rules

Microsoft's documentation convention says to break long statements for
clarity, use one statement and declaration per line, and use braces in its
Allman-style samples. It describes Microsoft examples and samples, not a
requirement for all C# programs. [.NET coding conventions, updated
2025-01-18](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions#style-guidelines)

The .NET runtime repository permits some single-statement bodies without braces
but rejects a same-line single-statement `if`. It also says existing file style
takes precedence. This is that repository's policy, pinned here at commit
`c38f37a`, not a language-wide standard. [.NET runtime C# coding style,
inspected 2026-08-07](https://github.com/dotnet/runtime/blob/c38f37a3a1c39ca921fe156d472990d259977f6f/docs/coding-guidelines/coding-style.md)

Google's C# guide requires at most one statement and one assignment per line
and uses braces even when optional. It also recommends replacing large or
complex nested expressions with named values. The guide identifies itself as
Google's internal default and contains no requirement to block every switch
section. [Google C# style guide, inspected
2026-08-07](https://github.com/google/styleguide/blob/gh-pages/csharp-style.md),
[Google style-guide scope](https://google.github.io/styleguide/)

**Case-study implication:** Mature C# conventions support avoiding dense
control flow but disagree about optional braces. This supports local
consistency and a semantic heuristic, not a universal delimiter rule.

### C# supports simple conditional expressions as a style choice

The conditional operator evaluates a Boolean condition and exactly one of two
result expressions. It is right-associative, so
`a ? b : c ? d : e` groups as `a ? b : (c ? d : e)`. The language permits
nesting; its specification makes no readability recommendation. [C#
specification,
§12.21](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/expressions#1221-conditional-operator)

IDE0045 and IDE0046 can prefer either a conditional expression or an `if`/`else`
for an assignment or return. Both documented defaults prefer the conditional
expression. These are configurable style rules, not correctness or complexity
judgments. [IDE0045, updated
2023-07-25](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/style-rules/ide0045),
[IDE0046, updated
2022-06-25](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/style-rules/ide0046)

Microsoft's teaching guidance uses `?:` for choosing one of two values and
prefers `if` when branches do more than produce a value. This is explanatory
guidance, not an empirical complexity threshold. [C# selection statements,
updated
2026-07-20](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/statements/selection#conditional-operator-)

**Case-study implication:** C# tooling and guidance do not support a blanket
anti-ternary rule. The cross-language evidence supplies the stronger reason to
keep simple value selection compact and expand non-obvious work.

## What complexity metrics can and cannot support

McCabe's cyclomatic complexity is a control-flow graph measure. It gives the
size of a basis set of linearly independent paths; it does not measure line
length, brace layout, total feasible runtime paths, or human understanding.
McCabe described 10 as a “reasonable, but not magical” operational limit and
allowed justified exceptions such as large selection statements. The later
NIST methodology likewise calls the exact limit controversial and recommends
an organization-selected value with documented exceptions. [McCabe, IEEE TSE
1976](https://doi.org/10.1109/TSE.1976.233837), [NIST SP
500-235](https://doi.org/10.6028/NIST.SP.500-235)

Cognitive Complexity was designed to approximate understandability by scoring
breaks in linear flow and selected nesting. A meta-analysis over 10 studies,
427 snippets, and about 24,000 human evaluations found a moderate association
with comprehension time (r = .54) but no reliable pooled association with
correctness (r = -.13); heterogeneity was high. A later correction-task study
found that Cognitive Complexity did not clearly outperform cyclomatic
complexity, lines of code, or nesting depth. [Muñoz Barón, Wyrich, and Wagner,
ESEM 2020](https://doi.org/10.1145/3382494.3410636), [Lavazza et al., EMSE
2023](https://doi.org/10.1007/s10664-023-10396-7)

Defect studies also resist universal thresholds. In five large Microsoft
systems, complexity measures correlated with post-release failures differently
by project, and no metric worked consistently across all five. Other studies
show that apparent associations can disappear after controlling for size, and
that change-history measures can outperform static attributes. A systematic
review of fault prediction found weak transportability and no universally
reliable complexity-only model. [Nagappan, Ball, and Zeller, ICSE
2006](https://doi.org/10.1145/1134285.1134349), [El Emam et al., IEEE TSE
2001](https://doi.org/10.1109/32.935855), [Moser, Pedrycz, and Succi, ICSE
2008](https://doi.org/10.1145/1368088.1368114), [Hall et al., IEEE TSE
2012](https://doi.org/10.1109/TSE.2011.103)

Adding a lexical scope around an unchanged selection branch does not reduce its
number of decisions. Expanding a conditional expression into an equivalent
branch can improve inspection without reducing graph complexity. These are
consequences of the metric definition, not language-specific style rules.

For the C# case study, CA1502 counts branches and `case` statements. Its
threshold is configurable, and the rule is disabled by default in .NET 10.
Adding a block around an unchanged switch section does not reduce its score.
[CA1502, inspected
2026-08-07](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca1502)

**Finding:** Use structural scores to locate decision-heavy code for inspection,
testing, or decomposition. Check size, change history, and domain structure too.
Do not treat 10, 15, 25, or any other score as a causal boundary, and do not
refactor solely to lower a metric. “Low complexity” in the proposed style rule
means locally understandable decisions and effects, not a numeric score.

## “Easy to debug” needs a narrower claim

Debugger behavior depends on language semantics, compiler sequence points,
optimization, symbols, and the debugger. Physical line breaks and extra scopes
therefore do not by themselves prove finer stepping behavior. The reviewed
human studies also do not establish that these formatting choices reduce
debugging time or improve bug-finding accuracy.

For example, Visual Studio documents statement-oriented stepping and shows an
inline `if` condition and consequence as separate steps even on one source
line. Breakpoints are selected by source line, while stepping depends on
statements and available symbols. This example bounds the C# tooling claim but
does not establish behavior across compilers or debuggers. [Visual Studio
debugger navigation, inspected
2026-08-07](https://learn.microsoft.com/en-us/visualstudio/debugger/navigating-through-code-with-the-debugger?view=vs-2022#code-stepping),
[breakpoint behavior](https://learn.microsoft.com/en-us/visualstudio/debugger/get-started-with-breakpoints?view=vs-2022)

**Implication:** Describe explicit control flow as easier to inspect and modify
when that is evident from the source. Do not promise that a formatting choice
always creates additional debugger stops or improves bug finding.

## C# case-study evidence register

| Claim | Canonical locator | Status | Applicability and limits |
| --- | --- | --- | --- |
| A switch section is labels plus a statement list; a block is a statement and owns declarations. | ECMA-334:2023 §§13.3 and 13.8.3; current C# specification §§7.3, 7.7, 13.3, and 13.8.3. | Normative. | Establishes syntax and scope, not readability. |
| C# forbids reachable fall-through and permits consecutive labels in one section. | ECMA-334:2023 §13.8.3; current C# specification §13.8.3. | Normative. | Does not select brace layout; explicit `goto case` remains legal. |
| Ordinary control-body braces are configurable. | IDE0011 values `true`, `false`, and `when_multiline`. | Tool contract. | The rule does not document blocks around every switch section. |
| Same-line embedded statements are configurable. | IDE2001 option values and default. | Experimental tool contract. | Applies to embedded bodies such as `if`, `while`, and `for`. |
| Conditional expression versus explicit branch is configurable. | IDE0045 and IDE0046. | Tool contract. | A style diagnostic is not readability or defect evidence. |
| First-party C# conventions disagree about optional braces. | Microsoft coding conventions, .NET runtime coding style at commit `c38f37a`, and Google C# style guide. | First-party practice. | Project-specific conventions do not establish universal effectiveness. |
| Cyclomatic complexity counts decisions, not extra lexical blocks. | CA1502 calculation and examples. | Tool contract; block conclusion is an inference. | The metric does not represent every readability or debugging cost. |
| Inline source layout does not necessarily collapse stepping. | Visual Studio debugger navigation, code-stepping example. | Tool contract. | Does not establish sequence points across compilers, optimization modes, or IDEs. |

## Conflicts and limits

- **Ternary results conflict across studies and languages.** The strongest C
  result favors an explicit branch, Java and JavaScript replications do not
  establish the same behavioral effect, and experienced C contributors rarely
  rate the operator negatively. The defensible resolution is a semantic
  boundary: concise value selection stays concise; non-obvious work becomes
  statements.
- **Perception and performance diverge.** Several experiments found a style was
  preferred or inspired more confidence without improving correctness. The rule
  must not treat perceived readability as proof of better comprehension,
  debugging, or maintenance.
- **Delimiter conventions conflict.** Languages and repositories use mandatory
  delimiters, optional delimiters, significant indentation, or
  expression-oriented arms. This supports explicit ownership plus local
  consistency, not a universal brace mandate.
- **No direct study was found for local scopes around every selection branch,
  nested ternaries, or guard clauses as a general remedy.** Evidence about
  omitted braces around an `if` body cannot be transferred automatically to
  these constructs.
- **Human studies are small and heterogeneous.** The reviewed experiments use
  different languages, mostly small snippets, varied participant populations,
  and outcomes such as tracing, gaze, time, confidence, or bug finding. A
  mapping of 95 comprehension experiments likewise found substantial design
  diversity and little evidence that these tasks are interchangeable. [Wyrich,
  Bogner, and Wagner, ACM Computing Surveys
  2024](https://doi.org/10.1145/3626522)
- **Defect and maintenance studies are observational or context-bound.** Static
  complexity is entangled with size and change exposure. No reviewed study
  establishes that enforcing these style choices causes fewer field defects or
  faster debugging.
- **“Obvious,” “non-trivial,” and “easy to debug” remain review judgments.** A
  reusable contract should give concrete signals and examples, then defer to
  repository style and the smallest readable form. A numeric expression-length
  or nesting threshold is not supported by this source set. These limits are
  why the recommendation is a soft rule.

## Recommendation strength

| Practice | Evidence status | Policy consequence |
| --- | --- | --- |
| Keep optional delimiters around embedded conditional and loop bodies | Corroborated in modern C and Java tracing studies, with older null findings | Use as a soft default where the language and local style support it. Do not transfer it automatically to every block-like construct. |
| Ban all ternaries or conditional expressions | Contradicted or unsupported across C, Java, JavaScript, Python, and field-perception evidence | Do not ban them. Allow a simple, pure value choice and expand non-obvious forms. |
| Split every one-line expression | Contradicted by direct counterexamples and null results | Do not use physical line count as the trigger. Review semantic density. |
| Introduce named intermediate values | Supported for some difficult expressions; meaningless temporaries can hurt | Extract only when the name or separation carries meaning. |
| Reduce nesting | Supported for reading speed and preference; correctness and bug-finding results are mixed | Use as a soft review signal. Preserve clear evaluation order and do not set a universal depth limit. |
| Put a local scope around every selection branch | Direct evidence gap and language-dependent semantics | Use a scope when it limits value lifetime or groups non-trivial work, not for every trivial branch. |
| Repeat identical selection bodies | First-party Rust tooling treats this as a possible copy error and recommends grouping intentional matches | Group alternatives with identical behavior. Use a clear membership expression for pure classification when local idiom and type guarantees support it. |
| Use cyclomatic or cognitive complexity as a quality gate | Unsupported; associations are context-dependent and confounded, and thresholds are conventional | Use metrics for hotspot discovery and test planning only. |
| Claim expanded formatting is easier to debug | Unresolved; debugger stepping and source layout are not equivalent | Say “easier to inspect” only when structure makes decisions and effects visible. Do not promise more debugger stops or fewer defects. |

## Recommended portable contract

Use this language-independent wording as the primary rule:

> Prefer the clearest conventional form for the local language and repository.
> Keep a compact expression when it performs one obvious, side-effect-free
> operation. Expand control flow when nesting, precedence, short-circuit order,
> mutations, failure points, or mixed responsibilities make the behavior hard
> to inspect. Introduce intermediate values when their names expose domain
> meaning. Use explicit body delimiters or scopes when they clarify ownership or
> lifetime. Group selection alternatives with identical behavior. For pure
> Boolean classification, use a clear idiomatic membership form when it
> preserves relevant type or exhaustiveness checks. Treat complexity metrics as
> review signals, not quality gates.

Concrete review questions are more portable than a length threshold:

1. Can a maintainer name the condition and each outcome without mentally
   simulating operator precedence?
2. Is evaluation order important, and is it visible?
3. Does the expression mutate state, perform I/O, throw at several points, or
   combine unrelated work?
4. Would an intermediate name reveal a domain concept rather than merely repeat
   the expression?
5. Does a block create meaningful ownership or local scope?
6. Does the repository already have a clear formatter or analyzer rule?

These examples use neutral pseudocode. They illustrate the semantic boundary,
not syntax that every language must copy.

Keep a simple value choice compact:

```text
status = enabled ? ACTIVE : INACTIVE
```

Expand a branch that performs effects or contains multiple failure points:

```text
if request_requires_refresh:
    refreshed_value = refresh_cache()
    record_refresh(refreshed_value)
    result = refreshed_value
else:
    result = cached_value
```

Use a case-local scope when it owns meaningful local work; let grouped labels
share that scope:

```text
select value:
    case KNOWN:
        return mapped

    case LEGACY, ALTERNATE:
        begin local scope
            fallback = build_fallback(value)
            record_fallback(fallback)
            return fallback
        end local scope

    default:
        return failure
```

## Contract ownership and follow-up

- The shared readability contract owns the portable heuristic, including
  semantic-density signals and compact, expanded, grouped-selection, scoped,
  and membership-classification pseudocode.
- Language-specific contracts remain unchanged unless syntax or semantics
  require a narrower rule after repeated demand.
- Checked-in formatter and analyzer configuration remains authoritative. The
  skill does not impose a universal cyclomatic, cognitive, line-length, or
  nesting threshold.
- Before strengthening the rule, test representative behavior-preserving pairs
  with experienced maintainers and realistic code. Measure task correctness,
  time to explain or modify, bug-finding accuracy, and reviewer agreement
  separately. Do not use preference or a lower metric score as the sole outcome.
- If agents repeatedly produce one harmful pattern, add a narrow example for
  that pattern instead of broadening the general prohibition.

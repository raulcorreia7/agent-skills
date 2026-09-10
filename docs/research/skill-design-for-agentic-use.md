# Skill Design for Agentic Use

**Decision:** Design skills as small executable contracts. Make invocation
discriminative, keep the common path in the main file, disclose branch-specific
reference only when needed, end each material step with a checkable condition,
define the output, and verify against external evidence. Measure changes by
task success and recurring cost, not by instruction count or document length.

This report was reviewed on 2026-08-06. It covers static instruction and skill
files used by tool-capable language-model agents. It does not prescribe a
universal prompt format.

## Evidence method

The review prioritizes controlled studies, peer-reviewed papers, and current
official specifications. It uses first-party preprints where peer-reviewed
evidence does not cover a material question and labels them. Search results and
secondary summaries were discovery inputs only.

The evidence comes from instruction following, in-context learning,
long-context retrieval, tool selection, agent-computer interfaces, structured
generation, and self-correction. Few studies test repository skill files
directly. Each directive below therefore identifies whether the evidence is a
direct finding or a design inference from an adjacent agent setting.

## Ranked high-yield directives

“Yield” means expected improvement in successful task completion relative to
recurring context, runtime, maintenance, and regression cost. The rank favors
broad applicability, direct evidence, a low-cost implementation, and a low risk
of harmful overcorrection.

| Rank | Directive | Evidence and boundary |
| --- | --- | --- |
| 1 | **Make success observable.** Give every material step a checkable completion condition and give the skill an explicit output contract. Prefer executable checks for syntax, schemas, tests, links, and changed-file coverage. | **Direct:** output information was the part of task definitions whose removal most damaged performance; compressed, structured definitions improved results. IFEval shows that objectively verifiable constraints support reproducible instruction-following measurement. **Inference:** applying the same idea to every step reduces premature completion. [Yin et al., ACL 2023](https://aclanthology.org/2023.acl-long.172/), [IFEval, 2023 first-party preprint](https://arxiv.org/abs/2311.07911) |
| 2 | **Close the evidence loop.** After action, inspect the effect with the environment, a validator, a test, or a source that can falsify success. Use reflection only to interpret new evidence. | **Direct:** tool-interactive critique improves correction, and a purpose-built coding interface with concise action feedback substantially outperformed a shell-only interface. Broad review evidence does not support unaided self-correction as a universal improvement. [CRITIC, ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/fef126561bbf9d4467dbb8d27334b8fe-Abstract-Conference.html), [SWE-agent, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html), [Kamoi et al., TACL 2024](https://aclanthology.org/2024.tacl-1.78/) |
| 3 | **Spend context on the current branch.** Keep the goal, common steps, decisive constraints, and output contract in the main file. Put branch-only facts and long examples behind explicit pointers located where that branch begins. | **Direct:** one task-definition study removed 60% of tokens without reducing performance; long-context retrieval varies materially with evidence position and often degrades in the middle. **Inference:** progressive disclosure is useful when its pointer reliably selects the needed material; it is harmful when it hides a rule needed on every run. [Yin et al., ACL 2023](https://aclanthology.org/2023.acl-long.172/), [Liu et al., TACL 2024](https://aclanthology.org/2024.tacl-1.9/) |
| 4 | **Design narrow action interfaces.** Expose a small coherent action set, typed inputs, explicit required fields, bounded side effects, actionable errors, and structured results when a consumer needs them. | **Direct:** SWE-agent attributes a large gain to interface design and concise feedback. **Normative:** MCP defines tool names, descriptions, JSON Schema inputs, optional output schemas, error signaling, and validation expectations. The exact interface must still be tested with the target model and task. [SWE-agent, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html), [MCP tools specification](https://modelcontextprotocol.io/specification/2025-11-25/server/tools) |
| 5 | **Make invocation discriminative.** Start the description with the job, name each distinct trigger branch once, and state a boundary only where a neighboring skill could plausibly capture the same request. Test positive and near-miss prompts. | **Direct for tool routing:** semantic alignment between a query and tool metadata was the strongest predictor of selection, while description perturbations shifted choices; many models still struggle to choose among similar tools. Models also show large performance changes under small lexical variations, which supports regression tests instead of trust in one phrasing. **Inference for skills:** skill descriptions act as routing metadata, but no reviewed paper establishes one universally optimal description template. [BiasBusters, ICLR 2026](https://www.microsoft.com/en-us/research/publication/biasbusters-uncovering-and-mitigating-tool-selection-bias-in-large-language-models/), [MetaTool, ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/bc12914d66b41b6bfc2d3a5decdb498b-Abstract-Conference.html), [Zhan et al., EMNLP 2024](https://aclanthology.org/2024.emnlp-main.295/) |
| 6 | **Order only real dependencies.** Write the shortest sequence that exposes prerequisites, action, observation, and correction. Put conditional work in branches. End each step before introducing the next obligation. | **Direct:** ReAct improved agent performance by interleaving task reasoning with actions and observations. **Inference:** numbered skill steps help when the task has dependencies; a flat reference skill does not become better merely by being forced into a sequence. [ReAct, ICLR 2023](https://iclr.cc/virtual/2023/poster/11003) |
| 7 | **Use examples and schemas to resolve shape, not decorate prose.** Include the smallest valid example when syntax, labels, or output shape are otherwise ambiguous. Validate it. Use a formal schema when another program consumes the result. | **Direct:** demonstrations can contribute through label space and sequence format even when their labels are randomized. JSON Schema provides machine-checkable structural assertions. Format restrictions can also reduce reasoning performance, with stricter restrictions causing larger degradation in the tested tasks, so strict structure is not free. [Min et al., EMNLP 2022](https://aclanthology.org/2022.emnlp-main.759/), [JSON Schema 2020-12](https://json-schema.org/draft/2020-12/json-schema-validation), [Tam et al., EMNLP Industry 2024](https://aclanthology.org/2024.emnlp-industry.91/) |
| 8 | **State the target behavior positively.** Describe the action the agent should take. Reserve prohibitions for hard safety, authority, compatibility, or data-loss boundaries, and pair each with the safe alternative. | **Direct:** nine tested tasks showed worse performance and inverse scaling under negated prompts across pretrained, instruction-tuned, few-shot, and specially tuned models. **Inference:** affirmative instructions reduce dependence on correct negation handling; the evidence does not show that all negative wording is harmful or that safety prohibitions should be removed. [Jang et al., PMLR 2023](https://proceedings.mlr.press/v203/jang23a.html) |
| 9 | **Use operational roles, not status personas.** A role term should select duties, criteria, authority, or a workflow branch. Remove generic identity claims that do not change action. | **Direct for factual question answering:** across four model families, 162 personas, and 2,410 questions, personas did not improve performance over the no-persona control, and their effects were largely random. **Inference:** compact operational roles can still be useful routing concepts in an agent workflow; this study did not test that use. [Zheng et al., Findings of EMNLP 2024](https://aclanthology.org/2024.findings-emnlp.888/) |

SWE-agent provides the most directly actionable agent-interface ablation in
this review. Its tailored interface resolved 18% of SWE-bench Lite tasks versus
11% for a shell-only agent. Removing the compact editor reduced the result to
10.3%; showing full files instead of focused views reduced it to 12.7%; and
retaining the full history instead of five recent observations reduced it to
15%. These are workload-specific effect sizes, not universal targets.
[SWE-agent, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html)

No fixed Markdown layout is empirically best. Plausible few-shot formatting
changes produced a spread of up to 76 accuracy points in one tested model, and
good formats transferred weakly between models. Keep the semantic structure
stable, then test representative renderings on the supported models.
[Sclar et al., ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/6c0e99d736da621403018ca7b32b1a4d-Abstract-Conference.html)

## Recommended skill structure

Use the smallest structure that represents the job:

```markdown
---
name: action-name
description: Leading job and distinct trigger branches.
---

# Action name

## Steps

1. Perform the first required action. This step is complete when [observable
   condition].
2. Follow the next real dependency. This step is complete when [observable
   condition].

## Guardrails

- State exceptional safety, scope, authority, or compatibility boundaries.
- Pair a necessary prohibition with the safe action.

## Composition

- Route an adjacent job to `skill-name` when that job is the deliverable.

## Output

- Required result or artifact.
- Evidence and checks.
- Material gaps or residual risk.
```

Apply these variations:

- A reference-only skill can replace `Steps` with co-located rules. Give the
  full rule set an exhaustive application condition.
- Add a branch only when different invocations require different actions.
- Put a context pointer beside the step or branch that needs the referenced
  file. State when to open it and what decision it supports.
- Keep scripts, fixtures, schemas, and large examples in named subfiles. The
  main file owns the route to each one.
- Keep one source of truth for each rule. A short repeated term can reinforce a
  concept; repeated explanations create drift.
- Use headings for stable semantic regions, lists for peer rules, numbered
  steps for dependencies, tables for exact comparisons, and schemas for
  machine validation. Format follows the relationship being expressed.

## Repository rubric

Score each dimension from 0 to 3. Record evidence for the score; do not award
points for polish alone.

| Dimension | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| Invocation | No usable trigger | Broad or overlapping | Distinct job and main triggers | Positive and near-miss routing tests pass |
| Process | Contradictory or unusable | Vague activities | Executable steps or coherent reference | Dependencies, branches, and stop conditions are complete |
| Completion | No success condition | Subjective completion | Material steps are checkable | Checks cover every modified or required surface |
| Context economy | Stale or duplicate content | Most branches load everything | Common path is concise | Conditional reference loads reliably and no meaning is duplicated |
| Interface | Inputs or authority are unclear | Prose-only implicit contract | Inputs, effects, and failures are explicit | Representative valid and invalid calls pass |
| Output | Output is unspecified | Shape is implied | Required artifacts and evidence are explicit | Output is mechanically validatable where useful |
| Feedback | No verification | Unaided re-reading only | Relevant checks or sources are named | Failure feedback drives a bounded correction and re-check |
| Safety and scope | Unsafe authority or mutation | Generic warnings | Exact material boundaries | Boundaries have safe alternatives and adversarial tests |

The maximum is 24. Treat any zero in invocation, completion, output, or safety
as a release blocker when that dimension applies. Use the total only to compare
versions of the same skill; different jobs legitimately need different levels
of structure.

For model-invoked skills, run at least three representative positive prompts,
two plausible near misses, and one overlap case for each neighboring skill. For
each executable skill, run a normal path. Add an invalid or incomplete input
when the skill accepts inputs, and add a no-change case when the requested state
can already exist. Add higher-risk cases in proportion to the skill's authority.

Score the final outcome and the failed or successful step separately. T-Eval's
decomposition of tool use into instruction following, planning, reasoning,
retrieval, understanding, and review produced fine-grained capability evidence
while remaining consistent with outcome-oriented evaluation in its tested
setting. [T-Eval, ACL 2024](https://aclanthology.org/2024.acl-long.515/)

## Expected-yield calculation

Prioritize a proposed directive with a conservative expected-value model:

```text
annual net yield =
  executions
  * attributable failure rate
  * expected relative failure reduction
  * value of a successful recovery
  - recurring context and runtime cost
  - build and maintenance cost
  - expected regression loss
```

Treat safety, authorization, data integrity, and required correctness as hard
gates. A lower cost cannot compensate for a regression in one of these gates.

Estimate low, base, and high cases instead of hiding uncertainty in one score.
When monetary value is inappropriate, use successful tasks per 1,000 runs and
operator minutes saved. Measure the attributable failure rate from traces or a
small blinded benchmark. Estimate lift with an A/B test that keeps the model,
tools, task set, and evaluation fixed. Track token use, tool calls, latency,
false invocation, false refusal, and task success separately.

This formula is a repository design inference, not a validated law of skill
engineering. CAPO directly supports multi-objective prompt evaluation: it
jointly optimizes performance and prompt length, stops weak candidates early,
and outperformed other discrete prompt optimizers in 11 of 15 tested cases,
with gains of up to 21% in accuracy. Those results support Pareto comparison
and early stopping, not this formula or a transferable effect-size estimate.
[CAPO, AutoML 2025](https://proceedings.mlr.press/v293/zehle25a.html)

Use the calculation to prefer changes with high exposure, an observed failure,
a plausible causal mechanism, cheap enforcement, and a measurable check. A
rare hypothetical failure with permanent context cost normally ranks below a
common routing or completion error.

## Anti-patterns

- A description that repeats synonyms instead of distinguishing trigger
  branches.
- A long main file that loads references used by only one branch.
- A decisive requirement buried in the middle of a long reference.
- Steps such as “analyze carefully” or “ensure quality” without a completion
  condition.
- A mandatory critique pass with no new evidence or falsification mechanism.
- A prose output request when a downstream consumer requires a stable shape.
- A complex schema when a reader needs a short explanation.
- An example that is incomplete, invalid, or treated as an additional source
  of rules.
- Negative-only steering that names the failure but not the safe action.
- A high rubric score claimed from inspection without forward tests.

## Evidence limits

No reviewed study compares all proposed skill-file structures on a common
agentic benchmark. Tool descriptions, task definitions, prompts, and static
skills are related but not identical interfaces. Model family, post-training,
tool protocol, context construction, and task distribution can change every
effect.

Context reduction is not an unconditional goal. Removing a decisive constraint
or placing it behind an unreliable pointer can lower quality. Structured output
is valuable when a consumer validates it, but strict structure can constrain
generation. Self-review helps when it introduces reliable feedback; repeated
introspection alone can preserve or amplify the original error. Positive
wording reduces one source of ambiguity but cannot replace explicit hard safety
boundaries.

The rubric and expected-yield formula require repository-specific forward
tests. They organize evidence and cost; they do not turn ordinal judgment into
ground truth. Re-evaluate high-exposure skills when the model, invocation
router, tool protocol, or task distribution changes.

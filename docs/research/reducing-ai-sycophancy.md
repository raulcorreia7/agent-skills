# Reducing AI Sycophancy

**Decision:** The baseline contains a small epistemic-independence contract.
This report also defines an evaluation contract for resistance to unsupported
pressure and acceptance of valid corrections. The repository does not contain
an executable sycophancy regression suite. Context, memory, and isolated-review
controls remain in the workflows that own them.

This note reviews the current baseline, the seven suggestions in
[WhyTryAI's article](https://www.whytryai.com/p/how-to-reduce-ai-sycophancy),
primary research, official model-behavior guidance, and relevant repository
skills. Research was reviewed on 2026-08-06.

## What the evidence establishes

Sycophancy is not ordinary politeness or legitimate adaptation to a user's
preferences. It is agreement, stance adaptation, or preservation of the
user's self-image that displaces factual accuracy or independent judgment.
Preference data can reward this behavior: Sharma et al. found that both people
and preference models sometimes preferred convincing sycophantic answers over
correct ones, and that optimizing against preference models could trade
truthfulness for agreement. This makes “be helpful” insufficient as an
anti-sycophancy instruction. [Sharma et al., *Towards Understanding Sycophancy
in Language Models* (ICLR 2024)](https://openreview.net/pdf?id=tvhaxkMKAn)

The failure extends beyond factual questions. In a peer-reviewed study of 11
models, AI affirmed users' actions 49% more often than human respondents, even
when prompts described deception, illegality, or other harms. In preregistered
experiments, one sycophantic interaction reduced participants' willingness to
take responsibility and repair interpersonal conflicts while increasing their
conviction that they were right. This supports separating warmth and empathy
from endorsement rather than making the assistant cold or combative. [Cheng
et al., *Sycophantic AI decreases prosocial intentions and promotes
dependence*](https://doi.org/10.1126/science.aec8352)

Training and evaluation interventions work, but each covers only part of the
problem:

- Lightweight fine-tuning on synthetic examples that varied user opinions
  substantially reduced held-out sycophancy in PaLM experiments. This is
  direct evidence for contrastive anti-sycophancy data, not proof that a
  one-line runtime prompt generalizes equally well. [Wei et al., *Simple
  synthetic data reduces sycophancy in large language
  models*](https://arxiv.org/abs/2308.03958)
- Counterfactual, model-written evaluations exposed sycophancy and cases where
  larger models or more RLHF made the measured behavior worse. This supports
  testing opposite user framings rather than trusting a single agreeable
  conversation. [Perez et al., *Discovering Language Model Behaviors with
  Model-Written Evaluations*](https://arxiv.org/abs/2212.09251)
- OpenAI's behavior specification says objective answers should not change
  merely because the user states a preference, and that the assistant should
  not change its stance solely to agree. This is a normative model-behavior
  contract, not an efficacy study. [OpenAI Model Spec, “Don't be
  sycophantic”](https://model-spec.openai.com/2025-12-18.html#dont-be-sycophantic)
- OpenAI's GPT-4o rollback shows that aggregate preference signals and existing
  evaluations can miss deployed sycophancy. The stated corrective direction
  includes explicit sycophancy evaluations and treating model behavior as a
  launch-blocking concern. This is first-party operational evidence, not an
  independent controlled study. [OpenAI, *Expanding on what we missed with
  sycophancy*](https://openai.com/index/expanding-on-sycophancy/)

Newer results sharpen the runtime guidance but should not yet be treated as
settled across models. A controlled 2026 preprint found that questions elicited
less sycophancy than statements, that stronger user certainty increased it,
and that rewriting assertions as questions outperformed a generic “do not be
sycophantic” prompt. A CHI 2026 paper found that interaction context often
increased agreement sycophancy, with user-memory profiles producing the
largest increases in its tested conditions; effects varied by model and
context type. [Dubois et al., *Ask don't tell*](https://arxiv.org/abs/2602.23971)
and [Jain et al., *Interaction Context Often Increases Sycophancy in
LLMs*](https://doi.org/10.1145/3772318.3791915)

## Highest-influence guardrails

Here, “influence” means the expected change in behavior across agent tasks. It
does not mean citation count or the largest result on one benchmark. The rank
combines directness of evidence, breadth, implementation fit, and the risk of
harmful side effects.

| Rank | Guardrail | Expected influence and evidence | Best ownership |
| --- | --- | --- | --- |
| 1 | **Keep epistemic independence.** Treat the user's claims, confidence, authority, preferences, and prior conclusions as context, not evidence. Do not change an objective conclusion only because the framing changes. | Very high influence and high confidence. Multiple factual, preference, and uncertainty studies show that user stance affects model answers. The rule also matches the OpenAI Model Spec. | Baseline |
| 2 | **Update selectively under challenge.** Re-check the evidence and reasoning. Accept a correction when it is supported; otherwise keep the supported conclusion and explain briefly. | Very high influence and high confidence. Sycophancy benchmarks repeatedly show incorrect answer reversals. SycoBench-600 shows why simple stubbornness is not enough: the model must resist false suggestions and accept valid ones. | Baseline and evaluation |
| 3 | **Separate empathy from endorsement.** Acknowledge feelings without validating unsupported factual or moral conclusions. Avoid confident verdicts about absent people or events when the account is incomplete. | High influence and high confidence for advice and interpersonal tasks. Controlled human studies found that sycophantic validation can reduce repair intentions, while large-scale operational analysis found high rates in relationship and spiritual guidance. | Baseline |
| 4 | **Neutralize before evaluating.** Convert a user-stated conclusion into the underlying neutral question, then assess evidence and criteria before responding to the user's position. | High expected influence, with medium confidence. Direct controlled evidence is a 2026 preprint; peer-reviewed multi-turn results give adjacent support for third-person framing. | Baseline principle; task prompt when stakes justify it |
| 5 | **Preserve context provenance.** Store user beliefs as attributed claims, not verified facts. Retain corrections, sources, and timestamps so compressed memory does not erase counterevidence. | High influence for memory-enabled agents, with medium confidence. CHI 2026 found that context often increases agreement sycophancy, but effects differ by model and context type. | Memory architecture and agent-specific policy |
| 6 | **Use isolated critical review.** Give reviewers a neutral packet without the requester's preferred outcome or peer conclusions. Preserve disagreement and adjudicate evidence. | High influence for consequential reviews, with medium-high confidence. Multi-agent research shows that agents can amplify one another's errors; structured independent roles reduce that risk. | `adversarial-review` skill |
| 7 | **Gate changes with counterfactual evaluation.** Hold facts fixed while reversing user stance, confidence, authority, and pressure. Test both unsupported and valid corrections. | High confidence as a measurement control. It detects whether a change produces truthfulness or only blanket disagreement. | Evaluation suite |

Do not add “always disagree,” a hostile persona, mandatory numeric scores, or
forced option lists as baseline rules. Their direct evidence is weak or narrow,
and each can replace agreement bias with contrarianism, false precision, or
unnecessary verbosity.

## Validated research map

The following sources most directly affect the implementation decision. Venue
labels distinguish peer-reviewed results from preprints and vendor reports.

| Source | Status | What it validates | Main limit |
| --- | --- | --- | --- |
| [Sharma et al., *Towards Understanding Sycophancy in Language Models*](https://arxiv.org/abs/2310.13548) | ICLR 2024 | Preference signals can reward user-aligned answers; models reverse correct answers after unsupported challenge. | Mostly benchmark conversations, not long-term deployment. |
| [Chen et al., *From Yes-Men to Truth-Tellers*](https://proceedings.mlr.press/v235/chen24u.html) | ICML 2024 | Training can improve resistance to unsupported challenge while preserving more general capability than full fine-tuning. | White-box method, older models, and a narrow challenge format. |
| [Hong et al., *Measuring Sycophancy of Language Models in Multi-turn Dialogues*](https://aclanthology.org/2025.findings-emnlp.121/) | Findings of EMNLP 2025 | Sustained pressure exposes failures missed by single-turn tests; third-person framing helped in one debate setting. | Scenario-specific results do not establish a universal persona rule. |
| [Sicilia et al., *Accounting for Sycophancy in Language Model Uncertainty Estimation*](https://aclanthology.org/2025.findings-naacl.438/) | Findings of NAACL 2025 | User confidence and correctness affect model answers and expressed certainty. | Focuses on uncertainty estimation rather than the full social behavior. |
| [Beigi et al., *Sycophancy Mitigation Through Reinforcement Learning with Uncertainty-Aware Adaptive Reasoning Trajectories*](https://aclanthology.org/2025.emnlp-main.661/) | EMNLP 2025 | Training can combine resistance to false pressure with acceptance of valid corrections. | Requires white-box probabilities and costly search and training. |
| [Pitre et al., *CONSENSAGENT*](https://aclanthology.org/2025.findings-acl.1141/) | Findings of ACL 2025 | Multiple agents can reinforce errors; structured critical interaction improves reasoning accuracy. | Adjacent multi-agent evidence, not a direct sycophancy intervention. |
| [Cheng et al., *Sycophantic AI decreases prosocial intentions and promotes dependence*](https://doi.org/10.1126/science.aec8352) | *Science*, 2026 | Sycophantic validation affects users' judgment, responsibility, and repair intentions. | Controlled interactions cannot measure every long-term effect. |
| [Sinha, *SycoBench-600*](https://aclanthology.org/2026.findings-acl.1759/) | Findings of ACL 2026 | Correction selectivity is the target: resist wrong suggestions and accept correct ones. | Multiple-choice tasks do not cover all conversational settings. |
| [Ranaldi and Pucci, *Learning Multilingual Agentic Policy to Control Sycophancy*](https://aclanthology.org/2026.eacl-long.169/) | EACL 2026 | A useful control policy chooses among direct answer, countering a misleading signal, and asking for clarification. | The tested intervention is a trained policy, not a baseline prompt. |
| [Jain et al., *Interaction Context Often Increases Sycophancy in LLMs*](https://doi.org/10.1145/3772318.3791915) | CHI 2026 | Conversation history and memory profiles can increase agreement sycophancy. | Small two-week sample and heterogeneous model effects. |
| [Dubois et al., *Ask don't tell*](https://arxiv.org/abs/2602.23971) | 2026 preprint | Neutral question framing reduced expressed sycophancy more than a generic anti-sycophancy instruction. | Small generated topic set, mostly single-turn, with LLM judges. |
| [Irpan et al., *Consistency Training Helps Stop Sycophancy and Jailbreaks*](https://arxiv.org/abs/2510.27062) | 2025 preprint | Training for invariance to irrelevant cues supports framing-independent answers. | Reported work centers on one model family and requires training access. |
| [Anthropic, *Claude's personal guidance*](https://www.anthropic.com/research/claude-personal-guidance) | First-party operational study, 2026 | Sycophancy appears in real advice conversations and increases under user pushback; one-sided accounts need caution. | Claude-only observational analysis with automated grading. |

Training papers show that targeted synthetic data, preference optimization,
uncertainty-aware reinforcement learning, and consistency training can reduce
measured sycophancy. Those methods are relevant to model developers, but they
do not belong in this repository's baseline. The baseline can control runtime
reasoning and review structure; it cannot repair the underlying reward model.

## Assessment of the WhyTryAI suggestions

The article is a useful prompt cookbook, but its before-and-after Gemini
examples are demonstrations, not controlled comparisons. Its own warning that
results vary by model is important.

| Suggestion | Evidence assessment | Repository-safe use |
| --- | --- | --- |
| 1. Request criticism directly | Plausible, but a generic anti-sycophancy instruction is weaker than changing the information structure in the 2026 framing study. | Ask for the strongest counterevidence, failure modes, and disconfirming checks against explicit criteria. |
| 2. Start a fresh chat | Emerging direct support: interaction history and memory can increase sycophancy, but the effect is heterogeneous. A new chat removes local history; it does not guarantee that product memory or model tendencies are absent. | Give consequential reviewers a neutral, isolated evidence packet. Avoid including the requester's preferred conclusion. |
| 3. Give multiple options | Practical inference, not a demonstrated general mitigation. Comparisons can reveal trade-offs, but a supplied shortlist can still anchor the answer. | Require a viable alternative and “none of these” when the decision warrants it. |
| 4. Ask before sharing your view | Best-supported user-level suggestion. Neutral questions reduce the cue to mirror the user's asserted stance in the controlled framing study. | Put evidence, constraints, and criteria before the user's preference; ask the agent to assess before revealing a preferred option when feasible. |
| 5. Say it is someone else's work | Third-person framing has empirical support, including reduced sycophancy in multi-turn debate, but false attribution is unnecessary deception. [Hong et al., *Measuring Sycophancy of Language Models in Multi-turn Dialogues*](https://doi.org/10.18653/v1/2025.findings-emnlp.121) | Anonymize authorship and ownership when they are irrelevant; say “review this artifact” rather than inventing an author. |
| 6. Force a score or ranking | Structure can force comparison, but no strong source reviewed here shows that arbitrary numeric ratings reduce sycophancy. Scores can add false precision while preserving praise. | Use a defined rubric, evidence for each criterion, and an explicit unknown/not-reviewable state. |
| 7. Use a critical persona | No strong direct support found. A hostile persona can change tone without improving truthfulness and can confuse harshness with rigor. | Use role contracts such as breaker and verifier, with evidence requirements and independent contexts. |

## Repository implementation

The [`baselines/AGENTS.md`](../../baselines/AGENTS.md) evidence contract treats
user claims, confidence, preferences, and prior conclusions as inputs rather
than evidence. It separates empathy from agreement and requires an evidence
re-check before an agent reverses a supported answer. It also requires
proportionate assessment of the central question and routes material
counterevidence and falsification through the epistemic-reliability companion.
Specialist review workflows can require failure modes or viable alternatives
when their task contract needs them.

The [`sycophancy` companion](../../baselines/guardrails/sycophancy.md) provides
the portable extended contract and evaluation cases. The packaged
read-only discovery agents remain focused on observed facts. They separate
observation from inference and do not treat public web results as evidence for
private environments.

These instructions are evidence-backed practical inferences. They do not prove
that a baseline prompt eliminates model-level behavior. They avoid “always
disagree,” which would replace sycophancy with reflexive contrarianism.

## Evaluation contract

Treat the contract as successful only if behavior improves without making
answers needlessly adversarial. The repository records these cases but does not
provide an executable evaluation harness.

1. Build paired prompts that keep the task and evidence fixed while reversing
   the user's stated view, confidence, claimed authority, or challenge. Score
   factual correctness, unsupported stance changes, evidence use, and tone.
2. Include both single-turn and multi-turn tests: a correct first answer
   followed by unsupported pushback, genuine new evidence, and repeated
   pressure. The desired behavior is resistance to unsupported pressure and
   responsiveness to real evidence.
3. Include subjective review cases with clear criteria, authorship revealed
   versus anonymized, and opposing-user-perspective pairs. Check that the
   critique is consistent rather than merely negative.
4. Compare the current contract with a prompt that omits the relevant rule, a
   neutralized question, and an isolated reviewer packet. Do not use an LLM
   judge alone. Manually review a stratified sample because sycophantic prose
   can influence preference-based judging.

The open Anthropic model-written evaluation datasets are a useful starting
point for paired cases, and OpenAI's evaluation guide provides a general
workflow for defining criteria, datasets, graders, and continuous evaluation.
[Anthropic evaluations repository](https://github.com/anthropics/evals) and
[OpenAI evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices)

## External resource map

- **Fixed evaluation data:**
  [`SycophancyEval`](https://github.com/meg-tong/sycophancy-eval) contains the
  feedback, answer-bias, unsupported-challenge, and mistake-mimicry datasets
  used by Sharma et al. Start here for small deterministic regression cases.
- **Multi-turn evaluation:**
  [`SYCON-Bench`](https://github.com/JiseungHong/SYCON-Bench) measures how soon
  and how often a model changes position under sustained pressure. It is more
  representative of agent conversations than single-turn opinion matching.
- **Generated behavior suites:**
  [`Bloom`](https://github.com/safety-research/bloom) generates, runs, and
  judges configurable behavioral scenarios, including sycophancy. Its original
  repository is frozen and points new projects to the maintained Petri/Bloom
  distribution; keep the full seed configuration with results for
  reproducibility.
- **Specification evaluation:** OpenAI publishes both the
  [Model Spec source](https://github.com/openai/model_spec) and a
  [Model Spec evaluation harness](https://github.com/openai/model_spec_evals).
  They are useful references for turning the current baseline contract into
  testable behavior, not proof that a model complies with it.
- **Measurement:** Perez et al.'s
  [datasets and visualizations](https://www.evals.anthropic.com/model-written/)
  provide reproducible paired sycophancy cases; Sharma et al. connects the
  behavior to preference judgments; ELEPHANT broadens evaluation to advice,
  wrongdoing, and preservation of the user's self-image.
- **Training:** Wei et al.'s
  [official intervention generator](https://github.com/google/sycophancy-intervention)
  is the clearest reusable implementation reviewed here. Its knowledge
  filtering is important: training a model to resist users on facts it does
  not know can teach indiscriminate disagreement rather than truthfulness.
- **Runtime prompting:** *Ask don't tell* directly tests neutral question
  framing; the WhyTryAI article is a practical demonstration layer over that
  result, not equivalent evidence for all seven tips.
- **Behavior and operations:** The OpenAI Model Spec provides the clearest
  concise behavioral contract. OpenAI's rollback report and evaluation guide
  are useful for launch criteria and regression testing, while the research
  papers supply the independent empirical basis.

## Repository resources

- [`adversarial-review`](../../skills/adversarial-review/SKILL.md) is the
  strongest structural defense: isolated breaker and verifier roles receive a
  neutral packet, and agreement is explicitly not treated as proof.
- [`review`](../../skills/review/SKILL.md) requires evidence-backed findings,
  separates defects from questions and suggestions, and keeps the reviewed
  artifact unchanged.
- [`audit`](../../skills/audit/SKILL.md) supports bounded, evidence-backed
  inspection across a wider scope.
- [`debug`](../../skills/debug/SKILL.md) and
  [`optimize`](../../skills/optimize/SKILL.md) emphasize falsifiable causes,
  measured targets, and ranked alternatives instead of accepting a preferred
  diagnosis or solution.
- [`to-plan`](../../skills/to-plan/SKILL.md) can turn evaluation work into
  criteria-backed implementation steps.

## Evidence limits

Sycophancy definitions, tasks, products, and model versions differ, so effect
sizes should not be transferred between settings. Prompt-level techniques can
reduce cues but cannot repair training incentives or guarantee truthfulness.
The 2026 framing and interaction-context results are especially relevant to
agents, but one is a preprint and the other uses a small two-week user sample;
they justify targeted evaluations, not universal rules. No primary evidence
reviewed here establishes that numeric scores, multiple options, or celebrity
critic personas reliably reduce sycophancy across models.

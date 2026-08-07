# Visual Design

Review faithfulness before presentation. Never trade a correct model for style.

## Design And Release Pass

1. State the reader question and diagram scope in one sentence.
2. Choose one abstraction level and a familiar notation.
3. Establish a stable reading direction and the primary path.
4. Group by real boundaries, ownership, lifecycle phase, or responsibility.
5. Label elements and non-obvious relationships with concise nouns and verbs.
6. Reduce clutter, choose the visual strategy, then add only the roles and
   emphasis that help answer the reader question.
7. Render at normal destination size. Reject clipping, overlaps, tiny text,
   ambiguous crossings, low contrast, excessive whitespace, or unclear meaning.

For durable architecture diagrams, include title, scope, freshness, and useful
references. Add a legend only for introduced notation.

## Readable Layout And Density

- Review crossings, bends, overlaps, path continuity, edge length, and aspect
  ratio together.
- Keep one reading direction: usually `LR` for pipelines/dependencies and
  `TB` for decomposition/lifecycle. Use curves only when they improve tracing.
- Keep the primary path direct. Move exceptions and secondary paths outward.
- Prefer whitespace and alignment to decorative boxes. Every boundary is real.
- Split mixed questions or abstraction levels. For dense graphs, filter, layer,
  cluster, or add an adjacency table. Do not merge identifiable routes.
- In comparisons, preserve IDs, order, grouping, and direction. Highlight the
  difference.

## Labels And Notation

- Use domain names. Add responsibility or technology only when it answers the
  question.
- Label a non-obvious direction with an active verb such as `calls`,
  `publishes`, `reads`, or `owns`.
- Prefer separate one-way arrows. Label a truly symmetric relationship.
- Use one symbol per meaning and reinforce it with text. Define unfamiliar
  acronyms once and keep terminology consistent.

## Purposeful Visual Style

- Start with readable type, spacing, real boundaries, and a declared color
  strategy.
- Color may encode role, status, category, magnitude, or emphasis. Every
  distinct color needs a named job and consistent meaning.
- Use structural colors for stable roles, semantic colors for outcomes, a
  sequential ramp for magnitude, and a diverging ramp around a named midpoint.
- Keep the main subject strongest and connectors quiet. Accent an edge only
  when its path is the subject or exception, and reinforce it with a label or
  line pattern.
- Preserve meaning in monochrome with labels, shapes, borders, or patterns.
- Choose a readable background. Avoid decorative gradients, shadows, novelty
  fonts, crowded legends, low contrast, and arbitrary rainbow colors.

## Choose A Color Strategy

| Visual purpose | Strategy | Guardrail |
|---|---|---|
| Topology or process | Neutral context plus one or two semantic accents | Accent the subject, boundary, exception, or status—not arbitrary nodes |
| Categories or part-to-whole | Three to six distinguishable hues from an ordered categorical palette | Put the category and value in the tile or legend. Hue never replaces the label |
| Ordered magnitude | One sequential lightness ramp | State the direction and show values. Verify text contrast at both ends |
| Positive/negative change | Two diverging ramps with a quiet midpoint | Name the midpoint and pair color with signs, arrows, or values |
| Risk, health, or state | Stable semantic roles | Do not use red/green alone. Add text, icons, shapes, or patterns |

Select the visual variable before hex-value selection. Use the same mapping in
related views. Reserve the strongest color for the most important reading task,
and remove any color that has no explainable job. For labeled categorical tiles,
multiple saturated hues can improve scanning and visual appeal. This palette
does not justify an unexplained color on every node in a relationship graph.
Keep the full palette in this reference. Individual diagrams should use only
the neutral base and the one or two roles they actually contain.

## Visual Tokens And Family Defaults

The bundled `*.DESIGN.md` files are the canonical token sources. **Carbon**
is the default. Material, Tailwind, Nord, Catppuccin, Dracula, Gruvbox,
Solarized, and Tokyo Night are alternatives. Use
the light tokens unless the destination requires dark mode. Prefer
renderer-native tokens for editable source and fixed reviewed values for local
assets. A project DESIGN.md, project notation, and official brand colors take
precedence.

Apply tokens after you choose a strategy. Most diagrams use neutral plus one or
two roles. Use the data role for ordinary class/ER entities. Express keys,
cardinality, selection, and ownership with notation, labels, weight, or
patterns. Use categorical palettes only for genuinely categorical views. A role
color needs a modelled role and text, shape, border, or pattern reinforcement.
Keep vendor icons approved, labelled, and unrecolored.

Use these family defaults after you select a design system:

| Family | Default treatment | Use color when |
|---|---|---|
| Context or architecture | Neutral boundaries, context, and quiet edges | A structural role or focus is useful |
| Flow or activity | Process on the main path and decision on branches | An outcome or exception is material |
| Sequence | Stable actor or service participants and neutral messages | A path, failure branch, or external participant is material |
| State or lifecycle | Neutral ordinary states and labeled transitions | Active work or a terminal outcome needs emphasis |
| Class or ER | One data treatment for ordinary entities | Selection or external ownership is in scope |
| Timeline or Gantt | Neutral tasks and restrained process emphasis | A milestone, blocked task, risk, or completion differs |
| Mind map or tree | Focus root and neutral hierarchy | First-level branches are stable labeled categories |
| Formal model | Domain notation and shapes first | A domain-defined state or outcome needs emphasis |
| Dependency network | Neutral peers and quiet links | A stable role or investigated subject must stand out |
| Organization | Restrained people treatment and quiet reporting lines | Executive focus or a vacancy needs emphasis |
| Chart or analysis | A matching categorical, sequential, or diverging palette | Series, magnitude, or status differs in the source data |

## Motion

Motion is optional and supplementary. Animate only a path, transition, or
short staged change when direction or change over time is the reader question.
Keep class/ER, organization, static hierarchy, state notation, and formal-model
relationships static unless movement itself is part of the modeled evidence.
Never turn a solid relationship into a dashed one merely to animate it. Respect
reduced-motion preferences and preserve the complete meaning in a static view.

## Accessibility

- Give the diagram an accessible title and concise description of its purpose.
- For a complex diagram, provide both a short identifier/purpose and a nearby
  or linked structured description of essential elements, relationships,
  order, and conclusion. Keep the long description visible to all when
  practical. Renderer metadata supplements but does not replace it.
- Preserve meaningful sequence in the source and prose. Include the underlying
  data table for a quantitative chart when practical.
- Do not rely on color alone. Keep text, edges, and essential boundaries at
  strong contrast against adjacent colors.
- Icons always have nearby text labels.

## Family Recipes

| Family | Composition | Common failure |
|---|---|---|
| Context/architecture | Put diagram type and scope in the title. Name boundaries. Give each element a short purpose and relevant technology | Mixing conceptual and deployed components |
| Flow/activity | One main direction. Place decisions on the path and label outcomes | Backtracking arrows and unlabeled branches |
| Sequence | Stable participant order. Show one scenario and explicit failure paths | Too many participants or unrelated scenarios |
| State | Name transition events/guards. Group real composite states | Confusing actions with states |
| Class/ER | Use one data treatment, show only relevant members, and use standard keys, cardinality, and relation notation | Rainbow entities, decorative class colors, or a full schema dump |
| Timeline/Gantt | Declare time scale and dependencies. Emphasize milestones sparingly | False precision or unreadable task density |
| Chart/analysis | Choose by comparison/trend/part-to-whole/correlation/flow. Label units, period, source, and series. Preserve values in a table | Truncated magnitude axes, interpolated missing data, or unexplained series |
| Mindmap/tree | One hierarchy and consistent depth. Use tidy spacing | Cross-links that defeat the tree model |
| Automaton/transition system | Mark the initial state, accepting/terminal states, and every transition with domain convention | Decorative state colors, ambiguous terminal meaning, or tangled self/reciprocal transitions |
| Petri/fault/decision model | Preserve formal place, transition, gate, and branch semantics. Label every non-obvious condition | A pretty graph that is not valid domain notation |
| Force-directed network | Use one homogeneous edge meaning in overview views. Filter or split before labeling every relation | Hairballs, label collisions, unstable mental maps, and unexplained proximity |
| Organization | Use one reporting direction, consistent role cards, and explicit vacant positions | Rainbow departments, implied reporting lines, or vacancies that look like people |

Accessibility sources: [WCAG 2.2](https://www.w3.org/TR/WCAG22/),
[W3C non-text contrast](https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast),
[W3C color and pattern technique](https://www.w3.org/WAI/WCAG22/Techniques/general/G111.html),
[W3C complex images](https://www.w3.org/WAI/tutorials/images/complex/).
Design sources: [Carbon visualization palettes](https://carbondesignsystem.com/data-visualization/color-palettes/),
[Carbon chart guidance](https://carbondesignsystem.com/data-visualization/chart-types/),
[C4 notation](https://c4model.com/diagrams/notation),
[C4 review checklist](https://c4model.com/diagrams/checklist).
Research sources: [Diagrams 2024 domain-specific study](https://link.springer.com/chapter/10.1007/978-3-031-71291-3_4),
[Graph Drawing 2025 metrics](https://doi.org/10.4230/LIPIcs.GD.2025.30),
[Graph Drawing 2025 human-validity study](https://doi.org/10.4230/LIPIcs.GD.2025.7),
and [2024 process-diagram eye-tracking study](https://doi.org/10.1016/j.dss.2024.114292).

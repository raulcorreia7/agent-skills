# Metrics And Proxy Limits

- Name the decision or question before you select a measure. Keep the measured
  outcome, baseline, sample, and tool definition visible.
- Use coverage to find unexecuted code, mutation to probe test sensitivity, and
  complexity to locate review candidates. Do not treat their scores as proof.
- Use smells, clone counts, coupling, cohesion, churn, co-change, and
  maintainability scores to locate a concrete question. Do not refactor only to
  remove a smell or lower a score.
- Use change history when divergence, change spread, or recurring defects are
  material. Treat it as a predictive signal, not evidence that change caused
  poor quality or that an author performed poorly.
- Use counts for inventory and triage. Do not rank people or teams by lines,
  commits, defects, findings, tests, comments, reviews, or dependencies.
- Pair an early proxy with an outcome or harm measure and qualitative
  inspection. Publish known blind spots.
- Audit samples for manipulation and measurement drift. Change or retire a
  measure when it no longer answers its question.
- Apply a numeric threshold when an owned contract or applicable standard
  requires it. Do not present that threshold as a complete quality model.

Example—use coverage to direct inspection:

```text
Question: Did the parser change leave a material branch unexercised?
Proxy: changed-line branch coverage from the repository tool
Action: inspect the uncovered branch and its contract
Limit: execution does not prove that assertions detect incorrect behavior
```

Coverage and complexity studies report context-dependent associations, not
universal defect predictors. Proxy-target pressure can also distort the work
that the proxy was meant to describe.

Sources: [Inozemtseva and Holmes, 2014](https://doi.org/10.1145/2568225.2568271),
[Nagappan, Ball, and Zeller, 2006](https://doi.org/10.1145/1134285.1134349),
[Petrović et al., 2021](https://research.google/pubs/long-term-effects-of-mutation-testing/),
[Sjøberg et al., 2013](https://doi.org/10.1109/TSE.2012.89),
[Graves et al., 2000](https://doi.org/10.1109/32.859533), and
[Campbell, 1976](https://eric.ed.gov/?id=ED303512).

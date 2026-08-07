# Graphviz Decision Trees

```dot
// engine: dot
digraph deployment_decision {
  graph [rankdir=TB, splines=polyline, label="Deployment strategy decision"];
  node [shape=diamond, style=filled];
  compatible [label="Backward\ncompatible?"];
  reversible [label="Fast\nrollback?"];
  exposure [label="Limit\nexposure?"];
  rolling [label="Rolling\ndeployment", shape=box];
  bluegreen_compat [label="Blue-green\ndeployment", shape=box];
  bluegreen_rollback [label="Blue-green\ndeployment", shape=box];
  canary [label="Canary\ndeployment", shape=box];
  compatible -> reversible [label="YES"];
  compatible -> bluegreen_compat [label="NO"];
  reversible -> exposure [label="YES"];
  reversible -> bluegreen_rollback [label="NO"];
  exposure -> canary [label="YES"];
  exposure -> rolling [label="NO"];
}
```

Phrase decisions as answerable questions and label every outgoing branch with
consistent vocabulary. Duplicate a recommendation leaf when the view must stay
a true tree; merge it only for an intentional decision DAG. Treat leaves as
recommendations only when assumptions are documented.

Sources: [DOT language](https://graphviz.org/doc/info/lang.html) and
[`dot` layout](https://graphviz.org/docs/layouts/dot/).

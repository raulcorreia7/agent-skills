# Graphviz Finite Automata

Use a point node and incoming arrow for the initial state, `doublecircle` for
accepting states, and label every transition with its alphabet symbol or
predicate. Keep semantic IDs distinct from labels.

## Deterministic Finite Automaton

```dot
// engine: dot
digraph even_ones_dfa {
  graph [rankdir=LR, label="DFA: binary strings with an even number of 1s"];
  node [shape=circle, style=filled];
  start [shape=point, width=0.12, label=""];
  even [label="even", shape=doublecircle];
  odd [label="odd"];
  start -> even;
  even -> even [label="0"];
  even -> odd [label="1"];
  odd -> odd [label="0"];
  odd -> even [label="1"];
}
```

## Nondeterministic Automaton

```dot
// engine: dot
digraph suffix_ab_nfa {
  graph [rankdir=LR, label="NFA: strings over {a,b} ending in ab"];
  node [shape=circle, style=filled];
  start [shape=point, width=0.12, label=""];
  q0 [label="q0"];
  q1 [label="q1"];
  q2 [label="q2", shape=doublecircle];
  start -> q0;
  q0 -> q0 [label="a, b"];
  q0 -> q1 [label="a"];
  q1 -> q2 [label="b"];
  q1 -> q0 [label="ε", style=dashed];
}
```

Nondeterministic transitions can share a symbol; do not merge distinct
destinations. Use `ε` only with controlled fonts and encoding, otherwise an
explained `eps`. A dashed epsilon edge is reinforcement, not sole meaning.
Check self-loops and opposing transitions for separation.

Sources: [Graphviz FSM example](https://graphviz.org/Gallery/directed/fsm.html)
and [node shapes](https://graphviz.org/doc/info/shapes.html).

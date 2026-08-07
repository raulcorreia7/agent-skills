# Graphviz Rendering

Pin Graphviz, the selected layout plugin, and fonts in CI or a container. Use
the smallest probe that exercises the chosen engine.

```text
dot -V
dot -Tpng probe.dot -o probe.png
neato -Tpng probe.dot -o probe-neato.png
dot -Tpng -Gdpi=192 graph.dot -o graph.png
```

Some operating systems package non-`dot` engines separately. For example,
Ubuntu releases can require an additional layout package and `dot -c`; package
names vary by release. Keep setup in team documentation or CI. When readers
lack the runtime, retain `.dot` or `.gv` and publish a reviewed PNG.

Force-directed coordinates can change across Graphviz versions, platforms,
fonts, and backends. Use a numeric seed where supported and review meaning and
readability rather than pixel identity.

Source: [Graphviz command line](https://graphviz.org/doc/info/command.html).

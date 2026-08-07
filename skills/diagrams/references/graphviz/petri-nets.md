# Graphviz Petri Nets

```dot
// engine: dot
digraph order_petri_net {
  graph [rankdir=LR, label="Petri net: single-order fulfillment"];
  ready [label="●", xlabel="Ready", shape=circle];
  reserved [label="Reserved", shape=circle];
  complete [label="Complete", shape=circle];
  reserve [label="", xlabel="reserve", shape=box, width=0.16, height=0.75,
           fixedsize=true];
  ship [label="", xlabel="ship", shape=box, width=0.16, height=0.75,
        fixedsize=true];
  ready -> reserve;
  reserve -> reserved;
  reserved -> ship;
  ship -> complete;
}
```

Places are circles and transitions are bars or narrow rectangles. Arcs connect
places to transitions, never like to like. Mark tokens explicitly and provide
a textual initial marking; here it is one token in `Ready`. Label arc weights
greater than one. Use a specialized Petri-net tool for reachability, liveness,
simulation, or interchange validation.

Source: [ISO/IEC 15909-2](https://www.iso.org/standard/67235.html).

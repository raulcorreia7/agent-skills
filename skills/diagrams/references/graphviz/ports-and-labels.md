# Graphviz Ports And Rich Labels

Use record labels for compact field structure and HTML-like labels for precise,
shallow table composition.

## Record Labels

```dot
// engine: dot
digraph record_ports {
  graph [rankdir=TB, splines=polyline, label="Event projection mapping"];
  node [shape=record, style=filled];
  event [label="{OrderPlaced|{<id> orderId: UUID|<total> total: Money}}"];
  projection [label="{Order summary|{<key> orderId|<amount> amount}}"];
  event:id:s -> projection:key:n [label="key"];
  event:total:s -> projection:amount:n [label="value"];
}
```

A field port is `<portName>`; attach through `node:port` and optionally a
compass point. Escape literal record delimiters. Record routing is limited with
some rank directions and non-`dot` engines.

## HTML-Like Table Labels

```dot
// engine: dot
digraph table_ports {
  graph [rankdir=LR, label="Command validation mapping"];
  node [shape=plain];
  command [label=<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="8">
      <TR><TD COLSPAN="2"><B>Create order</B></TD></TR>
      <TR><TD ALIGN="LEFT">customerId</TD><TD PORT="customer">UUID</TD></TR>
      <TR><TD ALIGN="LEFT">items</TD><TD PORT="items">Item[]</TD></TR>
    </TABLE>
  >];
  handler [label=<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="8">
      <TR><TD><B>Order handler</B></TD></TR>
      <TR><TD PORT="identity">validate identity</TD></TR>
      <TR><TD PORT="catalog">validate catalog</TD></TR>
    </TABLE>
  >];
  command:customer -> handler:identity [label="customer"];
  command:items -> handler:catalog [label="items"];
}
```

HTML-like labels use Graphviz's XML-like grammar, not HTML. Balance tags,
escape XML-sensitive text, quote attributes, keep tables shallow, and provide
the same information in an accessibility description.

Sources: [node shapes](https://graphviz.org/doc/info/shapes.html) and
[attributes](https://graphviz.org/doc/info/attrs.html).

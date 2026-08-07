# Mermaid Sankey

Use `sankey-beta` for conserved or comparable quantities flowing between
stages. Source is CSV-like `source,target,value`; quote fields containing
commas or quotation marks.

```mermaid
sankey-beta
Traffic,Product page,1000
Product page,Checkout,420
Product page,Exit,580
Checkout,Completed,310
Checkout,Failed,110
```

State units and period, keep stages ordered, combine negligible flows, and do
not imply conservation across incompatible bases. Preserve accessible data in
prose or a table. This family is renderer-sensitive; split or simplify when
curves obscure identity or labels collide.

Source: [Mermaid Sankey](https://mermaid.js.org/syntax/sankey.html).

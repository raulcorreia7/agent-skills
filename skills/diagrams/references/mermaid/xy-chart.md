# Mermaid XY Chart

Use `xychart-beta` for compact bars or lines on categorical or numeric axes.
Declare a title, axes, optional ranges, and `bar` or `line` series.

```mermaid
xychart-beta
    title "Weekly completed orders"
    x-axis [Mon, Tue, Wed, Thu, Fri]
    y-axis "Orders" 0 --> 1400
    bar [820, 910, 1010, 1180, 1260]
```

Label units and time basis, start magnitude bars at zero, do not interpolate
missing periods, and provide values in text or a table. Use one series when the
renderer cannot label multiple series clearly.

Source: [Mermaid XY chart](https://mermaid.js.org/syntax/xyChart.html).

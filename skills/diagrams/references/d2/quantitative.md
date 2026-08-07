# D2 Quantitative Grouping Pattern

Use one sequential ramp for one measure. Here color encodes total cost of
ownership while every node also carries its exact value. Containers encode
business units, not another color scale. Use ELK for nested cross-container
layout.

```d2
direction: right
vars: {
  colors: {
    q1: "#FEE8C8"
    q2: "#FDBB84"
    q3: "#FC8D59"
    q4: "#E34A33"
    q5: "#B30000"
  }
}
bank: Bank securities portfolio {
  style.fill: "#F8FAFC"
  corporate: Corporate {
    source: "Data Source\nTCO: USD 100k" {style.fill: ${colors.q1}}
  }
  equities: Equities {
    risk: "Risk Global\nTCO: USD 600k" {style.fill: ${colors.q3}}
    apac: "APAC Ace\nTCO: USD 400k" {style.fill: ${colors.q2}}
    pricing: "Pricing Hub\nTCO: USD 900k" {
      style.fill: ${colors.q4}
      style.font-color: white
    }
  }
  finance: Finance {
    ledger: "Data Ledger\nTCO: USD 1.2m" {
      style.fill: ${colors.q5}
      style.font-color: white
    }
  }
  risk: Risk {
    guard: "Credit Guard\nTCO: USD 700k" {style.fill: ${colors.q3}}
  }
}
bank.risk.guard -> bank.equities.pricing: risk limits
bank.equities.risk -> bank.equities.pricing: sensitivities
bank.equities.pricing -> bank.corporate.source: trades
bank.equities.apac -> bank.finance.ledger: orders
```

Exact values and the sequential ramp are the review focus.

Sources: [D2 classes](https://d2lang.com/tour/classes/) and
[D2 gallery](https://d2lang.com/examples/overview/).

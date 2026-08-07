---
type: diagram
title: "{{system title}} deployment"
description: "Code-to-cloud deployment and environment topology."
timestamp: "{{timestamp}}"
---

# purpose

{{question this view answers}}

# scope

{{environment and deployment boundary}}

# diagram

```mermaid
graph LR
    source["{{observed source or artifact}}"] -->|{{observed build or release relationship}}| delivery["{{observed delivery mechanism}}"]
    delivery -->|{{observed deployment relationship}}| runtime["{{observed runtime resource}}"]
```

# legend

{{notation and environment explanation}}

# evidence

{{portable evidence citations for every material relationship}}

# known omissions

{{evidence-backed omissions or none}}

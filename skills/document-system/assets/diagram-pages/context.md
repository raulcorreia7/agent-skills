---
type: diagram
title: "{{system title}} context"
description: "System context and external relationships."
timestamp: "{{timestamp}}"
---

# purpose

{{question this view answers}}

# scope

{{included boundary and audience}}

# diagram

```mermaid
graph LR
    actor["{{confirmed actor}}"] -->|{{confirmed or observed relationship}}| system["{{system in scope}}"]
    system -->|{{confirmed or observed relationship}}| external["{{external system}}"]
```

# legend

{{notation and boundary explanation}}

# evidence

{{portable evidence citations for every material relationship}}

# known omissions

{{evidence-backed omissions or none}}

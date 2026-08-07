---
type: diagram
title: "{{system title}} logical structure"
description: "Logical components, interfaces, and dependencies within the system boundary."
timestamp: "{{timestamp}}"
---

# purpose

{{reader question about component responsibilities or interfaces}}

# scope

{{included system boundary, audience, and single logical abstraction level. exclude runtime placement}}

# source basis

{{human-confirmed context references and portable evidence citations used for this view}}

# diagram

```mermaid
graph TB
    external["{{observed external system or actor}}"] -->|{{observed relationship}}| component
    subgraph boundary["{{confirmed system boundary}}"]
        component["{{observed component}}"] -->|{{observed relationship}}| interface["{{observed interface or internal dependency}}"]
    end
    interface -->|{{observed relationship}}| dependency["{{observed external dependency}}"]
```

# legend

{{notation and boundary explanation}}

# evidence

{{portable evidence citations for every material component and relationship}}

# known omissions

{{evidence-backed omissions or none}}

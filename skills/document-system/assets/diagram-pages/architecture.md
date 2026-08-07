---
type: diagram
title: "{{system title}} architecture"
description: "Architecture view sourced from confirmed context and/or observed deployment evidence."
timestamp: "{{timestamp}}"
---

# purpose

{{reader question answered by this architecture overview}}

# scope

{{single abstraction-level overview. audience. included boundary. and environment when applicable}}

# source basis

{{human-confirmed context references and/or portable deployment evidence citations used for this view}}

# diagram

```mermaid
graph LR
    source["{{observed actor, repository, or upstream system}}"] -->|{{observed relationship}}| workload["{{observed system entry point or deployed workload}}"]
    workload -->|{{observed relationship}}| dependency["{{observed component, data store, or external dependency}}"]
```

# legend

{{notation, boundary, and environment explanation}}

# evidence

{{portable evidence citations for every material relationship}}

# known omissions

{{evidence-backed omissions or none}}

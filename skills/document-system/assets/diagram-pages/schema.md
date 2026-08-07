---
type: diagram
title: "{{system title}} schema"
description: "Data structures and relationships from observed storage schemas or interface contracts."
timestamp: "{{timestamp}}"
---

# purpose

{{reader question about data structures, ownership, or relationships}}

# scope

{{schema kind. included store or contract boundary. version. and excluded structures}}

# source basis

{{portable schema, migration, contract, or live-metadata evidence citations used for this view}}

# structures

| structure | kind | identifiers or fields in scope | source |
|---|---|---|---|
| {{structure}} | {{table, collection, message, or contract}} | {{keys or fields}} | {{portable evidence citation}} |

# diagram

```mermaid
graph LR
    source["{{observed source structure}}"] -->|{{observed relationship and cardinality}}| target["{{observed target structure}}"]
```

# legend

{{notation, cardinality convention, and version explanation}}

# evidence

{{portable evidence citations for every material structure and relationship}}

# known omissions

{{evidence-backed omissions or none}}

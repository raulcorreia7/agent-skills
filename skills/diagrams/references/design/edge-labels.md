# Edge Labels

Label an edge when the arrow alone does not explain the action, event, data,
guard, side effect, ownership, dependency type, boundary crossing, or failure
path. Prefer concise verb phrases such as `calls`, `publishes`, `writes`,
`owns`, `validates`, or `retries`.

Do not label an edge when the text only repeats node names or the same obvious
action on every connection. Use nearby prose or a legend when many edges share
one meaning.

For state diagrams and automata:

- label important or surprising guards and side effects.
- group repeated simple transitions through structure or adjacent prose.
- label formal automata transitions with their symbols when those symbols are
  the subject of the diagram.

| Diagram | Syntax | Example |
|---|---|---|
| Graph | `A -->|label| B` | `API -->|writes order| Store` |
| Sequence | `A->>B: label` | `App->>API: POST /orders` |
| State | `A --> B : label` | `Draft --> Submitted : user submits` |
| Class | `A --> B : label` | `Controller --> Service : uses` |
| ER | `A ||--o{ B : label` | `Customer ||--o{ Order : places` |

An unlabeled arrow should mean only the obvious connection implied by the
diagram title and node names.

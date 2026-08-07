# D2 Infrastructure Pattern

Use ELK when nested cloud and subnet boundaries are the main structure. Reuse
role classes and keep product names in labels. Built-in shapes preserve offline
portability.

```d2
vars: {
  d2-config: {
    layout-engine: elk
  }
}
direction: right
classes: {
  compute: {shape: rectangle}
  messaging: {shape: queue}
  data: {shape: cylinder}
}
customer: Customer {shape: person}
cloud: Production cloud {
  edge: Edge gateway {class: compute}
  app_subnet: Application subnet {
    app: Application service {class: compute}
    queue: Message queue {class: messaging}
    orders: SQL database {class: data}
  }
}
customer -> cloud.edge: HTTPS
cloud.edge -> cloud.app_subnet.app: route request
cloud.app_subnet.app -> cloud.app_subnet.queue: publish order
cloud.app_subnet.queue -> cloud.app_subnet.orders: persist order
```

Class names describe roles, so the visual grammar supports other providers.
Add an official local icon only after license, brand, file, and render review;
keep the text label and do not add a runtime URL.

Sources: [D2 classes](https://d2lang.com/tour/classes/),
[D2 icons](https://d2lang.com/tour/icons/).

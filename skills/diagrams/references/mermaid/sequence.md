# Mermaid Sequence Diagram

Use `sequenceDiagram` for one ordered scenario. Declare participant order, use
actors only for people, and label every message. Available constructs include
activation, notes, loops, alternatives, options, parallel or critical regions,
breaks, participant boxes, creation and destruction, and autonumbering.

```mermaid
sequenceDiagram
    accTitle: Submit order
    accDescr: The customer submits an order. The API reserves inventory, then confirms the order or releases the reservation after payment failure.
    autonumber
    actor Customer
    participant API as Order API
    participant Stock as Inventory
    participant Pay as Payment provider
    Customer->>API: POST /orders
    API->>Stock: Reserve items
    Stock-->>API: Reservation
    API->>Pay: Authorise payment
    alt Payment authorised
        Pay-->>API: Authorisation
        API-->>Customer: 201 Created
    else Payment declined
        Pay-->>API: Decline
        API->>Stock: Release reservation
        API-->>Customer: 422 Payment required
    end
```

Keep one scenario, stable participant order, and short messages. A tall image
is preferable to squeezed labels. Split unrelated use cases and avoid long
self-calls, decorative activation bars, or prose-sized messages.

Source: [Mermaid sequence diagram](https://mermaid.js.org/syntax/sequenceDiagram.html).

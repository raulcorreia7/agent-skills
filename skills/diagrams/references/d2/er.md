# D2 Entity Relationship Pattern

Use D2's `sql_table` shape for a physical schema. Keep ordinary tables in one
data treatment; PK/FK markers, field rows, relationship labels, and row-level
connections carry the distinctions. ELK routes to exact rows.

```d2
direction: right

customer: Customer {
  shape: sql_table
  customer_id: uuid {constraint: primary_key}
  email: varchar {constraint: unique}
}
order: Order {
  shape: sql_table
  order_id: uuid {constraint: primary_key}
  customer_id: uuid {constraint: foreign_key}
  status: varchar
}
order_item: Order item {
  shape: sql_table
  order_id: uuid {constraint: foreign_key}
  sku: varchar
  quantity: integer
}
customer.customer_id -> order.customer_id: places {
  source-arrowhead.shape: cf-one-required
  target-arrowhead.shape: cf-many
}
order.order_id -> order_item.order_id: contains {
  source-arrowhead.shape: cf-one-required
  target-arrowhead.shape: cf-many-required
}
```

For a logical model, omit implementation-only foreign keys when relationships
already communicate the association. Do not color every table.

Source: [D2 SQL tables](https://d2lang.com/tour/sql-tables/).

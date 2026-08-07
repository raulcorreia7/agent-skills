# Mermaid Gantt

Use `gantt` for tasks, dates, durations, dependencies, milestones, and
exclusions. Directives include `dateFormat`, `axisFormat`, `tickInterval`,
`excludes`, `includes`, and `todayMarker`; tags include `done`, `active`,
`crit`, and `milestone`.

```mermaid
gantt
    title Checkout release
    dateFormat YYYY-MM-DD
    axisFormat %d %b
    excludes weekends
    section Delivery
    API implementation       :done, api, 2026-07-01, 5d
    Integration verification :crit, test, after api, 4d
    Release decision         :milestone, release, after test, 0d
```

Declare the time basis and exclusions. Give horizontal schedules enough
viewport width before increasing scale. Avoid false precision, excessive color
states, and a task list too dense for publication width.

Source: [Mermaid Gantt](https://mermaid.js.org/syntax/gantt.html).

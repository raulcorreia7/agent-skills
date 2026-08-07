# Mermaid TreeView

Use `treeView-beta` for a directory-like hierarchy. Indentation defines depth;
a trailing `/` marks a directory. Quoted labels allow spaces. Built-in
file/folder icons require `showIcons`. TreeView requires Mermaid 11.14 or later
and older hosts can report “No diagram type detected.”

```text
treeView-beta
    ordering-service/
        src/
            api/
                orders.ts
            domain/
                order.ts
        tests/
            orders.test.ts
        README.md
```

Omit generated and irrelevant files. Large inventories belong in searchable
text. Mermaid 11.16 renders an implicit `/` root above the first item; inspect
the result. Preserve and locally render the source on older hosts. A small
`graph TB` fallback can preserve parent-child edges when native editability
matters more than file/folder semantics, but do not silently substitute it.

Source: [Mermaid TreeView](https://mermaid.js.org/syntax/treeView.html).

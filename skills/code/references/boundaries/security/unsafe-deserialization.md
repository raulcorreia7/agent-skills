# Unsafe Deserialization

- Do not deserialize untrusted native object graphs. Prefer a simple data
  format, an owned type, a strict schema, and a bounded parser.
- Reject dynamic type names, unexpected members, executable hooks, and object
  constructors that can select behavior from the payload.
- Bound document bytes, nesting, collections, strings, references, processing
  time, memory, and output before the parser can exhaust resources.
- Use the [structured-data router](../structured-data/index.md) to select the
  JSON or XML contract when that format applies.
- If a legacy native format is unavoidable, authenticate its envelope before
  parsing. Allow only required types, remove gadget-capable dependencies, and
  isolate parsing with strict resource and privilege limits.
- Treat authenticity as one control. It does not make a gadget-capable parser
  safe or grant authorization to the decoded operation.

Example—decode an owned command instead of a native object:

```text
bounded bytes -> strict JSON parser -> CreateOrderInput schema
              -> reject unknown members and type metadata -> domain command
```

The payload cannot name a runtime class or invoke a constructor.

Source: pinned OWASP [Deserialization Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Deserialization_Cheat_Sheet.md).

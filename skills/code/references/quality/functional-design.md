# Functional Design

Apply this guidance only when the user requests a functional technique, the
repository already establishes one, or a concrete proposal makes its trade-off
relevant. Do not make an application functional by default. Prefer direct,
locally conventional code when the technique would surprise maintainers or
make debugging less obvious.

- Separate deterministic decisions from I/O and other effects when that
  boundary makes the rule, effect ownership, or verification clearer.
- Prefer immutable values when aliasing, concurrency, or unintended state
  change creates a concrete risk. Keep necessary mutation with its owner.
- Model alternatives as closed variants when the domain is genuinely closed
  and the language can check exhaustive handling.
- Represent absence or failure explicitly when it belongs to the contract.
- Use composition, folds, or pipelines when they expose obvious transformation
  stages. Expand them when evaluation order, failure, effects, or intermediate
  state becomes hard to inspect.
- Do not impose application-wide purity, immutability, totality, effect
  abstractions, or a functional-pattern catalog.

Example—a deterministic core owns the rule while the shell owns effects:

```text
input = read_request()
decision = decide(input, current_policy)
persist(decision)
```

Formal work supports bounded guarantees for effects, exhaustive matching, and
totality. It does not establish a universal maintainability advantage. A small
controlled immutability study supports compiler enforcement for its tasks, not
an application-wide default.

Sources: [Moggi, 1991](https://doi.org/10.1016/0890-5401(91)90052-4),
[Maranget, 2007](https://doi.org/10.1017/S0956796807006223),
[Turner, 2004](https://doi.org/10.3217/jucs-010-07-0751), and
[Coblenz et al., 2017](https://doi.org/10.1109/ICSE.2017.52).

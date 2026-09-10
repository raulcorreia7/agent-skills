# Case Tables

One behavior, one table, one body.

## Shape

- Each row carries a friendly name, the inputs, the expected result, and the
  risk it protects.
- Name rows for what the behavior does, prefixed by path: `happy: applies
  percentage discount`, `edit: accepts the exact minimum`, `unhappy: rejects an
  expired coupon`. Name the behavior, not the implementation step.
- Order rows: happy first, then boundaries, then named failures.
- One body arranges, acts, and asserts once. A row that needs its own branch is
  a different behavior and belongs in its own table.
- Take expected results from the oracle, never from recomputing with the code
  under test.

## Count

Cover every promise the contract makes on the happy path, each boundary, and
each failure mode you can name. Usually 3 to 8 rows. A row that cannot name the
risk it protects is deleted. Past roughly ten rows, split by behavior so a
failure points at one thing.

## TypeScript

```ts
const cases = [
  { name: "happy: applies percentage discount", input: { code: "SAVE10", total: 100 }, expected: 90 },
  { name: "happy: waives shipping", input: { code: "SHIP", total: 50 }, expected: 50 },
  { name: "edit: accepts the exact minimum", input: { code: "MIN50", total: 50 }, expected: 45 },
  { name: "unhappy: rejects an unknown code", input: { code: "NOPE", total: 100 }, expected: { error: "invalid_code" } },
  { name: "unhappy: rejects an expired coupon", input: { code: "OLD", total: 100, now: PAST }, expected: { error: "expired" } },
];

describe("applyCoupon", () => {
  it.each(cases)("$name", ({ input, expected }) => {
    expect(applyCoupon(input)).toEqual(expected);
  });
});
```

## Python

```python
CASES = [
    ("happy: applies percentage discount", {"code": "SAVE10", "total": 100}, 90),
    ("edit: accepts the exact minimum", {"code": "MIN50", "total": 50}, 45),
    ("unhappy: rejects an expired coupon", {"code": "OLD", "total": 100}, {"error": "expired"}),
]


@pytest.mark.parametrize("name,payload,expected", CASES, ids=[case[0] for case in CASES])
def test_apply_coupon(name, payload, expected):
    assert apply_coupon(payload) == expected
```

## Go

```go
cases := []struct {
	name     string
	in       Request
	expected Result
}{
	{"happy: applies percentage discount", Request{Code: "SAVE10", Total: 100}, Result{Total: 90}},
	{"unhappy: rejects an expired coupon", Request{Code: "OLD", Total: 100}, Result{Err: ErrExpired}},
}

for _, tc := range cases {
	t.Run(tc.name, func(t *testing.T) {
		if got := ApplyCoupon(tc.in); got != tc.expected {
			t.Fatalf("got %+v, want %+v", got, tc.expected)
		}
	})
}
```

## Table Styles

Prefer the runner's row runner, so each row reports its own name:
`it.each` in TypeScript, `parametrize` in pytest, `t.Run` subtests in Go.
When the runner has no row runner, loop the rows in one test and assert each
with its name in the failure message.

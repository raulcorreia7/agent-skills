# Case Tables

One behavior, rows grouped by path, one body per group.

## Shape

- Groups, in order: `happy`, then `edge` (boundaries and ambiguous input), then
  `unhappy` (named failures). Three at most.
- Each row carries a friendly name, the inputs, the expected result, and the
  risk it protects. Name what the behavior does, not the implementation step.
- The group carries the path and the test name repeats it, so a failure reads
  `unhappy: rejects an expired coupon`. Do not prefix the row name as well.
- One body per group: arrange, act, and assert once. A row that needs its own
  branch is a different behavior and belongs in its own group.
- Take expected results from the oracle, never from recomputing with the code
  under test.

## Count

Cover every promise the contract makes on the happy path, each boundary, and
each failure mode you can name. Usually 3 to 8 rows across all groups. A row
that cannot name the risk it protects is deleted. Past roughly ten rows, split
by behavior so a failure points at one thing.

## TypeScript

```ts
type Case = { name: string; input: CouponInput; expected: number | { error: string } };

const happy: Case[] = [
  { name: "applies percentage discount", input: { code: "SAVE10", total: 100 }, expected: 90 },
  { name: "waives shipping", input: { code: "SHIP", total: 50 }, expected: 50 },
];

const edge: Case[] = [
  { name: "accepts the exact minimum", input: { code: "MIN50", total: 50 }, expected: 45 },
  { name: "rejects an empty code", input: { code: "", total: 100 }, expected: { error: "invalid_code" } },
];

const unhappy: Case[] = [
  { name: "rejects an unknown code", input: { code: "NOPE", total: 100 }, expected: { error: "invalid_code" } },
  { name: "rejects an expired coupon", input: { code: "OLD", total: 100, now: PAST }, expected: { error: "expired" } },
];

describe("applyCoupon", () => {
  const check = (c: Case) => expect(applyCoupon(c.input)).toEqual(c.expected);

  it.each(happy)("happy: $name", check);
  it.each(edge)("edge: $name", check);
  it.each(unhappy)("unhappy: $name", check);
});
```

## Python

```python
CASES = [
    ("happy", "applies percentage discount", {"code": "SAVE10", "total": 100}, 90),
    ("edge", "accepts the exact minimum", {"code": "MIN50", "total": 50}, 45),
    ("unhappy", "rejects an expired coupon", {"code": "OLD", "total": 100}, {"error": "expired"}),
]


@pytest.mark.parametrize(
    "group,name,payload,expected", CASES, ids=[f"{group}: {name}" for group, name, _, _ in CASES]
)
def test_apply_coupon(group, name, payload, expected):
    assert apply_coupon(payload) == expected
```

## Go

```go
groups := map[string][]case{
	"happy":   {{name: "applies percentage discount", in: Request{Code: "SAVE10", Total: 100}, want: Result{Total: 90}}},
	"unhappy": {{name: "rejects an expired coupon", in: Request{Code: "OLD", Total: 100}, want: Result{Err: ErrExpired}}},
}

for group, rows := range groups {
	for _, tc := range rows {
		t.Run(group+": "+tc.name, func(t *testing.T) {
			if got := ApplyCoupon(tc.in); got != tc.want {
				t.Fatalf("got %+v, want %+v", got, tc.want)
			}
		})
	}
}
```

## Table Styles

Prefer the runner's row runner so each row reports its own name: `it.each` in
TypeScript, `parametrize` with explicit `ids` in pytest, and `t.Run` subtests in
Go. When the runner has no row runner, loop the rows in one test and assert each
with its group and name in the failure message.

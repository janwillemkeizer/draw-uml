# Communication diagram

Annex A: Communication Diagram — Interactions (Clause 17). Notation: 17.9.

Frame kind `interaction` or `sd`. UML 1.x name “collaboration diagram” is not used.

Clause 17.9: Communication diagrams correspond to **simple** sequence diagrams that use **none** of the structuring mechanisms such as InteractionUses and CombinedFragments. Message overtaking is assumed not to occur or to be irrelevant.

## Nodes (Table 17.3)

- Frame for the Interaction (17.2.4)
- Lifeline (17.3.4) as a rectangle — **no** dashed tail

## Paths (Table 17.4)

A line between lifelines. The Message is a **small arrow** in the message direction **close to** the message name and sequence number (17.4.4, 17.9.1).

## Sequence expression (17.9.1.3)

```
sequence-term ‘.’ … ‘:’
<sequence-term> ::= [ integer | name ] [ recurrence ]
<recurrence> ::= ‘*’ ‘[’ iteration-clause ‘]’ | ‘[’ guard ‘]’
```

Concurrent iteration: `*||`. Nested recurrence is **not** repeated at inner levels.

Integer: order within the next higher procedural nesting (`3.1.4` follows `3.1.3` within `3.1`). Name: concurrent thread at that nest (`3.1a` concurrent with `3.1b`). Guard example: `[x > y]`. Iteration example: `*[i := 1..n]`. UML does not prescribe the iteration-clause or guard language.

Do not add a vertical time axis.

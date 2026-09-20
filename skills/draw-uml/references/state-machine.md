# State machine diagram

Annex A: State Machine Diagram — State Machines (Clause 14). Frame kind `state machine` or `stm`. Box-header keyword for the metaclass is `«statemachine»` (Annex C, one word).

Protocol state machine: keyword `«protocol»` after the name or in the box header (Annex C).

## State (14.2.4)

Rounded rectangle. Name in the upper compartment. Optional compartments: `entry / <behavior>`, `do / <behavior>`, `exit / <behavior>`, internal transitions.

Composite state: nested substates. Orthogonal regions: dashed line through the composite. Submachine state: rake icon and referenced machine name.

## Pseudostates and final (14.2.4)

| Kind | Notation |
| --- | --- |
| Initial | Filled circle; **one unlabeled** outgoing transition |
| Terminate | X |
| Choice | Hollow diamond (guards evaluated when reached) |
| Junction | Small filled circle |
| Fork / join | Thick bar (orthogonal regions) |
| Shallow history | Circled `H` |
| Deep history | Circled `H*` |
| Entry point | Hollow circle on the border, named |
| Exit point | Circled X on the border, named |
| Final state | Bullseye (a State, not a pseudostate) |

Keyword `«extended»` after the name of an extended Region or StateMachine (Annex C). `{final}` / keyword `«final»` after the name of a leaf State (`isLeaf`).

## Transition (14.2.4)

Solid arrow:

```
<event> [‘[’ <guard> ‘]’] [‘/’ <effect>]
```

Any part MAY be omitted. Completion transitions have no trigger. The transition from the initial pseudostate SHALL NOT have a trigger.

Signal event: signal name. Call event: `op(args)`. Time: `after(…)` / `at(…)`. Change: `when(…)`.

Protocol transitions use `[precondition] operation / [postcondition]` (14.4.4).

# Sequence diagram

Annex A: Sequence Diagram — Interactions (Clause 17). Notation tables: 17.8.1, Messages 17.4.4, Lifelines 17.3.4, Fragments 17.6.4.

Frame kind `interaction` or `sd`. Time increases **downward**.

## Lifeline (17.3.4)

A rectangle head followed by a vertical line (which MAY be dashed) for the lifetime of the participant. Identifying text inside the head:

```
<lifelineident> ::= ([<connectable-element-name>[‘[’ <selector> ‘]’]] [: <connectable-element-type>] [<decomposition>]) | ‘self’
<selector> ::= <expression>
<decomposition> ::= ‘ref’ <interactionident> [‘strict’]
```

Although this syntax allows emptiness, `<lifelineident>` cannot be empty (17.3.4). The head shape is based on the classifier of the represented part; often a white rectangle. Name `self` means the instance of the enclosing classifier. Ports of the encloser MAY be shown separately when `self` is included.

Time increases down the page. Distances are not measurements of time (17.3.3).

ExecutionSpecification: thin gray or white rectangle covering the lifeline (17.2.4.4, 17.3.4). Overlapping executions: overlapping rectangles (Figure 17.2).

DestructionOccurrenceSpecification: X on the lifeline (Table 17.1, 17.4.4).

## Messages (17.4.4) — complete rules

| messageSort | Line | Arrow head |
| --- | --- | --- |
| `asynchCall`, `asynchSignal` | solid | **open** |
| `synchCall` | solid | **filled** |
| `reply` | **dashed** | open **or** filled |
| `createMessage` | **dashed** | **open** |
| `deleteMessage` | (as for the sort used) | MUST end in a DestructionOccurrenceSpecification |

Lost: small black circle at the **arrow** end. Found: small black circle at the **start** end.

Label BNF (17.4.4):

```
<message-label> ::= <request-message-label> | <reply-message-label> | ‘*’
<request-message-label> ::= <message-name> [ ‘(’ [<input-argument-list>] ‘)’ ]
```

`*` is shorthand for an alternative CombinedFragment matching any message type (asterisk triggers in state machines). Argument `-` is a wildcard. Named in-parameters MUST all be named or none.

Creation: createMessage (dashed, open head) typically meets the head of the created lifeline, which starts at that height.

## Combined fragments (17.6.4)

Rectangle with the InteractionOperator in a pentagon. Operands separated by a dashed horizontal line. Operators: `alt`, `opt`, `loop`, `break`, `par`, `seq`, `strict`, `critical`, `neg`, `assert`, `ignore`, `consider`. `ignore` / `consider` list message names.

InteractionUse: frame with operator `ref` (17.7.4).

StateInvariant: `{constraint}` or a small state icon on the lifeline (17.2.4).

GeneralOrdering: dotted line between two occurrence specifications with an arrowhead **in the middle**, not at an end (17.5.4).

Do not number messages with Dewey decimals here; that is communication-diagram notation (17.9).

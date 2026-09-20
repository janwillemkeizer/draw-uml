# Timing diagram

Annex A: Timing Diagram — Interactions (Clause 17). Notation: 17.11, Table 17.6.

Frame kind `interaction` or `sd`. Time increases to the **right**.

## Nodes and paths (Table 17.6)

- Frame for the Interaction (17.2.4)
- Message: same messageSort notation as 17.4.4 (open head async, filled head call, dashed reply, …)
- MessageLabel: notational shorthand; two labels with the same name denote one disrupted message
- State or condition timeline: the state of the classifier or attribute, or a testable condition. The state dimension MAY be continuous as well as discrete
- General value lifeline: value of the connectable element as a function of time
- Lifeline
- DestructionOccurrenceSpecification
- DurationConstraint / DurationObservation
- TimeConstraint / TimeObservation

Stacked lifelines share one time axis.

If the question is only message order, use a sequence diagram. Timing diagrams are for time of occurrence of events that change modeled conditions.

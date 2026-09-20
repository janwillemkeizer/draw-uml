# Interaction overview diagram

Annex A: Interaction Overview Diagram — Interactions (Clause 17). Notation: 17.10.

Frame kind `interaction` or `sd`. The heading text MAY include a list of contained Lifelines that do not appear graphically (17.10.1).

## Relation to activities (17.10.1)

Interaction overview diagrams use **activity diagram notation** (Clause 15) where the nodes are Interactions or InteractionUses. Lifelines and Messages do not appear at this overview level except inside an inline Interaction.

Differences from Activity diagrams stated in 17.10.1:

- In place of ObjectNodes: only (inline) Interactions or InteractionUses. These are special forms of CallBehaviorAction.
- Alternative CombinedFragments → DecisionNode plus corresponding MergeNode.
- Parallel CombinedFragments → ForkNode plus corresponding JoinNode.
- Loop CombinedFragments → simple cycles.
- Branching and joining of branches MUST be properly nested (more restrictive than Activity diagrams).

## Additional nodes (Table 17.5)

- Frame for the Interaction (17.2.4)
- Inline Interaction (anonymous or named)
- InteractionUse (`ref`)

A tool MAY explode an InteractionUse into an inline replica with arguments substituted for parameters.

Do not put ordinary Actions (`Approve loan`) on this canvas; put a `ref` or an inline `sd`.

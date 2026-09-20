# Activity diagram

Annex A: Activity Diagram — Activities (Clause 15). Actions: Clause 16.

Frame kind `activity` or `act`. Parameter nodes sit on the frame when a frame is used (15.2.4). The round-cornered activity border MAY replace the Annex A frame; it MAY also be omitted.

## Action (16.2.4)

Rounded rectangle. Name is a verb phrase. CallBehaviorAction that invokes an Activity: rake (trident) in the lower right (16.3.4).

Keyword `«activity»` when an Activity is shown with Classifier notation (15.2.4).

## Control nodes (15.3.4)

| Node | Notation |
| --- | --- |
| InitialNode | Filled circle. One outgoing edge. |
| ActivityFinalNode | Filled circle in a hollow circle (bullseye). |
| FlowFinalNode | Circle with an X. |
| DecisionNode | Hollow diamond; outgoing edges have guards `[expression]`, including `[else]` when needed. |
| MergeNode | Hollow diamond; multiple incoming, one outgoing; no guards. |
| ForkNode | Thick bar; one incoming, multiple outgoing. |
| JoinNode | Thick bar; multiple incoming, one outgoing. |

A diamond SHALL NOT be used as a fork. Guards belong on edges, not inside the diamond.

## Object nodes (15.4.4)

Rectangle (not rounded) labeled with the object or type. Pins: small squares on an action border. Central buffer: `«centralBuffer»`. Data store: `«datastore»` (Annex C spellings). ObjectFlow MAY carry `«multicast»` or `«multireceive»`.

## Partitions (15.6.4)

Vertical or horizontal swimlanes. External partition: keyword `«external»` in the swimlane header (Annex C). Partitions do not change token semantics.

## Interruptible region (15.6.4)

Dashed rounded rectangle. An interrupting edge leaving the region is drawn with a lightning-bolt presentation option.

## Expansion region (16.12 / 15.x)

Dashed rounded rectangle. Mode keywords (Annex C, top left corner): `«iterative»`, `«parallel»`, `«stream»`.

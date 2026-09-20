# Selecting a UML 2.5.1 diagram kind

Use only the fourteen kinds listed in Annex A. Primary symbols in the contents area decide the kind.

## Structure vs behavior (Annex A)

Structure diagrams show the static structure of objects in a system (elements irrespective of time). They MAY show relationships to behaviors of the classifiers they depict. They do not show the details of dynamic behavior.

Behavior diagrams show the dynamic behavior of objects, including methods, collaborations, activities, and state histories.

Annex A NOTE: this taxonomy does not preclude mixing kinds (for example a state machine nested in an internal structure). Boundaries are not strictly enforced. Prefer one kind per diagram.

## Structure

| Need | Kind | Primary symbols |
| --- | --- | --- |
| Types, features, associations, generalizations | Class | class rectangles and those relationships |
| Snapshot of instances and links | Object | instance specifications (Clause 9) |
| Namespaces, imports, merges | Package | package symbols |
| Parts, ports, connectors of one classifier | Composite structure | parts inside a classifier frame |
| Provided/required interfaces of replaceable units | Component | `«component»` rectangles, balls/sockets |
| Artifacts on deployment targets | Deployment | nodes, artifacts, communication paths |
| Stereotypes extending the metamodel | Profile | `«profile»`, `«Stereotype»`, `«Metaclass»`, extensions |

## Behavior

| Need | Kind | Primary symbols |
| --- | --- | --- |
| Actors and observable goals on a subject | Use case | ellipses, stick-man actors, subject rectangle |
| Token flow (control/object) | Activity | actions, control nodes, activity edges |
| Discrete states and transitions of one context | State machine | states, transitions, pseudostates |
| Message order in time | Sequence | lifelines, messages, fragments |
| Links among participants plus numbered messages | Communication | lifeline boxes, numbered messages (no combined fragments / interaction uses — §17.9) |
| Control flow whose nodes are interactions | Interaction overview | activity control nodes + `sd` / `ref` frames |
| Condition/value versus time | Timing | timelines on a horizontal time axis |

## Not in Annex A

Do not name these as UML 2.5.1 diagram kinds: data-flow, flowchart, ERD, BPMN, C4, SysML requirement/parametric, ArchiMate, “manifestation diagram”, “network architecture diagram”. Information flows (Clause 20) are a model construct, not a fifteenth diagram kind.

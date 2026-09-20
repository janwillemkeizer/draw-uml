# Composite structure diagram

Annex A: Composite Structure Diagram — Structured Classifiers (Clause 11). Collaborations: 11.7.

This is a diagram **of a class or component**. Frame kind is `class` or `cmp` / `component` (Annex A), not a made-up “composite structure” kind string.

## Parts (11.2.4)

A part (Property of a StructuredClassifier) is a box **inside** the owning classifier’s rectangle:

```
<roleName> : <typeName> [<multiplicity>]
```

## Ports (11.3.4)

Squares on the boundary of the classifier or of a part. Name and type MAY be shown. Provided Interfaces: lollipops on the port. Required Interfaces: sockets. Conjugated type: `~` prepended to the type name. Behavior port: notational option in 11.3.4 (state-symbol / line into the owned behavior).

## Connectors (11.2.4)

Solid line between connectable elements (parts, ports). Multiplicity MAY appear at connector ends. Delegation: from an outer port to an inner part or port.

## Collaborations (11.7.4)

Dashed ellipse with the Collaboration name. A CollaborationUse is a dashed ellipse labeled `<name> : <CollaborationType>` with dashed lines to the roles’ participants, keyword `«occurrence»` on the use when shown as a dependency (Annex C).

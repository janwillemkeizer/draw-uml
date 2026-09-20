# Component diagram

Annex A: Component Diagram — Structured Classifiers (Clause 11). Notation: 11.6.4.

Primary symbols: component rectangles, provided/required interface balls and sockets.

## Component (11.6.4)

Classifier rectangle with keyword `«component»` (Annex C). Optionally a classifier icon (two small rectangles on the left edge of a box) in the upper-right corner; if that icon is shown, the keyword MAY be hidden.

Black-box: name plus lollipops/sockets. White-box: nested classifiers, realizing classifiers, or internal structure.

## Interfaces (10.4.4, 11.6.4)

Provided: ball, or InterfaceRealization (dashed line, hollow triangle on the `«interface»`). Required: socket, or Usage `«use»` to an Interface. A Dependency MAY join a socket to a lollipop.

## Realization and manifestation

A ComponentRealization may be shown as a dashed realization arrow or listed in a realizations compartment.

An Artifact manifests a Component: dashed open arrow from Artifact to Component, keyword `«manifest»` (Annex C). Deployment of that Artifact is a deployment diagram (Clause 19). UML 2.x does not deploy a Component directly onto a Node.

## Ports

Same port notation as structured classifiers (11.3.4) on the component border.

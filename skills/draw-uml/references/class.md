# Class diagram

Annex A: Class Diagram — Structured Classifiers (Clause 11). Classifier and feature notation also in Clauses 9–10.

Primary symbols: Classifier rectangles, associations, generalizations.

## Classifier (9.2.4, 11.4.4)

Solid-outline rectangle. Name centered, boldface. **Class has no keyword.** Other metaclasses use the Annex C box-header keyword (`«interface»`, `«dataType»`, `«primitive»`, `«enumeration»`, `«signal»`, `«component»`, …).

Abstract: italic name and/or `{abstract}`.

Active Class (`isActive = true`): extra vertical bar on each side of the rectangle (11.4.4).

Mandatory compartments when not suppressed, in this order: attributes, operations, receptions (9.2.4). Internal structure is also mandatory for Class when shown (11.4.4). Optional: nested classifiers, owned behaviors, constraints.

A suppressed compartment does not imply the model lacks those features.

Static feature: underline. Derived: `/` before the name. Inherited: `^` before the textual form (9.2.4).

## Generalization (9.2.4)

Solid line. Hollow triangle on the **general** Classifier. Separate-target or shared-target style.

Do not use generalization from a Class to an Interface; InterfaceRealization is a dashed line with a hollow triangle on the Interface, or ball notation (10.4.4).

## Association (11.5.4)

Solid line. End adornments, all optional except that a qualifier SHALL NOT be suppressed if present:

- role name
- multiplicity (omitted ⇒ **unspecified**)
- `{prop-modifier}` as in 9.5.4
- visibility
- navigable: open arrowhead; non-navigable: small `x` (style chosen per diagram: show all arrows and crosses; suppress all; or suppress crosses and two-way arrows)
- derived end: `/` before the role name
- end owned by the opposite Classifier: small filled dot at that classifier (if used, used on every end in the diagram)
- qualifier: small rectangle on the path at the qualified end

Shared aggregation: hollow diamond on the end **opposite** the end with aggregation = shared (the whole). Composite aggregation: the same, with the diamond **filled**. The diamond SHALL be noticeably smaller than the n-ary association diamond.

N-ary association (N ≥ 3): a diamond at the junction of the solid lines.

AssociationClass: Class symbol attached to the association path by a dashed line; one name.

Reading-direction triangle next to the association name is documentation only.

Navigability, aggregation, and end ownership are distinct; the old convention that navigable ends are classifier-owned is deprecated (11.5.4).

## Interfaces (10.4.4)

Classifier form: rectangle + `«interface»`. Provided: labeled solid circle (ball, “lollipop”). Required: half-circle socket. Optional dashed Dependency from socket to lollipop.

## Templates (7.3.4)

Dashed rectangle, upper right of the Classifier, listing parameters. Binding: dashed arrow labeled `«bind»` with substitutions.

## Attribute vs association (9.5.3)

Convention (not enforced): a Property typed by a Class is an association end; a Property typed by a DataType is an attribute. Do not show the same Property twice.

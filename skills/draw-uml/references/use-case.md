# Use case diagram

Annex A: Use Case Diagram — Use Cases (Clause 18). Notation: 18.1.4.

Primary symbols: UseCase ellipses, Actor stick-men, subject rectangle.

## UseCase (18.1.4)

Ellipse, name inside or below. An optional stereotype keyword MAY be placed above the name.

Alternatively: Classifier rectangle with an ellipse icon in the upper-right corner; `extension points` is then an optional compartment.

Extension points (compartment heading `extension points`):

```
<extension point> ::= <name> [‘:’ <explanation>]
```

Attributes and operations MAY be shown in compartments inside the oval, with the same content as a Classifier rectangle.

## Subject (18.1.4)

Rectangle, name in the top-left corner, UseCase ellipses visually inside. This is **not** the normal Classifier rectangle (no header compartment stack). It does **not** imply that the subject owns the UseCases.

If the subject is a Classifier with a standard stereotype, that stereotype keyword SHALL be shown in guillemets above the subject name. If the metaclass is otherwise ambiguous, the Classifier keyword from 9.2.4 SHALL be shown.

The same UseCase MAY appear as separate ellipses in multiple subject rectangles.

## Actor (18.1.4)

Stick-man icon with the name usually above or below. Alternatively: Classifier rectangle, keyword `«actor»`. Other icons that convey the kind of Actor MAY be used (for example a distinct icon for non-human Actors).

Actor generalization: hollow triangle on the general Actor (Classifier generalization, 9.2.4).

## Include (18.1.4)

Dashed arrow, **open arrowhead**, from the **base** UseCase to the **included** UseCase, labeled `«include»`.

## Extend (18.1.4)

Dashed arrow, **open arrowhead**, from the **extending** UseCase toward the **extended** UseCase, labeled `«extend»`. Condition and ExtensionPoint references MAY appear in a note attached to that arrow.

## Associations

Solid lines between Actor and UseCase. Multiplicity MAY be shown. Associations between two UseCases are not Include/Extend; those use the dashed forms above.

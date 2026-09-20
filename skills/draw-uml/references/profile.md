# Profile diagram

Annex A: Profile Diagram — Packages (Clause 12). Notation: 12.3.4.

Primary symbols: Profile packages, Stereotype classifiers, metaclasses, Extensions.

## Profile (12.3.4)

Package with keyword `«profile»`.

ProfileApplication (usually shown on the user model): dashed open arrow from the applying Package to the Profile, keyword `«apply»`. If `isStrict = true`, keyword `«strict»` (Annex C).

Metamodel/metaclass reference: dashed line with `«reference»`.

## Stereotype (12.3.4)

Classifier rectangle, keyword `«Stereotype»` — Annex C spelling is `Stereotype` (capital S). Attributes of the Stereotype are tagged values.

## Metaclass

Classifier rectangle, Standard Profile stereotype `«Metaclass»` (Clause 22), typically on a UML metaclass such as Class or Property.

## Extension (12.3.4)

Solid line from the Stereotype to the metaclass with a **filled** triangle on the **metaclass** end. This is an Extension, not a Generalization (Generalization uses a hollow triangle). `{required}` MAY appear when the extension is required.

## Constraints

OCL or prose in a note, constrained to the Stereotype.

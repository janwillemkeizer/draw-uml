# Package diagram

Annex A: Package Diagram — Packages (Clause 12).

Primary symbols: package symbols.

## Package (12.2.4)

Rectangle with a tab containing the name, or a rectangle with the name in the tab and members in the body. Qualified names use `::`.

Keyword `«model»` when the Package is a Model (Annex C). Keyword `«profile»` when it is a Profile.

## Relationships

| Metaclass | Notation | Keyword (Annex C) |
| --- | --- | --- |
| PackageImport, visibility public | dashed open arrow, importer → imported | `«import»` |
| PackageImport, visibility not public | same | `«access»` |
| ElementImport, visibility public | same | `«element import»` |
| ElementImport, visibility not public | same | `«element access»` |
| PackageMerge | dashed open arrow, merging → merged | `«merge»` |
| Nesting | nested symbol, or composed association with a circled plus at the containing end | (none) |

Alias of an imported element MAY be shown.

Packages MAY show contained classifiers; large models SHOULD keep this diagram as a dependency map and put features on a class diagram headed `pkg <PackageName>`.

There is no generalization relationship between packages.

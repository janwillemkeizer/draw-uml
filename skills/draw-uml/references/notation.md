# Shared notation (UML 2.5.1)

Source: OMG UML 2.5.1, Annex A, Annex C, Clauses 7–11. This file states only rules that appear in those subdivisions.

## Diagrams and frames (Annex A)

Each diagram has a contents area. Optionally it has a **frame** (a rectangle) and a **heading** in a name tag (rectangle with a cutoff corner) at the upper left.

Heading syntax (Annex A):

```
[<kind>]<name>[<parameters>]
```

The heading names the namespace enclosing, or the model element owning, the elements shown — **not** the diagram type. The diagram type is defined by the primary graphical symbols in the contents area.

The frame is used when the diagrammed element has border elements (ports on classes/components; entry/exit points on state machines). If the frame is not needed, it MAY be omitted and implied by the tool border. If the frame is omitted, the heading is also omitted.

### Frame `kind` values (complete list, Annex A)

Long forms:

- `activity`
- `class`
- `component`
- `deployment`
- `interaction`
- `package`
- `state machine`
- `use case`

Abbreviations (complete list, Annex A):

- `act` = activity
- `cmp` = component
- `dep` = deployment
- `sd` = interaction
- `pkg` = package
- `stm` = state machine
- `uc` = use case

There is no abbreviation for `class`. Do not invent `obj`, `prf`, `tm`, `iod`, or `cmpst`.

Example: a class diagram of package `Library` is headed `pkg Library` or `package Library`.

Annex A lists fourteen diagram kinds (see SKILL.md). The taxonomy (structure vs behavior) is organizational. Mixing kinds is not forbidden; it is not the default.

## Keywords and stereotypes (Annex C)

UML keywords are reserved words, always enclosed in guillemets: `«keyword»`.

Annex C NOTE: guillemets are not `<<` / `>>`. Replace them with duplicated less-than/greater-than **only** when the character set has no guillemets.

Guillemets also mark stereotype labels. Therefore:

- not every word in guillemets is a keyword;
- not every word in guillemets is a stereotype.

Multiple labels (Annex C):

```
« <label> [ , <label> ]* »
```

or each label in its own guillemets, listed one after the other.

`<label>` is a keyword or a stereotype-label.

Use **only** keyword spellings from Annex C Table C.1. Use Standard Profile stereotype names from Clause 22 Table 22.1. Do not invent keywords. Those tables are in this skill as `references/keywords.md` and `references/standard-profile.md` (load from SKILL.md, not from here).

Keywords are context-sensitive. Reusing a keyword as a user stereotype in a conflicting context is allowed in principle and discouraged (Annex C).

## Classifier rectangle (Clause 9.2.4)

Default notation for a Classifier: solid-outline rectangle, name **centered in boldface**. For case-sensitive languages, Classifier names SHOULD begin with an uppercase character.

If this default is used, a keyword for the metaclass SHALL be shown in guillemets **above the name**, except that **no keyword is needed when the metaclass is Class**.

Keywords and stereotype names: centered, plain face, in guillemets above the name.

Abstract Classifier: italic name, and/or `{abstract}` after or below the name.

Compartment order when not suppressed: **attributes**, then **operations**, then **receptions**. Optional further compartments (nested classifiers, owned behaviors, constraints, internal structure). Any compartment MAY be suppressed; a suppressed compartment does not imply emptiness. A separator line is not drawn for a suppressed compartment.

The attributes compartment, if shown, is always above the other feature compartments. The operations compartment, if shown, is below attributes. The receptions compartment, if shown, is below operations.

Visibility grouping under `public` / `private` / `protected` is optional. Inherited members MAY be shown with a leading `^`.

## Visibility (Clause 7.4, 9.5.4)

```
<visibility> ::= ‘+’ | ‘-’ | ‘#’ | ‘~’
```

| Mark | VisibilityKind |
| --- | --- |
| `+` | public |
| `-` | private |
| `#` | protected |
| `~` | package |

## Property string (Clause 9.5.4)

```
<property> ::= [<visibility>] [‘/’] <name> [‘:’ <prop-type>] [[‘[’ <multiplicity> ‘]’]] [‘=’ <default>] [‘{’ <prop-modifier> [‘,’ <prop-modifier>]* ‘}’]
```

`/` means isDerived. Prop-modifiers defined in 9.5.4: `readOnly`, `union`, `subsets <id>`, `redefines <id>`, `ordered`, `unordered`, `unique`, `nonunique`, `seq` / `sequence`, `id`, plus a constraint expression.

In a Classifier, type, visibility, default, multiplicity, and the property string MAY be suppressed even if present in the model.

**Multiplicity of an attribute:** if the multiplicity term is omitted, it implies 1 (Clause 9.5.4).

**Multiplicity of an association end:** if no multiplicity is shown, no conclusion may be drawn about the multiplicity in the model (Clause 11.5.4).

## Operation string (Clause 9.6.4)

```
<operation> ::= [<visibility>] <name> ‘(’ [<parameter-list>] ‘)’ [‘:’ <return-type> [[‘[’ <multiplicity> ‘]’]] [‘{’ <oper-property> [‘,’ <oper-property>]* ‘}’]]
```

A constructor Operation is marked with the Standard Profile stereotype `«Create»` (Clause 11.4.4, Clause 22). `create` is not an Annex C keyword.

## Generalization (Clause 9.2.4)

Solid line, **hollow triangle** arrowhead on the symbol of the **general** Classifier. Separate-target or shared-target style.

## Substitution (Clause 9.2.4)

Dependency with keyword `«substitute»`.

## Dependency (Clause 7.7.4)

Dashed arrow, open arrowhead, client → supplier. Specialized forms use Annex C keywords on the dashed line (`«use»`, `«import»`, `«access»`, `«merge»`, `«deploy»`, `«manifest»`, `«apply»`, `«bind»`, `«extend»`, `«include»`, and the rest of Table C.1).

PackageImport: `«import»` if visibility is public; `«access»` if not public (Clause 7.7.4 / Annex C).

ElementImport: `«element import»` (public) or `«element access»` (not public).

## Comments and constraints (Clause 7.2.4, 7.6.4)

Comment: note symbol (rectangle with a folded upper-right corner) attached by a dashed line.

Constraint: `{expression}` near the constrained element, or in a `constraints` compartment.

## Instance specification names (Clause 9.8.4)

Underlined name string:

```
<name> : <classifier> [, <classifier>]*
```

Either the name or the classifier MAY be omitted (`: Book` or `copy12`).

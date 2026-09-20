---
name: draw-uml
description: "Draw UML 2.5.1 diagrams using OMG Unified Modeling Language graphical notation (formal/17-12-05). Use whenever the user asks to draw, sketch, generate, update, or review UML, or to model a system as any of the fourteen UML diagram kinds: class, object, package, composite structure, component, deployment, profile, use case, activity, state machine, sequence, communication, interaction overview, or timing — including requests to show classes, objects, APIs, interactions, workflows, states, components, deployments, actors, or use cases as diagrams, even if they never say UML."
license: MIT
compatibility: "Python 3.9+ (stdlib only) for scripts/check.py and scripts/render.py"
metadata:
  version: "1.0.0"
  omg-uml: "2.5.1"
  omg-document: "formal/17-12-05"
---

# Draw UML

The only notation this skill may emit as UML is **OMG UML 2.5.1** concrete syntax ([https://www.omg.org/spec/UML/2.5.1](https://www.omg.org/spec/UML/2.5.1), document formal/17-12-05). PlantUML, Mermaid, crow’s-foot ERD, flowcharts, BPMN, and C4 are not UML. Do not label them as UML.

A diagram is a graphical view of a model (Annex A). The **primary graphical symbols in the contents area** determine the diagram kind. Mixing kinds is permitted by Annex A but is not the default.

## Workflow

1. Identify the question the diagram must answer.
2. Choose exactly one of the **fourteen** kinds in the table below (Annex A). If the request is ambiguous, read [references/select-diagram.md](references/select-diagram.md).
3. Read [references/notation.md](references/notation.md) and the matching kind file before drawing. For keywords, read [references/keywords.md](references/keywords.md). For Standard Profile names, read [references/standard-profile.md](references/standard-profile.md).
4. Author the diagram as JSON using [assets/diagram.schema.json](assets/diagram.schema.json) (an authoring encoding of UML 2.5.1 abstract syntax plus layout — **not** UML notation). Start from a template in `assets/templates/`.
5. Validate against the spec tables:

   ```bash
   python3 scripts/check.py path/to/diagram.json
   ```

6. Render UML concrete syntax (SVG):

   ```bash
   python3 scripts/render.py path/to/diagram.json -o path/to/diagram.svg
   ```

7. Return the SVG (the UML diagram), the JSON, the Annex A kind, the frame heading if any, and a list of notation that was omitted rather than invented.

If `check.py` reports errors, fix them before delivery. Do not ship a drawing that uses a keyword, frame kind, or diagram kind outside UML 2.5.1.

## Fourteen diagram kinds (Annex A)

The list below is the complete Annex A taxonomy. There is no fifteenth kind.

| id | Annex A name | Clause | Reference |
| --- | --- | --- | --- |
| `activity` | Activity Diagram | 15 Activities | [references/activity.md](references/activity.md) |
| `class` | Class Diagram | 11 Structured Classifiers | [references/class.md](references/class.md) |
| `communication` | Communication Diagram | 17 Interactions | [references/communication.md](references/communication.md) |
| `component` | Component Diagram | 11 Structured Classifiers | [references/component.md](references/component.md) |
| `composite-structure` | Composite Structure Diagram | 11 Structured Classifiers | [references/composite-structure.md](references/composite-structure.md) |
| `deployment` | Deployment Diagram | 19 Deployments | [references/deployment.md](references/deployment.md) |
| `interaction-overview` | Interaction Overview Diagram | 17 Interactions | [references/interaction-overview.md](references/interaction-overview.md) |
| `object` | Object Diagram | 9 Classification | [references/object.md](references/object.md) |
| `package` | Package Diagram | 12 Packages | [references/package.md](references/package.md) |
| `profile` | Profile Diagram | 12 Packages | [references/profile.md](references/profile.md) |
| `state-machine` | State Machine Diagram | 14 State Machines | [references/state-machine.md](references/state-machine.md) |
| `sequence` | Sequence Diagram | 17 Interactions | [references/sequence.md](references/sequence.md) |
| `timing` | Timing Diagram | 17 Interactions | [references/timing.md](references/timing.md) |
| `use-case` | Use Case Diagram | 18 Use Cases | [references/use-case.md](references/use-case.md) |

Clause map: [references/spec.md](references/spec.md). Delivery checklist: [references/checklist.md](references/checklist.md).

## Non-negotiable notation (UML 2.5.1)

- **Guillemets.** Keywords and stereotype labels use `« »` (Annex C). Do not replace them with `<< >>` unless the character set has no guillemets; then say so.
- **Keywords.** Only spellings in Annex C Table C.1. Stereotypes from Clause 22 Table 22.1 are not keywords.
- **Frames.** Optional rectangle plus pentagonal heading `[<kind>]<name>[<parameters>]`. `kind` is the owner/namespace, not the diagram type. Long forms and abbreviations are only those in Annex A (see [references/notation.md](references/notation.md)). If the frame is omitted, omit the heading.
- **Invent nothing.** If multiplicity, visibility, or navigability is unknown, omit it. On an association end, omitted multiplicity is unspecified (§11.5.4); it is not 1.
- **No substitute languages.** If the user insists on PlantUML or Mermaid, produce the UML SVG first, then a clearly labeled non-UML export, listing every deviation.

## Output

1. Annex A diagram name and one sentence of purpose.
2. Frame heading string, or “frame omitted”.
3. The SVG (UML concrete syntax).
4. The authoring JSON.
5. Omitted adornments, assumptions, and any follow-on UML diagram that would complete the view.

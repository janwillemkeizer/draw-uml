# Annex C keywords (UML 2.5.1 Table C.1)

Complete keyword list. Spellings are those of Table C.1 (without guillemets). Render every keyword as `«…»`.

This table is the reserved-word vocabulary of UML notation. It is not the Standard Profile (Clause 22).

| Keyword | Metamodel element | Placement |
| --- | --- | --- |
| `abstraction` | Abstraction | dashed-line label |
| `access` | PackageImport (visibility not public) | dashed-line label |
| `activity` | Activity | box header |
| `actor` | Actor | box header |
| `apply` | ProfileApplication | dashed-line label |
| `artifact` | Artifact | box header |
| `centralBuffer` | CentralBufferNode | box header |
| `bind` | TemplateBinding | dashed-line label |
| `collaboration` | Collaboration | box header |
| `component` | Component | box header |
| `datastore` | DataStoreNode | box header |
| `dataType` | DataType | box header |
| `decisionInput` | DecisionNode::decisionInput | note label |
| `decisionInputFlow` | DecisionNode::decisionInputFlow | line label |
| `deploy` | Deployment | dashed-line label |
| `deployment spec` | DeploymentSpecification | box header |
| `device` | Device | box header |
| `element access` | ElementImport (visibility not public) | dashed-line label |
| `element import` | ElementImport (visibility public) | dashed-line label |
| `enumeration` | Enumeration | box header |
| `executionEnvironment` | ExecutionEnvironment | box header |
| `extend` | Extend | dashed-line label |
| `extended` | Region or StateMachine with extended* not empty | after name |
| `external` | ActivityPartition isExternal = true | swimlane header |
| `final` | State::isLeaf | after name |
| `flow` | InformationFlow | dashed-line label |
| `import` | PackageImport (visibility public) | dashed-line label |
| `include` | Include | dashed-line label |
| `information` | InformationItem | box header |
| `interface` | Interface | box header |
| `iterative` | ExpansionRegion mode = iterative | top left corner |
| `localPostcondition` | Action::localPostcondition | box header |
| `localPrecondition` | Action::localPrecondition | box header |
| `manifest` | Manifestation | dashed-line label |
| `merge` | PackageMerge | dashed-line label |
| `model` | Model | box header |
| `multicast` | ObjectFlow isMulticast = true | line label |
| `multireceive` | ObjectFlow isMultireceive = true | line label |
| `occurrence` | CollaborationUse | dashed-line label |
| `parallel` | ExpansionRegion mode = parallel | top left corner |
| `postcondition` | Behavior::postcondition | box header |
| `protocol` | ProtocolStateMachine | after name / box header |
| `precondition` | Behavior::precondition | box header |
| `primitive` | PrimitiveType | box header |
| `profile` | Profile | box header |
| `reference` | Profile metaclassReference or metamodelReference | dashed-line label |
| `representation` | InformationItem::represented | dashed-line label |
| `selection` | ObjectFlow::selection | note label |
| `signal` | Signal | box header |
| `singleExecution` | Activity isSingleExecution = true | inside box |
| `statemachine` | StateMachine | box header |
| `stream` | ExpansionRegion mode = stream | top left corner |
| `Stereotype` | Stereotype | box header |
| `strict` | ProfileApplication isStrict = true | dashed-line label |
| `structured` | StructuredActivityNode | box header |
| `substitute` | Substitution | dashed-line label |
| `transformation` | ObjectFlow::transformation | note label |
| `use` | Usage | dashed-line label |

Machine-readable copy: `assets/spec-tables.json` (`annexC.keywords`).

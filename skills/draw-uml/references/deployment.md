# Deployment diagram

Annex A: Deployment Diagram — Deployments (Clause 19). Frame kind `deployment` or `dep`.

## UML 2.x deployment

Artifacts are deployed to deployment targets. Artifacts MAY `«manifest»` Components. Components are not deployed directly onto Nodes (that was UML 1.x).

## Node (19.2.4, 19.3.4)

A Node is drawn as a three-dimensional box. Box-header keywords (Annex C):

- `«device»` — Device
- `«executionEnvironment»` — ExecutionEnvironment

An ExecutionEnvironment is often nested inside a Device.

Instance-level: underlined `appserver1 : ApplicationServer` with the keyword still in guillemets as required by 9.2.4 / 19.x.

## Artifact (19.4.4)

Classifier rectangle, keyword `«artifact»`. Optional document icon. File names (`loans.jar`) are Artifact names.

Manifestation: dashed open arrow Artifact → Component, `«manifest»`.

Deployment: nest the Artifact in the target, or dashed Dependency `«deploy»` from Artifact to target (Annex C). Nesting is the usual form.

DeploymentSpecification: keyword `«deployment spec»` (Annex C; two words).

## Communication path (19.2.4)

An Association between Nodes: a solid line. Multiplicity and name follow Association rules. It is not a Dependency.

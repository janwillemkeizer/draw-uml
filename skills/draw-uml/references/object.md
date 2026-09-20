# Object diagram

Annex A: Object Diagram — Classification (Clause 9). UML 2.5.1 does not define a separate ObjectDiagram metaclass; the kind is a class diagram whose primary symbols are InstanceSpecifications (9.8).

## Instance specification (9.8.4)

Rectangle. Name string **underlined**:

```
<name> : <classifier> [, <classifier>]*
```

Anonymous: `: Loan`. Name only: `cart`. Multiple classifiers: `kiosk : Terminal, PaymentDevice`.

Slots in a second compartment: `<attribute-name> = <value>`.

## Links

A link is an instance of an Association: a solid line between instance specifications. Role names MAY appear. Do **not** draw generalization triangles, aggregation diamonds, or multiplicities on a link (those belong on the classifying Association).

## Not on this diagram

Operations. Generalization between instances. Treat hybrid class+instance drawings as mixed kinds (Annex A permits mixing; prefer a separate class diagram).

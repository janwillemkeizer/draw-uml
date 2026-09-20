# Delivery checklist (UML 2.5.1)

Run `python3 scripts/check.py <file>.json` first. Then this list.

## Annex A

- [ ] Kind is one of the fourteen names in Annex A.
- [ ] Primary symbols match that kind.
- [ ] Frame `kind`, if present, is one of: `activity`, `class`, `component`, `deployment`, `interaction`, `package`, `state machine`, `use case`, or the abbreviations `act`, `cmp`, `dep`, `sd`, `pkg`, `stm`, `uc`.
- [ ] Heading omitted if and only if the frame is omitted.

## Annex C / Clause 22

- [ ] Every keyword spelling is in Table C.1.
- [ ] Every stereotype spelling is in Table 22.1 or a user Profile (then the Profile is in the model).
- [ ] Guillemets `« »`, not `<< >>`, unless the character set has no guillemets (stated).
- [ ] `«Create»` on a constructor is the Standard Profile stereotype, not a keyword.

## Edges

- [ ] Generalization: solid line, hollow triangle on the general classifier (9.2.4).
- [ ] Interface realization: dashed line, hollow triangle on the interface — not generalization.
- [ ] Shared aggregation: hollow diamond on the whole (11.5.4).
- [ ] Composite aggregation: filled diamond on the whole (11.5.4). The diamond SHALL be noticeably smaller than an n-ary association diamond.
- [ ] Association-end multiplicity omitted ⇒ unspecified, not 1 (11.5.4).
- [ ] Messages (17.4.4): asynchCall/asynchSignal = open arrow head; synchCall = filled arrow head; reply = dashed line, open **or** filled head; createMessage = dashed line, open head; lost/found = filled circle on the unknown end.
- [ ] Include: dashed open arrow, `«include»`, base → included (18.1.4).
- [ ] Extend: dashed open arrow, `«extend»`, extending → extended (18.1.4).

## Kind-specific

- [ ] Communication diagrams use none of InteractionUse or CombinedFragment (§17.9).
- [ ] Interaction overview: nodes are Interactions or InteractionUses, not ordinary actions; branching is properly nested (§17.10).
- [ ] Deployment: artifacts on targets; components are manifested by artifacts, not deployed as in UML 1.x (Clause 19).
- [ ] Object diagram: underlined instance names; no generalization or aggregation diamonds on links (9.8).

## Authoring / render

- [ ] `scripts/check.py` exits 0.
- [ ] `scripts/render.py` produced SVG.
- [ ] Unknown adornments omitted, not guessed.

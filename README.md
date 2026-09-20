# UML 2.5.1 drawing skill

An [Agent Skill](https://agentskills.io/specification) that draws diagrams using **OMG Unified Modeling Language 2.5.1** graphical notation ([formal/17-12-05](https://www.omg.org/spec/UML/2.5.1)).

The skill directory is `skills/draw-uml`. Its `name` is `draw-uml`, matching the directory name required by the Agent Skills specification.

## What “UML” means here

UML 2.5.1 concrete syntax is the notation in the OMG specification (Clauses 7–22, Annex A, Annex C). This skill:

- Uses the fourteen diagram kinds listed in Annex A, and only those
- Uses Annex A frame kinds and abbreviations, and only those
- Uses Annex C Table C.1 keyword spellings, in guillemets `« »`
- Uses Clause 22 Table 22.1 for Standard Profile stereotype names
- Emits **SVG** as the UML diagram (concrete syntax)

PlantUML, Mermaid, crow’s-foot ERD, flowcharts, BPMN, and C4 are not UML 2.5.1. The skill will not label them as UML.

The JSON files under `assets/` are an **authoring encoding** of UML abstract syntax plus layout. They are not UML notation. `scripts/render.py` turns them into SVG that follows the OMG graphical rules.

## Install (user-level)

Repository: [github.com/janwillemkeizer/draw-uml](https://github.com/janwillemkeizer/draw-uml)

Clone it and copy the skill into your personal Cursor skill directories (available in every project on that machine):

```bash
git clone https://github.com/janwillemkeizer/draw-uml.git
cd draw-uml
./scripts/install-user.sh
```

Same install without a long-lived clone:

```bash
npx skills add janwillemkeizer/draw-uml --skill draw-uml --global --agent cursor --copy --yes
```

`./scripts/install-user.sh` copies `skills/draw-uml` into user-level skill directories so Cursor can load it outside this repo.

The folder name stays `draw-uml` (required: it must match the `name` field in `SKILL.md`). Destinations:

| Path | Scope |
| --- | --- |
| `~/.cursor/skills/draw-uml` | Cursor personal skills. Enable **Settings → Agents → Sync Skills for Cloud Agents** if you want Cloud Agents to use the same copy. |
| `~/.agents/skills/draw-uml` | Agent Skills user directory |
| `~/.claude/skills/draw-uml` | Compatibility path Cursor also loads |
| `~/.codex/skills/draw-uml` | Compatibility path Cursor also loads |

Re-run the script after you pull skill updates.

### Project-level

Copy or symlink `skills/draw-uml` into a project skill search path:

```text
<project>/.agents/skills/draw-uml
<project>/.cursor/skills/draw-uml
```

This repository already links `.agents/skills/draw-uml` to `skills/draw-uml`.

Validate the skill package:

```bash
pip install skills-ref
skills-ref validate skills/draw-uml
```

## Draw a diagram

From the skill directory (or with paths adjusted):

```bash
python3 scripts/check.py assets/examples/library-classes.json
python3 scripts/render.py assets/examples/library-classes.json -o /tmp/library-classes.svg
```

Both scripts need Python 3.9+ and the standard library only.

## Layout

```text
skills/draw-uml/
├── SKILL.md                 # required: frontmatter + instructions
├── LICENSE.txt
├── scripts/
│   ├── check.py             # Annex A / C / Clause 22 checks
│   ├── render.py            # JSON → SVG
│   └── uml_spec.py
├── references/              # notation, loaded on demand
├── assets/
│   ├── spec-tables.json     # machine-readable Annex A, C, Clause 22
│   ├── diagram.schema.json
│   ├── templates/           # one JSON skeleton per Annex A kind
│   └── examples/
└── evals/
```

## Normative sources

- UML: https://www.omg.org/spec/UML/2.5.1
- Agent Skills: https://agentskills.io/specification

UML, OMG, and Unified Modeling Language are trademarks of the Object Management Group. This skill is not affiliated with OMG. Notation rules are restated for agents; the OMG PDF and XMI remain authoritative (UML 2.5.1 Clause 2).

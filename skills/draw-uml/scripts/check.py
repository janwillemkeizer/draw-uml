#!/usr/bin/env python3
"""Validate a UML 2.5.1 authoring JSON document against OMG tables.

Exit codes:
  0  valid
  1  validation errors
  2  usage / file errors
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from uml_spec import (  # noqa: E402
    SKILL_ROOT,
    diagram_kind_ids,
    frame_kinds,
    keywords,
    message_sorts,
    stereotypes,
)

GUILLEMET_RE = re.compile(r"«([^»]+)»")
ASCII_FAKE_RE = re.compile(r"<<([^>]+)>>")

ALLOWED_NODE_METACLASSES = {
    "Class",
    "Interface",
    "DataType",
    "PrimitiveType",
    "Enumeration",
    "Signal",
    "InstanceSpecification",
    "Package",
    "Model",
    "Profile",
    "Stereotype",
    "Component",
    "Artifact",
    "Node",
    "Device",
    "ExecutionEnvironment",
    "DeploymentSpecification",
    "Actor",
    "UseCase",
    "Collaboration",
    "Port",
    "Property",
    "Activity",
    "Action",
    "InitialNode",
    "ActivityFinalNode",
    "FlowFinalNode",
    "DecisionNode",
    "MergeNode",
    "ForkNode",
    "JoinNode",
    "CentralBufferNode",
    "DataStoreNode",
    "ObjectNode",
    "ActivityPartition",
    "State",
    "Pseudostate",
    "FinalState",
    "Lifeline",
    "CombinedFragment",
    "InteractionUse",
    "ExecutionSpecification",
    "DestructionOccurrenceSpecification",
    "InformationItem",
}

ALLOWED_EDGE_METACLASSES = {
    "Association",
    "Generalization",
    "InterfaceRealization",
    "Dependency",
    "Usage",
    "PackageImport",
    "PackageMerge",
    "ElementImport",
    "Include",
    "Extend",
    "Extension",
    "Connector",
    "Message",
    "Transition",
    "ControlFlow",
    "ObjectFlow",
    "Manifestation",
    "Deployment",
    "CommunicationPath",
    "InformationFlow",
    "TemplateBinding",
    "Substitution",
    "ComponentRealization",
    "ProfileApplication",
}

KEYWORD_EDGE = {
    "Include": "include",
    "Extend": "extend",
    "PackageMerge": "merge",
    "Manifestation": "manifest",
    "Deployment": "deploy",
    "Usage": "use",
    "Substitution": "substitute",
    "TemplateBinding": "bind",
    "ProfileApplication": "apply",
    "InformationFlow": "flow",
}


def _collect_strings(value: object) -> list[str]:
    found: list[str] = []
    if isinstance(value, str):
        found.append(value)
    elif isinstance(value, list):
        for item in value:
            found.extend(_collect_strings(item))
    elif isinstance(value, dict):
        for item in value.values():
            found.extend(_collect_strings(item))
    return found


def validate(doc: dict) -> list[str]:
    errors: list[str] = []
    kinds = diagram_kind_ids()
    frames = frame_kinds()
    kw = keywords()
    stereo = stereotypes()
    sorts = message_sorts()

    if doc.get("umlVersion") != "2.5.1":
        errors.append("umlVersion must be the string '2.5.1' (OMG UML 2.5.1).")

    kind = doc.get("diagramKind")
    if kind not in kinds:
        errors.append(
            f"diagramKind {kind!r} is not an Annex A kind. "
            f"Allowed: {', '.join(sorted(kinds))}."
        )

    frame = doc.get("frame")
    if frame is not None:
        if not isinstance(frame, dict):
            errors.append("frame must be an object with kind and name.")
        else:
            fk = frame.get("kind")
            if fk not in frames:
                errors.append(
                    f"frame.kind {fk!r} is not an Annex A frame kind. "
                    f"Allowed: {', '.join(sorted(frames))}."
                )
            if not frame.get("name"):
                errors.append("frame.name is required when a frame is present (Annex A).")

    nodes = doc.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        errors.append("nodes must be a non-empty array.")
        nodes = []
    node_ids: set[str] = set()
    metaclasses: dict[str, str] = {}
    for i, node in enumerate(nodes):
        if not isinstance(node, dict):
            errors.append(f"nodes[{i}] must be an object.")
            continue
        nid = node.get("id")
        if not nid:
            errors.append(f"nodes[{i}] is missing id.")
        elif nid in node_ids:
            errors.append(f"duplicate node id {nid!r}.")
        else:
            node_ids.add(nid)
        mc = node.get("metaclass")
        if mc not in ALLOWED_NODE_METACLASSES:
            errors.append(
                f"node {nid!r} metaclass {mc!r} is not a UML 2.5.1 metaclass "
                f"used by this authoring form."
            )
        if nid:
            metaclasses[nid] = mc or ""
        for field in ("x", "y"):
            if field not in node or not isinstance(node[field], (int, float)):
                errors.append(f"node {nid!r} is missing numeric {field} (layout).")
        kwd = node.get("keyword")
        if kwd and kwd not in kw:
            errors.append(
                f"node {nid!r} keyword {kwd!r} is not in Annex C Table C.1."
            )
        for s in node.get("stereotypes") or []:
            if s not in stereo:
                has_profile = any(
                    isinstance(n, dict) and n.get("metaclass") in {"Profile", "Stereotype"}
                    for n in nodes
                    if isinstance(n, dict)
                )
                if not has_profile:
                    errors.append(
                        f"node {nid!r} stereotype {s!r} is not in Clause 22 Table 22.1 "
                        "and the document has no Profile/Stereotype definition (12.3)."
                    )

    edges = doc.get("edges") or []
    if not isinstance(edges, list):
        errors.append("edges must be an array.")
        edges = []
    for i, edge in enumerate(edges):
        if not isinstance(edge, dict):
            errors.append(f"edges[{i}] must be an object.")
            continue
        mc = edge.get("metaclass")
        if mc not in ALLOWED_EDGE_METACLASSES:
            errors.append(f"edges[{i}] metaclass {mc!r} is not a UML 2.5.1 relationship used here.")
        src, tgt = edge.get("source"), edge.get("target")
        if src not in node_ids:
            errors.append(f"edges[{i}] source {src!r} does not name a node.")
        if tgt not in node_ids:
            errors.append(f"edges[{i}] target {tgt!r} does not name a node.")
        kwd = edge.get("keyword")
        if kwd and kwd not in kw:
            errors.append(f"edges[{i}] keyword {kwd!r} is not in Annex C Table C.1.")
        expected = KEYWORD_EDGE.get(mc)
        if expected and kwd and kwd != expected:
            errors.append(
                f"edges[{i}] metaclass {mc} requires keyword {expected!r} (Annex C), not {kwd!r}."
            )
        if mc == "Message":
            ms = edge.get("messageSort")
            if ms not in sorts:
                errors.append(
                    f"edges[{i}] Message must have messageSort in {sorted(sorts)} (17.4.2)."
                )
        agg = edge.get("aggregation", "none")
        if agg in {"shared", "composite"} and edge.get("aggregationOn") not in {"source", "target"}:
            errors.append(
                f"edges[{i}] aggregation {agg} requires aggregationOn 'source' or 'target' "
                "(diamond on the whole, 11.5.4)."
            )

    if kind == "communication":
        for node in nodes:
            if isinstance(node, dict) and node.get("metaclass") in {
                "CombinedFragment",
                "InteractionUse",
            }:
                errors.append(
                    "Communication diagrams use none of CombinedFragment or InteractionUse (17.9)."
                )
                break

    for text in _collect_strings(doc):
        if ASCII_FAKE_RE.search(text):
            errors.append(
                "Found ASCII << >> in place of guillemets. Annex C requires « » unless the "
                "character set has no guillemets."
            )
            break
        for inner in GUILLEMET_RE.findall(text):
            for label in (part.strip() for part in inner.split(",")):
                if label and label not in kw and label not in stereo:
                    errors.append(
                        f"«{label}» is neither an Annex C keyword nor a Clause 22 stereotype."
                    )

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate a UML 2.5.1 authoring JSON file against OMG Annex A / Annex C / Clause 22."
    )
    parser.add_argument("input", help="Path to diagram JSON")
    parser.add_argument("--json", action="store_true", help="Write errors as JSON to stdout")
    args = parser.parse_args(argv)

    path = Path(args.input)
    if not path.is_file():
        print(f"Error: file not found: {path}", file=sys.stderr)
        print("Usage: python3 scripts/check.py <diagram.json>", file=sys.stderr)
        return 2
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"Error: invalid JSON: {exc}", file=sys.stderr)
        return 2
    if not isinstance(doc, dict):
        print("Error: document must be a JSON object.", file=sys.stderr)
        return 2

    errors = validate(doc)
    if args.json:
        json.dump({"ok": not errors, "errors": errors, "skillRoot": str(SKILL_ROOT)}, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        if errors:
            print(f"{path}: {len(errors)} error(s)")
            for err in errors:
                print(f"  - {err}")
        else:
            print(f"{path}: valid UML 2.5.1 authoring document")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

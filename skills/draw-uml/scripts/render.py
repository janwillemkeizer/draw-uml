#!/usr/bin/env python3
"""Render a UML 2.5.1 authoring JSON document to SVG concrete syntax."""

from __future__ import annotations

import argparse
import html
import json
import math
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from uml_spec import tables  # noqa: E402

FONT = "Times New Roman, Times, serif"
SANS = "Helvetica, Arial, sans-serif"


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def guillemet(label: str) -> str:
    return f"«{label}»"


class Svg:
    def __init__(self) -> None:
        self.parts: list[str] = []
        self.min_x = 0.0
        self.min_y = 0.0
        self.max_x = 400.0
        self.max_y = 300.0

    def include(self, x: float, y: float) -> None:
        self.min_x = min(self.min_x, x - 8)
        self.min_y = min(self.min_y, y - 8)
        self.max_x = max(self.max_x, x + 8)
        self.max_y = max(self.max_y, y + 8)

    def box(self, x: float, y: float, w: float, h: float) -> None:
        self.include(x, y)
        self.include(x + w, y + h)

    def add(self, fragment: str) -> None:
        self.parts.append(fragment)

    def line(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        *,
        dashed: bool = False,
        marker_end: str | None = None,
        marker_start: str | None = None,
        width: float = 1.2,
    ) -> None:
        self.include(x1, y1)
        self.include(x2, y2)
        dash = ' stroke-dasharray="6 4"' if dashed else ""
        end = f' marker-end="url(#{marker_end})"' if marker_end else ""
        start = f' marker-start="url(#{marker_start})"' if marker_start else ""
        self.add(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="#111" stroke-width="{width}"{dash}{end}{start} />'
        )

    def text(
        self,
        x: float,
        y: float,
        content: str,
        *,
        size: int = 13,
        anchor: str = "start",
        italic: bool = False,
        bold: bool = False,
        underline: bool = False,
        font: str = FONT,
    ) -> None:
        self.include(x - 40, y - 12)
        self.include(x + 40, y + 4)
        weight = "bold" if bold else "normal"
        style = "italic" if italic else "normal"
        deco = " text-decoration='underline'" if underline else ""
        self.add(
            f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" '
            f'font-family="{font}" font-size="{size}" font-weight="{weight}" '
            f'font-style="{style}"{deco} fill="#111">{esc(content)}</text>'
        )

    def polyline(self, points: list[tuple[float, float]], *, fill: str = "none", stroke: str = "#111") -> None:
        for x, y in points:
            self.include(x, y)
        pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
        self.add(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="1.2" />')

    def dump(self) -> str:
        pad = 24
        x = self.min_x - pad
        y = self.min_y - pad
        w = self.max_x - self.min_x + 2 * pad
        h = self.max_y - self.min_y + 2 * pad
        markers = """
<defs>
  <marker id="open" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="10" markerHeight="10" orient="auto">
    <path d="M 1 1 L 10 6 L 1 11" fill="none" stroke="#111" stroke-width="1.4"/>
  </marker>
  <marker id="filled" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="10" markerHeight="10" orient="auto">
    <path d="M 1 1 L 10 6 L 1 11 Z" fill="#111" stroke="#111"/>
  </marker>
  <marker id="hollow" viewBox="0 0 14 12" refX="13" refY="6" markerWidth="12" markerHeight="12" orient="auto">
    <path d="M 1 1 L 13 6 L 1 11 Z" fill="#fff" stroke="#111" stroke-width="1.2"/>
  </marker>
  <marker id="filled-gen" viewBox="0 0 14 12" refX="13" refY="6" markerWidth="12" markerHeight="12" orient="auto">
    <path d="M 1 1 L 13 6 L 1 11 Z" fill="#111" stroke="#111" stroke-width="1.2"/>
  </marker>
</defs>
"""
        body = "\n".join(self.parts)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x:.1f} {y:.1f} {w:.1f} {h:.1f}" '
            f'width="{w:.0f}" height="{h:.0f}" role="img">\n'
            f"{markers}\n{body}\n</svg>\n"
        )


def _labels(node: dict) -> list[str]:
    lines: list[str] = []
    kwd = node.get("keyword")
    stereos = list(node.get("stereotypes") or [])
    labels = ([kwd] if kwd else []) + stereos
    if labels:
        lines.append(" ".join(guillemet(s) for s in labels))
    name = node.get("name") or node.get("id")
    lines.append(name)
    return lines


def _rect(svg: Svg, x: float, y: float, w: float, h: float, rx: float = 0) -> None:
    svg.box(x, y, w, h)
    rr = f' rx="{rx}" ry="{rx}"' if rx else ""
    svg.add(
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}"{rr} '
        f'fill="#fff" stroke="#111" stroke-width="1.3"/>'
    )


def draw_classifier(svg: Svg, node: dict) -> tuple[float, float, float, float]:
    x, y = node["x"], node["y"]
    attrs = node.get("attributes") or []
    ops = node.get("operations") or []
    recs = node.get("receptions") or []
    lits = node.get("literals") or []
    slots = node.get("slots") or []
    ext = node.get("extensionPoints") or []
    header = _labels(node)
    rows = [
        ("header", header),
        ("attributes", attrs),
        ("operations", ops),
        ("receptions", recs),
        ("literals", lits),
        ("slots", slots),
        ("extension points", ext),
    ]
    shown = [(name, lines) for name, lines in rows if lines or name == "header"]
    line_h = 16
    pad = 8
    inner_w = node.get("width") or max(
        140,
        max((len(s) for _, lines in shown for s in lines), default=10) * 7.2,
    )
    heights: list[float] = []
    for name, lines in shown:
        extra = 10 if name == "extension points" else 0
        heights.append(extra + 2 * pad + line_h * max(1, len(lines)))
    total_h = node.get("height") or sum(heights)
    if node.get("isActive"):
        _rect(svg, x - 4, y, inner_w + 8, total_h)
    _rect(svg, x, y, inner_w, total_h)
    cy = y
    for (name, lines), hh in zip(shown, heights):
        if cy > y:
            svg.line(x, cy, x + inner_w, cy)
        ty = cy + pad + 12
        if name == "extension points":
            svg.text(x + inner_w / 2, ty, "extension points", size=11, anchor="middle", italic=True)
            ty += line_h
        for i, line in enumerate(lines):
            italic = bool(node.get("isAbstract")) and name == "header" and i == len(lines) - 1
            bold = name == "header" and i == len(lines) - 1
            underline = bool(node.get("underline")) or (
                node.get("metaclass") == "InstanceSpecification" and name == "header" and i == len(lines) - 1
            )
            svg.text(
                x + inner_w / 2 if name == "header" else x + pad,
                ty,
                line,
                size=12 if name != "header" else 14,
                anchor="middle" if name == "header" else "start",
                italic=italic,
                bold=bold,
                underline=underline,
            )
            ty += line_h
        cy += hh
    node["_bbox"] = (x, y, inner_w, total_h)
    if node.get("metaclass") == "Component":
        # classifier icon, 11.6.4 — two small rectangles on a box, upper right
        ix, iy = x + inner_w - 28, y + 8
        svg.add(
            f'<rect x="{ix}" y="{iy}" width="18" height="14" fill="#fff" stroke="#111"/>'
            f'<rect x="{ix-4}" y="{iy+2}" width="7" height="4" fill="#fff" stroke="#111"/>'
            f'<rect x="{ix-4}" y="{iy+8}" width="7" height="4" fill="#fff" stroke="#111"/>'
        )
    return x, y, inner_w, total_h


def draw_actor(svg: Svg, node: dict) -> None:
    x, y = node["x"], node["y"]
    svg.add(
        f'<circle cx="{x}" cy="{y}" r="10" fill="none" stroke="#111" stroke-width="1.3"/>'
        f'<line x1="{x}" y1="{y+10}" x2="{x}" y2="{y+36}" stroke="#111" stroke-width="1.3"/>'
        f'<line x1="{x-16}" y1="{y+18}" x2="{x+16}" y2="{y+18}" stroke="#111" stroke-width="1.3"/>'
        f'<line x1="{x}" y1="{y+36}" x2="{x-12}" y2="{y+54}" stroke="#111" stroke-width="1.3"/>'
        f'<line x1="{x}" y1="{y+36}" x2="{x+12}" y2="{y+54}" stroke="#111" stroke-width="1.3"/>'
    )
    svg.include(x - 20, y - 14)
    svg.include(x + 20, y + 70)
    svg.text(x, y + 72, node.get("name") or node["id"], size=13, anchor="middle")
    node["_bbox"] = (x - 20, y - 12, 40, 88)


def draw_usecase(svg: Svg, node: dict) -> None:
    x, y = node["x"], node["y"]
    w = node.get("width") or 140
    h = node.get("height") or 48
    svg.box(x, y, w, h)
    svg.add(
        f'<ellipse cx="{x+w/2}" cy="{y+h/2}" rx="{w/2}" ry="{h/2}" '
        f'fill="#fff" stroke="#111" stroke-width="1.3"/>'
    )
    svg.text(x + w / 2, y + h / 2 + 4, node.get("name") or node["id"], size=13, anchor="middle")
    node["_bbox"] = (x, y, w, h)


def draw_subject(svg: Svg, node: dict) -> None:
    x, y = node["x"], node["y"]
    w = node.get("width") or 280
    h = node.get("height") or 220
    _rect(svg, x, y, w, h)
    header = _labels(node)
    ty = y + 16
    for line, is_last in [(ln, i == len(header) - 1) for i, ln in enumerate(header)]:
        svg.text(x + 10, ty, line, size=13, bold=is_last, anchor="start")
        ty += 16
    node["_bbox"] = (x, y, w, h)


def draw_package(svg: Svg, node: dict) -> None:
    x, y = node["x"], node["y"]
    w = node.get("width") or 180
    h = node.get("height") or 90
    tab_w, tab_h = 70, 16
    svg.box(x, y, w, h + tab_h)
    svg.add(
        f'<rect x="{x}" y="{y}" width="{tab_w}" height="{tab_h}" fill="#fff" stroke="#111"/>'
        f'<rect x="{x}" y="{y+tab_h}" width="{w}" height="{h}" fill="#fff" stroke="#111"/>'
    )
    header = _labels(node)
    svg.text(x + 8, y + 12, header[0] if len(header) > 1 else "", size=11)
    svg.text(x + 10, y + tab_h + 22, header[-1], size=14, bold=True)
    node["_bbox"] = (x, y, w, h + tab_h)


def draw_node3d(svg: Svg, node: dict) -> None:
    x, y = node["x"], node["y"]
    w = node.get("width") or 160
    h = node.get("height") or 90
    d = 14
    _rect(svg, x, y + d, w, h)
    svg.polyline([(x, y + d), (x + d, y), (x + w + d, y), (x + w, y + d)], fill="#fff")
    svg.polyline([(x + w, y + d), (x + w + d, y), (x + w + d, y + h), (x + w, y + h + d)], fill="#fff")
    header = _labels(node)
    ty = y + d + 20
    for i, line in enumerate(header):
        svg.text(x + w / 2, ty, line, size=13, bold=i == len(header) - 1, anchor="middle")
        ty += 16
    node["_bbox"] = (x, y, w + d, h + d)


def draw_state(svg: Svg, node: dict) -> None:
    x, y = node["x"], node["y"]
    w = node.get("width") or 140
    h = node.get("height") or 50
    _rect(svg, x, y, w, h, rx=16)
    svg.text(x + w / 2, y + h / 2 + 4, node.get("name") or node["id"], size=14, bold=True, anchor="middle")
    node["_bbox"] = (x, y, w, h)


def draw_pseudostate(svg: Svg, node: dict) -> None:
    x, y = node["x"], node["y"]
    kind = node.get("kind") or {
        "InitialNode": "initial",
        "ActivityFinalNode": "activityFinal",
        "FlowFinalNode": "flowFinal",
        "DecisionNode": "decision",
        "MergeNode": "merge",
        "ForkNode": "fork",
        "JoinNode": "join",
        "FinalState": "final",
    }.get(node.get("metaclass"), "initial")
    if kind == "initial":
        svg.add(f'<circle cx="{x}" cy="{y}" r="7" fill="#111"/>')
        node["_bbox"] = (x - 8, y - 8, 16, 16)
    elif kind in {"final", "activityFinal"}:
        svg.add(
            f'<circle cx="{x}" cy="{y}" r="10" fill="none" stroke="#111" stroke-width="1.3"/>'
            f'<circle cx="{x}" cy="{y}" r="6" fill="#111"/>'
        )
        node["_bbox"] = (x - 12, y - 12, 24, 24)
    elif kind == "flowFinal":
        svg.add(
            f'<circle cx="{x}" cy="{y}" r="10" fill="none" stroke="#111" stroke-width="1.3"/>'
            f'<line x1="{x-6}" y1="{y-6}" x2="{x+6}" y2="{y+6}" stroke="#111"/>'
            f'<line x1="{x+6}" y1="{y-6}" x2="{x-6}" y2="{y+6}" stroke="#111"/>'
        )
        node["_bbox"] = (x - 12, y - 12, 24, 24)
    elif kind in {"decision", "merge", "choice"}:
        svg.polyline([(x, y - 16), (x + 16, y), (x, y + 16), (x - 16, y)], fill="#fff")
        node["_bbox"] = (x - 16, y - 16, 32, 32)
    elif kind in {"fork", "join"}:
        svg.add(f'<rect x="{x-20}" y="{y-4}" width="40" height="8" fill="#111"/>')
        node["_bbox"] = (x - 20, y - 4, 40, 8)
    elif kind == "terminate":
        svg.add(
            f'<line x1="{x-8}" y1="{y-8}" x2="{x+8}" y2="{y+8}" stroke="#111" stroke-width="2"/>'
            f'<line x1="{x+8}" y1="{y-8}" x2="{x-8}" y2="{y+8}" stroke="#111" stroke-width="2"/>'
        )
        node["_bbox"] = (x - 10, y - 10, 20, 20)
    else:
        svg.add(f'<circle cx="{x}" cy="{y}" r="6" fill="#111"/>')
        node["_bbox"] = (x - 6, y - 6, 12, 12)
    svg.include(x, y)


def draw_action(svg: Svg, node: dict) -> None:
    x, y = node["x"], node["y"]
    w = node.get("width") or 140
    h = node.get("height") or 40
    _rect(svg, x, y, w, h, rx=12)
    svg.text(x + w / 2, y + h / 2 + 4, node.get("name") or node["id"], size=13, anchor="middle")
    node["_bbox"] = (x, y, w, h)


def draw_lifeline(svg: Svg, node: dict) -> None:
    x, y = node["x"], node["y"]
    w = node.get("width") or 120
    hh = node.get("headHeight") or 36
    length = node.get("lifelineLength") or 260
    _rect(svg, x, y, w, hh)
    ident = node.get("name") or node["id"]
    if node.get("lifelineType"):
        ident = f"{ident} : {node['lifelineType']}" if ident != "self" else "self"
        if ident != "self" and not node.get("name"):
            ident = f": {node['lifelineType']}"
    svg.text(x + w / 2, y + 22, ident, size=13, anchor="middle")
    if length > 0:
        svg.line(x + w / 2, y + hh, x + w / 2, y + hh + length, dashed=True)
        node["_bbox"] = (x, y, w, hh + length)
    else:
        node["_bbox"] = (x, y, w, hh)
    node["_axis"] = (x + w / 2, y + hh)


def draw_frame(svg: Svg, frame: dict, content_bbox: tuple[float, float, float, float]) -> None:
    x, y, w, h = content_bbox
    pad = 28
    fx, fy = x - pad, y - pad - 10
    fw, fh = w + 2 * pad, h + 2 * pad + 18
    _rect(svg, fx, fy, fw, fh)
    kind = frame["kind"]
    name = frame["name"]
    params = frame.get("parameters") or ""
    heading = f"{kind} {name}{params}"
    tag_w = max(90, 8 * len(heading) + 16)
    svg.add(
        f'<path d="M {fx:.1f} {fy:.1f} L {fx+tag_w:.1f} {fy:.1f} L {fx+tag_w+10:.1f} {fy+18:.1f} '
        f'L {fx:.1f} {fy+18:.1f} Z" fill="#fff" stroke="#111" stroke-width="1.2"/>'
    )
    svg.text(fx + 8, fy + 14, heading, size=12, font=SANS)


def _center(node: dict) -> tuple[float, float]:
    x, y, w, h = node["_bbox"]
    return x + w / 2, y + h / 2


def _anchor(node: dict, toward: tuple[float, float]) -> tuple[float, float]:
    x, y, w, h = node["_bbox"]
    cx, cy = x + w / 2, y + h / 2
    tx, ty = toward
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    # intersect axis-aligned rect
    sx = (w / 2) / abs(dx) if dx else math.inf
    sy = (h / 2) / abs(dy) if dy else math.inf
    t = min(sx, sy)
    return cx + dx * t, cy + dy * t


def draw_diamond(svg: Svg, x: float, y: float, filled: bool) -> None:
    s = 8
    svg.polyline(
        [(x - s, y), (x, y - s), (x + s, y), (x, y + s)],
        fill="#111" if filled else "#fff",
    )


def draw_edge(svg: Svg, edge: dict, nodes: dict[str, dict]) -> None:
    src = nodes[edge["source"]]
    tgt = nodes[edge["target"]]
    if src.get("metaclass") == "Lifeline" and tgt.get("metaclass") == "Lifeline" and edge.get("metaclass") == "Message":
        comm = (src.get("lifelineLength") or 0) == 0 or (tgt.get("lifelineLength") or 0) == 0
        if comm:
            sc, tc = _center(src), _center(tgt)
            x1, y1 = _anchor(src, tc)
            x2, y2 = _anchor(tgt, sc)
            svg.line(x1, y1, x2, y2, marker_end="open")
            label = " ".join(filter(None, [edge.get("sequenceExpression"), edge.get("label") or edge.get("name")]))
            if label:
                svg.text((x1 + x2) / 2, (y1 + y2) / 2 - 8, label, size=12, anchor="middle")
            return
        y = edge.get("y") or (src["_axis"][1] + 40)
        x1 = src["_axis"][0]
        x2 = tgt["_axis"][0]
        sort = edge.get("messageSort", "synchCall")
        dashed = sort in {"reply", "createMessage"}
        if sort in {"asynchCall", "asynchSignal", "createMessage"}:
            marker = "open"
        elif sort == "reply":
            marker = "open"
        else:
            marker = "filled"
        svg.line(x1, y, x2, y, dashed=dashed, marker_end=marker)
        label = edge.get("label") or edge.get("name") or ""
        if label:
            svg.text((x1 + x2) / 2, y - 6, label, size=12, anchor="middle")
        return

    sc = _center(src)
    tc = _center(tgt)
    x1, y1 = _anchor(src, tc)
    x2, y2 = _anchor(tgt, sc)
    mc = edge.get("metaclass")
    dashed = mc in {
        "Dependency",
        "Usage",
        "PackageImport",
        "PackageMerge",
        "ElementImport",
        "Include",
        "Extend",
        "InterfaceRealization",
        "Manifestation",
        "Deployment",
        "TemplateBinding",
        "Substitution",
        "ProfileApplication",
        "InformationFlow",
        "ComponentRealization",
    }
    marker = None
    if mc in {"Generalization"}:
        marker = "hollow"
    elif mc in {"InterfaceRealization", "ComponentRealization", "Extension"}:
        marker = "filled-gen" if mc == "Extension" else "hollow"
    elif mc in {
        "Dependency",
        "Usage",
        "PackageImport",
        "Include",
        "Extend",
        "Manifestation",
        "Deployment",
        "TemplateBinding",
        "Substitution",
        "ProfileApplication",
        "InformationFlow",
        "ElementImport",
        "PackageMerge",
    }:
        marker = "open"
    elif mc == "Association":
        if edge.get("targetNavigable") and not edge.get("sourceNavigable"):
            marker = "open"
        elif edge.get("sourceNavigable") and not edge.get("targetNavigable"):
            # reverse open head: draw from target to source
            x1, y1, x2, y2 = x2, y2, x1, y1
            marker = "open"
    elif mc in {"ControlFlow", "ObjectFlow", "Transition", "CommunicationPath"}:
        marker = "open"

    svg.line(x1, y1, x2, y2, dashed=dashed, marker_end=marker)
    mid = ((x1 + x2) / 2, (y1 + y2) / 2)
    kwd = edge.get("keyword")
    name = edge.get("name") or edge.get("label") or ""
    if kwd:
        svg.text(mid[0], mid[1] - 8, guillemet(kwd), size=11, anchor="middle")
    if name:
        svg.text(mid[0], mid[1] + 12, name, size=11, anchor="middle")
    if mc == "Association":
        if edge.get("sourceRole") or edge.get("sourceMultiplicity"):
            svg.text(x1, y1 - 10, " ".join(filter(None, [edge.get("sourceRole"), edge.get("sourceMultiplicity")])), size=11)
        if edge.get("targetRole") or edge.get("targetMultiplicity"):
            svg.text(x2, y2 - 10, " ".join(filter(None, [edge.get("targetRole"), edge.get("targetMultiplicity")])), size=11, anchor="end")
        if edge.get("aggregation") in {"shared", "composite"}:
            whole = src if edge.get("aggregationOn") == "source" else tgt
            wx, wy = _anchor(whole, _center(tgt if whole is src else src))
            draw_diamond(svg, wx, wy, filled=edge["aggregation"] == "composite")
    if mc == "Message" and edge.get("sequenceExpression"):
        svg.text(mid[0], mid[1] - 10, edge["sequenceExpression"], size=11, anchor="middle")


def draw_comment(svg: Svg, comment: dict) -> None:
    x, y = comment["x"], comment["y"]
    w = comment.get("width") or 140
    h = comment.get("height") or 50
    fold = 12
    svg.add(
        f'<path d="M {x} {y} L {x+w-fold} {y} L {x+w} {y+fold} L {x+w} {y+h} L {x} {y+h} Z" '
        f'fill="#fff" stroke="#111" stroke-width="1.2"/>'
        f'<polyline points="{x+w-fold},{y} {x+w-fold},{y+fold} {x+w},{y+fold}" fill="none" stroke="#111"/>'
    )
    svg.box(x, y, w, h)
    svg.text(x + 8, y + 20, comment["body"], size=11)


def draw_interaction_use(svg: Svg, node: dict) -> None:
    x, y = node["x"], node["y"]
    w = node.get("width") or 160
    h = node.get("height") or 56
    _rect(svg, x, y, w, h)
    heading = f"ref {node.get('name') or node['id']}"
    tag_w = max(70, 7 * len(heading) + 12)
    svg.add(
        f'<path d="M {x:.1f} {y:.1f} L {x+tag_w:.1f} {y:.1f} L {x+tag_w+8:.1f} {y+16:.1f} '
        f'L {x:.1f} {y+16:.1f} Z" fill="#fff" stroke="#111" stroke-width="1.2"/>'
    )
    svg.text(x + 6, y + 12, heading, size=11, font=SANS)
    node["_bbox"] = (x, y, w, h)


NODE_DRAWERS = {
    "Class": draw_classifier,
    "Interface": draw_classifier,
    "DataType": draw_classifier,
    "PrimitiveType": draw_classifier,
    "Enumeration": draw_classifier,
    "Signal": draw_classifier,
    "InstanceSpecification": draw_classifier,
    "Stereotype": draw_classifier,
    "Component": draw_classifier,
    "Artifact": draw_classifier,
    "Collaboration": draw_classifier,
    "InformationItem": draw_classifier,
    "Actor": draw_actor,
    "UseCase": draw_usecase,
    "Package": draw_package,
    "Model": draw_package,
    "Profile": draw_package,
    "Node": draw_node3d,
    "Device": draw_node3d,
    "ExecutionEnvironment": draw_node3d,
    "State": draw_state,
    "FinalState": draw_pseudostate,
    "Pseudostate": draw_pseudostate,
    "InitialNode": draw_pseudostate,
    "ActivityFinalNode": draw_pseudostate,
    "FlowFinalNode": draw_pseudostate,
    "DecisionNode": draw_pseudostate,
    "MergeNode": draw_pseudostate,
    "ForkNode": draw_pseudostate,
    "JoinNode": draw_pseudostate,
    "Action": draw_action,
    "Activity": draw_action,
    "ObjectNode": draw_classifier,
    "Lifeline": draw_lifeline,
    "CombinedFragment": draw_classifier,
    "InteractionUse": draw_interaction_use,
    "Port": draw_classifier,
    "Property": draw_classifier,
    "ActivityPartition": draw_classifier,
    "CentralBufferNode": draw_classifier,
    "DataStoreNode": draw_classifier,
    "DeploymentSpecification": draw_classifier,
}


def render(doc: dict) -> str:
    tables()  # ensure spec tables load
    svg = Svg()
    nodes = {n["id"]: n for n in doc["nodes"]}
    for node in doc["nodes"]:
        drawer = NODE_DRAWERS.get(node["metaclass"], draw_classifier)
        if node.get("subject"):
            drawer = draw_subject
        drawer(svg, node)
    for edge in doc.get("edges") or []:
        draw_edge(svg, edge, nodes)
    for comment in doc.get("comments") or []:
        draw_comment(svg, comment)
    if doc.get("frame"):
        xs = [n["_bbox"][0] for n in nodes.values()]
        ys = [n["_bbox"][1] for n in nodes.values()]
        rights = [n["_bbox"][0] + n["_bbox"][2] for n in nodes.values()]
        bottoms = [n["_bbox"][1] + n["_bbox"][3] for n in nodes.values()]
        bbox = (min(xs), min(ys), max(rights) - min(xs), max(bottoms) - min(ys))
        draw_frame(svg, doc["frame"], bbox)
    return svg.dump()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Render UML 2.5.1 authoring JSON to SVG concrete syntax (OMG notation)."
    )
    parser.add_argument("input", help="Path to diagram JSON")
    parser.add_argument("-o", "--output", help="SVG output path (default: input with .svg)")
    args = parser.parse_args(argv)
    path = Path(args.input)
    if not path.is_file():
        print(f"Error: file not found: {path}", file=sys.stderr)
        print("Usage: python3 scripts/render.py <diagram.json> [-o out.svg]", file=sys.stderr)
        return 2
    doc = json.loads(path.read_text(encoding="utf-8"))
    svg = render(doc)
    out = Path(args.output) if args.output else path.with_suffix(".svg")
    out.write_text(svg, encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

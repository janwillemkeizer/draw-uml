"""Load UML 2.5.1 tables bundled with this skill (Annex A, Annex C, Clause 22)."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
TABLES_PATH = SKILL_ROOT / "assets" / "spec-tables.json"


@lru_cache(maxsize=1)
def tables() -> dict:
    return json.loads(TABLES_PATH.read_text(encoding="utf-8"))


def diagram_kind_ids() -> set[str]:
    return {k["id"] for k in tables()["annexA"]["diagramKinds"]}


def frame_kinds() -> set[str]:
    annex = tables()["annexA"]
    return set(annex["frameKindsLong"]) | set(annex["frameKindsShort"])


def keywords() -> set[str]:
    return {row["keyword"] for row in tables()["annexC"]["keywords"]}


def stereotypes() -> set[str]:
    return set(tables()["clause22"]["stereotypes"])


def message_sorts() -> set[str]:
    return set(tables()["messageSort"])

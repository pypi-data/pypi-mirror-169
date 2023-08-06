from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class EdgePattern(Enum):
    DASHED = "dashed"
    DOTTED = "dotted"
    SOLID = "solid"
    WAVY = "wavy"

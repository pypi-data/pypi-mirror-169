from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class NodeSymbol(Enum):
    CIRCLE = "circle"
    CROSS = "cross"
    CUBE = "cube"
    DIAMOND = "diamond"
    PLUS = "plus"
    POINT = "point"
    PYRAMID = "pyramid"
    SPHERE = "sphere"
    STAR = "star"
    TETRAHEDRON = "tetrahedron"

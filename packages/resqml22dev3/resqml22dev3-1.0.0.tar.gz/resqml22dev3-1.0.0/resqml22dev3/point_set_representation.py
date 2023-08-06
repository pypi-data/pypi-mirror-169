from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.abstract_representation import AbstractRepresentation
from resqml22dev3.node_patch import NodePatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PointSetRepresentation(AbstractRepresentation):
    """A representation that consists of one or more node patches.

    Each node patch is an array of XYZ coordinates for the 3D points.
    There is no implied linkage between the multiple patches.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    node_patch: List[NodePatch] = field(
        default_factory=list,
        metadata={
            "name": "NodePatch",
            "type": "Element",
            "min_occurs": 1,
        }
    )

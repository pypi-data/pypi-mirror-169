from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.subnode_patch import SubnodePatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class UniformSubnodePatch(SubnodePatch):
    """
    Use this subnode construction if the number of subnodes is the same for
    every object, e.g., 3 subnodes per edge for all edges.

    :ivar subnode_count_per_object: Number of subnodes per object, with
        the same number for each of this data-object kind in the grid.
    """
    subnode_count_per_object: Optional[int] = field(
        default=None,
        metadata={
            "name": "SubnodeCountPerObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        }
    )

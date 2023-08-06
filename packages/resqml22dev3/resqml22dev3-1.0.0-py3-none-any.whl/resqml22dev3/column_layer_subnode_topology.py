from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.column_subnode_patch import ColumnSubnodePatch
from resqml22dev3.subnode_topology import SubnodeTopology

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ColumnLayerSubnodeTopology(SubnodeTopology):
    """
    This data-object consists of the unstructured cell finite elements subnode
    topology plus the column subnodes.
    """
    column_subnode_patch: List[ColumnSubnodePatch] = field(
        default_factory=list,
        metadata={
            "name": "ColumnSubnodePatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )

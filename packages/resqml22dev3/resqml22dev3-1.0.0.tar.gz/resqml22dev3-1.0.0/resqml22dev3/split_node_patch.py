from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_integer_array import AbstractIntegerArray
from resqml22dev3.jagged_array import JaggedArray
from resqml22dev3.patch import Patch
from resqml22dev3.split_faces import SplitFaces

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SplitNodePatch(Patch):
    """Optional construction used to introduce additional nodes on coordinate
    lines.

    Used to represent complex geometries, e.g., for stair-step grids and
    reverse faults. BUSINESS RULE: Patch index must be positive because
    a patch index of 0 refers to the fundamental column-layer coordinate
    line nodes.

    :ivar count: Number of additional split nodes. Count must be
        positive.
    :ivar parent_node_indices: Parent coordinate line node index for
        each of the split nodes. Used to implicitly define cell
        geometry.
    :ivar cells_per_split_node: Cell indices for each of the split
        nodes. Used to implicitly define cell geometry. List-of-lists
        construction used to support split nodes shared between multiple
        cells.
    :ivar split_faces:
    """
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
    parent_node_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ParentNodeIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    cells_per_split_node: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "CellsPerSplitNode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    split_faces: Optional[SplitFaces] = field(
        default=None,
        metadata={
            "name": "SplitFaces",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )

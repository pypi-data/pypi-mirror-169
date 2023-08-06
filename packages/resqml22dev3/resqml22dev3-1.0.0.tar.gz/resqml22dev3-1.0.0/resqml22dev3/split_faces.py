from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_integer_array import AbstractIntegerArray
from resqml22dev3.split_edges import SplitEdges

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SplitFaces:
    """Optional construction used to introduce additional faces created by
    split nodes.

    Used to represent complex geometries, e.g., for stair-step grids and
    reverse faults.

    :ivar count: Number of additional split faces. Count must be
        positive.
    :ivar parent_face_indices: Parent unsplit face index for each of the
        additional split faces.
    :ivar cell_per_split_face: Cell index for each split face. Used to
        implicitly define cell geometry.
    :ivar split_edges:
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
    parent_face_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ParentFaceIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    cell_per_split_face: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "CellPerSplitFace",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    split_edges: Optional[SplitEdges] = field(
        default=None,
        metadata={
            "name": "SplitEdges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_integer_array import AbstractIntegerArray
from resqml22dev3.jagged_array import JaggedArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SplitEdges:
    """If split nodes are used in the construction of a column-layer grid and
    indexable elements of kind edges are referenced, then the grid edges need
    to be re-defined.

    Use Case: finite elements, especially for higher order geometry.

    :ivar count: Number of edges. Must be positive.
    :ivar parent_edge_indices: Parent unsplit edge index for each of the
        additional split edges.
    :ivar faces_per_split_edge: Association of faces with the split
        edges, used to infer continuity of property, geometry, or
        interpretation with an attachment kind of edges.
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
    parent_edge_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ParentEdgeIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    faces_per_split_edge: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "FacesPerSplitEdge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )

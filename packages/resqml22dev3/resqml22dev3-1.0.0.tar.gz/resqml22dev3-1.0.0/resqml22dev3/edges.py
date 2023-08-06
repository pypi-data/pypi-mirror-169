from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_integer_array import AbstractIntegerArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Edges:
    """Unstructured cell grids require the definition of edges if the subnode
    attachment is of kind edges.

    Use Case: Finite elements, especially for higher order geometry.
    BUSINESS RULE: Edges must be defined for unstructured cell grids if
    subnode nodes of kind edges are used.

    :ivar count: Number of edges. Must be positive.
    :ivar nodes_per_edge: Defines a list of 2 nodes per edge. Count = 2
        x EdgeCount
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
    nodes_per_edge: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "NodesPerEdge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.jagged_array import JaggedArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class UnstructuredColumnEdges:
    """Column edges are used to construct the index for faces.

    For unstructured column-layer grids, the column edge indices must be
    defined explicitly. Column edges are not required to describe lowest
    order grid geometry, but may be needed for higher order geometries
    or properties.

    :ivar count: Number of unstructured column edges in this grid. Must
        be positive.
    :ivar pillars_per_column_edge: Definition of the column edges in
        terms of the pillars-per-column edge. Pillar count per edge is
        usually 2, but the list-of-lists construction is used to allow
        column edges to be defined by more than 2 pillars.
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
    pillars_per_column_edge: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "PillarsPerColumnEdge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )

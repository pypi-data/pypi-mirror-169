from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_truncated_column_layer_grid_representation import AbstractTruncatedColumnLayerGridRepresentation
from resqml22dev3.ijk_grid_geometry import IjkGridGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class TruncatedIjkGridRepresentation(AbstractTruncatedColumnLayerGridRepresentation):
    """Grid class with an underlying IJK topology, together with a 1D split-
    cell list.

    The truncated IJK cells have more than the usual 6 faces. The split
    cells are arbitrary polyhedra, identical to those of an unstructured
    cell grid.

    :ivar ni: Count of I-indices in the grid. Must be positive.
    :ivar nj: Count of J-indices in the grid. Must be positive.
    :ivar geometry:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    ni: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ni",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        }
    )
    nj: Optional[int] = field(
        default=None,
        metadata={
            "name": "Nj",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        }
    )
    geometry: Optional[IjkGridGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "required": True,
        }
    )

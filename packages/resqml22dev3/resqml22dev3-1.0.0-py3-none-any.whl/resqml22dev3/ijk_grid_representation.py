from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_column_layer_grid_representation import AbstractColumnLayerGridRepresentation
from resqml22dev3.ijk_grid_geometry import IjkGridGeometry
from resqml22dev3.kgaps import Kgaps

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class IjkGridRepresentation(AbstractColumnLayerGridRepresentation):
    """Grid whose topology is characterized by structured column indices (I,J)
    and a layer index, K. Cell geometry is characterized by nodes on coordinate
    lines, where each column of the model has 4 sides. Geometric degeneracy is
    permitted. IJK grids support the following specific extensions:

    - IJK radial grids
    - K-Layer gaps
    - IJ-Column gaps

    :ivar ni: Count of cells in the I-direction in the grid. Must be
        positive. I=1,...,NI, I0=0,...,NI-1.
    :ivar nj: Count of cells in the J-direction in the grid. Must be
        positive. J=1,...,NJ, J0=0,...,NJ-1.
    :ivar radial_grid_is_complete: TRUE if the grid is periodic in J,
        i.e., has the topology of a complete 360 degree circle. If TRUE,
        then NJL=NJ. Otherwise, NJL=NJ+1 May be used to change the grid
        topology for either a Cartesian or a radial grid, although
        radial grid usage is by far the more common.
    :ivar kgaps:
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
    radial_grid_is_complete: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RadialGridIsComplete",
            "type": "Element",
        }
    )
    kgaps: Optional[Kgaps] = field(
        default=None,
        metadata={
            "name": "KGaps",
            "type": "Element",
        }
    )
    geometry: Optional[IjkGridGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.patch import Patch
from resqml22dev3.point_geometry import PointGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Grid2DPatch(Patch):
    """Patch representing a single 2D grid and its geometry. The
    FastestAxisCount and the SlowestAxisCount determine the indexing of this
    grid 2D patch, by defining a 1D index for the 2D grid as follows:

    Index = FastestIndex + FastestAxisCount * SlowestIndex
    When stored in HDF5, this indexing order IS the data order, in which case, in HDF5 it would be a 2D array of the SlowestAxisCount*FastestAxisCount.
    I is the fastest axis; J is the slowest.
    Inline is the fastest axis; crossline is the slowest axis.

    :ivar fastest_axis_count: The number of nodes in the fastest
        direction.
    :ivar slowest_axis_count: The number of nodes in the slowest
        direction.
    :ivar geometry:
    """
    class Meta:
        name = "Grid2dPatch"

    fastest_axis_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "FastestAxisCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
    slowest_axis_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "SlowestAxisCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
    geometry: Optional[PointGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )

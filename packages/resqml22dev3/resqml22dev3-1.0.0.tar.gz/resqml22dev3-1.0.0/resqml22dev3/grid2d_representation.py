from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_surface_representation import AbstractSurfaceRepresentation
from resqml22dev3.grid2d_patch import Grid2DPatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Grid2DRepresentation(AbstractSurfaceRepresentation):
    """Representation based on a 2D grid.

    For definitions of slowest and fastest axes of the array, see
    Grid2dPatch.
    """
    class Meta:
        name = "Grid2dRepresentation"
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    grid2d_patch: Optional[Grid2DPatch] = field(
        default=None,
        metadata={
            "name": "Grid2dPatch",
            "type": "Element",
            "required": True,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.abstract_surface_representation import AbstractSurfaceRepresentation
from resqml22dev3.grid2d_patch import Grid2DPatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Grid2DSetRepresentation(AbstractSurfaceRepresentation):
    """Set of representations based on a 2D grid.

    Each 2D grid representation corresponds to one patch of the set.
    """
    class Meta:
        name = "Grid2dSetRepresentation"
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    grid2d_patch: List[Grid2DPatch] = field(
        default_factory=list,
        metadata={
            "name": "Grid2dPatch",
            "type": "Element",
            "min_occurs": 2,
        }
    )

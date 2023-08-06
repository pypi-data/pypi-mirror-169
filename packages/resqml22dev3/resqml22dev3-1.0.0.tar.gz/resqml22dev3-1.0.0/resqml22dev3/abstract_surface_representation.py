from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.abstract_representation import AbstractRepresentation
from resqml22dev3.patch_boundaries import PatchBoundaries
from resqml22dev3.surface_role import SurfaceRole

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractSurfaceRepresentation(AbstractRepresentation):
    """Parent class of structural surface representations, which can be bounded
    by an outer ring and has inner rings.

    These surfaces may consist of one or more patches.
    """
    surface_role: Optional[SurfaceRole] = field(
        default=None,
        metadata={
            "name": "SurfaceRole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    boundaries: List[PatchBoundaries] = field(
        default_factory=list,
        metadata={
            "name": "Boundaries",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )

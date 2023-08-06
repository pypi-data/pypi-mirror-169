from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_geometry import AbstractGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PatchOfGeometry:
    """
    Indicates which patch of the representation has a new geometry.

    :ivar representation_patch_index: Patch index for the geometry
        attachment, if required.
    :ivar geometry:
    """
    representation_patch_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "RepresentationPatchIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_inclusive": 0,
        }
    )
    geometry: Optional[AbstractGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )

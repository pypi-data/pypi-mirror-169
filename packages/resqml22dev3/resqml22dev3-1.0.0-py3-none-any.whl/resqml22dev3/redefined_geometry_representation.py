from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.abstract_representation import AbstractRepresentation
from resqml22dev3.data_object_reference import DataObjectReference
from resqml22dev3.patch_of_geometry import PatchOfGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class RedefinedGeometryRepresentation(AbstractRepresentation):
    """A representation derived from an existing representation by redefining
    its geometry.

    Example use cases include deformation of the geometry of an object,
    change of coordinate system, and change of time &lt;=&gt; depth.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    patch_of_geometry: List[PatchOfGeometry] = field(
        default_factory=list,
        metadata={
            "name": "PatchOfGeometry",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    supporting_representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SupportingRepresentation",
            "type": "Element",
            "required": True,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_object import AbstractObject
from resqml22dev3.single_point_geometry import SinglePointGeometry
from resqml22dev3.wellbore_datum_reference import WellboreDatumReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class MdDatum(AbstractObject):
    """Specifies the location of the measured depth = 0 reference point.
    The location of this reference point is defined with respect to a CRS, which need not be the same as the CRS of a wellbore trajectory representation, which may reference this location.

    :ivar location: The location of the MD reference point relative to a
        local CRS.
    :ivar md_reference:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    location: Optional[SinglePointGeometry] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "required": True,
        }
    )
    md_reference: Optional[WellboreDatumReference] = field(
        default=None,
        metadata={
            "name": "MdReference",
            "type": "Element",
            "required": True,
        }
    )

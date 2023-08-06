from __future__ import annotations
from dataclasses import dataclass
from resqml22dev3.ellipsoidal_csproperty_type import EllipsoidalCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class EllipsoidalCs2(EllipsoidalCspropertyType):
    """
    gml:ellipsoidalCS is an association role to the ellipsoidal coordinate
    system used by this CRS.
    """
    class Meta:
        name = "ellipsoidalCS"
        namespace = "http://www.opengis.net/gml/3.2"

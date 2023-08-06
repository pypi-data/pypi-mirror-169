from __future__ import annotations
from dataclasses import dataclass
from resqml22dev3.ellipsoid_property_type import EllipsoidPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Ellipsoid2(EllipsoidPropertyType):
    """
    gml:ellipsoid is an association role to the ellipsoid used by this geodetic
    datum.
    """
    class Meta:
        name = "ellipsoid"
        namespace = "http://www.opengis.net/gml/3.2"

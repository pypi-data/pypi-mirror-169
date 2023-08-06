from __future__ import annotations
from dataclasses import dataclass
from resqml22dev3.prime_meridian_property_type import PrimeMeridianPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PrimeMeridian2(PrimeMeridianPropertyType):
    """
    gml:primeMeridian is an association role to the prime meridian used by this
    geodetic datum.
    """
    class Meta:
        name = "primeMeridian"
        namespace = "http://www.opengis.net/gml/3.2"

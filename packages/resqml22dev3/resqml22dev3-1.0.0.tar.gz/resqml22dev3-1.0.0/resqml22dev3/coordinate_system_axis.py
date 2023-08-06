from __future__ import annotations
from dataclasses import dataclass
from resqml22dev3.coordinate_system_axis_type import CoordinateSystemAxisType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CoordinateSystemAxis(CoordinateSystemAxisType):
    """
    gml:CoordinateSystemAxis is a definition of a coordinate system axis.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"

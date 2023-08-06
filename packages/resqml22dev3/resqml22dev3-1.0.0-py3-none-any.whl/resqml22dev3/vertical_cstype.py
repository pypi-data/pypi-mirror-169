from __future__ import annotations
from dataclasses import dataclass
from resqml22dev3.abstract_coordinate_system_type import AbstractCoordinateSystemType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class VerticalCstype(AbstractCoordinateSystemType):
    class Meta:
        name = "VerticalCSType"

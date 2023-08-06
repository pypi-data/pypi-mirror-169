from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.identified_object_type import IdentifiedObjectType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PrimeMeridianType(IdentifiedObjectType):
    greenwich_longitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "greenwichLongitude",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )

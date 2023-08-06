from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.abstract_time_object_type import AbstractTimeObjectType
from resqml22dev3.related_time_type import RelatedTimeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractTimePrimitiveType(AbstractTimeObjectType):
    related_time: List[RelatedTimeType] = field(
        default_factory=list,
        metadata={
            "name": "relatedTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )

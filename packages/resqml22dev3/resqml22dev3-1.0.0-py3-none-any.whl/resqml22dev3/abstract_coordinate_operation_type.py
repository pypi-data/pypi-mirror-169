from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.coordinate_operation_accuracy import CoordinateOperationAccuracy
from resqml22dev3.ex_vertical_extent_type import DomainOfValidity
from resqml22dev3.identified_object_type import IdentifiedObjectType
from resqml22dev3.source_crs import SourceCrs
from resqml22dev3.target_crs import TargetCrs

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractCoordinateOperationType(IdentifiedObjectType):
    domain_of_validity: Optional[DomainOfValidity] = field(
        default=None,
        metadata={
            "name": "domainOfValidity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    scope: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        }
    )
    operation_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "operationVersion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    coordinate_operation_accuracy: List[CoordinateOperationAccuracy] = field(
        default_factory=list,
        metadata={
            "name": "coordinateOperationAccuracy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    source_crs: Optional[SourceCrs] = field(
        default=None,
        metadata={
            "name": "sourceCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    target_crs: Optional[TargetCrs] = field(
        default=None,
        metadata={
            "name": "targetCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22dev3.actuate_value import ActuateValue
from resqml22dev3.nil_reason_enumeration_value import NilReasonEnumerationValue
from resqml22dev3.show_value import ShowValue

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CoordinateOperationAccuracy:
    """gml:coordinateOperationAccuracy is an association role to a
    DQ_PositionalAccuracy object as encoded in ISO/TS 19139, either referencing
    or containing the definition of that positional accuracy.

    That object contains an estimate of the impact of this coordinate
    operation on point accuracy. That is, it gives position error
    estimates for the target coordinates of this coordinate operation,
    assuming no errors in the source coordinates.
    """
    class Meta:
        name = "coordinateOperationAccuracy"
        namespace = "http://www.opengis.net/gml/3.2"

    type: str = field(
        init=False,
        default="simple",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        }
    )

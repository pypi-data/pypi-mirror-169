from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class GeologicTime:
    """This class is used to represent a time at several scales:

    - A mandatory and precise DateTime used to characterize a TimeStep in a TimeSeries
    - An optional Age Offset (corresponding to a geological event occurrence) in  years. This age offset must be positive when it represents a GeologicalEvent occurrence in the past. This Age Offset is not required to be positive, to allow for the case of simulating future geological events.
    When geological time is used to represent a geological event cccurrence, the DateTime must be set by the software writer at a date no earlier than 01/01/1950. Any DateTime (even the creation DateTime of the instance) can be set in this attribute field.

    :ivar age_offset_attribute: A Value in Years of the Age Offset
        between the DateTime Attribute value and the DateTime of a
        GeologicalEvent Occurrence. This value must be POSITIVE when it
        represents a Geological Event in The past.
    :ivar date_time: A date, which can be represented according to the
        W3CDTF format.
    """
    age_offset_attribute: Optional[int] = field(
        default=None,
        metadata={
            "name": "AgeOffsetAttribute",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DateTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )

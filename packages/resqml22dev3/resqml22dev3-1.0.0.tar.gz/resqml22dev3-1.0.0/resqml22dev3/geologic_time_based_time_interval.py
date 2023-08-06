from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_time_interval import AbstractTimeInterval
from resqml22dev3.geologic_time import GeologicTime

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GeologicTimeBasedTimeInterval(AbstractTimeInterval):
    """A time interval that is bounded by two geologic times.

    Can correspond to a TimeStep in a TimeSeries, such as the
    International Chronostratigraphic Scale or a regional
    chronostratigraphic scale.
    """
    start: Optional[GeologicTime] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    end: Optional[GeologicTime] = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )

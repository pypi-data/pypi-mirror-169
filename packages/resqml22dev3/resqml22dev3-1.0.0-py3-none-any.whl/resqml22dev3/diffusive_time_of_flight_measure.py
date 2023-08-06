from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.diffusive_time_of_flight_uom import DiffusiveTimeOfFlightUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DiffusiveTimeOfFlightMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[DiffusiveTimeOfFlightUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

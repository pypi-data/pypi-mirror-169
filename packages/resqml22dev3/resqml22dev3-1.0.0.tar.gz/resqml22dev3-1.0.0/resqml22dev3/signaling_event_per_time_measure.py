from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.signaling_event_per_time_uom import SignalingEventPerTimeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class SignalingEventPerTimeMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[SignalingEventPerTimeUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

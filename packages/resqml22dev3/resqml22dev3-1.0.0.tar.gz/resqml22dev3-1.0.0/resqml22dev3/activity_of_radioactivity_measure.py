from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.activity_of_radioactivity_uom import ActivityOfRadioactivityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ActivityOfRadioactivityMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ActivityOfRadioactivityUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

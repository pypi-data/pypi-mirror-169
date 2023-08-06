from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.volume_per_time_per_length_uom import VolumePerTimePerLengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VolumePerTimePerLengthMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[VolumePerTimePerLengthUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.pressure_time_per_volume_uom import PressureTimePerVolumeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PressureTimePerVolumeMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[PressureTimePerVolumeUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

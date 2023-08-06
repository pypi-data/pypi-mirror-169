from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.volume_per_pressure_uom import VolumePerPressureUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VolumePerPressureMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[VolumePerPressureUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

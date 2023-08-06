from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.pressure_per_volume_uom_with_legacy import PressurePerVolumeUomWithLegacy

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PressurePerVolumeMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[PressurePerVolumeUomWithLegacy] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

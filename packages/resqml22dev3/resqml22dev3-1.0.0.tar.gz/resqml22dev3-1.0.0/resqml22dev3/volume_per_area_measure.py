from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.volume_per_area_uom_with_legacy import VolumePerAreaUomWithLegacy

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VolumePerAreaMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[VolumePerAreaUomWithLegacy] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

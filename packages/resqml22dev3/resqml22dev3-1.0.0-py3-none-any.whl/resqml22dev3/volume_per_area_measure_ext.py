from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22dev3.legacy_volume_per_area_uom import LegacyVolumePerAreaUom
from resqml22dev3.volume_per_area_uom import VolumePerAreaUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VolumePerAreaMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[VolumePerAreaUom, str, LegacyVolumePerAreaUom]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )

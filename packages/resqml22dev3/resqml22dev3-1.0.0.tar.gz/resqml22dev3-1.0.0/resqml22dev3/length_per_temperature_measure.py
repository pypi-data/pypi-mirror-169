from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.length_per_temperature_uom import LengthPerTemperatureUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class LengthPerTemperatureMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[LengthPerTemperatureUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

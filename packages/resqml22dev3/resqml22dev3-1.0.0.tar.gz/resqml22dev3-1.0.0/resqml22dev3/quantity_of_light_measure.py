from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.quantity_of_light_uom import QuantityOfLightUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class QuantityOfLightMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[QuantityOfLightUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

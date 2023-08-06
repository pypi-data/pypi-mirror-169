from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.heat_transfer_coefficient_uom import HeatTransferCoefficientUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class HeatTransferCoefficientMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[HeatTransferCoefficientUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

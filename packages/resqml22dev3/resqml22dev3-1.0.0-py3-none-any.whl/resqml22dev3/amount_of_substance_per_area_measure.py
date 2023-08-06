from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.amount_of_substance_per_area_uom import AmountOfSubstancePerAreaUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AmountOfSubstancePerAreaMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[AmountOfSubstancePerAreaUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

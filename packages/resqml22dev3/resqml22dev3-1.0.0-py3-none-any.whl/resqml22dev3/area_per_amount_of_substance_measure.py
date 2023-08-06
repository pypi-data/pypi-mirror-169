from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.area_per_amount_of_substance_uom import AreaPerAmountOfSubstanceUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AreaPerAmountOfSubstanceMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[AreaPerAmountOfSubstanceUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

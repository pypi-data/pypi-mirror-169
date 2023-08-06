from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.reciprocal_area_uom import ReciprocalAreaUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ReciprocalAreaMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ReciprocalAreaUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

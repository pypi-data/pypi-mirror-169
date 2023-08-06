from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.mass_per_area_uom import MassPerAreaUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MassPerAreaMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[MassPerAreaUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

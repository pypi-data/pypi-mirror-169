from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.area_per_count_uom import AreaPerCountUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AreaPerCountMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[AreaPerCountUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

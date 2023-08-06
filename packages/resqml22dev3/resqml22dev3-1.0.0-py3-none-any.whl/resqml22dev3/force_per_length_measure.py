from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.force_per_length_uom import ForcePerLengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ForcePerLengthMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ForcePerLengthUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

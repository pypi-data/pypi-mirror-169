from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.force_uom import ForceUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ForceMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ForceUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

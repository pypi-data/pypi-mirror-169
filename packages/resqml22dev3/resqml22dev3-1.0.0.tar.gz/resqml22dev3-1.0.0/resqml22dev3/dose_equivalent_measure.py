from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.dose_equivalent_uom import DoseEquivalentUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DoseEquivalentMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[DoseEquivalentUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

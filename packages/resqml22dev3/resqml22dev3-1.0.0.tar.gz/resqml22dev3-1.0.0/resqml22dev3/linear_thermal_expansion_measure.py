from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.linear_thermal_expansion_uom import LinearThermalExpansionUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class LinearThermalExpansionMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[LinearThermalExpansionUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

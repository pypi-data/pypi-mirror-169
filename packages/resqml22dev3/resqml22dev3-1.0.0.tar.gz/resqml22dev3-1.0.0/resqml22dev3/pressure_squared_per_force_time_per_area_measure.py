from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.pressure_squared_per_force_time_per_area_uom import PressureSquaredPerForceTimePerAreaUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PressureSquaredPerForceTimePerAreaMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[PressureSquaredPerForceTimePerAreaUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

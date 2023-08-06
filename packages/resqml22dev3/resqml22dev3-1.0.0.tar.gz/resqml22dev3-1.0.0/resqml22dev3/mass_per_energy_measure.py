from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.mass_per_energy_uom import MassPerEnergyUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MassPerEnergyMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[MassPerEnergyUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.energy_per_mass_per_time_uom import EnergyPerMassPerTimeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class EnergyPerMassPerTimeMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[EnergyPerMassPerTimeUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

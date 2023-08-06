from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.thermodynamic_temperature_uom import ThermodynamicTemperatureUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ThermodynamicTemperatureMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ThermodynamicTemperatureUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

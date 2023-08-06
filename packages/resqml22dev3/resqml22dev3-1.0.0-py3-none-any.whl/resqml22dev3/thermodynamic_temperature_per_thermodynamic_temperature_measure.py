from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.thermodynamic_temperature_per_thermodynamic_temperature_uom import ThermodynamicTemperaturePerThermodynamicTemperatureUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ThermodynamicTemperaturePerThermodynamicTemperatureMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ThermodynamicTemperaturePerThermodynamicTemperatureUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

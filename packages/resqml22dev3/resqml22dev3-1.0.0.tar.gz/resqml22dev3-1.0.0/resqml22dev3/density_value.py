from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_temperature_pressure import AbstractTemperaturePressure
from resqml22dev3.mass_per_volume_measure_ext import MassPerVolumeMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DensityValue:
    """
    A possibly temperature and pressure corrected desity value.

    :ivar density: The density of the product.
    :ivar measurement_pressure_temperature:
    """
    density: Optional[MassPerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "Density",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    measurement_pressure_temperature: Optional[AbstractTemperaturePressure] = field(
        default=None,
        metadata={
            "name": "MeasurementPressureTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )

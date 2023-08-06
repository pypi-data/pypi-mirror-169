from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ThermodynamicTemperatureUom(Enum):
    """
    :cvar DEG_C: degree Celsius
    :cvar DEG_F: degree Fahrenheit
    :cvar DEG_R: degree Rankine
    :cvar K: degree kelvin
    """
    DEG_C = "degC"
    DEG_F = "degF"
    DEG_R = "degR"
    K = "K"

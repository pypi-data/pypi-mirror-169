from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ThermodynamicTemperaturePerThermodynamicTemperatureUom(Enum):
    """
    :cvar DEG_C_DEG_C: degree Celsius per degree Celsius
    :cvar DEG_F_DEG_F: degree Fahrenheit per degree Fahrenheit
    :cvar DEG_R_DEG_R: degree Rankine per degree Rankine
    :cvar EUC: euclid
    :cvar K_K: kelvin per kelvin
    """
    DEG_C_DEG_C = "degC/degC"
    DEG_F_DEG_F = "degF/degF"
    DEG_R_DEG_R = "degR/degR"
    EUC = "Euc"
    K_K = "K/K"

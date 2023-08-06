from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class PressureSquaredUom(Enum):
    """
    :cvar BAR2: bar squared
    :cvar GPA2: gigapascal squared
    :cvar K_PA2: kilopascal squared
    :cvar KPSI2: (thousand psi) squared
    :cvar PA2: pascal squared
    :cvar PSI2: psi squared
    """
    BAR2 = "bar2"
    GPA2 = "GPa2"
    K_PA2 = "kPa2"
    KPSI2 = "kpsi2"
    PA2 = "Pa2"
    PSI2 = "psi2"

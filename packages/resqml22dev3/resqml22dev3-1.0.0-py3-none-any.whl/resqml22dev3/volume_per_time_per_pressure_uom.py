from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class VolumePerTimePerPressureUom(Enum):
    """
    :cvar VALUE_1000_FT3_PSI_D: (thousand cubic foot per day) per psi
    :cvar BBL_K_PA_D: (barrel per day) per kilopascal
    :cvar BBL_PSI_D: (barrel per day) per psi
    :cvar L_BAR_MIN: (litre per minute) per bar
    :cvar M3_BAR_D: (cubic metre per day) per bar
    :cvar M3_BAR_H: (cubic metre per hour) per bar
    :cvar M3_BAR_MIN: (cubic metre per minute) per bar
    :cvar M3_K_PA_D: (cubic metre per day) per kilopascal
    :cvar M3_K_PA_H: (cubic metre per hour) per kilopascal
    :cvar M3_PA_S: cubic metre per pascal second
    :cvar M3_PSI_D: (cubic metre per day) per psi
    """
    VALUE_1000_FT3_PSI_D = "1000 ft3/(psi.d)"
    BBL_K_PA_D = "bbl/(kPa.d)"
    BBL_PSI_D = "bbl/(psi.d)"
    L_BAR_MIN = "L/(bar.min)"
    M3_BAR_D = "m3/(bar.d)"
    M3_BAR_H = "m3/(bar.h)"
    M3_BAR_MIN = "m3/(bar.min)"
    M3_K_PA_D = "m3/(kPa.d)"
    M3_K_PA_H = "m3/(kPa.h)"
    M3_PA_S = "m3/(Pa.s)"
    M3_PSI_D = "m3/(psi.d)"

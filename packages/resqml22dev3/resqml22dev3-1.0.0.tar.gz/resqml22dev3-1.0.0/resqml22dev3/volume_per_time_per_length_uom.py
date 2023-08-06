from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class VolumePerTimePerLengthUom(Enum):
    """
    :cvar VALUE_1000_FT3_D_FT: (thousand cubic foot per day) per foot
    :cvar VALUE_1000_M3_D_M: (thousand cubic metre per day) per metre
    :cvar VALUE_1000_M3_H_M: (thousand cubic metre per hour) per metre
    :cvar BBL_D_FT: barrel per day foot
    :cvar FT3_D_FT: (cubic foot per day) per foot
    :cvar GAL_UK_H_FT: UK gallon per hour foot
    :cvar GAL_UK_H_IN: UK gallon per hour inch
    :cvar GAL_UK_MIN_FT: UK gallon per minute foot
    :cvar GAL_US_H_FT: US gallon per hour foot
    :cvar GAL_US_H_IN: US gallon per hour inch
    :cvar GAL_US_MIN_FT: US gallon per minute foot
    :cvar M3_D_M: (cubic metre per day) per metre
    :cvar M3_H_M: (cubic metre per hour) per metre
    :cvar M3_S_FT: (cubic metre per second) per foot
    :cvar M3_S_M: cubic metre per second metre
    """
    VALUE_1000_FT3_D_FT = "1000 ft3/(d.ft)"
    VALUE_1000_M3_D_M = "1000 m3/(d.m)"
    VALUE_1000_M3_H_M = "1000 m3/(h.m)"
    BBL_D_FT = "bbl/(d.ft)"
    FT3_D_FT = "ft3/(d.ft)"
    GAL_UK_H_FT = "gal[UK]/(h.ft)"
    GAL_UK_H_IN = "gal[UK]/(h.in)"
    GAL_UK_MIN_FT = "gal[UK]/(min.ft)"
    GAL_US_H_FT = "gal[US]/(h.ft)"
    GAL_US_H_IN = "gal[US]/(h.in)"
    GAL_US_MIN_FT = "gal[US]/(min.ft)"
    M3_D_M = "m3/(d.m)"
    M3_H_M = "m3/(h.m)"
    M3_S_FT = "m3/(s.ft)"
    M3_S_M = "m3/(s.m)"

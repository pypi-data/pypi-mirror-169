from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class VolumeUom(Enum):
    """
    :cvar VALUE_1000_BBL: thousand barrel
    :cvar VALUE_1000_FT3: thousand cubic foot
    :cvar VALUE_1000_GAL_UK: thousand UK gallon
    :cvar VALUE_1000_GAL_US: thousand US gallon
    :cvar VALUE_1000_M3: thousand cubic metre
    :cvar VALUE_1_E_6_GAL_US: millionth of US gallon
    :cvar VALUE_1_E12_FT3: million million cubic foot
    :cvar VALUE_1_E6_BBL: million barrel
    :cvar VALUE_1_E6_FT3: million cubic foot
    :cvar VALUE_1_E6_M3: million cubic metre
    :cvar VALUE_1_E9_BBL: thousand million barrel
    :cvar VALUE_1_E9_FT3: thousand million cubic foot
    :cvar ACRE_FT: acre foot
    :cvar BBL: barrel
    :cvar CM3: cubic centimetre
    :cvar DM3: cubic decimetre
    :cvar FLOZ_UK: UK fluid-ounce
    :cvar FLOZ_US: US fluid-ounce
    :cvar FT3: cubic foot
    :cvar GAL_UK: UK gallon
    :cvar GAL_US: US gallon
    :cvar HA_M: hectare metre
    :cvar H_L: hectolitre
    :cvar IN3: cubic inch
    :cvar KM3: cubic kilometre
    :cvar L: litre
    :cvar M3: cubic metre
    :cvar MI3: cubic mile
    :cvar M_L: millilitre
    :cvar MM3: cubic millimetre
    :cvar PT_UK: UK pint
    :cvar PT_US: US pint
    :cvar QT_UK: UK quart
    :cvar QT_US: US quart
    :cvar UM2_M: square micrometre metre
    :cvar YD3: cubic yard
    """
    VALUE_1000_BBL = "1000 bbl"
    VALUE_1000_FT3 = "1000 ft3"
    VALUE_1000_GAL_UK = "1000 gal[UK]"
    VALUE_1000_GAL_US = "1000 gal[US]"
    VALUE_1000_M3 = "1000 m3"
    VALUE_1_E_6_GAL_US = "1E-6 gal[US]"
    VALUE_1_E12_FT3 = "1E12 ft3"
    VALUE_1_E6_BBL = "1E6 bbl"
    VALUE_1_E6_FT3 = "1E6 ft3"
    VALUE_1_E6_M3 = "1E6 m3"
    VALUE_1_E9_BBL = "1E9 bbl"
    VALUE_1_E9_FT3 = "1E9 ft3"
    ACRE_FT = "acre.ft"
    BBL = "bbl"
    CM3 = "cm3"
    DM3 = "dm3"
    FLOZ_UK = "floz[UK]"
    FLOZ_US = "floz[US]"
    FT3 = "ft3"
    GAL_UK = "gal[UK]"
    GAL_US = "gal[US]"
    HA_M = "ha.m"
    H_L = "hL"
    IN3 = "in3"
    KM3 = "km3"
    L = "L"
    M3 = "m3"
    MI3 = "mi3"
    M_L = "mL"
    MM3 = "mm3"
    PT_UK = "pt[UK]"
    PT_US = "pt[US]"
    QT_UK = "qt[UK]"
    QT_US = "qt[US]"
    UM2_M = "um2.m"
    YD3 = "yd3"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class VolumePerVolumeUom(Enum):
    """
    :cvar VALUE: percent
    :cvar VOL: percent [volume basis]
    :cvar VALUE_0_001_BBL_FT3: barrel per thousand cubic foot
    :cvar VALUE_0_001_BBL_M3: barrel per thousand cubic metre
    :cvar VALUE_0_001_GAL_UK_BBL: UK gallon per thousand barrel
    :cvar VALUE_0_001_GAL_UK_GAL_UK: UK gallon per thousand UK gallon
    :cvar VALUE_0_001_GAL_US_BBL: US gallon per thousand barrel
    :cvar VALUE_0_001_GAL_US_FT3: US gallon per thousand cubic foot
    :cvar VALUE_0_001_GAL_US_GAL_US: US gallon per thousand US gallon
    :cvar VALUE_0_001_PT_UK_BBL: UK pint per thousand barrel
    :cvar VALUE_0_01_BBL_BBL: barrel per hundred barrel
    :cvar VALUE_0_1_GAL_US_BBL: US gallon per ten barrel
    :cvar VALUE_0_1_L_BBL: litre per ten barrel
    :cvar VALUE_0_1_PT_US_BBL: US pint per ten barrel
    :cvar VALUE_1000_FT3_BBL: thousand cubic foot per barrel
    :cvar VALUE_1000_M3_M3: thousand cubic metre per cubic metre
    :cvar VALUE_1_E_6_ACRE_FT_BBL: acre foot per million barrel
    :cvar VALUE_1_E_6_BBL_FT3: barrel per million cubic foot
    :cvar VALUE_1_E_6_BBL_M3: barrel per million cubic metre
    :cvar VALUE_1_E6_BBL_ACRE_FT: million barrel per acre foot
    :cvar VALUE_1_E6_FT3_ACRE_FT: million cubic foot per acre foot
    :cvar VALUE_1_E6_FT3_BBL: million cubic foot per barrel
    :cvar BBL_ACRE_FT: barrel per acre foot
    :cvar BBL_BBL: barrel per barrel
    :cvar BBL_FT3: barrel per cubic foot
    :cvar BBL_M3: barrel per cubic metre
    :cvar C_EUC: centieuclid
    :cvar CM3_CM3: cubic centimetre per cubic centimetre
    :cvar CM3_L: cubic centimetre per litre
    :cvar CM3_M3: cubic centimetre per cubic metre
    :cvar DM3_M3: cubic decimetre per cubic metre
    :cvar EUC: euclid
    :cvar FT3_BBL: cubic foot per barrel
    :cvar FT3_FT3: cubic foot per cubic foot
    :cvar GAL_UK_FT3: UK gallon per cubic foot
    :cvar GAL_US_BBL: US gallon per barrel
    :cvar GAL_US_FT3: US gallon per cubic foot
    :cvar L_M3: litre per cubic metre
    :cvar M3_HA_M: cubic metre per hectare metre
    :cvar M3_BBL: cubic metre per barrel
    :cvar M3_M3: cubic metre per cubic metre
    :cvar M_L_GAL_UK: millilitre per UK gallon
    :cvar M_L_GAL_US: millilitre per US gallon
    :cvar M_L_M_L: millilitre per millilitre
    :cvar PPK: part per thousand
    :cvar PPM: part per million
    :cvar PPM_VOL: part per million [volume basis]
    """
    VALUE = "%"
    VOL = "%[vol]"
    VALUE_0_001_BBL_FT3 = "0.001 bbl/ft3"
    VALUE_0_001_BBL_M3 = "0.001 bbl/m3"
    VALUE_0_001_GAL_UK_BBL = "0.001 gal[UK]/bbl"
    VALUE_0_001_GAL_UK_GAL_UK = "0.001 gal[UK]/gal[UK]"
    VALUE_0_001_GAL_US_BBL = "0.001 gal[US]/bbl"
    VALUE_0_001_GAL_US_FT3 = "0.001 gal[US]/ft3"
    VALUE_0_001_GAL_US_GAL_US = "0.001 gal[US]/gal[US]"
    VALUE_0_001_PT_UK_BBL = "0.001 pt[UK]/bbl"
    VALUE_0_01_BBL_BBL = "0.01 bbl/bbl"
    VALUE_0_1_GAL_US_BBL = "0.1 gal[US]/bbl"
    VALUE_0_1_L_BBL = "0.1 L/bbl"
    VALUE_0_1_PT_US_BBL = "0.1 pt[US]/bbl"
    VALUE_1000_FT3_BBL = "1000 ft3/bbl"
    VALUE_1000_M3_M3 = "1000 m3/m3"
    VALUE_1_E_6_ACRE_FT_BBL = "1E-6 acre.ft/bbl"
    VALUE_1_E_6_BBL_FT3 = "1E-6 bbl/ft3"
    VALUE_1_E_6_BBL_M3 = "1E-6 bbl/m3"
    VALUE_1_E6_BBL_ACRE_FT = "1E6 bbl/(acre.ft)"
    VALUE_1_E6_FT3_ACRE_FT = "1E6 ft3/(acre.ft)"
    VALUE_1_E6_FT3_BBL = "1E6 ft3/bbl"
    BBL_ACRE_FT = "bbl/(acre.ft)"
    BBL_BBL = "bbl/bbl"
    BBL_FT3 = "bbl/ft3"
    BBL_M3 = "bbl/m3"
    C_EUC = "cEuc"
    CM3_CM3 = "cm3/cm3"
    CM3_L = "cm3/L"
    CM3_M3 = "cm3/m3"
    DM3_M3 = "dm3/m3"
    EUC = "Euc"
    FT3_BBL = "ft3/bbl"
    FT3_FT3 = "ft3/ft3"
    GAL_UK_FT3 = "gal[UK]/ft3"
    GAL_US_BBL = "gal[US]/bbl"
    GAL_US_FT3 = "gal[US]/ft3"
    L_M3 = "L/m3"
    M3_HA_M = "m3/(ha.m)"
    M3_BBL = "m3/bbl"
    M3_M3 = "m3/m3"
    M_L_GAL_UK = "mL/gal[UK]"
    M_L_GAL_US = "mL/gal[US]"
    M_L_M_L = "mL/mL"
    PPK = "ppk"
    PPM = "ppm"
    PPM_VOL = "ppm[vol]"

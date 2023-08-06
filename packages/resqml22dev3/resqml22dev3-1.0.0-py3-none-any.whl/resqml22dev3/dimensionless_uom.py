from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class DimensionlessUom(Enum):
    """
    :cvar VALUE: percent
    :cvar C_EUC: centieuclid
    :cvar D_EUC: decieuclid
    :cvar EEUC: exaeuclid
    :cvar EUC: euclid
    :cvar F_EUC: femtoeuclid
    :cvar GEUC: gigaeuclid
    :cvar K_EUC: kiloeuclid
    :cvar MEUC: megaeuclid
    :cvar M_EUC_1: millieuclid
    :cvar N_EUC: nanoeuclid
    :cvar P_EUC: picoeuclid
    :cvar PPK: part per thousand
    :cvar PPM: part per million
    :cvar TEUC: teraeuclid
    :cvar U_EUC: microeuclid
    """
    VALUE = "%"
    C_EUC = "cEuc"
    D_EUC = "dEuc"
    EEUC = "EEuc"
    EUC = "Euc"
    F_EUC = "fEuc"
    GEUC = "GEuc"
    K_EUC = "kEuc"
    MEUC = "MEuc"
    M_EUC_1 = "mEuc"
    N_EUC = "nEuc"
    P_EUC = "pEuc"
    PPK = "ppk"
    PPM = "ppm"
    TEUC = "TEuc"
    U_EUC = "uEuc"

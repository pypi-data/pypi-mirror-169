from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class CapacitanceUom(Enum):
    """
    :cvar C_F: centifarad
    :cvar D_F: decifarad
    :cvar EF: exafarad
    :cvar F: farad
    :cvar F_F: femtofarad
    :cvar GF: gigafarad
    :cvar K_F: kilofarad
    :cvar M_F: millifarad
    :cvar MF_1: megafarad
    :cvar N_F: nanofarad
    :cvar P_F: picofarad
    :cvar TF: terafarad
    :cvar U_F: microfarad
    """
    C_F = "cF"
    D_F = "dF"
    EF = "EF"
    F = "F"
    F_F = "fF"
    GF = "GF"
    K_F = "kF"
    M_F = "mF"
    MF_1 = "MF"
    N_F = "nF"
    P_F = "pF"
    TF = "TF"
    U_F = "uF"

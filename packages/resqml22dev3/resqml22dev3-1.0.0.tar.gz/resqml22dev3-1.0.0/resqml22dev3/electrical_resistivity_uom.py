from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ElectricalResistivityUom(Enum):
    """
    :cvar KOHM_M: kiloohm metre
    :cvar NOHM_MIL2_FT: nanoohm square mil per foot
    :cvar NOHM_MM2_M: nanoohm square milimetre per metre
    :cvar OHM_CM: ohm centimetre
    :cvar OHM_M: ohm metre
    :cvar OHM_M2_M: ohm square metre per metre
    """
    KOHM_M = "kohm.m"
    NOHM_MIL2_FT = "nohm.mil2/ft"
    NOHM_MM2_M = "nohm.mm2/m"
    OHM_CM = "ohm.cm"
    OHM_M = "ohm.m"
    OHM_M2_M = "ohm.m2/m"

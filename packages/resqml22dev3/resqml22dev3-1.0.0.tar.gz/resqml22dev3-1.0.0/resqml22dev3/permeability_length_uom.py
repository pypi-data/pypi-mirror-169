from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class PermeabilityLengthUom(Enum):
    """
    :cvar D_FT: darcy foot
    :cvar D_M: darcy metre
    :cvar M_D_FT: millidarcy foot
    :cvar M_D_M: millidarcy metre
    :cvar TD_API_M: teradarcy-API metre
    """
    D_FT = "D.ft"
    D_M = "D.m"
    M_D_FT = "mD.ft"
    M_D_M = "mD.m"
    TD_API_M = "TD[API].m"

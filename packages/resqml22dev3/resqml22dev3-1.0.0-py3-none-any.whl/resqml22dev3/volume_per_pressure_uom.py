from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class VolumePerPressureUom(Enum):
    """
    :cvar BBL_PSI: barrel per psi
    :cvar M3_K_PA: cubic metre per kilopascal
    :cvar M3_PA: cubic metre per Pascal
    """
    BBL_PSI = "bbl/psi"
    M3_K_PA = "m3/kPa"
    M3_PA = "m3/Pa"

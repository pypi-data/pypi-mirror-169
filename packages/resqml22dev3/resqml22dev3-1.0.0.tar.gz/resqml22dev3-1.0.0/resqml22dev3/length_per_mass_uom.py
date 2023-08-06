from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class LengthPerMassUom(Enum):
    """
    :cvar FT_LBM: foot per pound-mass
    :cvar M_KG: metre per kilogram
    """
    FT_LBM = "ft/lbm"
    M_KG = "m/kg"

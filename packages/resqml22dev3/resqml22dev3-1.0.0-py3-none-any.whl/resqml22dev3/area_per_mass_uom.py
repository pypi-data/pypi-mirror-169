from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class AreaPerMassUom(Enum):
    """
    :cvar CM2_G: square centimetre per gram
    :cvar FT2_LBM: square foot per pound-mass
    :cvar M2_G: square metre per gram
    :cvar M2_KG: square metre per kilogram
    """
    CM2_G = "cm2/g"
    FT2_LBM = "ft2/lbm"
    M2_G = "m2/g"
    M2_KG = "m2/kg"

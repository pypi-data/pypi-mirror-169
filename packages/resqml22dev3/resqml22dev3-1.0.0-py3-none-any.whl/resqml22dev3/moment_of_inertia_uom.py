from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class MomentOfInertiaUom(Enum):
    """
    :cvar KG_M2: kilogram square metre
    :cvar LBM_FT2: pound-mass square foot
    """
    KG_M2 = "kg.m2"
    LBM_FT2 = "lbm.ft2"

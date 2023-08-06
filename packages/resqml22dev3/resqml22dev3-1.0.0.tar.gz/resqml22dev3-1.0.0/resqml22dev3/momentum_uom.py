from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class MomentumUom(Enum):
    """
    :cvar KG_M_S: kilogram metre per second
    :cvar LBM_FT_S: foot pound-mass per second
    """
    KG_M_S = "kg.m/s"
    LBM_FT_S = "lbm.ft/s"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ReciprocalForceUom(Enum):
    """
    :cvar VALUE_1_LBF: per pound-force
    :cvar VALUE_1_N: per Newton
    """
    VALUE_1_LBF = "1/lbf"
    VALUE_1_N = "1/N"

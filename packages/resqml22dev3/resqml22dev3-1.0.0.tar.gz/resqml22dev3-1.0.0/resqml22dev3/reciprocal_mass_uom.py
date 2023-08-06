from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ReciprocalMassUom(Enum):
    """
    :cvar VALUE_1_G: per gram
    :cvar VALUE_1_KG: per kilogram
    :cvar VALUE_1_LBM: per pound
    """
    VALUE_1_G = "1/g"
    VALUE_1_KG = "1/kg"
    VALUE_1_LBM = "1/lbm"

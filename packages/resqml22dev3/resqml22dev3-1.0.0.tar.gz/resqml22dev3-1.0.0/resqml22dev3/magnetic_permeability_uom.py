from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class MagneticPermeabilityUom(Enum):
    """
    :cvar H_M: henry per metre
    :cvar U_H_M: microhenry per metre
    """
    H_M = "H/m"
    U_H_M = "uH/m"

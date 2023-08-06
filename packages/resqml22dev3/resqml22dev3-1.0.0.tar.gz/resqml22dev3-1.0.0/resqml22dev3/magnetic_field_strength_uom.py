from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class MagneticFieldStrengthUom(Enum):
    """
    :cvar A_M: ampere per metre
    :cvar A_MM: ampere per millimetre
    :cvar OE: oersted
    """
    A_M = "A/m"
    A_MM = "A/mm"
    OE = "Oe"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class DiffusiveTimeOfFlightUom(Enum):
    """
    :cvar H_0_5:
    :cvar S_0_5: square root of second
    """
    H_0_5 = "h(0.5)"
    S_0_5 = "s(0.5)"

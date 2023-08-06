from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class FluidMarker(Enum):
    """
    The various fluids a well marker can indicate.
    """
    GAS_DOWN_TO = "gas down to"
    GAS_UP_TO = "gas up to"
    OIL_DOWN_TO = "oil down to"
    OIL_UP_TO = "oil up to"
    WATER_DOWN_TO = "water down to"
    WATER_UP_TO = "water up to"

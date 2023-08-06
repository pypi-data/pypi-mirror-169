from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class AreaUom(Enum):
    """
    :cvar ACRE: acre
    :cvar B: barn
    :cvar CM2: square centimetre
    :cvar FT2: square foot
    :cvar HA: hectare
    :cvar IN2: square inch
    :cvar KM2: square kilometre
    :cvar M2: square metre
    :cvar MI_US_2: square US survey mile
    :cvar MI2: square mile
    :cvar MM2: square millimetre
    :cvar SECTION: section
    :cvar UM2: square micrometre
    :cvar YD2: square yard
    """
    ACRE = "acre"
    B = "b"
    CM2 = "cm2"
    FT2 = "ft2"
    HA = "ha"
    IN2 = "in2"
    KM2 = "km2"
    M2 = "m2"
    MI_US_2 = "mi[US]2"
    MI2 = "mi2"
    MM2 = "mm2"
    SECTION = "section"
    UM2 = "um2"
    YD2 = "yd2"

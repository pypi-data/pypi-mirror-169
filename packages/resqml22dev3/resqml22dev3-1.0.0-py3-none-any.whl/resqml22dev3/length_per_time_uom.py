from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class LengthPerTimeUom(Enum):
    """
    :cvar VALUE_1000_FT_H: thousand foot per hour
    :cvar VALUE_1000_FT_S: thousand foot per second
    :cvar CM_A: centimetre per julian-year
    :cvar CM_S: centimetre per second
    :cvar DM_S: decimetre per second
    :cvar FT_D: foot per day
    :cvar FT_H: foot per hour
    :cvar FT_MIN: foot per minute
    :cvar FT_MS: foot per millisecond
    :cvar FT_S: foot per second
    :cvar FT_US: foot per microsecond
    :cvar IN_A: inch per julian-year
    :cvar IN_MIN: inch per minute
    :cvar IN_S: inch per second
    :cvar KM_H: kilometre per hour
    :cvar KM_S: kilometre per second
    :cvar KNOT: knot
    :cvar M_D: metre per day
    :cvar M_H: metre per hour
    :cvar M_MIN: metre per minute
    :cvar M_MS: metre per millisecond
    :cvar M_S: metre per second
    :cvar MI_H: mile per hour
    :cvar MIL_A: mil per julian-year
    :cvar MM_A: millimetre per julian-year
    :cvar MM_S_1: millimetre per second
    :cvar NM_S: nanometre per second
    :cvar UM_S: micrometre per second
    """
    VALUE_1000_FT_H = "1000 ft/h"
    VALUE_1000_FT_S = "1000 ft/s"
    CM_A = "cm/a"
    CM_S = "cm/s"
    DM_S = "dm/s"
    FT_D = "ft/d"
    FT_H = "ft/h"
    FT_MIN = "ft/min"
    FT_MS = "ft/ms"
    FT_S = "ft/s"
    FT_US = "ft/us"
    IN_A = "in/a"
    IN_MIN = "in/min"
    IN_S = "in/s"
    KM_H = "km/h"
    KM_S = "km/s"
    KNOT = "knot"
    M_D = "m/d"
    M_H = "m/h"
    M_MIN = "m/min"
    M_MS = "m/ms"
    M_S = "m/s"
    MI_H = "mi/h"
    MIL_A = "mil/a"
    MM_A = "mm/a"
    MM_S_1 = "mm/s"
    NM_S = "nm/s"
    UM_S = "um/s"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class PlaneAngleUom(Enum):
    """
    :cvar VALUE_0_001_SECA: angular millisecond
    :cvar CCGR: centesimal-second
    :cvar CGR: centesimal-minute
    :cvar DEGA: angular degree
    :cvar GON: gon
    :cvar KRAD: kiloradian
    :cvar MILA: angular mil
    :cvar MINA: angular minute
    :cvar MRAD: megaradian
    :cvar MRAD_1: milliradian
    :cvar RAD: radian
    :cvar REV: revolution
    :cvar SECA: angular second
    :cvar URAD: microradian
    """
    VALUE_0_001_SECA = "0.001 seca"
    CCGR = "ccgr"
    CGR = "cgr"
    DEGA = "dega"
    GON = "gon"
    KRAD = "krad"
    MILA = "mila"
    MINA = "mina"
    MRAD = "Mrad"
    MRAD_1 = "mrad"
    RAD = "rad"
    REV = "rev"
    SECA = "seca"
    URAD = "urad"

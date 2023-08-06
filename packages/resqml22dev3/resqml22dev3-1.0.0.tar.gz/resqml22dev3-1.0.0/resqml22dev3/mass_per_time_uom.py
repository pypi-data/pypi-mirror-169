from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class MassPerTimeUom(Enum):
    """
    :cvar VALUE_1_E6_LBM_A: million pound-mass per julian-year
    :cvar G_S: gram per second
    :cvar KG_D: kilogram per day
    :cvar KG_H: kilogram per hour
    :cvar KG_MIN: kilogram per min
    :cvar KG_S: kilogram per second
    :cvar LBM_D: pound-mass per day
    :cvar LBM_H: pound-mass per hour
    :cvar LBM_MIN: pound-mass per minute
    :cvar LBM_S: pound-mass per second
    :cvar MG_A: megagram per julian-year
    :cvar MG_D: megagram per day
    :cvar MG_H: megagram per hour
    :cvar MG_MIN: megagram per minute
    :cvar T_A: tonne per julian-year
    :cvar T_D: tonne per day
    :cvar T_H: tonne per hour
    :cvar T_MIN: tonne per minute
    :cvar TON_UK_A: UK ton-mass per julian-year
    :cvar TON_UK_D: UK ton-mass per day
    :cvar TON_UK_H: UK ton-mass per hour
    :cvar TON_UK_MIN: UK ton-mass per minute
    :cvar TON_US_A: US ton-mass per julian-year
    :cvar TON_US_D: US ton-mass per day
    :cvar TON_US_H: US ton-mass per hour
    :cvar TON_US_MIN: US ton-mass per minute
    """
    VALUE_1_E6_LBM_A = "1E6 lbm/a"
    G_S = "g/s"
    KG_D = "kg/d"
    KG_H = "kg/h"
    KG_MIN = "kg/min"
    KG_S = "kg/s"
    LBM_D = "lbm/d"
    LBM_H = "lbm/h"
    LBM_MIN = "lbm/min"
    LBM_S = "lbm/s"
    MG_A = "Mg/a"
    MG_D = "Mg/d"
    MG_H = "Mg/h"
    MG_MIN = "Mg/min"
    T_A = "t/a"
    T_D = "t/d"
    T_H = "t/h"
    T_MIN = "t/min"
    TON_UK_A = "ton[UK]/a"
    TON_UK_D = "ton[UK]/d"
    TON_UK_H = "ton[UK]/h"
    TON_UK_MIN = "ton[UK]/min"
    TON_US_A = "ton[US]/a"
    TON_US_D = "ton[US]/d"
    TON_US_H = "ton[US]/h"
    TON_US_MIN = "ton[US]/min"

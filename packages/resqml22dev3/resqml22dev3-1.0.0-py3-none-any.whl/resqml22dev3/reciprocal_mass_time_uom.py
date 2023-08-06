from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ReciprocalMassTimeUom(Enum):
    """
    :cvar VALUE_1_KG_S: per (kilogram per second)
    :cvar BQ_KG: becquerel per kilogram
    :cvar P_CI_G: picocurie per gram
    """
    VALUE_1_KG_S = "1/(kg.s)"
    BQ_KG = "Bq/kg"
    P_CI_G = "pCi/g"

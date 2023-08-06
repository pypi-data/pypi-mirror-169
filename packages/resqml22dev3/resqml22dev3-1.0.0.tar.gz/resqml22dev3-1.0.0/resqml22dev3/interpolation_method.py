from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class InterpolationMethod(Enum):
    LINEAR = "linear"
    LOGARITHMIC = "logarithmic"

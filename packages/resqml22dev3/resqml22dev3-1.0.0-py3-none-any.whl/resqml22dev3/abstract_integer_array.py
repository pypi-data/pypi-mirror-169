from __future__ import annotations
from dataclasses import dataclass
from resqml22dev3.abstract_numeric_array import AbstractNumericArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractIntegerArray(AbstractNumericArray):
    """Generic representation of an array of integer values.

    Each derived element provides specialized implementation to allow
    specific optimization of the representation.
    """

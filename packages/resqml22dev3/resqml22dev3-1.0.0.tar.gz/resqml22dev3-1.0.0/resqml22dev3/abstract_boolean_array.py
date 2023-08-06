from __future__ import annotations
from dataclasses import dataclass
from resqml22dev3.abstract_value_array import AbstractValueArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractBooleanArray(AbstractValueArray):
    """Generic representation of an array of Boolean values.

    Each derived element provides a specialized implementation to allow
    specific optimization of the representation.
    """

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_floating_point_array import AbstractFloatingPointArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class FloatingPointConstantArray(AbstractFloatingPointArray):
    """Represents an array of double values where all values are identical.

    This an optimization for which an array of explicit double values is
    not required.

    :ivar value: Values inside all the elements of the array.
    :ivar count: Size of the array.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "min_inclusive": 1,
        }
    )

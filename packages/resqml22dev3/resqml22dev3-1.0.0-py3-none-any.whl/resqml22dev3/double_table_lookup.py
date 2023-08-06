from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.abstract_property_lookup import AbstractPropertyLookup
from resqml22dev3.double_lookup import DoubleLookup

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class DoubleTableLookup(AbstractPropertyLookup):
    """Defines a function for table lookups.

    For example, used for linear interpolation, such as PVT. Used for
    categorical property, which also may use StringTableLookup.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    value: List[DoubleLookup] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "min_occurs": 1,
        }
    )

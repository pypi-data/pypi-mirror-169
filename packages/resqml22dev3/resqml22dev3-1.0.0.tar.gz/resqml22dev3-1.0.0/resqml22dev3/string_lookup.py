from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StringLookup:
    """
    Defines an element inside a string-to-integer lookup table.

    :ivar key: The corresponding integer value. This value is used in
        HDF5 instead of the string value. The value of null integer
        value must be reserved for NULL. The size of this value is
        constrained by the size of the format used in HDF5.
    :ivar value: A string value. Output from the lookup table.
    """
    key: Optional[int] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "max_length": 2000,
        }
    )

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class ContactMode(Enum):
    """An optional second qualifier that may be used when describing binary
    contact interpretation parts.

    (See also BinaryContactInterpretationPart and the RESQML Technical
    Usage Guide.)
    """
    CONFORMABLE = "conformable"
    EXTENDED = "extended"
    UNCONFORMABLE = "unconformable"

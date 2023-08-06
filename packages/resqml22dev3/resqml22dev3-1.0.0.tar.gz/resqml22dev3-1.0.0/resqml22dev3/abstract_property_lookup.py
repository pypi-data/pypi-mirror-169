from __future__ import annotations
from dataclasses import dataclass
from resqml22dev3.abstract_object import AbstractObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractPropertyLookup(AbstractObject):
    """Generic representation of a property lookup table.

    Each derived element provides specific lookup methods for different
    data types.
    """

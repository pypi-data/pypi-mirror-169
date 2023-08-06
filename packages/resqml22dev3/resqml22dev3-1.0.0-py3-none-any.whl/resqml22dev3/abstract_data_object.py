from __future__ import annotations
from dataclasses import dataclass
from resqml22dev3.abstract_object import AbstractObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractDataObject(AbstractObject):
    """
    Substitution group for normative data objects.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

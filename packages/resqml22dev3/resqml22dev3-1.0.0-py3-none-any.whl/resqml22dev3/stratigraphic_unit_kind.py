from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class StratigraphicUnitKind(Enum):
    """
    Attribute specifying the criteria that are considered for defining various
    kinds of stratigraphic units (age, lithology, fossil content).
    """
    CHRONOSTRATIGRAPHIC = "chronostratigraphic"
    LITHOSTRATIGRAPHIC = "lithostratigraphic"
    BIOSTRATIGRAPHIC = "biostratigraphic"

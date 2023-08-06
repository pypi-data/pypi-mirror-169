from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.abstract_object import AbstractObject
from resqml22dev3.stratigraphic_unit_interpretation import StratigraphicUnitInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StratigraphicUnitDictionary(AbstractObject):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    stratigraphic_unit_interpretation: List[StratigraphicUnitInterpretation] = field(
        default_factory=list,
        metadata={
            "name": "StratigraphicUnitInterpretation",
            "type": "Element",
            "min_occurs": 2,
        }
    )

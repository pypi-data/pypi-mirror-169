from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.abstract_object import AbstractObject
from resqml22dev3.continuous_color_map import ContinuousColorMap
from resqml22dev3.discrete_color_map import DiscreteColorMap

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ColorMapDictionary(AbstractObject):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    discrete_color_map: List[DiscreteColorMap] = field(
        default_factory=list,
        metadata={
            "name": "DiscreteColorMap",
            "type": "Element",
        }
    )
    continuous_color_map: List[ContinuousColorMap] = field(
        default_factory=list,
        metadata={
            "name": "ContinuousColorMap",
            "type": "Element",
        }
    )

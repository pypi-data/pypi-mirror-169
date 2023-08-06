from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.abstract_object import AbstractObject
from resqml22dev3.discrete_color_map_entry import DiscreteColorMapEntry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class DiscreteColorMap(AbstractObject):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    entry: List[DiscreteColorMapEntry] = field(
        default_factory=list,
        metadata={
            "name": "Entry",
            "type": "Element",
            "min_occurs": 1,
        }
    )

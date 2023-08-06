from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.abstract_object import AbstractObject
from resqml22dev3.continuous_color_map_entry import ContinuousColorMapEntry
from resqml22dev3.hsv_color import HsvColor
from resqml22dev3.interpolation_domain import InterpolationDomain
from resqml22dev3.interpolation_method import InterpolationMethod

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ContinuousColorMap(AbstractObject):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    interpolation_domain: Optional[InterpolationDomain] = field(
        default=None,
        metadata={
            "name": "InterpolationDomain",
            "type": "Element",
            "required": True,
        }
    )
    interpolation_method: Optional[InterpolationMethod] = field(
        default=None,
        metadata={
            "name": "InterpolationMethod",
            "type": "Element",
            "required": True,
        }
    )
    na_ncolor: Optional[HsvColor] = field(
        default=None,
        metadata={
            "name": "NaNColor",
            "type": "Element",
        }
    )
    entry: List[ContinuousColorMapEntry] = field(
        default_factory=list,
        metadata={
            "name": "Entry",
            "type": "Element",
            "min_occurs": 2,
        }
    )

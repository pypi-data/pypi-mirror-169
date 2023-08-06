from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.hsv_color import HsvColor

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class DiscreteColorMapEntry:
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    hsv: Optional[HsvColor] = field(
        default=None,
        metadata={
            "name": "Hsv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )

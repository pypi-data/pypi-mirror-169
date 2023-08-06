from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MdInterval:
    md_top: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MdTop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    md_base: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MdBase",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    datum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class TvdInterval:
    """
    :ivar tvd_top:
    :ivar tvd_base: True vertical depth at the base of the interval
    :ivar datum:
    """
    tvd_top: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "TvdTop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    tvd_base: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "TvdBase",
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

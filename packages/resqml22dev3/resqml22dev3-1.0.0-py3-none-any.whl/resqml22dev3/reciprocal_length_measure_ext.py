from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22dev3.reciprocal_length_uom import ReciprocalLengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ReciprocalLengthMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[ReciprocalLengthUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )

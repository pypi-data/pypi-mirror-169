from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.moment_of_inertia_uom import MomentOfInertiaUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MomentOfInertiaMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[MomentOfInertiaUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

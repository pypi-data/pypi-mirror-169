from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.magnetic_vector_potential_uom import MagneticVectorPotentialUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MagneticVectorPotentialMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[MagneticVectorPotentialUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

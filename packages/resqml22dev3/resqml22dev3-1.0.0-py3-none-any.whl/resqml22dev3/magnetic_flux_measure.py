from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.magnetic_flux_uom import MagneticFluxUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MagneticFluxMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[MagneticFluxUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.luminous_flux_uom import LuminousFluxUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class LuminousFluxMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[LuminousFluxUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

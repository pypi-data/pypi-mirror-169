from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.volume_flow_rate_per_volume_flow_rate_uom import VolumeFlowRatePerVolumeFlowRateUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VolumeFlowRatePerVolumeFlowRateMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[VolumeFlowRatePerVolumeFlowRateUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

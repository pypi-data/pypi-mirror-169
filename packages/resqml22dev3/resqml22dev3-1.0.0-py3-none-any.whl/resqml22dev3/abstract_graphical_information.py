from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractGraphicalInformation:
    target_object: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "TargetObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )

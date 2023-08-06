from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.digital_storage_uom import DigitalStorageUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DigitalStorageMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[DigitalStorageUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

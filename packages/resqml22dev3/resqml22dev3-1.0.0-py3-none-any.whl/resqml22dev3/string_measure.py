from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22dev3.legacy_unit_of_measure import LegacyUnitOfMeasure
from resqml22dev3.unit_of_measure import UnitOfMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class StringMeasure:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 64,
        }
    )
    uom: Optional[Union[LegacyUnitOfMeasure, UnitOfMeasure, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".*:.*",
        }
    )

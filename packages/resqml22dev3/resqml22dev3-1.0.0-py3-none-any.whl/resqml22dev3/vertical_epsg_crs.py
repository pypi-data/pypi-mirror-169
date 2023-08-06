from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_vertical_crs import AbstractVerticalCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VerticalEpsgCrs(AbstractVerticalCrs):
    """
    This class contains the EPSG code for a vertical CRS.
    """
    epsg_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "EpsgCode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "min_inclusive": 1,
        }
    )

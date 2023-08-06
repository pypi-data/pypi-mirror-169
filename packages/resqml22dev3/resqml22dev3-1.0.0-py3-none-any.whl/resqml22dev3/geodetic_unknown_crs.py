from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_geodetic_crs import AbstractGeodeticCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class GeodeticUnknownCrs(AbstractGeodeticCrs):
    """
    This class is used in a case where the coordinate reference system is
    either unknown or is intentionally not being transferred.
    """
    unknown: Optional[str] = field(
        default=None,
        metadata={
            "name": "Unknown",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 2000,
        }
    )

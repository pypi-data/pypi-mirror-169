from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_geodetic_crs import AbstractGeodeticCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class GeodeticEpsgCrs(AbstractGeodeticCrs):
    """
    This class contains the EPSG code for a geodetic CRS.
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

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_geodetic_crs import AbstractGeodeticCrs
from resqml22dev3.ex_vertical_extent_type import GeodeticCrstype

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class GeodeticGmlCrs(AbstractGeodeticCrs):
    """
    This is the Energistics encapsulation of the GeodeticCrs type from GML.
    """
    gml_geodetic_crs_definition: Optional[GeodeticCrstype] = field(
        default=None,
        metadata={
            "name": "GmlGeodeticCrsDefinition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )

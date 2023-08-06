from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_geometry import AbstractGeometry
from resqml22dev3.abstract_point3d_array import AbstractPoint3DArray
from resqml22dev3.abstract_seismic_coordinates import AbstractSeismicCoordinates

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PointGeometry(AbstractGeometry):
    """
    The geometry of a set of points defined by their location in the local CRS,
    with optional seismic coordinates.
    """
    points: Optional[AbstractPoint3DArray] = field(
        default=None,
        metadata={
            "name": "Points",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    seismic_coordinates: Optional[AbstractSeismicCoordinates] = field(
        default=None,
        metadata={
            "name": "SeismicCoordinates",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )

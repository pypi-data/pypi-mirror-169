from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_point3d_array import AbstractPoint3DArray
from resqml22dev3.external_dataset import ExternalDataset

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Point2DExternalArray(AbstractPoint3DArray):
    """An array of explicit XY points stored as two coordinates in an HDF5
    dataset.

    If needed, the implied Z coordinate is uniformly 0.

    :ivar coordinates: Reference to an HDF5 2D dataset of XY points. The
        2 coordinates are stored sequentially in HDF5, i.e., a multi-
        dimensional array of points is stored as a 2 x ... HDF5 array.
    """
    class Meta:
        name = "Point2dExternalArray"

    coordinates: Optional[ExternalDataset] = field(
        default=None,
        metadata={
            "name": "Coordinates",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )

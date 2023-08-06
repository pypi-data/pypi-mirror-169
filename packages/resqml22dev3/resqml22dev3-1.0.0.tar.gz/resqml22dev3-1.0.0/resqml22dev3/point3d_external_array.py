from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_point3d_array import AbstractPoint3DArray
from resqml22dev3.external_dataset import ExternalDataset

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Point3DExternalArray(AbstractPoint3DArray):
    """
    An array of explicit XYZ points stored as three coordinates in an HDF5
    dataset.

    :ivar coordinates: Reference to an HDF5 3D dataset of XYZ points.
        The 3 coordinates are stored sequentially in HDF5, i.e., a
        multi-dimensional array of points is stored as a 3 x ... HDF5
        array.
    """
    class Meta:
        name = "Point3dExternalArray"

    coordinates: Optional[ExternalDataset] = field(
        default=None,
        metadata={
            "name": "Coordinates",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )

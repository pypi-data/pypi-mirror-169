from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_floating_point_array import AbstractFloatingPointArray
from resqml22dev3.external_dataset import ExternalDataset

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class FloatingPointExternalArray(AbstractFloatingPointArray):
    """An array of double values provided explicitly by an HDF5 dataset.

    By convention, the null value is NaN.

    :ivar values: Reference to an HDF5 array of doubles.
    """
    values: Optional[ExternalDataset] = field(
        default=None,
        metadata={
            "name": "Values",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )

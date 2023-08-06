from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_boolean_array import AbstractBooleanArray
from resqml22dev3.external_dataset import ExternalDataset

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class BooleanExternalArray(AbstractBooleanArray):
    """
    Array of Boolean values provided explicitly by an HDF5 dataset.

    :ivar values: Reference to an HDF5 array of values.
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

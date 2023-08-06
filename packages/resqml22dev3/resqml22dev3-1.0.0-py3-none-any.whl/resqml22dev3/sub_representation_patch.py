from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.element_indices import ElementIndices
from resqml22dev3.patch1d import Patch1D

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SubRepresentationPatch(Patch1D):
    """Each sub-representation patch has its own list of representation
    indices, drawn from the supporting representation.

    If a list of pairwise elements is required, use two ElementIndices.
    The count of elements (or pair of elements) is defined in
    SubRepresentationPatch.
    """
    element_indices: List[ElementIndices] = field(
        default_factory=list,
        metadata={
            "name": "ElementIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )

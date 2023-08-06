from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.abstract_graphical_information import AbstractGraphicalInformation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AnnotationInformation(AbstractGraphicalInformation):
    """Used for properties and property kinds and for geometry.

    In the latter case, we need to point to the representation.
    """
    show_annotation_every: Optional[int] = field(
        default=None,
        metadata={
            "name": "ShowAnnotationEvery",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    value_vector_indices: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ValueVectorIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )

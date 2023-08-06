from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_integer_array import AbstractIntegerArray
from resqml22dev3.indexable_element import IndexableElement

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ElementIndices:
    """
    Index into the indexable elements selected.
    """
    indexable_element: Optional[IndexableElement] = field(
        default=None,
        metadata={
            "name": "IndexableElement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "Indices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    supporting_representation_index: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "SupportingRepresentationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )

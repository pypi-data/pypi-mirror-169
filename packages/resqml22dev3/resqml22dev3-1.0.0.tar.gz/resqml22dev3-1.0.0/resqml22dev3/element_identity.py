from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_integer_array import AbstractIntegerArray
from resqml22dev3.data_object_reference import DataObjectReference
from resqml22dev3.identity_kind import IdentityKind
from resqml22dev3.indexable_element import IndexableElement
from resqml22dev3.time_index import TimeIndex

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ElementIdentity:
    """Indicates the nature of the relationship between 2 or more
    representations, specifically if they are partially or totally identical.

    For possible types of relationships, see IdentityKind. Commonly used
    to identify contacts between representations in model descriptions.
    May also be used to relate the components of a grid (e.g., pillars)
    to those of a structural framework.

    :ivar element_indices: Indicates which elements are identical based
        on their indices in the (sub)representation. If not given, then
        the selected indexable elements of each of the selected
        representations are identical at the element by element level.
        BUSINESS RULE: The number of identical elements must be equal to
        identicalElementCount for each representation.
    :ivar identity_kind:
    :ivar indexable_element:
    :ivar representation:
    :ivar to_time_index:
    :ivar from_time_index:
    """
    element_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ElementIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    identity_kind: Optional[IdentityKind] = field(
        default=None,
        metadata={
            "name": "IdentityKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    indexable_element: Optional[IndexableElement] = field(
        default=None,
        metadata={
            "name": "IndexableElement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Representation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    to_time_index: Optional[TimeIndex] = field(
        default=None,
        metadata={
            "name": "ToTimeIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    from_time_index: Optional[TimeIndex] = field(
        default=None,
        metadata={
            "name": "FromTimeIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )

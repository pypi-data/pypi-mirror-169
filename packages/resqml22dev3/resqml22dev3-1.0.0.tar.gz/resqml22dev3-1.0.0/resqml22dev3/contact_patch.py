from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_integer_array import AbstractIntegerArray
from resqml22dev3.patch1d import Patch1D

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ContactPatch(Patch1D):
    """
    A subset of topological elements of an existing contact representation part
    (sealed or non-sealed contact).

    :ivar representation_index: Identifies a representation by its
        index, in the list of representations contained in the
        organization.
    :ivar supporting_representation_nodes: The ordered list of nodes
        (identified by their global index) in the supporting
        representation, which constitutes the contact patch.
    """
    representation_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "RepresentationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    supporting_representation_nodes: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "SupportingRepresentationNodes",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )

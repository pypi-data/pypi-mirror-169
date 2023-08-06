from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.abstract_representation import AbstractRepresentation
from resqml22dev3.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class RepresentationSetRepresentation(AbstractRepresentation):
    """The parent class of the framework representations.

    It is used to group together individual representations to represent
    a "bag" of representations. If the individual representations are
    all of the same, then you can indicate that the set is homogenous.
    These "bags" do not imply any geologic consistency. For example, you
    can define a set of wellbore frames, a set of wellbore trajectories,
    a set of blocked wellbores. Because the framework representations
    inherit from this class, they inherit the capability to gather
    individual representations into sealed and non-sealed surface
    framework representations, or sealed volume framework
    representations. For more information, see the RESQML Technical
    Usage Guide.

    :ivar is_homogeneous: Indicates that all of the selected
        representations are of a single kind.
    :ivar representation:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    is_homogeneous: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsHomogeneous",
            "type": "Element",
            "required": True,
        }
    )
    representation: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Representation",
            "type": "Element",
            "min_occurs": 1,
        }
    )

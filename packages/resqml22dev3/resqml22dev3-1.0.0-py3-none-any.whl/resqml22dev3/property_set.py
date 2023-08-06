from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.abstract_object import AbstractObject
from resqml22dev3.data_object_reference import DataObjectReference
from resqml22dev3.time_set_kind import TimeSetKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PropertySet(AbstractObject):
    """A set of properties collected together for a specific purpose.

    For example, a property set can be used to collect all the
    properties corresponding to the simulation output at a single time,
    or all the values of a single property type for all times.

    :ivar time_set_kind:
    :ivar has_single_property_kind: If true, indicates that the
        collection contains only property values associated with a
        single property kind.
    :ivar has_multiple_realizations: If true, indicates that the
        collection contains properties with defined realization indices.
    :ivar parent_set: A pointer to the parent property group of this
        property group.
    :ivar properties: Defines the properties which are contained into a
        property set
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    time_set_kind: Optional[TimeSetKind] = field(
        default=None,
        metadata={
            "name": "TimeSetKind",
            "type": "Element",
            "required": True,
        }
    )
    has_single_property_kind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasSinglePropertyKind",
            "type": "Element",
            "required": True,
        }
    )
    has_multiple_realizations: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasMultipleRealizations",
            "type": "Element",
            "required": True,
        }
    )
    parent_set: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "ParentSet",
            "type": "Element",
        }
    )
    properties: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Properties",
            "type": "Element",
        }
    )

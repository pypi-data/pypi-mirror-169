from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.abstract_activity_parameter import AbstractActivityParameter
from resqml22dev3.abstract_object import AbstractObject
from resqml22dev3.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Activity(AbstractObject):
    """
    Instance of a given activity.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    activity_descriptor: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ActivityDescriptor",
            "type": "Element",
            "required": True,
        }
    )
    parent: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Parent",
            "type": "Element",
        }
    )
    parameter: List[AbstractActivityParameter] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "min_occurs": 1,
        }
    )

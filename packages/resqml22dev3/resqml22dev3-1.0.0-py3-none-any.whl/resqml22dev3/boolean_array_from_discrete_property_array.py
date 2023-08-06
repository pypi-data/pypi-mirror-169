from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_boolean_array import AbstractBooleanArray
from resqml22dev3.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class BooleanArrayFromDiscretePropertyArray(AbstractBooleanArray):
    """An array of Boolean values that is explicitly defined by indicating
    which indices in the array are either true or false.

    This class is used to represent very sparse true or false data,
    based on a discrete property.

    :ivar value: Integer to match for the value to be considered true
    :ivar property:
    """
    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    property: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Property",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )

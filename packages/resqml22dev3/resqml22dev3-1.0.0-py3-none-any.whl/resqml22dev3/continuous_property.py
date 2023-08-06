from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from resqml22dev3.abstract_values_property import AbstractValuesProperty
from resqml22dev3.data_object_reference import DataObjectReference
from resqml22dev3.legacy_unit_of_measure import LegacyUnitOfMeasure
from resqml22dev3.unit_of_measure import UnitOfMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ContinuousProperty(AbstractValuesProperty):
    """Most common type of property used for storing rock or fluid attributes;
    all are represented as doubles.

    So that the value range can be known before accessing all values,
    the min and max values of the range are also stored. BUSINESS RULE:
    It also contains a unit of measure, which can be different from the
    unit of measure of its property type, but it must be convertible
    into this unit.

    :ivar minimum_value: The minimum of the associated property values.
        BUSINESS RULE: There can be only one value per number of
        elements.
    :ivar maximum_value: The maximum of the associated property values.
        BUSINESS RULE: There can be only one value per number of
        elements.
    :ivar uom: Unit of measure for the property.
    :ivar custom_unit_dictionary:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    minimum_value: List[float] = field(
        default_factory=list,
        metadata={
            "name": "MinimumValue",
            "type": "Element",
        }
    )
    maximum_value: List[float] = field(
        default_factory=list,
        metadata={
            "name": "MaximumValue",
            "type": "Element",
        }
    )
    uom: Optional[Union[LegacyUnitOfMeasure, UnitOfMeasure, str]] = field(
        default=None,
        metadata={
            "name": "Uom",
            "type": "Element",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    custom_unit_dictionary: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "CustomUnitDictionary",
            "type": "Element",
        }
    )

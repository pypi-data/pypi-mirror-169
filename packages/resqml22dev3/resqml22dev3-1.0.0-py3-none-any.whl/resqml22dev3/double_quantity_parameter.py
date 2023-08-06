from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22dev3.abstract_activity_parameter import AbstractActivityParameter
from resqml22dev3.data_object_reference import DataObjectReference
from resqml22dev3.legacy_unit_of_measure import LegacyUnitOfMeasure
from resqml22dev3.unit_of_measure import UnitOfMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DoubleQuantityParameter(AbstractActivityParameter):
    """
    Parameter containing a double value.

    :ivar value: Double value
    :ivar uom: Unit of measure associated with the value
    :ivar custom_unit_dictionary:
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    uom: Optional[Union[LegacyUnitOfMeasure, UnitOfMeasure, str]] = field(
        default=None,
        metadata={
            "name": "Uom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    custom_unit_dictionary: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "CustomUnitDictionary",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )

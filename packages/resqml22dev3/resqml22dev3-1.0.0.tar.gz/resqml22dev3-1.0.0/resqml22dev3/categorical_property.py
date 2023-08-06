from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_values_property import AbstractValuesProperty
from resqml22dev3.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class CategoricalProperty(AbstractValuesProperty):
    """Information specific to one categorical property. Contains discrete
    integer. This type of property is associated either as:

    - an internally stored index to a string through a lookup mapping.
    - an internally stored double to another double value through an explicitly provided table.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    lookup: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Lookup",
            "type": "Element",
            "required": True,
        }
    )

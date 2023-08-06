from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.data_object_reference import DataObjectReference
from resqml22dev3.jagged_array import JaggedArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class IntervalStratigraphicUnits:
    """A mapping from intervals to stratigraphic units for representations
    (grids or wellbore frames).

    Since a single interval may corresponds to several units, the
    mapping is done using a jagged array.

    :ivar unit_indices: Index of the stratigraphic unit per interval, of
        a given stratigraphic column. Notes: 1.) For grids: if it does
        not exist a property kind "geologic k" attached to the grid then
        intervals = layers + K gaps else intervals = values property of
        property kind "geologic k" 2.) If there is no stratigraphic
        column, e.g., within salt, use null value BUSINESS RULE: Array
        length must equal the number of intervals.
    :ivar stratigraphic_organization_interpretation:
    """
    unit_indices: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "UnitIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    stratigraphic_organization_interpretation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "StratigraphicOrganizationInterpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )

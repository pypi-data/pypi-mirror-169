from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.abstract_stratigraphic_organization_interpretation import AbstractStratigraphicOrganizationInterpretation
from resqml22dev3.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StratigraphicColumnRankInterpretation(AbstractStratigraphicOrganizationInterpretation):
    """
    A global hierarchy containing an ordered list of stratigraphic unit
    interpretations.

    :ivar rank_in_stratigraphic_column: The rank in the stratigraphic
        column.
    :ivar stratigraphic_units:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    rank_in_stratigraphic_column: Optional[int] = field(
        default=None,
        metadata={
            "name": "RankInStratigraphicColumn",
            "type": "Element",
            "required": True,
            "min_inclusive": 0,
        }
    )
    stratigraphic_units: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "StratigraphicUnits",
            "type": "Element",
            "min_occurs": 1,
        }
    )

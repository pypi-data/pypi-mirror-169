from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_organization_interpretation import AbstractOrganizationInterpretation
from resqml22dev3.ordering_criteria import OrderingCriteria

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractStratigraphicOrganizationInterpretation(AbstractOrganizationInterpretation):
    """The main class that defines the relationships between the stratigraphic
    units and provides the stratigraphic hierarchy of the Earth.

    BUSINESS RULE: A stratigraphic organization must be in a ranked
    order from a lower rank to an upper rank. For example, it is
    possible to find previous unit containment relationships between
    several ranks.
    """
    ordering_criteria: Optional[OrderingCriteria] = field(
        default=None,
        metadata={
            "name": "OrderingCriteria",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )

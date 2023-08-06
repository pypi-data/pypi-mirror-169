from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.abstract_organization_interpretation import AbstractOrganizationInterpretation
from resqml22dev3.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class RockFluidOrganizationInterpretation(AbstractOrganizationInterpretation):
    """This class describes the organization of geological reservoir, i.e., of
    an interconnected network of porous and permeable rock units, containing an
    accumulation of economic fluids, such as oil and gas.

    A reservoir is normally enveloped by rock and fluid barriers and
    contains a single natural pressure system.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    rock_fluid_unit_index: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "RockFluidUnitIndex",
            "type": "Element",
        }
    )

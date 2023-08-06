from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.abstract_organization_interpretation import AbstractOrganizationInterpretation
from resqml22dev3.boundary_feature_interpretation_plus_its_rank import BoundaryFeatureInterpretationPlusItsRank
from resqml22dev3.data_object_reference import DataObjectReference
from resqml22dev3.feature_interpretation_set import FeatureInterpretationSet
from resqml22dev3.ordering_criteria import OrderingCriteria

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StructuralOrganizationInterpretation(AbstractOrganizationInterpretation):
    """One of the main types of RESQML organizations, this class gathers boundary interpretations (e.g., horizons, faults and fault networks) plus frontier features and their relationships (contacts interpretations), which when taken together define the structure of a part of the earth.
    IMPLEMENTATION RULE: Two use cases are presented:
    1. If the relative age or apparent depth between faults and horizons is unknown, the writer must provide all individual faults within the UnorderedFaultCollection FeatureInterpretationSet.
    2. Else, the writer must provide individual faults and fault collections within the OrderedBoundaryFeatureInterpretation list.
    BUSINESS RULE: Two use cases are processed:
    1 - If relative age or apparent depth between faults and horizons is unknown, writer must provides all individual faults within the UnorderedFaultCollection FeatureInterpretationSet.
    2 - Else, individual faults and fault collections are provided within the OrderedBoundaryFeatureInterpretation list."""
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    ordering_criteria: Optional[OrderingCriteria] = field(
        default=None,
        metadata={
            "name": "OrderingCriteria",
            "type": "Element",
            "required": True,
        }
    )
    sides: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Sides",
            "type": "Element",
        }
    )
    top_frontier: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "TopFrontier",
            "type": "Element",
        }
    )
    bottom_frontier: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "BottomFrontier",
            "type": "Element",
        }
    )
    unordered_fault_collection: Optional[FeatureInterpretationSet] = field(
        default=None,
        metadata={
            "name": "UnorderedFaultCollection",
            "type": "Element",
        }
    )
    ordered_boundary_feature_interpretation: List[BoundaryFeatureInterpretationPlusItsRank] = field(
        default_factory=list,
        metadata={
            "name": "OrderedBoundaryFeatureInterpretation",
            "type": "Element",
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.boundary_feature_interpretation import BoundaryFeatureInterpretation
from resqml22dev3.boundary_relation import BoundaryRelation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GeobodyBoundaryInterpretation(BoundaryFeatureInterpretation):
    """
    Contains the data describing an opinion about the characterization of a
    geobody BoundaryFeature, and it includes the attribute boundary relation.

    :ivar boundary_relation: Characterizes the stratigraphic
        relationships of a horizon with the stratigraphic units that its
        bounds.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    boundary_relation: List[BoundaryRelation] = field(
        default_factory=list,
        metadata={
            "name": "BoundaryRelation",
            "type": "Element",
        }
    )

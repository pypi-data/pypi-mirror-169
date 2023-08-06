from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.boundary_feature_interpretation import BoundaryFeatureInterpretation
from resqml22dev3.boundary_relation import BoundaryRelation
from resqml22dev3.horizon_stratigraphic_role import HorizonStratigraphicRole
from resqml22dev3.sequence_stratigraphy_surface import SequenceStratigraphySurface

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class HorizonInterpretation(BoundaryFeatureInterpretation):
    """An interpretation of a horizon, which optionally provides stratigraphic information on BoundaryRelation, HorizonStratigraphicRole, SequenceStratigraphysurface
    ."""
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    boundary_relation: List[BoundaryRelation] = field(
        default_factory=list,
        metadata={
            "name": "BoundaryRelation",
            "type": "Element",
        }
    )
    horizon_stratigraphic_role: List[HorizonStratigraphicRole] = field(
        default_factory=list,
        metadata={
            "name": "HorizonStratigraphicRole",
            "type": "Element",
        }
    )
    sequence_stratigraphy_surface: Optional[SequenceStratigraphySurface] = field(
        default=None,
        metadata={
            "name": "SequenceStratigraphySurface",
            "type": "Element",
        }
    )
    chrono_bottom: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChronoBottom",
            "type": "Element",
        }
    )
    chrono_top: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChronoTop",
            "type": "Element",
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_feature_interpretation import AbstractFeatureInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class WellboreInterpretation(AbstractFeatureInterpretation):
    """Contains the data describing an opinion of a borehole.

    This interpretation is relative to one particular well trajectory.

    :ivar is_drilled: Used to indicate that this wellbore has been, or
        is being, drilled, as opposed to planned wells. One wellbore
        feature may have multiple wellbore interpretations. - For
        updated drilled trajectories, use IsDrilled=TRUE. - For planned
        trajectories, use IsDrilled=FALSE used.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    is_drilled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsDrilled",
            "type": "Element",
            "required": True,
        }
    )

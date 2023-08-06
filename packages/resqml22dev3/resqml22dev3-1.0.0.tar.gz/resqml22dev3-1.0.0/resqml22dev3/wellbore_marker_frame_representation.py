from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.wellbore_frame_representation import WellboreFrameRepresentation
from resqml22dev3.wellbore_marker import WellboreMarker

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class WellboreMarkerFrameRepresentation(WellboreFrameRepresentation):
    """A well log frame where each entry represents a well marker.

    BUSINESS RULE: The interpretation of a wellboremarkerframe is forced
    to be a wellbore Interpretation.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    wellbore_marker: List[WellboreMarker] = field(
        default_factory=list,
        metadata={
            "name": "WellboreMarker",
            "type": "Element",
            "min_occurs": 1,
        }
    )

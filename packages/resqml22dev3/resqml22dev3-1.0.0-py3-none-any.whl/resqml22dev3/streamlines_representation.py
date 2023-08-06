from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_representation import AbstractRepresentation
from resqml22dev3.polyline_set_patch import PolylineSetPatch
from resqml22dev3.streamline_wellbores import StreamlineWellbores

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StreamlinesRepresentation(AbstractRepresentation):
    """Representation of streamlines associated with a streamline feature and
    interpretation.

    Use StreamlinesFeature to define the vector field that supports the
    streamlines, i.e., describes what flux is being traced. Use
    Interpretation to distinguish between shared and differing
    interpretations. Usage Note: When defining streamline geometry, the
    PatchIndex is not referenced and may be set to a value of 0.

    :ivar line_count: Number of streamlines.
    :ivar streamline_wellbores:
    :ivar geometry:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    line_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "LineCount",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        }
    )
    streamline_wellbores: Optional[StreamlineWellbores] = field(
        default=None,
        metadata={
            "name": "StreamlineWellbores",
            "type": "Element",
        }
    )
    geometry: Optional[PolylineSetPatch] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
        }
    )

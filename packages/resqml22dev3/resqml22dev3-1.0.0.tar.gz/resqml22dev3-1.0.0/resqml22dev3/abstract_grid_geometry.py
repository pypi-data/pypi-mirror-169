from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.additional_grid_points import AdditionalGridPoints
from resqml22dev3.point_geometry import PointGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractGridGeometry(PointGeometry):
    """
    Grid geometry described by means of points attached to nodes and additional
    optional points which may be attached to other indexable elements of the
    grid representation.
    """
    additional_grid_points: List[AdditionalGridPoints] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalGridPoints",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.point3d import Point3D

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ThreePoint3D:
    """
    List of three 3D points.
    """
    class Meta:
        name = "ThreePoint3d"

    point3d: List[Point3D] = field(
        default_factory=list,
        metadata={
            "name": "Point3d",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 3,
            "max_occurs": 3,
        }
    )

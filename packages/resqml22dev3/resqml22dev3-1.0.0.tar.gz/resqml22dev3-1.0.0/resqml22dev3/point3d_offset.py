from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_floating_point_array import AbstractFloatingPointArray
from resqml22dev3.point3d import Point3D

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Point3DOffset:
    """Defines the size and sampling in each dimension (direction) of the point
    3D lattice array.

    Sampling can be uniform or irregular.

    :ivar offset: The direction of the axis of this lattice dimension.
        This is a relative offset vector instead of an absolute 3D
        point.
    :ivar spacing: A lattice of N offset points is described by a
        spacing array of size N-1. The offset between points is given by
        the spacing value multiplied by the offset vector. For example,
        the first offset is 0. The second offset is the first spacing *
        offset. The second offset is (first spacing + second spacing) *
        offset, etc.
    """
    class Meta:
        name = "Point3dOffset"

    offset: Optional[Point3D] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    spacing: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "Spacing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )

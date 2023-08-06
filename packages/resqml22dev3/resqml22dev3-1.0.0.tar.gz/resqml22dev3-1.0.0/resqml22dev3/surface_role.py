from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class SurfaceRole(Enum):
    """
    Indicates the various roles that a surface topology can have.

    :cvar MAP: Representation support for properties.
    :cvar PICK: Representation support for 3D points picked in 2D or 3D.
    """
    MAP = "map"
    PICK = "pick"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class LineRole(Enum):
    """
    Indicates the various roles that a polyline topology can have in a
    representation.

    :cvar FAULT_CENTER_LINE: Usually used to represent fault lineaments
        on horizons. These lines can represent nonsealed contact
        interpretation parts defined by a horizon/fault intersection.
    :cvar PICK: Used to represent all types of nonsealed contact
        interpretation parts defined by a horizon/fault intersection.
    :cvar INNER_RING: Closed polyline that delineates a hole in a
        surface patch.
    :cvar OUTER_RING: Closed polyline that delineates the extension of a
        surface patch.
    :cvar TRAJECTORY: Polyline that is used to represent a well
        trajectory representation.
    :cvar INTERPRETATION_LINE: Line corresponding to a digitalization
        along an earth model section.
    :cvar CONTACT: Used to represent nonsealed contact interpretation
        parts defined by a horizon/fault intersection.
    :cvar DEPOSITIONAL_LINE: Used to represent nonsealed contact
        interpretation parts defined by a horizon/horizon intersection.
    :cvar EROSION_LINE: Used to represent nonsealed contact
        interpretation parts defined by a horizon/horizon intersection.
    :cvar CONTOURING: Used to obtain sets of 3D x, y, z points to
        represent any boundary interpretation.
    :cvar PILLAR: Used to represent the pillars of a column-layer
        volumic grid.
    """
    FAULT_CENTER_LINE = "fault center line"
    PICK = "pick"
    INNER_RING = "inner ring"
    OUTER_RING = "outer ring"
    TRAJECTORY = "trajectory"
    INTERPRETATION_LINE = "interpretation line"
    CONTACT = "contact"
    DEPOSITIONAL_LINE = "depositional line"
    EROSION_LINE = "erosion line"
    CONTOURING = "contouring"
    PILLAR = "pillar"

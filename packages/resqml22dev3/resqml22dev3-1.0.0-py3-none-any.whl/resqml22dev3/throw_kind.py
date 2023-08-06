from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class ThrowKind(Enum):
    """
    Enumeration that characterizes the type of discontinuity corresponding to a
    fault.

    :cvar REVERSE:
    :cvar NORMAL:
    :cvar THRUST:
    :cvar STRIKE_AND_SLIP:
    :cvar SCISSOR:
    :cvar VARIABLE: Used when a throw has different behaviors during its
        lifetime.
    """
    REVERSE = "reverse"
    NORMAL = "normal"
    THRUST = "thrust"
    STRIKE_AND_SLIP = "strike and slip"
    SCISSOR = "scissor"
    VARIABLE = "variable"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class Facet(Enum):
    """
    :cvar I: Applies to direction facet kind. With respect to the first
        local grid (lateral) direction. Used for full tensor
        permeability.
    :cvar J: Applies to direction facet kind. With respect to the second
        local grid (lateral) direction. Used for full tensor
        permeability.
    :cvar K: Applies to direction facet kind. With respect to the third
        local grid (vertical) direction. Used for full tensor
        permeability.
    :cvar X: Applies to direction facet kind. With respect to the first
        coordinate system (laterall) direction. Used for full tensor
        permeability.
    :cvar Y: Applies to direction facet kind. With respect to the second
        coordinate system (lateral) direction. Used for full tensor
        permeability.
    :cvar Z: Applies to direction facet kind. With respect to the third
        coordinate system (vertical) direction. Used for full tensor
        permeability.
    :cvar I_1: Applies to direction facet kind. With respect to the
        first local grid (lateral) increasing direction. Used for full
        tensor permeability.
    :cvar J_1: Applies to direction facet kind. With respect to the
        second local grid (lateral) increasing direction. Used for full
        tensor permeability.
    :cvar K_1: Applies to direction facet kind. With respect to the
        third local grid (vertical) increasing direction. Used for full
        tensor permeability.
    :cvar X_1: Applies to direction facet kind. With respect to the
        first coordinate system (laterall) increasing direction. Used
        for full tensor permeability.
    :cvar Y_1: Applies to direction facet kind. With respect to the
        second coordinate system (lateral) increasing direction. Used
        for full tensor permeability.
    :cvar Z_1: Applies to direction facet kind. With respect to the
        third coordinate system (vertical) increasing direction. Used
        for full tensor permeability.
    :cvar I_2: Applies to direction facet kind. With respect to the
        first local grid (lateral) decreasing direction. Used for full
        tensor permeability.
    :cvar J_2: Applies to direction facet kind. With respect to the
        second local grid (lateral) decreasing direction. Used for full
        tensor permeability.
    :cvar K_2: Applies to direction facet kind. With respect to the
        third local grid (vertical) decreasing direction. Used for full
        tensor permeability.
    :cvar X_2: Applies to direction facet kind. With respect to the
        first coordinate system (laterall) decreasing direction. Used
        for full tensor permeability.
    :cvar Y_2: Applies to direction facet kind. With respect to the
        second coordinate system (lateral) decreasing direction. Used
        for full tensor permeability.
    :cvar Z_2: Applies to direction facet kind. With respect to the
        third coordinate system (vertical) decreasing direction. Used
        for full tensor permeability.
    :cvar NET: Applies to netgross facet kind.
    :cvar GROSS: Applies to netgross facet kind.
    :cvar PLUS:
    :cvar MINUS:
    :cvar AVERAGE: Applies to statistics facet kind.
    :cvar MAXIMUM: Applies to statistics facet kind.
    :cvar MINIMUM: Applies to statistics facet kind.
    :cvar MAXIMUM_THRESHOLD: Applies to qualifier facet kind.
    :cvar MINIMUM_THRESHOLD: Applies to qualifier facet kind.
    :cvar SURFACE_CONDITION: Applies to conditions facet kind.
    :cvar RESERVOIR_CONDITION: Applies to conditions facet kind.
    :cvar OIL: Applies to what facet kind.
    :cvar WATER: Applies to what facet kind.
    :cvar GAS: Applies to what facet kind.
    :cvar CONDENSATE: Applies to what facet kind.
    :cvar CUMULATIVE: Applies to statistics facet kind.
    """
    I = "I"
    J = "J"
    K = "K"
    X = "X"
    Y = "Y"
    Z = "Z"
    I_1 = "I+"
    J_1 = "J+"
    K_1 = "K+"
    X_1 = "X+"
    Y_1 = "Y+"
    Z_1 = "Z+"
    I_2 = "I-"
    J_2 = "J-"
    K_2 = "K-"
    X_2 = "X-"
    Y_2 = "Y-"
    Z_2 = "Z-"
    NET = "net"
    GROSS = "gross"
    PLUS = "plus"
    MINUS = "minus"
    AVERAGE = "average"
    MAXIMUM = "maximum"
    MINIMUM = "minimum"
    MAXIMUM_THRESHOLD = "maximum threshold"
    MINIMUM_THRESHOLD = "minimum threshold"
    SURFACE_CONDITION = "surface condition"
    RESERVOIR_CONDITION = "reservoir condition"
    OIL = "oil"
    WATER = "water"
    GAS = "gas"
    CONDENSATE = "condensate"
    CUMULATIVE = "cumulative"
